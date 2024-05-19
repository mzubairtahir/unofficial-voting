from django.urls import path
from .views import Result

urlpatterns = [
    path('', view=Result.as_view(),  name="result"),

]
