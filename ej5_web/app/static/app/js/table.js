$(document).ready(() => {
    var columns = []

    $('th').each((i, el) => {
        columns.push({ data: $(el).data('name') });
    });

  $('#tabela').DataTable({
    "ajax": $('#tabela').data('json'),
    "columns": columns,
    "scrollX": true,
    "scrollY": 700,
    "scrollCollapse": true,
    "dom": 'Bfrtip',
    "buttons": [
      {
        extend: 'collection',
        text: 'Exportar',
        buttons: [ 'csv' ]
      }
    ],
    "lengthMenu": ["15", "30", "50", "100"]
  });
});

$('#back-btn').on('click', () => {
  window.location = 'http://ej5-16.thunderatz.org/';
});
