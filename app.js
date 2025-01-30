// app.js

document.addEventListener("DOMContentLoaded", function () {
    const aside = document.querySelector("aside");
    let touchStartX = 0;
    let touchEndX = 0;

    // Function to open sidebar
    function openSidebar() {
        aside.classList.add("active");
    }

    // Function to close sidebar
    function closeSidebar() {
        aside.classList.remove("active");
    }

    // Detect touch start
    document.addEventListener("touchstart", (event) => {
        touchStartX = event.touches[0].clientX;
    });

    // Detect touch end
    document.addEventListener("touchend", (event) => {
        touchEndX = event.changedTouches[0].clientX;

        // If swiped right, open sidebar
        if (touchEndX > touchStartX + 50) {
            openSidebar();
        }
        // If swiped left, close sidebar
        else if (touchEndX < touchStartX - 50) {
            closeSidebar();
        }
    });

    // Add a menu button to toggle sidebar manually
    const menuButton = document.createElement("button");
    menuButton.textContent = "☰ Menu";
    menuButton.classList.add("menu-btn");
    document.body.appendChild(menuButton);
    menuButton.addEventListener("click", function () {
        if (aside.classList.contains("active")) {
            closeSidebar();
        } else {
            openSidebar();
        }
    });

    // Close sidebar when clicking outside of it
    document.addEventListener("click", (event) => {
        if (!aside.contains(event.target) && !menuButton.contains(event.target)) {
            closeSidebar();
        }
    });
});

// Image Upload and Preview Functionality
document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData();
    var imageFile = document.getElementById('image').files[0];
    formData.append('image', imageFile);

    fetch('https://pixelator-ioak.onrender.com/upload', {
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

