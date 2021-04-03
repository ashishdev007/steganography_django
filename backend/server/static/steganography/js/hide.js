var inputs = document.querySelectorAll('.inputfile');
var statusId = null;

inputs.forEach((input) => {
  input.addEventListener('change', fileUpload);
});

var nextBtn = document.getElementById('nextBtn');

nextBtn.addEventListener('click', (event) => {
  event.preventDefault();
  switchDisplays('first', 'second');
});

document.querySelector('form').addEventListener('submit', handleSubmit);

function handleSubmit(event) {
  event.preventDefault();

  let image = event.target.elements.image.files[0];
  let text = event.target.elements.text.value;
  let txtFile = event.target.elements.textFile.files[0];

  fetch('http://127.0.0.1:8000/status/')
    .then((res) => res.json())
    .then((data) => {
      statusId = data['id'];
      sendForEncoding(statusId, image, text, txtFile);
    });
}

function sendForEncoding(statusId, image, text, txtFile) {
  let data = new FormData();
  data.append('image', image);
  data.append('text', text);
  data.append('txtFile', txtFile);

  move(statusId);
  document.getElementById('progressHeader').innerHTML =
    'Encoding your Image...';

  switchDisplays('second', 'third');
  fetch(`http://127.0.0.1:8000/encode/${statusId}`, {
    method: 'POST',
    body: data,
  })
    .then((res) => res.blob())
    .then((blob) => {
      download(blob);
    });
}
