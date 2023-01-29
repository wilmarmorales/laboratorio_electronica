from django.urls import path
from .views import LoginFormView, logout_view

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
