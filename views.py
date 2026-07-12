from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Enrollment, Submission

def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        enrollment = Enrollment.objects.get(user=request.user, course=course)
        submission = Submission.objects.create(enrollment=enrollment)
        return redirect('show_exam_result', course_id=course_id)
    return render(request, 'submit.html')

def show_exam_result(request, course_id):
    return render(request, 'exam_result.html')
