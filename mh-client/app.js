$(function() {
// compile template
$.get('templates/panel.handlebars', function(data) {
  categories.forEach(function(cat) {
    var compiled = Handlebars.compile(data);
    var html = compiled(cat);
    $('#anchor').append(html);
  });
});

$('#anchor').on('click', '.panel', function() {
  $('.info').hide();
  $(this).children('.info').show();
  $('h3').removeClass('highlight');
  $(this).find('h3').addClass('highlight');
});

});