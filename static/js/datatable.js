$(document).ready(function() {
  $('#example').DataTable({
    language: {
      decimal: "",
      emptyTable: "No hay información",
      info: "Mostrando _START_ a _END_ de _TOTAL_ entradas",
      infoEmpty: "Mostrando 0 entradas",
      infoFiltered: "(filtrado de _MAX_ entradas)",
      infoPostFix: "",
      loadingRecords: "Cargando...",
      processing: "Procesando...",
      search: "Buscar:",
      zeroRecords: "No se encontraron registros",
      lengthMenu: "Mostrar _MENU_ entradas",
      paginate: {
        first: "Primero",
        previous: "Anterior",
        next: "Siguiente",
        last: "Último"
      },
      aria: {
        sortAscending: ": Activar para ordenar la columna en orden ascendente",
        sortDescending: ": Activar para ordenar la columna en orden descendente"
      }
    }
  });
});