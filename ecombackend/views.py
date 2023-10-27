from django.shortcuts import render


# INDEX PAGE VIEW
def index(request):
    """INDEX PAGE VIEW """
    return render(request,'welcome.html')