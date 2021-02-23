from django.shortcuts import render

# Create your views here.
def garbagebins(request):
    return render(request, 'GarbageBins/garbagebins.html')