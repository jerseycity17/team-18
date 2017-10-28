from django.db import models
# Leverage Django's built-in User models
from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    user =  models.ForeignKey(User, null=True, blank=True)
    firstName = models.CharField(max_length=128, null=False, blank=False)
    lastName = models.CharField(max_length=128, null=False, blank=False)
    affiliateCounty = models.CharField(max_length=128, null=False, blank=False)

    def __str__(self):
        """this sets the default return for this object"""
        return self.description

class caseManagerClient(models.Mode):
     fName = models.ForeignK
