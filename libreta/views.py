from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the libreta home page</h1>")
