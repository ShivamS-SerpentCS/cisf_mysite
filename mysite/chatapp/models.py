from django.db import models

# Create your models here.

# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(blank=False, max_length=20)
    email_id = models.CharField(blank=True,null=True, max_length=250)
    messager = models.CharField(blank=True,null=True, max_length=250)
    phone = models.CharField(blank=True,null=True,max_length=250)
    # phone = PhoneNumberField(blank=True, null=True)
    # verification = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " Allocation: " + str(self.email_id) + "%"
    
    
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
    
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title    