// Makes an ajax call to hellosaulut api
$(() => {
  $.ajax({
    type: 'GET',
    url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    success: (data) => $('div#hello').text(data.hello)
  });
});
