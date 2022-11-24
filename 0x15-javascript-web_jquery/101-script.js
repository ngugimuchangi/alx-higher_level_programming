// Appends: list item when add_item is clicked
// Removes:
// 1. last list item when remove_item is clicked
// 2. all list item s when clear list is clicked
$(() => {
  const data = '<li>Item</li>';
  $('div#add_item').bind('click', () => {
    $('ul.my_list').append(data);
  });
  $('div#remove_item').bind('click', () => {
    $('ul.my_list li').remove(':last-child');
  });
  $('div#clear_list').bind('click', () => {
    $('ul.my_list').empty();
  });
});
