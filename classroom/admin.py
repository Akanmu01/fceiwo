from django.contrib import admin
from .models import *
import calendar
from datetime import date
from django.utils.html import format_html, mark_safe
from .utils import ExportCsvMixin
admin.site.site_header = "My School Admin"
admin.site.site_title = "My School Admin Portal"
admin.site.index_title = "Welcome to FCEIWO"


class QuizAdmin(admin.ModelAdmin):
	list_display = ("owner", "name", "subject")


admin.site.register(User)
admin.site.register(Post)
admin.site.register(Admission)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(TakenQuiz)
admin.site.register(StudentAnswer)
admin.site.register(Profile)
admin.site.register(LoggedInUser)
admin.site.register(TeacherRegistrationApproval)