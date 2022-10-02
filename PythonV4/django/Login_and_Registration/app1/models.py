from django.db import models
import re
import bcrypt
import datetime
# Create your models here.
class RegistrationManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"
        if len(postData['email']) == 0:
            errors ['register_email'] = "You must enter an email"
        elif not EMAIL_REGEX.match(postData['email']):
            errors['register_email'] = ("Invalid email address!")
        current_users = Registration.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors['register_email'] = "That email already exists"
        if len(postData['password']) < 8:
            errors['register_password'] = "Password should be at least 8 characters"
        elif postData['password'] != postData['confirm_password']:
            errors['register_password'] = "Passwords do not match"
        if postData['birthday'] > str(datetime.date.today()):
            errors["birthday"] = "The birthday should be before this day"
        return errors

    

class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    birthday= models.DateField(null=True)
    objects = RegistrationManager()
