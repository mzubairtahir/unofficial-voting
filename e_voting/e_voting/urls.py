from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def redirect_to_results(request):

    return redirect("/results")


urlpatterns = [
    path('management/', admin.site.urls),
    path('vote/', include("vote.urls")),
    path('results/', include("results.urls")),
    path('about/', include("about.urls")),
    path('', view=redirect_to_results, name = "home"),

]
