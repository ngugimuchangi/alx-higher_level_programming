// Makes an ajax call to hellosaulut api
// NB: The endpoint https://fourtonfish.com/hellosalut/
//     has change to: https://stefanbohacek.com/hellosalut/
//     Using the former will yield a CORS error
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://stefanbohacek.com/hellosalut/?lang=fr',
    success: (data) => $('div#hello').text(data.hello)
  });
});
