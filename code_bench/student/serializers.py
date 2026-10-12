from rest_framework import serializers

from . models import Course,Student,Exam,ObjectiveQuestion,ObjectiveAnswer,SubjectiveAnswer,SubjectiveQuestion

from authentication.serializers import ProfileSerializer


class CourseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Course

        fields = '__all__'

class StudentReadSerializer(serializers.ModelSerializer):

    profile=ProfileSerializer()

    course=CourseSerializer()

    class Meta:

        model = Student

        fields = '__all__'

class StudentWriteSerializer(serializers.ModelSerializer):

    class Meta:

        model = Student

        fields = '__all__'

        read_only_fields=['profile']

class ExamSerializer(serializers.ModelSerializer):

    class Meta:
    
            model = Exam
    
            fields = '__all__'
    
class ObjectiveQuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = ObjectiveQuestion
    
        fields = '__all__'

        read_only_fields=['exam']

class SubjectiveQuestionSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = SubjectiveQuestion
    
        fields = '__all__'

        read_only_fields=['exam']

class SubjectiveAnswerSerializer(serializers.ModelSerializer):

    class Meta:
    
        model = SubjectiveAnswer
    
        fields = '__all__'

class ObjectiveAnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model= ObjectiveAnswer

        fields= '__all__'

        

       
            