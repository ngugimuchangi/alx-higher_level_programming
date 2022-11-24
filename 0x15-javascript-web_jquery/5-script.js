// Updates unorderd list items on click
$(() => {
  $('div#add_item').bind('click', () => {
    $('ul.my_list').append('<li>Item</li>');
  });
});
