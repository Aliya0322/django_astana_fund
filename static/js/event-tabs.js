document.addEventListener('DOMContentLoaded', function() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const eventCards = document.querySelectorAll('.event-card');

    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Удаляем active у всех кнопок и добавляем текущей
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter');

            eventCards.forEach(card => {
                if (filterValue === 'all') {
                    card.style.display = 'flex';
                } else {
                    const category = card.getAttribute('data-category');
                    card.style.display = category === filterValue ? 'flex' : 'none';
                }
            });
        });
    });
});