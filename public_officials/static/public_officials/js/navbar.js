
function makeNavBarAccessible(){
  $('.navbar-nav>li>a, navbar>a').css({'color': 'black', 'font-size': '12pt'})
  $('.navbar-brand').css('color', 'black')
  $('.navbar-nav>li, .navbar-brand').hover(function(){
    $(this).css({'background-color': "#ADD8E6", "font-weight": "bold"})
  }).mouseout(function(){
    $(this).css({'background-color': "#F8F8F8", "font-weight": "normal"})
  })
}

$(document).ready(function(){

  makeNavBarAccessible()
});
