$(document).ready(function() {
  $('#btn_translate').click(translate);

  $('#language_code').on('keydown', function(event) {
    if (event.key === 'Enter') {
      translate();
    }
  });

  function translate() {
    let languageCode = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function(data) {
      $('DIV#hello').text(data.hello);
    });
  }
  });