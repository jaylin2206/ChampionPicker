let count = 0;
let id = document.getElementById('id').textContent;
let images = document.getElementById('images');

for (let i = 0; i < skins.length; i++) {
  const image = document.createElement('img');
  image.id = skins[i].id;
  image.src = `https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-splashes/${id}/${skins[i].id}.jpg`;
  if (i != 0) image.style.display = 'none';

  images.append(image);
}

const scroll = (dir) => {
  let prev = count;
  count += dir;
  if (count == -1) count = skins.length - 1;
  else if (count == skins.length) count = 0;

  document.getElementById(skins[prev].id).style.display = 'none';
  document.getElementById(skins[count].id).style.display = 'block';
  document.getElementById('skin').textContent = skins[count].name;
};

document.getElementById('back').addEventListener('click', () => {
  scroll(-1);
});

document.getElementById('next').addEventListener('click', () => {
  scroll(1);
});
