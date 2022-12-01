from django.urls import path
from enquetes import views

urlpatterns = [
    # serão substituídas por urls para as baseviews
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='detail'),
    path('create', views.create, name="create_pull"),
    path('vote/<int:question_id>', views.vote, name="vote"),
]
