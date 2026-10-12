from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework.views import APIView
from . models import Course
from . models import Student,Exam,ObjectiveQuestion,ObjectiveAnswer,SubjectiveQuestion,SubjectiveAnswer
from . serializers import CourseSerializer,StudentReadSerializer,StudentWriteSerializer,ExamSerializer,ObjectiveQuestionSerializer,SubjectiveQuestionSerializer,SubjectiveAnswerSerializer,ObjectiveAnswerSerializer
from authentication.serializers import ProfileSerializer
from rest_framework.response import Response
from django.db import transaction
from . utils import evaluate_answer,evaluate_objective_answer
import threading
from authentication.permissions import IsAdmin,IsStudent
from rest_framework_simplejwt.authentication import JWTAuthentication

class CourseListCreateView(ListCreateAPIView):

    queryset=Course.objects.all()

    serializer_class=CourseSerializer

    authentication_classes=[JWTAuthentication]

    def get_permissions(self):

        if self.request.method == 'POST':

            permissions = [IsAdmin]
            
            return [permission() for permission in permissions]

class CourseRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):


    queryset=Course.objects.all()

    serializer_class=CourseSerializer

    lookup_field='id'


    authentication_classes=[JWTAuthentication]
    
    def get_permissions(self):
    
        if self.request.method in ['PATCH','DELETE']:
    
            permissions = [IsAdmin]
            
            return [permission() for permission in permissions]

class StudentListView(ListAPIView):

    queryset=Student.objects.all()

    serializer_class=StudentReadSerializer

    authentication_classes=[JWTAuthentication]

    permission_classes=[IsAdmin]

class StudentRegisterView(APIView):



    def post(self,request,*args,**kwargs):

        profile_serializer=ProfileSerializer(data=request.data)

        Student_Serializer=StudentWriteSerializer(data=request.data)

        with transaction.atomic():


        
        
            if profile_serializer.is_valid():

                password =profile_serializer.validated_data.get('password')

                profile = profile_serializer.save()

                profile.set_password(password)

                profile.role= 'Student'

                profile.save()
            
            
                if Student_Serializer.is_valid():

                    Student = Student_Serializer.save(profile=profile)

                

                    data={'msg':'student created successfully'}

                    return Response(data,status=200)

                return Response(Student_Serializer.errors,status=400)

            return Response(profile_serializer.errors,status=400)



class ExamListCreateView(ListCreateAPIView):

    queryset=Exam.objects.all()

    serializer_class=ExamSerializer

    authentication_classes=[JWTAuthentication]


    permission_classes=[IsAdmin]
    
    


class ExamRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):

    lookup_field = 'id'

    queryset=Exam.objects.all()

    serializer_class=ExamSerializer

    authentication_classes=[JWTAuthentication]
        
    def get_permissions(self):
        
        if self.request.method in ['PATCH','DELETE']:
        
            permissions = [IsAdmin]


        elif self.request.method=='GET':

            permissions=[IsStudent]


                
            return [permission() for permission in permissions]



class ObjectiveQuestionListCreateView(APIView):

    serializer_class=ObjectiveQuestionSerializer

    def get_permissions(self):
    
        if self.request.method == 'POST':
            
            permissions = [IsAdmin]
             
            return [permission() for permission in permissions]
    

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        exam=Exam.objects.get(id=id)

        questions=ObjectiveQuestion.objects.filter(exam=exam)

        serializer=self.serializer_class(questions,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        id=kwargs.get('id')

        exam=Exam.objects.get(id=id)

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save(exam=exam)

            data={'msg':'question addedd successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)


class ObjectiveQuestionRetrieveUpdateDestroyView(APIView):

    serializer_class=ObjectiveQuestionSerializer

    authentication_classes=[JWTAuthentication]
            
    def get_permissions(self):
            
            if self.request.method in ['PATCH','DELETE']:
            
                permissions = [IsAdmin]
                
                return [permission() for permission in permissions]
    


    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        question=ObjectiveQuestion.objects.get(id=id)

        serializer=self.serializer_class(question)

        return Response(serializer.data,status=200)


    def patch(self,request,*args,**kwargs):
        
        id=kwargs.get('id')

        question=ObjectiveQuestion.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=question,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'question updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
        
        question=ObjectiveQuestion.objects.get(id=id)

        question.delete()

        data={'msg':'question deleted successfully'}

        return Response(data,status=200)


      #  

class SubjectiveQuestionListCreateView(APIView):

    serializer_class=SubjectiveQuestionSerializer
    authentication_classes=[JWTAuthentication]
            
    def get_permissions(self):
            
            if self.request.method in ['PATCH','DELETE']:
            
                permissions = [IsAdmin]
                
                return [permission() for permission in permissions]
    





    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        exam=Exam.objects.get(id=id)

        questions=SubjectiveQuestion.objects.filter(exam=exam)

        serializer=self.serializer_class(questions,many=True)

        return Response(serializer.data,status=200)

    def post(self,request,*args,**kwargs):

        id=kwargs.get('id')

        exam=Exam.objects.get(id=id)

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            serializer.save(exam=exam)

            data={'msg':'question addedd successfully'}

            return Response(data,status=201)

        return Response(serializer.errors,status=400)


class SubjectiveQuestionRetrieveUpdateDestroyView(APIView):

    serializer_class=SubjectiveQuestionSerializer

    authentication_classes=[JWTAuthentication]
    
    def get_permissions(self):
    
        if self.request.method in ['PATCH','DELETE']:
    
            permissions = [IsAdmin]
            
            return [permission() for permission in permissions]

    def get(self,request,*args,**kwargs):

        id=kwargs.get('id')

        question=SubjectiveQuestion.objects.get(id=id)

        serializer=self.serializer_class(question)

        return Response(serializer.data,status=200)


    def patch(self,request,*args,**kwargs):
        
        id=kwargs.get('id')

        question=SubjectiveQuestion.objects.get(id=id)

        serializer=self.serializer_class(data=request.data,instance=question,partial=True)

        if serializer.is_valid():

            serializer.save()

            data={'msg':'question updated successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get('id')
        
        question=SubjectiveQuestion.objects.get(id=id)

        question.delete()

        data={'msg':'question deleted successfully'}

        return Response(data,status=200)

class SubjectiveAnswerSubmitView(APIView):

    serializer_class=SubjectiveAnswerSerializer

    authentication_classes=[JWTAuthentication]

    permission_classes=[IsStudent]

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            student=serializer.validated_data.get('student')

            exam=serializer.validated_data.get('exam')

            question=serializer.validated_data.get('question')

            student_answer=serializer.validated_data.get('answer')

            answer=SubjectiveAnswer.objects.filter(student=student,exam=exam,question=question)
            
            if answer.exists():

                answer=answer.first()

                answer.answer=student_answer

                answer.save()

            else:
                
                answer=serializer.save()

            thread=threading.Thread(target=evaluate_answer,args=(answer))

            thread.start()

            #result=evaluate_answer(answer)

            data={'msg':'answer submitted successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    
#
class ObjectiveAnswerSubmitView(APIView):

    serializer_class=ObjectiveAnswerSerializer
    
    authentication_classes=[JWTAuthentication]
    
    permission_classes=[IsStudent]

    def post(self,request,*args,**kwargs):

        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():

            student=serializer.validated_data.get('student')

            exam=serializer.validated_data.get('exam')

            question=serializer.validated_data.get('question')

            student_answer=serializer.validated_data.get('answer')

            answer=ObjectiveAnswer.objects.filter(student=student,exam=exam,question=question)
            
            if answer.exists():

                answer=answer.first()

                answer.answer=student_answer

                answer.save()

            else:
                
                answer=serializer.save()


            points= evaluate_objective_answer(answer)

            answer.point=points

            answer.save()

            

            #result=evaluate_answer(answer)

            data={'msg':'answer submitted successfully'}

            return Response(data,status=200)

        return Response(serializer.errors,status=400)

    












