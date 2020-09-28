$(function () {
  // Remove button click
  $(document).on(
    'click',
    '#button-remove',
    function (e) {
      e.preventDefault();
      $(this).closest('.form-inline').remove();
    }
  );
  // Add button click
  $(document).on(
    'click',
    '#button-add',
    function (e) {
      e.preventDefault();
      let container = $(this).closest('[data-role="dynamic-fields"]');
      let new_field_group = container.children().filter('.form-inline:first-child').clone();
      new_field_group.find('input').each(function () {
        $(this).val('');
      });
      container.append(new_field_group);
    }
  );
});
