from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>', views.DetailsQuestionView.as_view(), name='detail'),
    path('create', views.create, name="create_pull"),
    path('vote/<int:question_id>', views.vote, name="vote"),
]
