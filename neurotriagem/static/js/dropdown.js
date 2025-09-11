function toggleDropdown(buttonOrImage) {
    const dropdown = buttonOrImage.parentElement;
    dropdown.classList.toggle("show");

    // Fecha os outros dropdowns
    document.querySelectorAll('.dropdown').forEach(el => {
        if (el !== dropdown) {
            el.classList.remove("show");
        }
    });
}

// Fecha dropdowns ao clicar fora
document.addEventListener('click', function(e) {
    if (!e.target.closest('.dropdown')) {
        document.querySelectorAll('.dropdown').forEach(el => el.classList.remove('show'));
    }
});

function handleLogout() {
    const logoutForm = document.getElementById('logout-form');
    if (logoutForm) {
        logoutForm.submit();
    }
}

