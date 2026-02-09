from django.shortcuts import render
from school.models import Student
from django.db.models import Q
def home(request):
 
 student_data = Student.objects.filter(Q(id=2) & Q(roll=102))
#  student_data = Student.objects.filter(Q(id=2) | Q(roll=103))
#  student_data = Student.objects.filter(~Q(id=2))
#  student_data = Student.objects.filter(Q(city='bokaro') & Q(marks__gte=100))


 context = {'students':student_data}
 

 return render(request, 'school/home.html', context)