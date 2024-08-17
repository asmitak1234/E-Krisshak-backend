from django.urls import path
from .views import KrisshakView

urlpatterns = [
    path('krisshaks/', KrisshakView.as_view()),
    path('krisshaks/<int:pk>/',KrisshakView.as_view())
]
