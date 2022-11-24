// Toggles 'red' and 'green' classes in header tag accordingly
$(() => {
  $('div#toggle_header').bind('click', () => {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else if (header.hasClass('green')) {
      header.removeClass('green');
      header.addClass('red');
    } else {
      header.addClass('red');
    }
  });
});
