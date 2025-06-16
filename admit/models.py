import datetime
from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class NameStrModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name 


class School(NameStrModel):
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

class Applicant(NameStrModel):
    #gender choices
    class Genders(models.TextChoices):
        MALE = "male","male"
        FEMALE = "female","female"

    name = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField(max_length=20,choices=Genders.choices)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    previous_school = models.ForeignKey(School,on_delete=models.CASCADE,null=True,blank=True)
    date_joined_previous_school = models.DateField()
    exam_results = models.TextField(null=True, blank=True)
    next_class = models.CharField(max_length=50,null=True,blank=True)
    field_of_study = models.CharField(max_length=100, null=True,blank=True)
    Combination = models.CharField(max_length=100, null=True,blank=True)

class ApplicantModel(models.Model):
    """
    Abstract model for any model that needs to be associated with an applicant.
    """
    applicant:Applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    class Meta:
        abstract = True
    
    @property
    def applicant_name(self):
        return self.applicant.name if self.applicant else "No Applicant"
    
    @property
    def applicant_user(self):
        return self.applicant.user
    
    def __str__(self):
        return f"{self.__class__.__name__} for {self.applicant_name}"
    

class Application(ApplicantModel):
    class Status(models.TextChoices):
        PENDING = "pending","pending"
        ACCEPTED = "accepted","accepted"
        REJECTED = "rejected","rejected"
    
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length=20,choices=Status.choices, default=Status.PENDING)
    school = models.ForeignKey(School,on_delete=models.CASCADE)
    

class Payment(ApplicantModel):
    class Status(models.TextChoices):
        PAID = "paid","paid" 
        PENDING = "pending","pending"
        CANCELLED = "cancelled","cancelled"
    ref_id = models.CharField(max_length=100, unique=True,auto_created=True, editable=False,primary_key=True)
    application = models.ForeignKey(Application,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add = True)
    ammount = models.IntegerField()
    status = models.CharField(max_length=10,choices=Status.choices, default=Status.PENDING)

    #create a unique reference id for the payment
    def save(self, *args, **kwargs):
        if not self.ref_id:
            self.ref_id = f"PAY-{self.applicant_name}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

class Testimonial(models.Model):
    #applicant = models.ForeignKey(Applicant,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to="testimonials/" , validators=[FileExtensionValidator(["pdf","docx","doc","jpg","png"])])
