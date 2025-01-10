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
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to upload image');
        }
        return response.blob();
    })
    .then(blob => {
        var url = window.URL.createObjectURL(blob);
        var a = document.createElement('a');
        a.style.display = 'none';
        a.href = url;
        a.download = 'processed_image.jpg'; // Default name for the downloaded file
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);

        document.getElementById('result').innerText = 'Image processed successfully!';
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = 'Error uploading the image. Please try again.';
    });
});

// Image preview logic
document.getElementById('image').addEventListener('change', function(event) {
    var reader = new FileReader();
    reader.onload = function(e) {
        var imgPreview = document.createElement('img');
        imgPreview.src = e.target.result;
        imgPreview.style.maxWidth = '300px';
        imgPreview.style.marginTop = '10px';

        // Clear any previous content in the result div
        var resultDiv = document.getElementById('result');
        resultDiv.innerHTML = '';

        // Add the preview image to the result div
        resultDiv.appendChild(imgPreview);
    };
    reader.readAsDataURL(event.target.files[0]);
});

