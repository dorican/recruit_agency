from django.urls import path
from .views import *

app_name = 'mainapp'


urlpatterns = [
    path('', index, name='index'),
    path('recruit/create/', recruit_create, name='recruit_create'),
    path('questions/', recruit_questions, name='recruit_questions'),
    path('questions/<int:pk>/', question_detail, name='question_detail'),
    path('sitkh/', choice_sitkh, name='choice_sitkh'),
    path('recruit/answers/<int:pk>/<int:sitkh>/', recruit_answers, name='recruit_answers'),
    path('add/recruits/<int:pk>/<int:sitkh>/', add_recruit, name='add_recruit'),
    path('recruits/for/sitkh/<int:pk>/<int:sitkh>/', recruits_for_sitkh, name='recruits_for_sitkh'),
    path('list/sitkhs', list_of_sitkhs, name='list_of_sitkhs'),
]