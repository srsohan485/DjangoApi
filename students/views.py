from django.http import HttpResponse

def index(request):
    students = [
        {'id': 1,'name': 'Sayedur Rahman Sohan','roll':122}
    ]
    return HttpResponse(students)