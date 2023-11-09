from django.db import models

class SchedulerInterval(models.Model):
    interval = models.PositiveIntegerField(verbose_name='Interval (seconds)')

    def __str__(self):
        return f'{self.interval} seconds'
    

class CryptoNews(models.Model):
    crypto_name = models.CharField(max_length=200, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    
    def __str__(self):
        return self.title



