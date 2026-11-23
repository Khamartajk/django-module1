from django.shortcuts import render
from .models import CourseDetails
# Create your views here.

def index(request):
    courses = CourseDetails.objects.all()
    
    
    return render(request, 'index.html', {'courses': courses})