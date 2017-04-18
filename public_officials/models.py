from django.db import models

class Legislator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    state_name = models.CharField(max_length=30)
    cid = models.CharField(max_length=30)
    pid = models.CharField(max_length=30)
    chamber = models.CharField(max_length=25)
    term_start = models.CharField(max_length=30)
    term_end = models.CharField(max_length=30)
    party = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    @classmethod
    def get_senators_by_state(self):
        ALL_STATES = ['Alabama', "Alaska", "Arizona", "Arkansas", "California",
        "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii",
        "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"]
        senators_by_state = {}
        for state in ALL_STATES:
            senators = self.objects.filter(state_name=state).filter(chamber="senate")
            senators_by_state[state] = senators
        return senators_by_state

    @classmethod
    def get_representatives_by_state(self):
        ALL_STATES = ['Alabama', "Alaska", "Arizona", "Arkansas", "California",
        "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii",
        "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
        "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
        "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
        "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota",
        "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia",
        "Wisconsin", "Wyoming"]
        representatives_by_state = {}
        for state in ALL_STATES:
            senators = self.objects.filter(state_name=state).filter(chamber="house")
            representatives_by_state[state] = senators
        return representatives_by_state

    @classmethod
    def get_all_state_names(self):
        states = self.objects.values('state_name').distinct('state_name')
        return states
