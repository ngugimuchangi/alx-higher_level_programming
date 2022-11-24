// Adds class to header tag
$(() => {
  $('div#red_header').bind('click', () => {
    if (!$('header').hasClass('red')) $('header').addClass('red');
  });
});
