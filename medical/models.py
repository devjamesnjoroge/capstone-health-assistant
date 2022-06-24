from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('images')
    age = models.PositiveIntegerField()
    bio = models.TextField(max_length=100)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __repr__(self):
        print(self.user.username)

class MedicalHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    disease_diagnosed = models.TextField(max_length=100)
    disease_treatment = models.TextField(max_length=100)
    age_diagnosed = models.PositiveIntegerField()
    lab_results = models.TextField(max_length=100)
    recurrency = models.TextField(max_length=100)

    def save_medical_history(self):
        self.save()

    def delete_medical_history(self):
        self.delete()

    def __repr__(self):
        print(self.user.username)

class Diet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    carbohydrates = models.TextField(max_length=100)
    proteins = models.TextField(max_length=100)
    vitamins = models.TextField(max_length=100)
    junk = models.TextField(max_length=100)
    water_litres = models.PositiveIntegerField()

    def save_diet(self):
        self.save()

    def delete_diet(self):
        self.delete()

    def __repr__(self):
        print(self.user.username)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.TextField(max_length=100)
    image = CloudinaryField('images', null = True, blank = True)

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __repr__(self):
        print(self.user.username)