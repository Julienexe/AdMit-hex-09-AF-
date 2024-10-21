from django.db import models
from django.core.validators import FileExtensionValidator

class School(models.Model):
    class SchoolType(models.TextChoices):
        MIXED = "mixed","mixed"
        BOYS = "boys","boys"
        GIRLS = "girls","girls"
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
    previous_school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    date_joined_previous_school = models.DateField()
    exam_results = models.FileField(null=True, blank=True, upload_to=f"media/results/{id}", validators=[FileExtensionValidator(["pdf"])])
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
    status = models.CharField(max_length=20,choices=Status.choices, default=Status.PENDING)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    

class Payment(models.Model):
    class Status(models.TextChoices):
        PAID = "paid","paid" 
        UNPAID = "unpaid","unpaid" 
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add = True)
    ammount = models.IntegerField()
    status = models.CharField(max_length=10,choices=Status.choices)

class Testimonial(models.Model):
    #applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="testimonials/" , validators=[FileExtensionValidator(["pdf","docx","doc","jpg","png"])])