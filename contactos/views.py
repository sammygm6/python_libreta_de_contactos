from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the contactos home page</h1>")
