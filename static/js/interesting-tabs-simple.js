// Простой скрипт для переключения табов
console.log('Simple tabs script loaded');

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded, setting up tabs');
    
    // Находим все кнопки табов
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');
    
    console.log('Found buttons:', tabButtons.length);
    console.log('Found contents:', tabContents.length);
    
    // Проверяем каждый элемент
    tabButtons.forEach((btn, i) => {
        console.log(`Button ${i}:`, btn.textContent, btn.getAttribute('data-tab'));
    });
    
    tabContents.forEach((content, i) => {
        console.log(`Content ${i}:`, content.id, content.classList.contains('active'));
    });
    
    // Добавляем обработчики
    tabButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Button clicked:', this.textContent);
            
            const tabId = this.getAttribute('data-tab');
            console.log('Target tab:', tabId);
            
            // Убираем активный класс со всех кнопок
            tabButtons.forEach(btn => {
                btn.classList.remove('active');
            });
            
            // Убираем активный класс со всего контента
            tabContents.forEach(content => {
                content.classList.remove('active');
            });
            
            // Добавляем активный класс к текущей кнопке
            this.classList.add('active');
            
            // Находим и активируем соответствующий контент
            const targetContent = document.getElementById(tabId);
            if (targetContent) {
                targetContent.classList.add('active');
                console.log('Tab activated:', tabId);
                
                // Проверяем CSS состояние
                setTimeout(() => {
                    const computedStyle = getComputedStyle(targetContent);
                    console.log('CSS check for', tabId, ':', {
                        hasActiveClass: targetContent.classList.contains('active'),
                        computedDisplay: computedStyle.display,
                        computedVisibility: computedStyle.visibility,
                        computedOpacity: computedStyle.opacity
                    });
                }, 50);
            } else {
                console.error('Content not found for tab:', tabId);
            }
        });
    });
    
    console.log('Tab handlers set up');
});
