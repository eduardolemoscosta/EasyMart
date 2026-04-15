document.addEventListener('DOMContentLoaded', function() {
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
});
