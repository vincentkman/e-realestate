from django.db import models
import datetime

class Listing(models.Model): 
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
            return self.title

    def summary(self):
        return self.description[:100]
    
    def publish_date_convert(self):
        return self.publish_date.strftime('%b %e %Y')