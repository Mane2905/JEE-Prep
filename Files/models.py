from django.db import models
from datetime import datetime
class files(models.Model):
    N=models.IntegerField()
    chapter = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    pdf = models.FileField(upload_to='static/media')
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.chapter