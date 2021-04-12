from django.shortcuts import render


def inicio(request):
    return render(request, "roboworld_app/index.html")

def stats(request):
    return render(request, "roboworld_app/stats.html")

def micuenta(request):
    return render(request, "roboworld_app/micuenta.html")