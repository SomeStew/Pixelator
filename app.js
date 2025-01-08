// app.js
document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData();
    var imageFile = document.getElementById('image').files[0];
    formData.append('image', imageFile);

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
