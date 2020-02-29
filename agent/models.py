from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo = models.ImageField(upload_to='images/')
    hire_date = models.DateTimeField()
    phone = models.CharField(max_length=20, default=False)
    email = models.CharField(max_length=50, default=False)

    def __str__(self):
        return self.name

    def summary(self):
        return self.description[:100]
    
    def hire_date_convert(self):
        return self.hire_date.strftime('%b %e %Y')

# Add the About app to the settings

# Create a migration

# Migrate 

# Add to the admin

