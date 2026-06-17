from django.shortcuts import render, redirect
from core.services.registry import computer
# Create your views here.
def home(request):
    # Handle clear cache
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'clear':
            computer.clearCache()
            return render(request, "core/home.html", {
                "cache_status": "Cache cleared"
            })
    
    # Handle compute
    n = request.GET.get('n')
    if n is None:
        return render(request, "core/home.html")
    
    n = int(n)
    result = computer.compute(n)
    return render(request, "core/home.html", {
        "n": n,
        "sum" : result,
        "time_taken" : str(round(computer.lastElapsedTime, 5))+" milliseconds",
        "cache_status" : computer.lastStatus
    })