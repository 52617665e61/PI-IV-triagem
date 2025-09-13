// static/js/pages/registro.js

document.addEventListener("DOMContentLoaded", function () {
    const cards = document.querySelectorAll('.card');
    const btnVoltar = document.getElementById('voltar-btn')?.querySelector('button');

    // Clica em "Sou Paciente" ou "Sou Psicólogo" → redireciona com ?tipo=...
    cards.forEach(card => {
        card.addEventListener('click', () => {
            const tipo = card.dataset.tipo;
            const url = new URL(window.location.href);
            url.searchParams.set("tipo", tipo);
            window.location.href = url.toString();
        });
    });

    // Botão "voltar" → remove o parâmetro "tipo" e recarrega a tela
    btnVoltar?.addEventListener('click', () => {
        const url = new URL(window.location.href);
        url.searchParams.delete("tipo");
        window.location.href = url.pathname; // remove query string
    });
});
