
from django.db import models
from django.contrib.auth.models import User
# Django user model
'''
 - username
 - password
'''

class StudentDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname=models.CharField(max_length=30)
    mname=models.CharField(max_length=30)
    rollno=models.IntegerField()
    dob=models.DateTimeField()

class Term1(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField()  
    chem=models.IntegerField()
    math=models.IntegerField()
    comp=models.IntegerField()
    eng=models.IntegerField()

class Term2(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField()
    chem=models.IntegerField()
    math=models.IntegerField()
    comp=models.IntegerField()
    eng=models.IntegerField()

class Finals(models.Model):
    user = models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    rollno=models.IntegerField()
    phy=models.IntegerField()
    chem=models.IntegerField()
    math=models.IntegerField()
    comp=models.IntegerField()
    eng=models.IntegerField()

    

