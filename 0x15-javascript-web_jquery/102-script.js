// Adds click event listener to button to send ajax requests
$(() => {
  $('input#btn_translate').bind('click', () => {
    const language = $('input#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + language;
    $.ajax({
      type: 'GET',
      url: url,
      success: (data) => $('div#hello').text(data.hello)
    });
  });
});
