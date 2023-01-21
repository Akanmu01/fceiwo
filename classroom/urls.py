from django.urls import include, path

from .views import classroom, students, teachers, adminpages
from .views.students import *
from .views.teachers import *
from .views.adminpages import *


urlpatterns = [
    path('', classroom.home, name='home'),
    path('about/', classroom.about, name='about'),
    path('user/<str:username>/', profile, name='profile'),
    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('interests/', students.StudentInterestsView.as_view(), name='student_interests'),
        path('taken/', students.TakenQuizListView.as_view(), name='taken_quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
        path('editprofile/', students.editprofile, name='editprofile'),
        path('admission/', students.admission, name='admission'),
        path('apply/', students.admissionform, name='admissionform'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.QuizListView.as_view(), name='quiz_change_list'),
        path('quiz/add/', teachers.QuizCreateView.as_view(), name='quiz_add'),
        path('quiz/<int:pk>/', teachers.QuizUpdateView.as_view(), name='quiz_change'),
        path('quiz/<int:pk>/delete/', teachers.QuizDeleteView.as_view(), name='quiz_delete'),
        path('quiz/<int:pk>/results/', teachers.QuizResultsView.as_view(), name='quiz_results'),
        path('quiz/<int:pk>/question/add/', teachers.question_add, name='question_add'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/', teachers.question_change, name='question_change'),
        path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', teachers.QuestionDeleteView.as_view(), name='question_delete'),
       
    ], 'classroom'), namespace='teachers')),

    path('adminpage/', include(([
        path('', adminpages_home, name='adminpages_home'),
        path('addsubject/', adminpages.addsubject, name='addsubject'),
        path('allsubject/', adminpages.allsubject, name='allsubject'),
        path('allquiz/', adminpages.allquiz, name='allquiz'),
        path('subject_detail/<int:pk>/', adminpages.subject_detail, name='subject_detail'),
        path('edit_subject/<int:pk>/',adminpages.edit_subject, name='edit_subject'),
        path('edit_quiz/<int:pk>/',adminpages.edit_quiz, name='edit_quiz'),
    ], 'account'), namespace='adminpages')),
]
