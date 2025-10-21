document.addEventListener('DOMContentLoaded', function() {
    console.log('=== СКРИПТ МЕНЮ ЗАГРУЖЕН ===');
    
    // Элементы меню
    const nav = document.getElementById('nav-links');
    const menuToggle = document.getElementById('menu-toggle');
    const body = document.body;
    
    if (nav && menuToggle) {
        console.log('Навигационное меню и кнопка найдены');
        
        // Функция для открытия/закрытия меню
        function toggleMenu() {
            const isActive = nav.classList.contains('active');
            
            if (isActive) {
                closeMenu();
            } else {
                openMenu();
            }
        }
        
        // Функция для открытия меню
        function openMenu() {
            nav.classList.add('active');
            menuToggle.classList.add('active');
            body.classList.add('menu-open');
            
            // Блокируем прокрутку страницы
            body.style.overflow = 'hidden';
        }
        
        // Функция для закрытия меню
        function closeMenu() {
            nav.classList.remove('active');
            menuToggle.classList.remove('active');
            body.classList.remove('menu-open');
            
            // Восстанавливаем прокрутку страницы
            body.style.overflow = '';
        }
        
        // Обработчик клика по кнопке меню
        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            toggleMenu();
        });
        
        // Закрытие меню при клике вне его области
        document.addEventListener('click', function(e) {
            if (nav.classList.contains('active')) {
                const isMenuClick = nav.contains(e.target);
                const isToggleClick = menuToggle.contains(e.target);
                
                if (!isMenuClick && !isToggleClick) {
                    closeMenu();
                }
            }
        });
        
        // Закрытие меню при нажатии Escape
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && nav.classList.contains('active')) {
                closeMenu();
            }
        });
        
        // Закрытие меню при клике на ссылку
        const navLinks = nav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                // Небольшая задержка для плавности анимации
                setTimeout(() => {
                    closeMenu();
                }, 100);
            });
        });
        
        // Обработчик изменения размера окна
        window.addEventListener('resize', function() {
            const isMobile = window.innerWidth <= 768;
            
            if (!isMobile && nav.classList.contains('active')) {
                // Если переключились на десктоп, закрываем мобильное меню
                closeMenu();
            }
        });
        
        // Добавляем плавную прокрутку для якорных ссылок
        const anchorLinks = nav.querySelectorAll('a[href^="#"]');
        anchorLinks.forEach(link => {
            link.addEventListener('click', function(e) {
                const href = this.getAttribute('href');
                if (href !== '#' && href.length > 1) {
                    e.preventDefault();
                    const target = document.querySelector(href);
                    if (target) {
                        target.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                });
            }
        }
            });
        });
        
        // Добавляем активный класс при прокрутке (опционально)
        window.addEventListener('scroll', function() {
            const sections = document.querySelectorAll('section[id], .section[id]');
            const scrollPos = window.scrollY + 100;
            
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                const sectionHeight = section.offsetHeight;
                const sectionId = section.getAttribute('id');
                
                if (scrollPos >= sectionTop && scrollPos < sectionTop + sectionHeight) {
                    // Убираем активный класс со всех ссылок
                    nav.querySelectorAll('a').forEach(link => {
                        link.classList.remove('active');
                    });
                    
                    // Добавляем активный класс к соответствующей ссылке
                    const activeLink = nav.querySelector(`a[href="#${sectionId}"]`);
                    if (activeLink) {
                        activeLink.classList.add('active');
            }
        }
    });
        });
        
    } else {
        console.log('Навигационное меню или кнопка не найдены');
    }
});