$(document).ready(function() {
    $('#btn_translate').click(function() {
      let languageCode = $('#language_code').val();
      $.ajax({
        url: `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`,
        type: 'GET',
        success: function(data) {
          $('#hello').text(data.hello);
        },
        error: function() {
          $('#hello').text('Error fetching translation');
        }
      });
    });
  });