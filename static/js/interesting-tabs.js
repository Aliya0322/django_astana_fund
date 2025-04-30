document.addEventListener('DOMContentLoaded', function() {
    // Элементы модальных окон
    const videoModal = document.getElementById('videoModal');
    const audioModal = document.getElementById('audioModal');
    const videoContainer = videoModal ? videoModal.querySelector('.video-player-container') : null;
    const audioPlayer = document.getElementById('audioPlayer');
    const closeButtons = document.querySelectorAll('.close');

    // Универсальная функция открытия модального окна
    function showModal(modal) {
        if (modal) {
            modal.style.display = 'block';
            document.body.style.overflow = 'hidden';
        }
    }

    // Универсальная функция закрытия модальных окон
    function closeModals() {
        if (videoModal) {
            if (videoContainer) {
                const iframe = videoContainer.querySelector('iframe');
                const video = videoContainer.querySelector('video');

                if (iframe) iframe.src = '';
                if (video) {
                    video.pause();
                    video.src = '';
                }
                videoContainer.innerHTML = '';
            }
            videoModal.style.display = 'none';
        }

        if (audioModal) {
            if (audioPlayer) {
                audioPlayer.pause();
                audioPlayer.currentTime = 0;
                audioPlayer.src = '';
            }
            audioModal.style.display = 'none';
        }

        document.body.style.overflow = '';
    }

    // Обработчики закрытия
    closeButtons.forEach(button => {
        button.addEventListener('click', closeModals);
    });

    // Закрытие по клику вне окна
    window.addEventListener('click', function(event) {
        if (event.target === videoModal || event.target === audioModal) {
            closeModals();
        }
    });

    // Обработчики для видео
    document.querySelectorAll('.play-video').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const videoUrl = this.getAttribute('data-video');

            if (!videoModal || !videoContainer) return;

            // Очищаем предыдущее видео
            videoContainer.innerHTML = '';

            if (videoUrl.includes('youtube.com') || videoUrl.includes('youtu.be')) {
                let videoId = videoUrl.split('v=')[1]?.split('&')[0] ||
                             videoUrl.split('youtu.be/')[1]?.split('?')[0];

                if (videoId) {
                    const iframe = document.createElement('iframe');
                    iframe.src = `https://www.youtube.com/embed/${videoId}?autoplay=1&mute=1&rel=0&modestbranding=1`;
                    iframe.setAttribute('allowfullscreen', '');
                    iframe.setAttribute('allow', 'accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture');
                    videoContainer.appendChild(iframe);
                }
            } else {
                const video = document.createElement('video');
                video.src = videoUrl;
                video.controls = true;
                video.autoplay = true;
                video.style.width = '100%';
                videoContainer.appendChild(video);
            }

            showModal(videoModal);
        });
    });

    // Обработчики для аудио
    document.querySelectorAll('.play-audio').forEach(button => {
        button.addEventListener('click', async function(e) {
            e.preventDefault();

            if (!audioModal || !audioPlayer) return;

            const audioUrl = this.dataset.audio;
            const title = this.dataset.title;
            const artist = this.dataset.artist;
            const description = this.dataset.description;
            const thumbnail = this.dataset.thumbnail;

            // Обновляем информацию
            if (document.getElementById('audioTitle')) {
                document.getElementById('audioTitle').textContent = title;
            }
            if (document.getElementById('audioArtist')) {
                document.getElementById('audioArtist').textContent = artist;
            }
            if (document.getElementById('audioDescription')) {
                document.getElementById('audioDescription').textContent = description;
            }

            // Устанавливаем обложку
            const thumbEl = document.getElementById('audioThumbnail');
            if (thumbEl) {
                if (thumbnail) {
                    thumbEl.src = thumbnail;
                    thumbEl.style.display = 'block';
                } else {
                    thumbEl.style.display = 'none';
                }
            }

            // Управление аудио
            audioPlayer.src = audioUrl;
            showModal(audioModal);

            try {
                await audioPlayer.play();
            } catch (err) {
                console.log('Автовоспроизведение заблокировано:', err);
                const playBtn = document.createElement('button');
                playBtn.className = 'manual-play-btn';
                playBtn.innerHTML = '<i class="fas fa-play"></i> Воспроизвести';
                playBtn.onclick = () => {
                    audioPlayer.play();
                    playBtn.remove();
                };

                const modalContent = audioModal.querySelector('.modal-content');
                if (modalContent) {
                    modalContent.appendChild(playBtn);
                }
            }
        });
    });

    // Удаление кнопки воспроизведения
    if (audioPlayer) {
        audioPlayer.addEventListener('play', function() {
            const manualBtn = audioModal.querySelector('.manual-play-btn');
            if (manualBtn) manualBtn.remove();
        });
    }

    // Переключение вкладок
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabId = button.getAttribute('data-tab');
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            button.classList.add('active');
            document.getElementById(tabId).classList.add('active');
        });
    });
});