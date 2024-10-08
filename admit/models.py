from django.db import models
from django.core.validators import FileExtensionValidator

class School(models.Model):
    class SchoolType(models.TextChoices):
        MIXED = "mixed","mixed"
        SINGLE = "single","single"
    name = models.CharField(max_length=100)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    website = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    application_fee = models.IntegerField(null=True,blank=True)
    type = models.CharField(max_length=20,choices=SchoolType.choices)

class Applicant(models.Model):
    #gender choices
    class Genders(models.TextChoices):
        MALE = "male","male"
        FEMALE = "female","female"

    name = models.CharField(max_length=250)
    gender = models.CharField(max_length=20,choices=Genders.choices)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    previous_school = models.ForeignKey(School,on_delete=models.CASCADE)
    date_joined_previous_school = models.DateField()
    exam_results = models.FileField(null=True, blank=True, upload_to=f"media/results/{id}", validators=[FileExtensionValidator(["pdf"])])
    testimonial = models.TextField()
    next_class = models.CharField(max_length=50,null=True,blank=True)
    field_of_study = models.CharField(max_length=100, null=True,blank=True)
    Combination = models.CharField(max_length=100, null=True,blank=True)
    

class Application(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending","pending"
        ACCEPTED = "accepted","accepted"
        REJECTED = "rejected","rejected"
    applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20,choices=Status.choices)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    

class Payment(models.Model):
    class Status(models.TextChoices):
        PAID = "paid","paid" 
        UNPAID = "unpaid","unpaid" 
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add = True)
    ammount = models.IntegerField()
    status = models.CharField(max_length=10,choices=Status.choices)