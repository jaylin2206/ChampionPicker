const filter = (query) => {
  let champions = document.getElementsByClassName('champion-card');
  let found = false;
  let none = document.getElementById('none');

  for (let champion of champions) {
    let name = champion.id.toLowerCase();

    if (!(name.startsWith(query) || name.includes(query))) champion.classList.add('hide');
    else {
      champion.classList.remove('hide');
      found = true;
    }
  }

  if (found) none.style.display = 'none';
  else none.style.display = 'flex';
};

document.getElementById('search').addEventListener('input', (e) => {
  filter(e.target.value.toLowerCase());
});

document.getElementById('none').addEventListener('click', () => {
  document.getElementById('search').value = '';
  filter('');
});

let blurbs = document.querySelectorAll('.blurb');
let titles = document.querySelectorAll('.title');
let cards = document.querySelectorAll('.champion-card');
let container = document.getElementsByClassName('container')[0];

document.getElementById('select-format').addEventListener(`change`, function (event) {
  if (event.target && event.target.matches('#btnradio1')) {
    container.style.display = 'inherit';
    container.style.flexWrap = 'nowrap';
    blurbs.forEach(function (blurb) {
      blurb.hidden = false;
    });
    titles.forEach(function (title) {
      title.style.fontSize = '1.5em';
    });
    cards.forEach(function (card) {
      card.style.width = 'inherit';
      card.style.marginBottom = '20px';
    });
  } else if (event.target && event.target.matches('#btnradio2')) {
    container.style.display = 'flex';
    container.style.flexWrap = 'wrap';
    blurbs.forEach(function (blurb) {
      blurb.hidden = true;
    });
    titles.forEach(function (title) {
      title.style.fontSize = '1.1em';
    });
    cards.forEach(function (card) {
      card.style.width = '380px';
      card.style.marginBottom = '6px';
    });
  }
});
