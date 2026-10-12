from django.urls import path

from . import views

urlpatterns=[

    path('courses/',views.CourseListCreateView.as_view()),
    path('courses/<int:id>/',views.CourseRetrieveUpdateDestroyView.as_view()),
    path('students/',views.StudentListView.as_view()),
    path('student-register/',views.StudentRegisterView.as_view()),
    path('exams/',views.ExamListCreateView.as_view()),
    path('exams/<int:id>/',views.ExamRetrieveUpdateDestroyView.as_view()),
    path('Subjective-questions/<int:id>/',views.SubjectiveQuestionListCreateView.as_view()),
    path('Subjective-questions-rud/<int:id>/',views.SubjectiveQuestionRetrieveUpdateDestroyView.as_view()),
    path('Subjective-answer-submit/',views.SubjectiveAnswerSubmitView.as_view()),
    path('objective-answer-submit/',views.ObjectiveAnswerSubmitView.as_view()),
        
]