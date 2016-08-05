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
  $(this).find('h3').toggleClass('highlight');

  if (!$(this).next().is('.info')) {
    $(this).next('.info').remove();
    $(this).after('<section class="info"></section>')
  }

  var thisApi = $(this).attr('id').toLowerCase();
  var thisEndpoint = endpoints[thisApi];
  var currentSection = $(this).next('.info');

  if (!currentSection.html()) {

    thisEndpoint.forEach(function(item) {
      $.get('templates/info.handlebars', function(data) {
        var compiled = Handlebars.compile(data);
        var html = compiled(item);
        currentSection.append(html);
      });
    })
  }


    currentSection.slideToggle();
});


$('#anchor').on('click', '.info', function() {
  $(this).toggleClass('open');
});

});
