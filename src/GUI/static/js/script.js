const socket = io();
const sliceButton = document.getElementById('sliceButton');
const progressBar = document.getElementById('progressBar');
const statusText = document.getElementById('statusText');
const previewImage = document.getElementById('previewImage');
const imageInput = document.getElementById('imageInput');

let uploadedFilePath = null;

imageInput.addEventListener('change', () => {
    const file = imageInput.files[0];
    if (!file) {
        alert('Please select a file!');
        return;
    }

    const formData = new FormData();
    formData.append('file', file);

    fetch('/upload', {
        method: 'POST',
        body: formData,
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.preview) {
                uploadedFilePath = data.filePath; // Store the path for slicing
                previewImage.src = data.preview;
                previewImage.style.display = 'block';
                sliceButton.disabled = false;
            }
        })
        .catch((err) => {
            console.error('Error uploading file:', err);
        });
});

sliceButton.addEventListener('click', () => {
    if (!uploadedFilePath) return;

    sliceButton.disabled = true;
    progressBar.style.display = 'block';
    progressBar.value = 0;
    statusText.innerText = 'Processing...';

    socket.emit('slice_image', { path: uploadedFilePath });

    socket.on('slice_progress', (data) => {
        progressBar.value = data.progress;
        if (data.progress >= 100) {
            statusText.innerText = 'Done!';
            sliceButton.disabled = false;
            progressBar.style.display = 'none';
        }
    });
});