// Updates header content on click
$(() => {
  $('div#update_header').bind('click', () => {
    $('header').text('New Header!!!');
  });
});
