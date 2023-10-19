from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

# views.py

from django.shortcuts import render
from .models import teacher,student

def teacher_students(request):
    teachers = teacher.objects.all()
    selected_teacher = request.GET.get('teacher_id')
    students = []

    if selected_teacher:
        students = student.objects.filter(teachers__teacher_id=selected_teacher)

    return render(request, 'teacher_students.html', {'teachers': teachers, 'students': students})

def student_teachers(request):
    students = student.objects.all()
    selected_student = request.GET.get('student_id')
    teachers = []

    if selected_student:
        teachers = teacher.objects.filter(student__student_id=selected_student)

    return render(request, 'student_teachers.html', {'students': students, 'teachers': teachers,'selected_student':selected_student})


# views.py

import jwt  # You may need to install the PyJWT library
from django.http import HttpResponse
from django.shortcuts import render


def generate_certificate(request, student_id, teacher_id):
    # Find the selected student and teacher based on the provided IDs
    students = student.objects.get(student_id=student_id)
    teachers = teacher.objects.get(teacher_id=teacher_id)

   
    payload = {
            'student_id': student_id,
            'teacher_id': teacher_id,
            # Add other data you want to include
        }
    jwt_token = jwt.encode(payload, 'your-secret-key', algorithm='HS256')

        # Render the template with the JWT token
    return render(request, 'generate_certificate.html', {'student': students, 'teacher': teachers, 'jwt_token': jwt_token})

    
def verify_certificate(request):
    if request.method == 'POST':
        jwt_token = request.POST.get('jwt_token')
        # Verify the JWT token here

        # Extract data from the JWT token if it's valid
        try:
            payload = jwt.decode(jwt_token, 'your-secret-key', algorithms=['HS256'])
            student_id = payload['student_id']
            teacher_id = payload['teacher_id']
            # Perform certificate verification logic
            return HttpResponse(f'Certificate verified for Student ID: {student_id} and Teacher ID: {teacher_id}')
        except jwt.ExpiredSignatureError:
            return HttpResponse('JWT Token has expired')
        except jwt.DecodeError:
            return HttpResponse('JWT Token is invalid')

    return render(request, 'verify_certificate.html')
