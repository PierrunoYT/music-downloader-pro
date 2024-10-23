document.addEventListener('DOMContentLoaded', () => {
    const youtubeUrlInput = document.getElementById('youtube-url');
    const outputDirInput = document.getElementById('output-dir');
    const convertBtn = document.getElementById('convert-btn');
    const statusMessage = document.getElementById('status-message');
    const progressBar = document.getElementById('progress');

    function validateYoutubeUrl(url) {
        const regex = /(https?:\/\/)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)\/(watch\?v=|embed\/|v\/|.+\?v=)?([^&=%\?]{11})/;
        return regex.test(url);
    }

    function updateStatus(message, isError = false) {
        statusMessage.textContent = message;
        statusMessage.className = isError ? 'error' : 'success';
    }

    function updateProgress(percent) {
        progressBar.style.width = `${percent}%`;
    }

    function resetUI() {
        updateProgress(0);
        convertBtn.disabled = false;
    }

    function simulateConversion() {
        const url = youtubeUrlInput.value.trim();
        const outputDir = outputDirInput.value.trim();

        if (!validateYoutubeUrl(url)) {
            updateStatus('Please enter a valid YouTube URL', true);
            return;
        }

        convertBtn.disabled = true;
        updateStatus('Starting conversion...');
        updateProgress(0);

        let progress = 0;
        const interval = setInterval(() => {
            progress += 5;
            updateProgress(progress);
            
            if (progress < 30) {
                updateStatus('Downloading audio...');
            } else if (progress < 60) {
                updateStatus('Converting to MP3...');
            } else if (progress < 90) {
                updateStatus('Processing...');
            }

            if (progress >= 100) {
                clearInterval(interval);
                updateStatus('Conversion completed successfully!');
                setTimeout(resetUI, 3000);
            }
        }, 200);
    }

    convertBtn.addEventListener('click', simulateConversion);

    youtubeUrlInput.addEventListener('input', () => {
        if (youtubeUrlInput.value.trim() === '') {
            updateStatus('');
            updateProgress(0);
        }
    });
});
