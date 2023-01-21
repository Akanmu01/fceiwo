from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from ckeditor.fields import RichTextField
# from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator

# validators=[FileExtensionValidator(["jpg","png"]) , MaxFileSizeValidator(8*1024*1024)]



GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)

MONTHS_CHOICE = (
    ('1', 'January'),
    ('2', 'February'),
    ('3', 'March'),
    ('4', 'April'),
    ('5', 'May'),
    ('6', 'June'),
    ('7', 'July'),
    ('8', 'August'),
    ('9', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
)

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    # picture = CloudinaryField(blank=False, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    surname = models.CharField(max_length=200, blank=False)
    first_name = models.CharField(max_length=200, blank=False)
    other_name = models.CharField(max_length=200, blank=False)
    conference = models.CharField(max_length=200, blank=False)
    number = models.CharField(max_length=13, blank=False)

User.profile = property(lambda u:Profile.objects.get_or_create(user=u)[0])


STATUS = ((0, "Draft"), (1, "Publish"))

class TeacherRegistrationApproval(models.Model):
    teacher = models.CharField(max_length=10, default="Teacher")
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.teacher

STATUS = ((0, "Draft"), (1, "Publish"))

class AdminPageApproval(models.Model):
    teacher = models.CharField(max_length=10, default="Teacher")
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.teacher


class Subject(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    status = models.IntegerField(choices=STATUS, default=0)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255, null=True, blank=True)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')



STATUS = ((0, "Draft"), (1, "Publish"))

class Post(models.Model):
    cover_image = models.ImageField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    # cover_image = CloudinaryField(blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])])
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    updated_on = models.DateTimeField(auto_now=True)
    body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    postview = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Course(models.Model):
    course_name = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return f"{ self.course_name }"



class Admission(models.Model):
    admission_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="adminssion_owner")
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    other_name = models.CharField(max_length=50, blank=False, null=False)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(auto_now=True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="coursename")
    address = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11, default="08123456789")
    guardian_name = models.CharField(max_length=50, blank=False, null=False)
    guardian_phone_number = models.CharField(max_length=11, default="08123456789")
    guardian_profession = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='media', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
