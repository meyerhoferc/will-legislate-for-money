
function displayTweets(){
  $('#tweet-box').html('')
  let twitterId = this.getAttribute('data-twitter-id')
  let tweetLink = `<a class="twitter-timeline" data-width="700" href="https://twitter.com/${twitterId}">Tweets by ${twitterId}</a>`
  $('#tweet-box').append(`<script src="//platform.twitter.com/widgets.js" charset="utf-8"></script>`)
  $('#tweet-box').append(tweetLink)
}

function unfollowLegislator(){
  let legId = this.getAttribute('data-leg-id')
  let uId = this.getAttribute('data-user-id')
  let unfollowButton = $(this)
  removeLegislator(unfollowButton)
  $.post('/remove-follower', {lid: legId, uid: uId})
}

function removeLegislator(unfollowButton){
  unfollowButton.prev().prev().remove()
  unfollowButton.prev().remove()
  unfollowButton.remove()
}

function changeLegislatorHoverColor(){
  $(".list-group-item").hover(function() {
  $(this).css({"background-color": "#ADD8E6", "font-weight": "bold", "color": 'black'})
}).mouseout(function(){
  $(this).css({"background-color": "white", "font-weight": "normal"})
})
}
function makeNavBarAccessible(){
  $('li>a').css({'color': 'black', 'font-size': '12pt'})
  $('.navbar-brand').css('color', 'black')
  $('li, .navbar-brand').hover(function(){
    $(this).css({'background-color': "#ADD8E6", "font-weight": "bold"})
  }).mouseout(function(){
    $(this).css({'background-color': "#F8F8F8", "font-weight": "normal"})
  })
}
$(document).ready(function(){
  $('.display-tweets').on('click', displayTweets)
  $('.unfollow-button').on('click', unfollowLegislator)
  changeLegislatorHoverColor()
  makeNavBarAccessible()
});
