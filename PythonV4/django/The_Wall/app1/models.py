from django.db import models
import re
import bcrypt
import datetime

class userManager(models.Manager):

    def basic_validator(self,postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name should be at least 2 characters"

       
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"

      
        elif len(User.objects.filter(email=postData['email'])) > 0:
            errors['existingEmail'] = "That email already exists"
        
        
        if len(postData['pw']) < 8:
            errors['pw'] = "Password must be at least 8 characters!"
        elif postData['pw'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords do not match"

        return errors

    def login_validator(self,postData):
        errors = {}
       
        user = User.objects.filter(email=postData['email'])
        if len(user) < 1:
            errors['emailDoesNotExist'] = "Email does not exist"

        
        else:
            logged_user = user[0]
            if not bcrypt.checkpw(postData['pw'].encode(), logged_user.password.encode()):
                errors['badPW'] = "Password is incorrect!!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = userManager()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name="users", on_delete = models.CASCADE)
    message = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)