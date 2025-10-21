document.addEventListener('DOMContentLoaded', function() {
    console.log('Interesting tabs script loaded');
    
    // Элементы модальных окон
    const videoModal = document.getElementById('videoModal');
    const audioModal = document.getElementById('audioModal');
    const videoContainer = videoModal ? videoModal.querySelector('.video-player-container') : null;
    const audioPlayer = document.getElementById('audioPlayer');
    const closeButtons = document.querySelectorAll('.close');
    
    console.log('Modal elements found:', {
        videoModal: !!videoModal,
        audioModal: !!audioModal,
        videoContainer: !!videoContainer,
        audioPlayer: !!audioPlayer,
        closeButtons: closeButtons.length
    });

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
            console.log('Video button clicked, URL:', videoUrl);

            if (!videoModal || !videoContainer) {
                console.error('Video modal or container not found');
                return;
            }

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

    // Обработчики для клика по видео-превью и получение длительности
    document.querySelectorAll('.video-thumbnail').forEach((video, index) => {
        console.log(`Setting up video ${index + 1}:`, video);
        
        // Получаем длительность видео
        video.addEventListener('loadedmetadata', function() {
            console.log(`Video ${index + 1} metadata loaded, duration:`, this.duration);
            const duration = this.duration;
            if (duration && !isNaN(duration)) {
                const minutes = Math.floor(duration / 60);
                const seconds = Math.floor(duration % 60);
                const durationText = `${minutes}:${seconds.toString().padStart(2, '0')}`;
                console.log(`Video ${index + 1} duration text:`, durationText);
                
                // Находим badge с длительностью и обновляем его
                const durationBadge = this.closest('.resource-image').querySelector('.duration-badge');
                if (durationBadge) {
                    console.log(`Updating duration badge for video ${index + 1}:`, durationBadge.textContent, '->', durationText);
                    durationBadge.textContent = durationText;
                } else {
                    console.error(`Duration badge not found for video ${index + 1}`);
                }
            } else {
                console.error(`Invalid duration for video ${index + 1}:`, duration);
            }
        });
        
        // Принудительно загружаем метаданные
        video.load();

        // Обработчик клика
        video.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Video thumbnail clicked');
            const source = this.querySelector('source');
            if (!source) {
                console.error('No source element found in video');
                return;
            }
            const videoUrl = source.src;
            const playButton = this.closest('.resource-card').querySelector('.play-video');
            
            if (playButton) {
                // Устанавливаем data-video атрибут если его нет
                if (!playButton.getAttribute('data-video')) {
                    playButton.setAttribute('data-video', videoUrl);
                }
                console.log('Triggering play button click');
                playButton.click();
            } else {
                console.error('Play button not found');
            }
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

    // Переключение вкладок - упрощенная версия
    console.log('Setting up tabs...');
    
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    console.log('Found buttons:', tabButtons.length, 'contents:', tabContents.length);

    tabButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            const tabId = this.getAttribute('data-tab');
            console.log('Switching to tab:', tabId);
            
            // Убираем активный класс со всех элементов
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Добавляем активный класс к выбранным элементам
            this.classList.add('active');
            const targetContent = document.getElementById(tabId);
            if (targetContent) {
                targetContent.classList.add('active');
                console.log('Tab switched to:', tabId);
            }
        });
    });
    
    console.log('Tabs setup complete');
});