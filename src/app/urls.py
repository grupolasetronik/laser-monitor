from django.urls import path
from app.views import send_message

urlpatterns = [
    path("",send_message)
]


