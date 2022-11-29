from django.urls import path
from enquetes import views

urlpatterns = [
    # serão substituídas por urls para as baseviews
    path('', views.index, name='index'),
    path('<int:question_id>', views.details, name='detail'),
    path('create', views.create, name="create_pull"),
    path('create-user', views.create_user, name="create_user"),
    #path('', views.IndexView.as_view(), name="index"),
    # como está usando class views, o nome do atributo tem de ser pk
    #path('<int:pk>', views.DetailView.as_view(), name="detail")
]
