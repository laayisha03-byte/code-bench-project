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

class Typechoices(models.TextChoices):

    OBJECTIVE='objective','objective'

    SUBJECTIVE='subjective','subjective'

class Exam(models.Model):

    name=models.CharField(max_length=20)

    type=models.CharField(max_length=30,choices=Typechoices.choices)

    mark=models.IntegerField()

    subject=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.name


    class Meta:

        verbose_name='Exams'

        verbose_name_plural='Exams'

class ChoiceChoices(models.TextChoices):

    A='A','A'
    B='B','B'
    C='C','C'
    D='D','D'

class ObjectiveQuestion(models.Model):

    exam=models.ForeignKey('Exam',on_delete=models.CASCADE)

    question=models.TextField()

    choice_a=models.TextField()

    choice_b=models.TextField()

    choice_c=models.TextField()

    choice_d=models.TextField()

    correct_choice=models.CharField(max_length=5,choices=ChoiceChoices.choices)

    points=models.IntegerField()
    
    def __str__(self):
        return f'{self.exam.name}-{self.id}'


    class Meta:

        verbose_name='Objective Questions'

        verbose_name_plural='Objective Questions'

class SubjectiveQuestion(models.Model):

    exam=models.ForeignKey('Exam',on_delete=models.CASCADE)

    question=models.TextField()

    points=models.IntegerField()
    
    def __str__(self):
            
            return f'{self.exam.name}-{self.id}'
    
    class Meta:
    
            verbose_name='Subjective Questions'
    
            verbose_name_plural='Subjective Questions'

class ObjectiveAnswer(models.Model):

    student=models.ForeignKey('Student',on_delete=models.CASCADE)

    exam=models.ForeignKey('Exam',on_delete=models.CASCADE)

    question=models.ForeignKey('ObjectiveQuestion',on_delete=models.CASCADE)

    answer=models.CharField(max_length=10,choices=ChoiceChoices.choices)

    point=models.IntegerField(null=True)
    
    
    def __str__(self):
                
        return f'{self.exam.name}-{self.student.name}-{self.id}'
    
    
    class Meta:
        
        verbose_name='Objective Answers'
        
        verbose_name_plural='Objective Answers'

class SubjectiveAnswer(models.Model):

    student=models.ForeignKey('Student',on_delete=models.CASCADE)

    exam=models.ForeignKey('Exam',on_delete=models.CASCADE)

    question=models.ForeignKey('SubjectiveQuestion',on_delete=models.CASCADE)

    answer=models.TextField()

    point=models.IntegerField(null=True,blank=True)

    remarks=models.TextField(null=True)
    
    
    def __str__(self):
                
        return f'{self.exam.name}-{self.student.name}-{self.id}'
    
    
    class Meta:
        
        verbose_name='Subjective Answers'
        
        verbose_name_plural='Subjective Answers'
    