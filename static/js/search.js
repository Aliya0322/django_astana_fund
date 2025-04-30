document.addEventListener('DOMContentLoaded', function () {
    const searchButton = document.getElementById('search-button');
    const searchWrapper = document.querySelector('.search-wrapper');
    const searchContainer = document.getElementById('search-container');
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');

    // Показать/скрыть форму поиска по клику на кнопку поиска
    searchButton.addEventListener('click', function (e) {
        e.preventDefault(); // Остановить переход по ссылке
        searchWrapper.classList.toggle('active'); // Переключить класс для отображения

        if (searchWrapper.classList.contains('active')) {
            searchInput.focus(); // Фокусируем на поле ввода, если форма открыта
        } else {
            searchInput.value = ''; // Если форма скрыта, очищаем поле ввода
            searchResults.innerHTML = ''; // И очищаем результаты
        }
    });

    // Поиск по Enter
    searchInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            const query = searchInput.value.trim();
            if (!query) return; // Если строка пуста, ничего не делаем

            // Здесь будет ваш запрос к серверу
            fetch(`/search/?q=${encodeURIComponent(query)}`)
                .then(response => response.json())
                .then(data => {
                    searchResults.innerHTML = ''; // Очищаем результаты перед новыми
                    if (data.results.length > 0) {
                        data.results.forEach(item => {
                            const div = document.createElement('div');
                            div.classList.add('search-result');
                            div.innerHTML = `<a href="${item.url}">[${item.type.toUpperCase()}] ${item.title}</a>`;
                            searchResults.appendChild(div);
                        });
                    } else {
                        searchResults.innerHTML = '<p>Ничего не найдено</p>';
                    }
                })
                .catch(err => {
                    console.error('Ошибка поиска:', err);
                });
        }
    });
});


