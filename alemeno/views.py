from django.http import HttpResponse


def index(request):
    return HttpResponse("You can add objects by using django admin.")
