from django.urls import path, include
from . import views
app_name = 'studentapp'
urlpatterns = [
    path('studenthomepage/', views.studenthomepage, name='studenthomepage'),
]