from django.urls import path
from .views import home, profile, RegisterView
from . import views

urlpatterns = [
    path('', views.home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('index/', views.IndexView.as_view(), name='index'),
]
