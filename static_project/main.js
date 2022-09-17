$(document).ready(function () {
  $('.ui.dropdown')
      .dropdown();

  $('.message .close')
      .on('click', function () {
          $(this)
              .closest('.message')
              .transition('fade');
      });

  $('#modle-btn').click(function () {
      $('.ui.modal')
          .modal('show');
  })
  ;
}
)