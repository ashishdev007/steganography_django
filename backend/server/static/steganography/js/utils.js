function switchDisplays(hide, show) {
  let forHiding = document.querySelectorAll(`.${hide}`);
  forHiding.forEach((element) => {
    element.style.display = 'none';
  });

  let forShow = document.querySelectorAll(`.${show}`);

  forShow.forEach((element) => {
    element.setAttribute('style', 'display: block !important;');
  });
}

function fileUpload(e) {
  e.preventDefault();
  var label = e.target.nextElementSibling;
  let labelVal = label.innerHTML;
  var fileName = '';

  let showNextBtn = document.querySelector('#submitBtn')
    ? document.querySelector('#submitBtn').style.display != 'block'
    : true;

  if (this.files && this.files.length > 1)
    fileName = (this.getAttribute('data-multiple-caption') || '').replace(
      '{count}',
      this.files.length
    );
  else fileName = e.target.value.split('\\').pop();

  if (fileName) {
    label.querySelector('span').innerHTML = fileName;
    if (showNextBtn) {
      console.log(showNextBtn);
      console.log(e);
      nextBtn = document.querySelector('#nextBtn');
      nextBtn.style.display = 'block';
    }
  } else label.innerHTML = labelVal;
}
