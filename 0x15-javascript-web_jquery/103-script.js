$(document).ready(function() {
    $('#btn_translate').click(function() {
      var languageCode = $('#language_code').val();
      $.ajax({
        url: 'https://www.fourtonfish.com/hellosalut/hello/' + languageCode,
        method: 'GET',
        success: function(data) {
          $('#hello').text(data.hello);
        },
        error: function() {
          $('#hello').text('Error fetching translation');
        }
      });
    });
  
    $('#language_code').keypress(function(event) {
      if (event.keyCode === 13) {
        $('#btn_translate').click();
      }
    });
  });