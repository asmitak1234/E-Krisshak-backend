# <!-- Made By - Asmita Kumari -->

from django.urls import path
from .views import KrisshakView,UserDetailView

urlpatterns = [
    path('krisshaks/', KrisshakView.as_view()),
    path('krisshaks/<int:pk>/',KrisshakView.as_view()),
    path('user/',UserDetailView.as_view(), name='user-detail'),
]
