from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import student


# Create your views here.
def student_list(request):
    students = student.objects.order_by("id")
    return render(request, "index.html", {"students": students})


def student_info(request):
    form = StudentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student added successfully.")
        return redirect("student_list")

    return render(request, "student_info.html", {"form": form})


def edit_student(request, student_id):
    student_record = get_object_or_404(student, pk=student_id)
    form = StudentForm(request.POST or None, instance=student_record)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Student updated successfully.")
        return redirect("student_list")

    return render(request, "edit_student.html", {"form": form})


def delete_student(request, student_id):
    student_record = get_object_or_404(student, pk=student_id)
    if request.method == "POST":
        student_record.delete()
        messages.success(request, "Student deleted successfully.")
    return redirect("student_list")
