
from django.shortcuts import render

# Create your views here.




def home(request):
    return render(request, 'home.html', {'name': 'Rahul'})

def add(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        result = num1 + num2
        return render(request, 'result.html', {'result': result})
    return render(request, 'add.html')