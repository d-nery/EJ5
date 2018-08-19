$(document).ready(() => {
    var columns = []

    $('th').each((i, el) => {
        columns.push({ data: $(el).data('name') });
    });

  $('#tabela').DataTable({
    "ajax": $('#tabela').data('json'),
    "columns": columns,
    "scrollX": true,
  });
});

$('#back-btn').on('click', () => {
  window.location = 'http://127.0.0.1:8000/';
});
