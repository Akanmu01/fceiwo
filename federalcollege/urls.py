from django.contrib import admin
from django.urls import include, path
from classroom.views import classroom, students, teachers, adminpages
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
# PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('classroom.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
    path('admin_signup_page/', adminpages.AdminSignUpView.as_view(), name='adminpage_signup'),

#password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "password/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "password/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "password/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "password/password_reset_done.html"), name ='password_reset_complete'),
    
    # # path('accounts/password_change/', name='password_change'),
    # path('accounts/password_change/done/', name='password_change_done'),
    # path('accounts/password_reset/', name='password_reset'),
    # path('accounts/password_reset/done/', name='password_reset_done'),
    # path('accounts/reset/<uidb64>/<token>/', name='password_reset_confirm'),
    # path('accounts/reset/done/', name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
