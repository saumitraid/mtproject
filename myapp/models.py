from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=150, verbose_name='Name of Student')
    smobile=models.CharField(max_length=15, verbose_name='Student Contact Number')
    saddress=models.TextField( verbose_name='Student Address')

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True)
    cat_name=models.CharField(max_length=255, verbose_name='Name of Category')

    def __str__(self):
        return self.cat_name

class Product(models.Model):
    p_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    description=models.TextField()
    price=models.CharField(max_length=15)
    image=models.ImageField(upload_to='products/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Name of Category')
    def __str__(self):
        return self.name
    