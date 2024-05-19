from django.shortcuts import render

# Create your views here.

def about_view(request):
    if(request.method=="GET"):

        return render(template_name="about.html", request=request)
        