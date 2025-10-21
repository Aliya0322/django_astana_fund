document.addEventListener('DOMContentLoaded', function() {
    const menuIcon = document.getElementById('menu-icon');
    const navLinks = document.getElementById('nav-links');
    
    if (menuIcon && navLinks) {
        menuIcon.addEventListener('click', function() {
            navLinks.classList.toggle('active');
            menuIcon.classList.toggle('active');
            
            // Получаем иконку внутри кнопки
            const iconElement = menuIcon.querySelector('i');
            
            if (navLinks.classList.contains('active')) {
                // Меню открыто - меняем на крестик
                if (iconElement) {
                    iconElement.className = 'fa-solid fa-times';
                }
            } else {
                // Меню закрыто - меняем на гамбургер
                if (iconElement) {
                    iconElement.className = 'fa-solid fa-bars';
                }
            }
        });
    }
});