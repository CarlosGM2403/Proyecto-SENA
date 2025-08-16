//Inicio Sesión

document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("login-form");

    form.addEventListener("submit", function (e) {
        e.preventDefault(); 
        const email = document.getElementById("floatingInput").value.trim();
        const password = document.getElementById("floatingPassword").value.trim();

        if (!email || !password) {
            Swal.fire({
                icon: "warning",
                title: "Campos incompletos",
                text: "Por favor, complete todos los campos antes de continuar.",
                confirmButtonText: "Entendido"
            });
        } else {
            form.submit(); 
        }
    });
//Olvidé mi Contraseña
        const forgotForm = document.getElementById("forgot-form");
        
    if (forgotForm) {
        forgotForm.addEventListener("submit", function (e) {
            const email = document.getElementById("forgotEmail").value.trim();

            if (!email) {
                e.preventDefault();
                Swal.fire({
                    icon: "warning",
                    title: "Campo vacío",
                    text: "Por favor, ingrese su correo electrónico.",
                    confirmButtonText: "Entendido"
                });
            }
        });
    }
});
