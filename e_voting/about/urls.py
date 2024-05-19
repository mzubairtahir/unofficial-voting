from django.urls import path
from .views import about_view

urlpatterns = [
    path('', view=about_view,  name="about"),

]
