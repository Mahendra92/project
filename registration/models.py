import uuid
from datetime import datetime 
from django.db import models

class HubreeUser(models.Model):
    userid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.TextField()
    firstname = models.TextField()
    lastname = models.TextField()
    contact = models.TextField()
    pincode = models.TextField()
    #gender = models.TextField()
    password = models.TextField()
    verificationstatus = models.BooleanField(default=False)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True)
