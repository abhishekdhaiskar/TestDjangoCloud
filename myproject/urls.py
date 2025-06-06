from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello from Django on EC2 or Lambda!</h1>')

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
]
