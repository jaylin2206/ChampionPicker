from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from django.core.serializers import serialize

from partypes.models import Partype
from champions.models import Champion, Skin
from classes.models import Class

import requests

# Create your views here.


def getData():
    url = "https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json"

    result = requests.get(url)
    if result.status_code != 200:
        print('error fetching from api')

    result = result.json()
    champs = result["data"]

    classes = {"Fighter": "", "Tank": "", "Mage": "",
               "Assassin": "", "Marksman": "", "Support": ""}

    partypes = {'Mana': '', 'Manaless': '', 'Health': '', 'Energy': '', 'Fury': '', 'Resourceless': '', 'Rage': '', 'Shield': '', 'Heat': '',
                'Style': '', 'Ferocity': '', 'Blood Well': '', 'Flow': '', 'Moonlight': '', 'Grit': '', 'None': '', 'Courage': '', 'Crimson Rush': ''}

    for item in classes:
        cl = Class.objects.get(name=item)
        classes[item] = Class.objects.get(pk=cl.id)

    for item in partypes:
        pa = Partype.objects.get(name=item)
        partypes[item] = Partype.objects.get(pk=pa.id)

    for name in champs:
        data = champs[name]
        if Champion.objects.filter(id=data["key"]).exists():
            continue

        if data["partype"] == "":
            data["partype"] = "None"

        new = Champion.objects.create(
            id=data["key"], name=data["name"], alias=name, partype_id=partypes[data["partype"]], title=data["title"], blurb=data["blurb"])

        for cl in data["tags"]:
            new.classes.add(classes[cl])


def index(request):
    # only make requests if no data
    if (not Champion._meta.db_table in connection.introspection.table_names() or Champion.objects.count() < 166):
        getData()

    context = {"champions": Champion.objects.all().order_by('name'),
               "classes": Class.objects.all()}

    return render(request, "champions.html", context)


def champion(request, name):
    data = Champion.objects.get(name=name)
    id = data.id
    url = f'https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{id}.json'
    skins = Skin.objects.filter(champion_id=id)

    if skins.count() == 0:
        result = requests.get(url)
        if result.status_code != 200:
            print('error fetching from api')
        result = result.json()

        skins = [Skin(id=_["id"], name=_["name"], champion_id=data)
                 for _ in result["skins"]]
        Skin.objects.bulk_create(skins)

        data.blurb = result["shortBio"]
        data.save()

    skins_data = serialize('json', data.skin_set.all())

    context = {"name": name, "data": data, "skins": skins_data}
    return render(request, "champion.html", context)
