// Binds click event listener to an element to change color
$(() => {
  $('div#red_header').bind('click', function () {
    $(this).css('color', '#f00');
  });
});
