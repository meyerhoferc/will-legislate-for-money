var getIndustryContributors = function(id){
  $.get('/legislators/industry-contributions/', {legislator_id: id}, function(data){
    $.each(data, function(index, industry){
      $('#industry-data').append(
        "<tr><td><h6>"
        + industry['@attributes'].industry_name
        + "</h6></td><td><p>$"
        + industry['@attributes'].total
        + "</p></td><td><p>$"
        + industry['@attributes'].indivs
        + "</p></td><td><p>$"
        + industry['@attributes'].pacs
        + "</p></td></tr>"
      )
    });
  });
};

var getOrganizationContributors = function(id){
  $.get('/legislators/organization-contributions/', {legislator_id: id}, function(data){
    $.each(data, function(index, organization){
      $('#organization-data').append(
        "<tr><td><h6>"
        + organization['@attributes'].org_name
        + "</h6></td><td><p>$"
        + organization['@attributes'].total
        + "</p></td><td><p>$"
        + organization['@attributes'].indivs
        + "</p></td><td><p>$"
        + organization['@attributes'].pacs
        + "</p></td></tr>"
      )
    })
  });
};

var industryCounter = 0;
var organizationCounter = 0;

$(document).ready(function(){
  var legislator_id = $('.legislator').attr('data-legislator-id');
  getIndustryContributors(legislator_id);
  getOrganizationContributors(legislator_id);
});
