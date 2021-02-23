from django.shortcuts import render

# Create your views here.
def binsonmap(request):
    return render(request, 'BinsOnMap/binsonmap.html')