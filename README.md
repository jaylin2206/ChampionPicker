# Champion Picker

## SoftDev Fall 2023 Final Project

League of Legends champion catalog built with Django and Postgres\
Uses champion and skin data from Riot's [ddragon](https://ddragon.leagueoflegends.com/cdn/13.24.1/data/en_US/champion.json) and [cdragon](https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champions/{id}.json) APIs

## examples

![Champions](https://github.com/jaylin2206/ChampionPicker/blob/main/images/champions.png)
![Champion](https://github.com/jaylin2206/ChampionPicker/blob/main/images/champion.png)

## usage

start server via `python manage.py runserver` in `/champion_picker/`\
navigate to [localhost](http://127.0.0.1:8000/)

## installation

1. `git clone https://github.com/jaylin2206/ChampionPicker.git`
2. `pyenv local 3.11.5`
3. `python -m venv env`
4. `source env/bin/activate` or `source env/Scripts/activate`
5. `pip install -r requirements.txt`
6. `python manage.py migrate` in `/champion_picker/`

# disclaimer

Champion Picker is not endorsed by Riot Games and does not reflect the views or opinions of Riot Games or anyone officially involved in producing or managing Riot Games properties. Riot Games and all associated properties are trademarks or registered trademarks of Riot Games, Inc
