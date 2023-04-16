from django.db import models
import itertools




# Student
class GradStudent(models.Model):
    GENDER = (('M', 'MALE'),
              ('F', 'FEMALE'),
              ('O', 'OTHER')

              )

    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, primary_key=True)
    DOB = models.DateField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=50, default='M')

    def __str__(self):
        return self.username


class Career(models.Model):
    CHOICES = (('H', 'HIGH'),
               ('M', 'MODERATE'),
               ('F', 'FEW'),
               )

    carName = models.CharField(max_length=50)
    opportunities = models.CharField(max_length=50, choices=CHOICES)
    employability = models.FloatField()
    avg_carrer_length = models.IntegerField()
    travel_opps = models.FloatField()
    starting_pay = models.FloatField()


# Study program
class StudyProgram(models.Model):
    grade = (('A', 'Excellent'),
             ('B', 'Above average'),
             ('C', 'Credit'),
             ('D', 'Pass')
             )

    Sname = models.CharField(max_length=50)
    price = models.FloatField
    career = models.ForeignKey(Career, null=True, on_delete=models.SET_NULL)
   # career = models.CharField(max_length=50)
    emp_options = models.IntegerField()
    entry_grade = models.CharField(max_length=1, choices=grade, default='A')
    skills = models.CharField(max_length=500)


# Colleges
class College(models.Model):
    reputation = ((1, 'First Class'),
                  (2, 'Second Class'),
                  (3, 'Third Class'),
                  (4, 'Mediocre'))

    campus = ((1, 'Closed campus with student housing'),
              (2, 'Open campus with student housing'),
              (3, 'Open campus without student housing'),
              (4, 'Closed campus without student housing')

    )


    Cname = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    avg_price = models.FloatField()
    gen_reputuation = models.CharField(max_length=500, choices=reputation, default=1)
    total_programs = models.IntegerField(default=10)
    total_clubs = models.IntegerField(default=0)
    Campus_type = models.CharField(max_length=50, choices=campus, default=1)
    security_rating = models.FloatField(default=0)






# college offerings
class Offering(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    collegeName = models.ForeignKey(College, null=True, on_delete=models.SET_NULL)
    program = models.ForeignKey(StudyProgram, null=True, on_delete=models.SET_NULL)

#criterias classes
class Comparisions(models.Model):
    criterion = models.CharField(max_length=100)



class Crit_model(models.Model):
    class Meta():
        db_table = 'Criteria Model'

    name = models.TextField()
    decision = models.TextField(default='[["0"]]')


class Criteria(models.Model):
    class Meta():
        db_table = 'Criteria'

    crit1 = models.TextField("Criterion 1",max_length=100)
    crit2 = models.TextField("Criterion 2",max_length=100)
    crit3 = models.TextField("Criterion 3",max_length=100)
    crit4 = models.TextField("Criterion 4",max_length=100)
    crit_model = models.OneToOneField(Crit_model, on_delete=models.CASCADE)

    def get_fields(self):
        array = [(field.name, field.value_to_string(self)) for field in Element._meta.fields]
        array.pop(0)
        array.pop(-1)
        return array

    def get_pairs(self):
        array = []
        for pair in itertools.combinations([field.value_to_string(self) for field in Element._meta.fields], 2):
            array.append((pair))

        return array


class Element(models.Model):
    class Meta():
        db_table = 'Element'

    name = models.TextField()
    attrib1 = models.TextField("Attribute 1")
    attrib2 = models.TextField("Attribute 2")
    attrib3 = models.TextField("Attribute 3")
    attrib4 = models.TextField("Attribute 4")
    crit_model = models.ForeignKey(Crit_model, on_delete=models.CASCADE)

    #
    def get_fields(self):
        array = [(field.name, field.value_to_string(self)) for field in Element._meta.fields]
        array.pop(0)
        array.pop(-1)
        return array

    def get_pairs(self):
        array = []
        for pair in itertools.combinations([field.value_to_string(self) for field in Element._meta.fields], 2):
            array.append((pair))

        return array

