from django.db import models
import os
import requests
# Create your models here.
class Location(models.Model):

    ENTITY_CHOICES = (
        ('company', 'Company'),
        ('person','Person'),
    )

    entity_id = models.UUIDField() #company or worker id should work
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    entity_type = models.CharField(max_length=7, choices=ENTITY_CHOICES)

    def __str__(self):
        return f'{self.entity_type} Location for {self.entity_id}'

    #find lat and long from Google Maps api
    def fetch_coordinates(self):
        api_key = os.getenv('GOOGLE_API_KEY')

        if not api_key:
            raise ValueError('GOOGLE_API_KEY environment variable is not set')

        address = f'{self.street}, {self.city}, {self.state}'
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'

        response = requests.get(url)
        data = response.json()

        if data['status'] == 'OK':
            self.latitude = data['results'][0]['geometry']['location']['lat']
            self.longitude = data['results'][0]['geometry']['location']['lng']
        else:
            # Handle errors if no result is found
            raise ValueError('Failed to fetch coordinates')

    # Override save method to fetch coordinates before saving
    def save(self, *args, **kwargs):
        # Check if any of the address fields have changed
        if self.pk is not None:
            old_location = Location.objects.get(pk=self.pk)
            if (self.street != old_location.street or
                self.city != old_location.city or
                self.state != old_location.state):
                # If address fields have changed, re-fetch the coordinates
                self.fetch_coordinates()
        else:
            # If this is a new location, fetch the coordinates
            self.fetch_coordinates()

        # Save the location after fetching coordinates
        super().save(*args, **kwargs)
