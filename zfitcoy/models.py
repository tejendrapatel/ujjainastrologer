from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from djrichtextfield.models import RichTextField


class Shop(models.Model):
    name =  models.CharField(max_length=50)
    detail = models.TextField(null=True,max_length=300)
    image = models.FileField(null=True)
    Orginal_price = models.TextField(null=True)
    Discount_price = models.TextField(null=True)
    Discountpercent = models.TextField(null=True)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name =  models.CharField(null=True,max_length=50)
    email = models.EmailField(null=True)
    message =  models.TextField(null=True)
    def __str__(self):
        return self.name


class Team(models.Model):
    name =  models.CharField(null=True,max_length=50)
    post =  models.CharField(null=True,max_length=50)
    detail = models.CharField(null=True,max_length=300)
    image = models.FileField(null=True)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    name =  models.CharField(max_length=50)
    email = models.EmailField(null=True)
    mobile = IntegerField(null=True)
    gender =  models.CharField(max_length=50)
    Time_of_day =  models.CharField(max_length=50)
    Way_to_reach =  models.CharField(max_length=50)
    date =  models.DateField(max_length=50)
    time =  models.TimeField(max_length=50)
    Address = models.CharField(max_length=200,null=True)
    Reason_for_appointment = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Services(models.Model):
    name =  models.CharField(null=True,max_length=50)
    detail = models.CharField(null=True,max_length=500)
    discription = RichTextField(null=True)
    image = models.FileField(null=True)
    date = models.DateField(auto_now=True)
    def __str__(self):
        return self.name


class Appionment(models.Model):
    name =  models.CharField(null=True,max_length=50)
    image = models.FileField(null=True)
    mobile = IntegerField(null=True)
    time = models.CharField(null=True,max_length=500)
    message =  models.TextField(null=True)
    def __str__(self):
        return self.name

class Rashi(models.Model):
    name =  models.CharField(null=True,max_length=50)
    image = models.FileField(null=True)
    detail = RichTextField(null=True)
    def __str__(self):
        return self.name

class About(models.Model):
    image = models.FileField(null=True)
    description =  models.TextField(null=True)


class Newsletter(models.Model):
    email = models.EmailField(null=True)
    def __str__(self):
        return self.email



class Demo_Images(models.Model):
    image = models.FileField(null=True)


class SERVICE_CONTACT(models.Model):
    name =  models.CharField(null=True,max_length=50)
    email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    age =  models.IntegerField(null=True)
    message =  models.TextField(null=True)
    def __str__(self):
        return self.name

class TERMS_CONDITIONSs(models.Model):
    cont = RichTextField(null=True)

class PRIVACY_POLICYs(models.Model):
    cont = RichTextField(null=True)


class COMPANEY_SUPPORTS(models.Model):
    cont = RichTextField(null=True)

class WHY_CHOOSE_Us(models.Model):
    cont = RichTextField(null=True)

class Water(models.Model):
    cont = RichTextField(null=True)

class Fire(models.Model):
    cont = RichTextField(null=True)

class Body_Typess(models.Model):
    cont = RichTextField(null=True)

class Air(models.Model):
    cont = RichTextField(null=True)

class Earth(models.Model):
    cont = RichTextField(null=True)

class Space(models.Model):
    cont = RichTextField(null=True)

class faqss(models.Model):
    quction =  models.CharField(null=True,max_length=50)
    answer = models.TextField(null=True)

class MCQQUCTIONS(models.Model):
    quctions = models.TextField(max_length=200,null=True,blank=True)
    choice1 = models.CharField(max_length=200,null=True,blank=True)
    choice2 = models.CharField(max_length=200,null=True,blank=True)
    choice3 = models.CharField(max_length=200,blank=True,null=True)
    choice4 = models.CharField(max_length=200,blank=True,null=True)
    def __str__(self):
        return self.quctions

class MCQUSER(models.Model):
    name = models.CharField(max_length=100,null=True)
    email = models.EmailField(null=True)
    mobile = models.IntegerField(null=True)
    def __str__(self):
        return self.name

class MCQANSWERS(models.Model):
    categorys = models.ForeignKey(MCQUSER, on_delete=models.CASCADE, null=True)
    quctions = models.TextField(max_length=200,null=True)
    choice1 = models.CharField(max_length=200,null=True)
    

class QuesModel(models.Model):
    question = models.CharField(max_length=200,null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.question