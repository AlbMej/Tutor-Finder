from django.db import models

# Create your models here.
class UserInfo(models.Model):
    #this is all database info for a tutoruser profile
    LEVELS = (
             ('' , 'Choose'),
             ('Fr', 'Freshman'),
             ('So', 'Sophmore'),
             ('Jr', 'Junior'),
             ('Sr', 'Senior'),
             ('M', 'Masters'),
             ('P', 'Phd')
             )
    #first and last name
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    #contact information
    #TB = text box
    email_TB = models.EmailField("Email",
                        help_text="Please fill in at least 1 form of contact",
                        default="N/A")
    phone_TB = models.CharField("Phone Number", max_length=12,
                        help_text="Please fill in at least 1 form of contact",
                        default="N/A")
    other_TB1 = models.CharField("Other Contact Type", max_length=32,
                        help_text="Please fill in at least 1 form of contact",
                        default = "N/A")
    other_TB2 = models.CharField("Other Contact Information", max_length=32,
                                default="N/A")

    #their school and level (FR/SO/JR/SR/G/PHD)
    school = models.CharField("College/University", max_length=32, default="N/A")
    level = models.CharField("Level/Year", max_length=20, choices=LEVELS,
                             default="N/A")

    #terms and conditions that have yet to be written
    agreeMsg = "Do you agree to the terms and conditions listed below?"
    agree = models.BooleanField(agreeMsg)  #required=True




class School(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=32)

class Course(models.Model):
    name = models.CharField(max_length=64)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    department = models.CharField(max_length=64)
    course_number = models.CharField(max_length=32)

class Tutor(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default = None)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default = None)


    def __str__(self):
        return self.name
