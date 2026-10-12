from django.db import models

class DurationChoices(models.TextChoices):

    THREE_MONTH ='3 Months' , '3 Months'

    SIX_MONTH = '6 Months' , '6 Months'

    TWO_MONTH = '2 Months' , '2 Months'


class Course(models.Model):

    name=models.CharField(max_length=50)

    duration=models.CharField(max_length=30,choices=DurationChoices.choices)

    price=models.FloatField()
    
    
    def __str__(self):

        return self.name
    
    class Meta:

        verbose_name='Courses'

        verbose_name_plural='Courses'

class Student(models.Model):

    profile=models.OneToOneField('authentication.profile',on_delete=models.CASCADE)

    name=models.CharField(max_length=20)

    Dob=models.DateField()

    Place=models.CharField(max_length=20)

    photo=models.ImageField(upload_to='student-images')

    course=models.ForeignKey('Course',on_delete=models.CASCADE)


    def __str__(self):
        return self.name


    class Meta:

        verbose_name='Students'

        verbose_name_plural='Students'