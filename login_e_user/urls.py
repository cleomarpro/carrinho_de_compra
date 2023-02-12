from .views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.urls import path

urlpatterns = [
    path('login', LoginView.as_view()),
]
