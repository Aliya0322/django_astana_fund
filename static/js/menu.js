document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const navLinks = document.getElementById("nav-links");

    menuIcon.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });

    document.querySelectorAll("#nav-links a").forEach(link => {
        link.addEventListener("click", function () {
            navLinks.classList.remove("active");
        });
    });
});