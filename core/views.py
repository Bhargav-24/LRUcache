from django.shortcuts import render

# Create your views here.
def home(request):
    n =  request.GET.get('n')
    if n is not None:
        
    return render(request, 'home.html')
