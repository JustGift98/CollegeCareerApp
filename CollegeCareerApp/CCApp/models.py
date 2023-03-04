from django.db import models

# Student
class GradStudent(models.Model):


    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,primary_key=True)
    DOB = models.DateField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=50,default='male')

    def __str__(self):
        return self.fname+' '+self.lname


#Study program
class StudyProgram(models.Model):
    Sname = models.CharField(max_length=50)
    price = models.FloatField()
    career = models.CharField(max_length=50)
    employability = models.FloatField()
    emp_options = models.IntegerField()
    travel_opps = models.FloatField()
    avg_carrer_length = models.IntegerField()



#Colleges
class College(models.Model):
    Cname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    avg_price = models.FloatField()
    gen_reputuation = models.CharField(max_length=500)
    graduation_rate = models.FloatField()



