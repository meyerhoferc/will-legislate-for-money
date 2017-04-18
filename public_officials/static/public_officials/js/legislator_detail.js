var getIndustryContributors = function(id){
  $.get('/legislators/industry-contributions/', {legislator_id: id}, function(data){
    $('.industry-contributors').html(data);
  });
}
$(document).ready(function(){
  var legislator_id = $('.legislator').attr('data-legislator-id');
  getIndustryContributors(legislator_id);
  // getOrganizationContributors(legislator_id);
});
