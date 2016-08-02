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
  $('h3').removeClass('highlight');
  $(this).find('h3').addClass('highlight');

  $('.info').remove();
  $(this).after('<section class="info"></section>')

  var thisApi = $(this).attr('id');
  $('.info').html('<p>This is the ' + thisApi + ' API list</p>');
  $('.info').addClass('open');
});

$('#anchor').on('click', '.info', function() {
  console.log('click');
  $(this).toggleClass('open');
});

});