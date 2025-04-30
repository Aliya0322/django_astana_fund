document.addEventListener('DOMContentLoaded', function() {
    // Функция для фильтрации проектов
    function filterProjects(category) {
        const projectCards = document.querySelectorAll('.project-card');

        projectCards.forEach(card => {
            if (category === 'all' || card.dataset.category === category) {
                card.style.display = 'block';
            } else {
                card.style.display = 'none';
            }
        });
    }

    // Обработчики для кнопок фильтрации
    const filterButtons = document.querySelectorAll('.filter-btn');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Удаляем активный класс у всех кнопок
            filterButtons.forEach(btn => btn.classList.remove('active'));

            // Добавляем активный класс текущей кнопке
            this.classList.add('active');

            // Фильтруем проекты
            const filterValue = this.dataset.filter;
            filterProjects(filterValue);
        });
    });

    // Инициализация - показываем все проекты при загрузке
    filterProjects('all');

    // Анимация карточек при прокрутке
    const animateOnScroll = function() {
        const projectCards = document.querySelectorAll('.project-card');
        const windowHeight = window.innerHeight;

        projectCards.forEach((card, index) => {
            const cardPosition = card.getBoundingClientRect().top;
            const animationPoint = windowHeight - 100;

            if (cardPosition < animationPoint && card.style.opacity !== '1') {
                // Задержка для последовательного появления
                card.style.transitionDelay = `${index * 0.1}s`;
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }
        });
    };

    // Настройка Intersection Observer для анимации
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);

    document.querySelectorAll('.project-card').forEach(card => {
        observer.observe(card);
    });

    // Обработчик события прокрутки
    window.addEventListener('scroll', animateOnScroll);
    // Инициализация при загрузке
    animateOnScroll();
});