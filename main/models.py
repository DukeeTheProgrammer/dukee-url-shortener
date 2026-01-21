from django.db import models

class Link(models.Model):
    ip = models.CharField(max_length=200, blank=True)
    requests = models.IntegerField(default=0)
    main_link = models.CharField(max_length=200, blank=True)
    shortened = models.CharField(max_length=200,blank=True)
    useragent = models.CharField(max_length=200, blank=True)
    link_id = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"Shortened Link : {self.shortened}"
