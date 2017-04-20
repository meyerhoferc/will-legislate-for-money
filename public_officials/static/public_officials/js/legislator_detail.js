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

var getSponsoredBills = function(id){
  $.get('/legislators/sponsored-bills', {legislator_id: id}, function(bills){
    $.each(bills, function(index, bill){
      $('#sponsored-bills').append(
        "<tr><td><h6><a href='"
        + bill.congressdotgov_url
        + "'>"
        + bill.title
        + "</a><//h6></td><td><p>"
        + bill.introduced_date
        + "</p></td></tr>"
      )
    })
  });
};

$(document).ready(function(){
  $('#tabs').tabs();
  var legislator_id = $('.legislator').attr('data-legislator-id');
  var legislator_pid = $('.legislator').attr('data-legislator-pid');
  getOrganizationContributors(legislator_id);
  getIndustryContributors(legislator_id);
  getSponsoredBills(legislator_pid);
});
