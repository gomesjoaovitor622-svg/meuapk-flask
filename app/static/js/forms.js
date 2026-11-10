// Progressive enhancement do formulário de login (referência didática).
// A autenticação real é feita pelo próprio formulário: POST /autenticar.
// Nunca registre senha no console.
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('formLogin');
    if (!form) {
        return;
    }

    form.addEventListener('submit', function () {
        const botao = form.querySelector('button[type="submit"]');
        if (botao) {
            botao.disabled = true;
            botao.textContent = 'Entrando...';
        }
    });
});
