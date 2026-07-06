function init() {
    const confirmLinks = document.querySelectorAll('.confirm-pedido');
    confirmLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            const produtoName = this.dataset.produtoName || 'este produto';
            if (!confirm(`Deseja enviar um pedido ao fornecedor para ${produtoName}?`)) {
                event.preventDefault();
            }
        });
    });

    const messageField = document.getElementById('message');
    const counter = document.getElementById('message-count');
    if (messageField && counter) {
        const updateCounter = function() {
            counter.textContent = `${messageField.value.length} caracteres`;
        };
        updateCounter();
        messageField.addEventListener('input', updateCounter);
    }

    // Lógica do modo escuro
    const themeToggleBtn = document.getElementById('theme-toggle');

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', function() {
            const isDark = document.documentElement.classList.toggle('dark-mode');
            document.body.classList.toggle('dark-mode', isDark);
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
