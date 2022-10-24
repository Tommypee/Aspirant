from django.db import models

from general.models import CustomUser

# Create your models here

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

def __str__(self):
    return self.name

class Ssce(models.Model):
    SUBJECT_TYPE = (("Eng", "English"), ("Math", "Mathematics"),("che", "Chemistry"),("Phy", "Physics"),("Bio", "Biology"),("civic", "Civic Education"),("Gov", "Government"),("eco", "Economics"),("com", "Commerce"),("acc", "Financial Accounting"), ("Liter", "Literature_in_English"),("Agric", "Agricultural Science"))
    GRADE_TYPE =   (("A1", "A1"), ("B2", "B2"),("B3", "B3"),("C4", "C4"),("C5", "C5"),
              ("C6", "C6"),("D7", "D7"),("E8", "E8"), ("E8", "E8"),("F9", "F9"),)
    subject_type = models.CharField(max_length=50, choices=SUBJECT_TYPE)
    grade_type = models.CharField(max_length=50,choices=GRADE_TYPE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

def __str__(self):
    return self.SUBJECT_TYPE