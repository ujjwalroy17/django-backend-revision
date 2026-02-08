from django.shortcuts import render
from school.models import Student, Teacher

def home(request):
 
 all_data = Student.objects.all()

#  all_data = Student.objects.filter(city="bokaro")

#  all_data = Student.objects.exclude(city="bokaro")

#  all_data = Student.objects.order_by('marks')
#  all_data = Student.objects.order_by('-marks')
#  all_data = Student.objects.order_by('name')
#  all_data = Student.objects.order_by('?')
#  all_data = Student.objects.order_by('name').reverse()
#  all_data = Student.objects.order_by('name')[0:5]

#  all_data = Student.objects.values()
#  all_data = Student.objects.values('name', 'city')
#  all_data = Student.objects.values_list()
#  all_data = Student.objects.values_list('id', 'name')
#  all_data = Student.objects.values_list('id', 'name', named=True)

#  qs1 = Student.objects.values_list('id', 'name', named=True)
#  qs2 = Teacher.objects.values_list('id', 'name', named=True)
#  all_data = qs2.union(qs1)

#  qs1 = Student.objects.values_list('id', 'name', named=True)
#  qs2 = Teacher.objects.values_list('id', 'name', named=True)
#  all_data = qs2.union(qs1, all=True)

#  qs1 = Student.objects.values_list('id', 'name', named=True)
#  qs2 = Teacher.objects.values_list('id', 'name', named=True)
#  all_data = qs1.intersection(qs2)

#  qs1 = Student.objects.values_list('id', 'name', named=True)
#  qs2 = Teacher.objects.values_list('id', 'name', named=True)
#  all_data = qs2.difference(qs1)

#  all_data = Student.objects.filter(name="rohit") & Student.objects.filter(city="ranchi")
#  all_data = Student.objects.filter(name="rohit", city="ranchi")

#  all_data = Student.objects.filter(name="rohit") | Student.objects.filter(city="ranchi")


#  print("All Data:", all_data)
#  print()
#  print("SQL Query: ", all_data.query)
 return render(request, 'school/home.html', {'all_data':all_data})