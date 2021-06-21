from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    Profile_picture = models.ImageField(null=True, blank=True, upload_to="ProfilePictures/")
    def __str__(self):
        return (str(self.first_name) + " " + str(self.last_name) + " | @" + str(self.user))
    class Meta:
        ordering = ("first_name", "last_name", "user", "email")

class Airport(models.Model):
    city = models.CharField(max_length=50)
    airportname = models.CharField(max_length=50)
    airportLatitude = models.FloatField(max_length=10, null=False, blank=False)
    airportLongitude = models.FloatField(max_length=10, null=False, blank=False)
    def __str__(self):
        return self.city
    class Meta:
        ordering = ("city", "airportname")
        verbose_name_plural = "Airports"


class flightbookingshistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    journey = models.CharField(max_length = 500, null = True)
    journeydate = models.CharField(max_length = 50, null=True)
    bookedon = models.CharField(max_length = 50, null=True)
    category = models.CharField(max_length = 30, null = True)
    total_price = models.IntegerField(null = True)
    def __str__(self):
        return str(self.user)
    

class User_querie(models.Model):
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=250)
    messsage = models.TextField(max_length=10000)
    def __str__(self):
        return str(self.email) + " " + str(self.subject)
    class Meta:
        verbose_name_plural = "Customer Queries"


class state(models.Model):
    state = models.CharField(primary_key=True, max_length=100)
    slug = models.SlugField(max_length=100, default='state')
    header_image = models.ImageField(null=True, blank=True, upload_to="statesimg")
    def __str__(self):
        return str(self.state)

category = (
    ('Heritage', 'Heriatge'),
    ('Outdoors & Adventures', 'Outdoors & Adventures'),
    ('Shopping & Nightlife', 'Shopping & Nightlife'),
)

class Points_of_Interest(models.Model):
    State_name = models.ForeignKey(state, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, default='state')
    Point_of_interest = models.CharField(max_length=100, null=True)
    poislug = models.SlugField(max_length=100, null=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="POIs")
    category = models.CharField(max_length=50, choices=category)
    Short_Description = models.TextField(max_length=300, default='', help_text='Write a short catchy description about the POI in 100 words max')
    city = models.CharField(max_length=50, default='')
    Description = models.TextField(max_length=2000, default='', help_text='500 words max')
    Latitude = models.FloatField()
    Longitude = models.FloatField()
    Tips = models.TextField(max_length=500, default='')
    Entry_fees_Adults = models.CharField(max_length=50, default='')
    Entry_fees_Children = models.CharField(max_length=50, default='')
    Transport_methods = models.TextField(max_length=300, default='')
    Suggestions = models.TextField(max_length=500, default='', help_text='Suggest something about the place. Example: The best food to try around this area (or) other places of interests around (or) Visitors food is not allowed')
    def __str__(self):
        return (self.Point_of_interest)
    
    




