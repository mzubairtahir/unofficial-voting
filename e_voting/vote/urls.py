from django.urls import path
from .views import VoteView

urlpatterns = [
    path('', view=VoteView.as_view(),  name="vote"),

]
