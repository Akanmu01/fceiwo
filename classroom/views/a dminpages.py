from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView
from ..forms import *
from django.shortcuts import redirect, render
from ..forms import *
# BaseAnswerInlineFormSet, QuestionForm, TeacherSignUpForm, SubjectForm
from ..models import *
from django.contrib.auth.decorators import login_required



class AdminSignUpView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('adminpages:adminpages_home')


def adminpages_home(request):
    qry = User.objects.all()
    teacher = User.objects.filter(is_teacher=True)
    student = User.objects.filter(is_student=True)
    context = {
        "qry": qry,
        "teacher": teacher,
        "student": student,
    }
    return render(request, 'classroom/adminpages/home.html', context)


def addsubject(request):
    subject = Subject.objects.all()
    current_user = request.GET.get('user')

    if request.method == 'POST':
        form = SubjectForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('teachers:quiz_change_list')
    else:
        form = SubjectForm()
        
    return render(request, 'classroom/adminpages/subject_add_form.html',
        {
            "form": form,
            "current_user": current_user,
            "subjects": subject
        })




# def edit_subject(request, pk):
#     subject = Subject.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = SubjectForm(request.POST, instance=subject)

#         if form.is_valid():
#             form.save()

#             return redirect('adminpages:allsubject')
#     else:
#         form = SubjectForm(instance=subject)
    
#     context = {
#         'form': form
#     }

#     return render(request, 'classroom/adminpages/edit_subject.html', context)



# def addsubject(request, pk):
#     current_user = request.GET.get(user)
#     subject = Book.objects.filter(author=author)
#     form = BookForm(request.POST or None)

#     if request.method == "POST":
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.author = author
#             book.save()
#             return redirect("detail-book", pk=book.id)
#         else:
#             return render(request, "partials/book_form.html", context={
#                 "form": form
#             })

#     context = {
#         "form": form,
#         "author": author,
#         "books": books
#     }

#     return render(request, "create_book.html", context)





def allsubject(request):
    subject = Subject.objects.all()
    context = {
        'subjects': subject
    }
    return render(request, 'classroom/adminpages/allsubject.html', context)

def edit_subject(request, pk):
    subject = Subject.objects.get(pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)

        if form.is_valid():
            form.save()

            return redirect('adminpages:allsubject')
    else:
        form = SubjectForm(instance=subject)
    
    context = {
        'form': form
    }

    return render(request, 'classroom/adminpages/edit_subject.html', context)
























def allquiz(request):
    quiz = Quiz.objects.all()
    context = {
        'quizs': quiz
    }
    return render(request, 'classroom/adminpages/allquiz.html', context)


def edit_quiz(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    if request.method == 'POST':
        form = QuizForm(request.POST, instance=quiz)

        if form.is_valid():
            form.save()

            return redirect('adminpages:allquiz')
    else:
        form = QuizForm(instance=quiz)
    
    context = {
        'form': form
    }

    return render(request, 'classroom/adminpages/edit_quiz.html', context)


def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    
    context = {
        "subject": subject,
    }
    return render(request, 'classroom/adminpages/subject_detail.html', context)
