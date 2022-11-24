// Adds keypress and click event listeners to
// text field and button, respectively, in order
// to send ajax requests
function translate () {
  const language = $('input#language_code').val();
  const url = 'https://www.fourtonfish.com/hellosalut/?lang=' + language;
  $.ajax({
    type: 'GET',
    url: url,
    success: (data) => $('div#hello').text(data.hello)
  });
}
$(() => {
  $('input#language_code').keypress((event) => {
    if (event.which === 13) {
      translate();
    }
  });
  $('input#btn_translate').bind('click', translate);
});
