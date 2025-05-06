from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class FavoriteLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('user', 'location')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username}'s favorite: {self.location}"

    @classmethod
    def add_favorite(cls, user, location):
        """Add a favorite location if it doesn't exist, or update the existing one."""
        favorite, created = cls.objects.get_or_create(
            user=user,
            location=location,
            defaults={'created_at': timezone.now()}
        )
        return favorite, created


class FarmerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_location = models.CharField(max_length=100, blank=True, null=True)
    farm_size = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    crops = models.CharField(max_length=200, blank=True)
    irrigation_system = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s farmer profile"

class PilotProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_location = models.CharField(max_length=100, blank=True, null=True)
    license_number = models.CharField(max_length=50, blank=True)
    aircraft_type = models.CharField(max_length=100, blank=True)
    flight_hours = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s pilot profile"

class WeatherAlert(models.Model):
    SEVERITY_CHOICES = [
        ('info', 'Information'),
        ('warning', 'Warning'),
        ('danger', 'Danger'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    location = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.location}"

class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    elevation = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SoilMoistureData(models.Model):
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)
    date = models.DateField()
    moisture_level = models.DecimalField(max_digits=5, decimal_places=2)
    depth = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('station', 'date', 'depth')

    def __str__(self):
        return f"{self.station.name} - {self.date} - {self.depth}m"

class FlightCondition(models.Model):
    airport = models.CharField(max_length=100)
    visibility = models.CharField(max_length=50)
    wind_speed = models.CharField(max_length=50)
    wind_direction = models.CharField(max_length=50)
    ceiling = models.CharField(max_length=50)
    temperature = models.DecimalField(max_digits=4, decimal_places=1)
    pressure = models.DecimalField(max_digits=6, decimal_places=1)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.airport} - {self.updated_at}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a basic profile for new users
        if instance.email.endswith('@farmer.com'):
            FarmerProfile.objects.create(user=instance)
        elif instance.email.endswith('@pilot.com'):
            PilotProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'farmerprofile'):
        instance.farmerprofile.save()
    if hasattr(instance, 'pilotprofile'):
        instance.pilotprofile.save()