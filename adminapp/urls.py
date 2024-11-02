from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.projecthomepage, name = 'projecthomepage'),
    path('printpagecall/',views.printpagecall, name = 'printpagecall'),
    path('printpagelogic/',views.printpagelogic, name = 'printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall, name = 'exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic, name = 'exceptionpagelogic'),
    path('UserRegisterCall/',views.UserRegisterCall, name = 'UserRegisterCall'),
    path('UserRegisterLogic/', views.UserRegisterLogic, name='UserRegisterLogic'),
    path('add_task/', views.add_task, name='add_task'),
    path('<int:pk>/delete/', views.delete_task, name='delete_task'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('UserLoginPageCall/', views.UserLoginPageCall, name='UserLoginPageCall'),
    path('studentlist/', views.studentlist, name='studentlist'),
    path('add_student/', views.add_student, name='add_student'),
    path('datetimepagecall/', views.datetimepagecall, name='datetimepagecall'),
    path('datetimepagelogic/', views.datetimepagelogic, name='datetimepagelogic'),
    path('logout/', views.logout, name='logout'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('feedback_view/', views.feedback_view, name='feedback_view'),

]


