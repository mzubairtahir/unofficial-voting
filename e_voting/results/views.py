from django.views import View
import json
from django.db.models import Count
from django.core.serializers import serialize
from vote.models import Party, Vote
from django.shortcuts import render

# Create your views here.


class Result(View):

    def get_data(self):
        query_set = Party.objects.annotate(total_votes = Count("vote")).values("name", "picture", "total_votes", "code")
        


        return list(query_set)


    def get(self, request):
        data = self.get_data()
        return render(request=request, template_name="results.html", context={"DATA":data})
