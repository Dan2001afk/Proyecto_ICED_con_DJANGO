document.addEventListener('DOMContentLoaded', function() {
    // Obtén una referencia al botón de abrir modal y al modal de actualización
    const openUpdateModalBtn = document.querySelector('.btnInsertar');
    const updateModal = document.getElementById('myModal2');
  
    // Agrega un evento de escucha al botón para abrir el modal de actualización
    openUpdateModalBtn.addEventListener('click', function() {
      updateModal.style.display = 'block'; // Muestra el modal de actualización
    });
  
    // Busca el botón de cierre en el modal de actualización y agrega un evento de escucha para cerrar el modal
    const closeUpdateModalBtn = updateModal.querySelector('.close2');
    closeUpdateModalBtn.addEventListener('click', function() {
      updateModal.style.display = 'none'; // Cierra el modal de actualización
    });
  
    // Agrega eventos de escucha para cambiar el color del cursor al pasar cerca de la "x"
    closeUpdateModalBtn.addEventListener('mouseenter', function() {
      closeUpdateModalBtn.style.color = 'red'; // Cambia el color al pasar cerca del cursor
    });
  
    closeUpdateModalBtn.addEventListener('mouseleave', function() {
      closeUpdateModalBtn.style.color = '#aaa'; // Restaura el color original
    });
  });


//segundo modal

   document.addEventListener('DOMContentLoaded', function() {
  // Obtén una referencia al botón de abrir modal y al modal de actualización
  const openUpdateModalBtn = document.querySelector('.btnActualizar');
  const updateModal = document.getElementById('myModal');

  // Agrega un evento de escucha al botón para abrir el modal de actualización
  openUpdateModalBtn.addEventListener('click', function() {
    updateModal.style.display = 'block'; // Muestra el modal de actualización
  });

  // Busca el botón de cierre en el modal de actualización y agrega un evento de escucha para cerrar el modal
  const closeUpdateModalBtn = updateModal.querySelector('.close');
  closeUpdateModalBtn.addEventListener('click', function() {
    updateModal.style.display = 'none'; // Cierra el modal de actualización
  });

  // Agrega eventos de escucha para cambiar el color del cursor al pasar cerca de la "x"
  closeUpdateModalBtn.addEventListener('mouseenter', function() {
    closeUpdateModalBtn.style.color = 'red'; // Cambia el color al pasar cerca del cursor
  });

  closeUpdateModalBtn.addEventListener('mouseleave', function() {
    closeUpdateModalBtn.style.color = '#aaa'; // Restaura el color original
  });
});

