var getIndustryContributors = function(id){
  $.get('/legislators/industry-contributions/', {legislator_id: id}, function(data){
    if (data == "empty") {
      $('.industry-contributors').html('')
      $('.industry-contributors').append(
        "<h3 class='text-center'>No Data Available Yet</h3>"
      );
    } else {
      industryDonationsChart(data)
      totalDonationsChart(data)
      $.each(data, function(index, industry){
        $('#industry-data').append(
          "<tr><td><h5>"
          + industry['@attributes'].industry_name
          + "</h5></td><td><p>$"
          + industry['@attributes'].total
          + "</p></td><td><p>$"
          + industry['@attributes'].indivs
          + "</p></td><td><p>$"
          + industry['@attributes'].pacs
          + "</p></td></tr>"
        )
      });
    }
  });
};

var totalDonationsChart = function(info){
  var data = []
  var indiv_total = []
  var pac_total = []
  info.forEach(function(industry){
    var indiv = parseInt(industry['@attributes'].indivs)
    var pacs = parseInt(industry['@attributes'].pacs)
    indiv_total.push(indiv)
    pac_total.push(pacs)
  })
  var indiv_sum = ["Individual Donations", (indiv_total.reduce((a, b) => a + b, 0))]
  var pac_sum = ["Pac Donations", (pac_total.reduce((a, b) => a + b, 0))]
  data.push(indiv_sum)
  data.push(pac_sum)
  new Chartkick.PieChart("total-donations", data)
}

var industryDonationsChart = function(info){
  var data = []
  info.forEach(function (industry){
    var name = industry['@attributes'].industry_name
    var total = industry['@attributes'].total
    var industry = [name, total]
    data.push(industry)
  })
  new Chartkick.PieChart("industry-donations", data)
}

var orgDonationsChart = function(info){
  var data = []
  info.forEach(function (organization){
    var name = organization['@attributes'].org_name
    var total = organization['@attributes'].total
    var org = [name, total]
    data.push(org)
  })
  new Chartkick.PieChart("org-donations", data)
};

var getOrganizationContributors = function(id){
  $.get('/legislators/organization-contributions/', {legislator_id: id}, function(data){
    if (data == "empty") {
      $('.organization-contributors').html('')
      $('.organization-contributors').append(
        "<h3 class='text-center'>No Data Available Yet</h3>"
      );
    } else {
      orgDonationsChart(data);
      $.each(data, function(index, organization){
        $('#organization-data').append(
          "<tr><td><h5>"
          + organization['@attributes'].org_name
          + "</h5></td><td><p>$"
          + organization['@attributes'].total
          + "</p></td><td><p>$"
          + organization['@attributes'].indivs
          + "</p></td><td><p>$"
          + organization['@attributes'].pacs
          + "</p></td></tr>"
        )
      })
    }
  });
};

var getSponsoredBills = function(id){
  $.get('/legislators/sponsored-bills', {legislator_id: id}, function(bills){
    if (bills == "empty") {
      $('.sponsored-bills').html('')
      $('.sponsored-bills').append(
        "<h3 class='text-center'>No Data Available Yet</h3>"
      );
    } else {
      $.each(bills, function(index, bill){
        $('#sponsored-bills').append(
          "<tr><td><h5><a href='"
          + bill.congressdotgov_url
          + "' class='link'>"
          + bill.title
          + "</a><//h5></td><td><p>"
          + bill.introduced_date
          + "</p></td></tr>"
        )
      });
    }
  });
};

var determineTitle = function(vote){
  var title;
  if (vote['bill'].title == undefined ) {
    title = vote.description
  } else {
    title = vote['bill'].title
  }
  return title;
};

var determineQuestion = function(title){
  var proposition;
  if (title == undefined || title == '') {
    proposition = "empty";
  };
  return proposition;
};

var getVotingHistory = function(id){
  $.get('/legislators/voting-history', {legislator_id: id}, function(votes){
    $.each(votes, function(index, vote){
      var title = determineTitle(vote);
      var proposition = determineQuestion(title);
      if (proposition != "empty") {
        $('#votes').append(
          "<tr><td><h5>"
          + title
          + "</h5></td><td><p>"
          + vote.position
          + "</p></td><td class='col-md-2'><p>"
          + vote.result
          + "</p></td></tr>"
        )
      };
    })
  });
};

var followLegislator = function() {
  if ($('.follow').text() == 'Follow') {
    return $('.follow').text('Unfollow')
  }
  $('.follow').text('Follow')
};

$(document).ready(function(){
  $('#tabs').tabs();
  var legislator_id = $('.legislator').attr('data-legislator-id');
  var legislator_pid = $('.legislator').attr('data-legislator-pid');
  getOrganizationContributors(legislator_id);
  getIndustryContributors(legislator_id);
  getSponsoredBills(legislator_pid);
  getVotingHistory(legislator_pid);
  $('.follow').on('click', followLegislator);
});
