window.addEventListener('scroll', function () {
  const top = document.getElementById('top');
  if (window.scrollY >= 300) top.style.display = 'block';
  else top.style.display = 'none';
});
