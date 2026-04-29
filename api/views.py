from django.shortcuts import render
from django.http import JsonResponse

def studentsView(request):
    students = {
            'id': 1,
            'name': 'Sayedur',
            'class': 'Computer Science'
        }
    return JsonResponse(students)  # ← safe=False যোগ করুন , safe=False