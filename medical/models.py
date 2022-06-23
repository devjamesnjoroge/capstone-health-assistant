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