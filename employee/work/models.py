from django.db import models
# Create your models here.

class Employee(models.Model):
    uname=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    place=models.CharField(max_length=30)
    email=models.EmailField(null=True)

    def __str__(self):
        return self.uname

    


class student(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    age=models.PositiveIntegerField()
    gender=models.CharField(max_length=30)   

    def __str__(self):
        return self.name
    def __str__(self):
        return self.place
    def __str__(self):
        return self.gender
    
    
    

class Emp(models.Model):
     name=models.CharField(max_length=20)
     place=models.CharField(max_length=20)
     salary=models.PositiveIntegerField()
     contact=models.CharField(max_length=20)


class book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    publication_year=models.PositiveIntegerField()
    genre=models.CharField(max_length=30)    

    def __str__(self):
         return self.title
    


class Movies(models.Model):
    name=models.CharField(max_length=30)
    year=models.PositiveIntegerField()
    category=models.CharField(max_length=30)
    review=models.CharField(max_length=30)



class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=False,null=True)
    course=models.CharField(max_length=30)


class Mobile(models.Model):
    name=models.CharField(max_length=30)
    price=models.PositiveIntegerField()
    colour=models.CharField(max_length=30)

class Students(models.Model):
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    course=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    place=models.CharField(max_length=30)    

    def __str__(self):
        return self.name



 








