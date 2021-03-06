$(function() {
// compile template
$.get('static/JS/templates/panel.handlebars', function(data) {
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
      $.get('static/JS/templates/info.handlebars', function(data) {
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


// $('.copyButton').on('click', function() {
//   console.log('fuck');
//   var thisLink = $(this).prev('input');
//   copyToClipboard(thisLink);
// });

// function copyToClipboard(elem) {
//   var succeed;
//   // elem.setSelectionRange(0, elem.value.length);
//   succeed = document.execCommand("copy");
// }

});
