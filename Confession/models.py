from django.db import models


class myconfessionmodel(models.Model):
    tosendto = models.CharField(max_length=50)
    facultyis = models.CharField(max_length=50)
    confessionmsg = models.TextField()
    youridentification = models.CharField(max_length=50)


class feedbackmodel(models.Model):
    feedbackdetails = models.TextField()
    feedbackprovider = models.CharField(max_length=20)
