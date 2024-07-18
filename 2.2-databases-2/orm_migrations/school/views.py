from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = "school/students_list.html"
    students = Student.objects.all()
    # students = Student.objects.prefetch_related('teacher').all()
    # .order_by('group')
    ordering = "group"
    context = {"object_list": students.order_by(ordering)}

    return render(request, template, context)
