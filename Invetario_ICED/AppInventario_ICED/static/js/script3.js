alert("holaa")

    // Obtén una referencia al botón y al modal
    var openModalBtn = document.getElementById("openModalBtn");
    var modal = document.getElementById("myModal2");

    // Agrega un evento de escucha al botón para abrir el modal
    openModalBtn.addEventListener("click", function() {
        modal.style.display = "block"; // Muestra el modal
    });

    // Busca el botón de cierre en el modal y agrega un evento de escucha para cerrar el modal
    var closeBtn = modal.querySelector(".close2");
    closeBtn.addEventListener("click", function() {
        modal.style.display = "none"; // Cierra el modal
    });

