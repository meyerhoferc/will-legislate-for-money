
function displayTweets(){
  $('#tweet-box').html('')
  let twitterId = this.getAttribute('data-twitter-id')
  let tweetLink = `<a class="twitter-timeline" data-width="450" href="https://twitter.com/${twitterId}">Tweets by ${twitterId}</a>`
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

$(document).ready(function(){
  $('.display-tweets').on('click', displayTweets)
  $('.unfollow-button').on('click', unfollowLegislator)

});
