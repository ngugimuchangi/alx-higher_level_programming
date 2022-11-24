// Adds click event listener to button to send ajax requests
// NB: The endpoint https://fourtonfish.com/hellosalut/
//     has change to: https://stefanbohacek.com/hellosalut/
$(() => {
  $('input#btn_translate').bind('click', () => {
    const language = $('input#language_code').val();
    const url = 'https://stefanbohacek.com/hellosalut/?lang=' + language;
    $.ajax({
      type: 'GET',
      url: url,
      success: (data) => $('div#hello').text(data.hello)
    });
  });
});
