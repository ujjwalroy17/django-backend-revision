from django.shortcuts import render
from django.core.cache import cache

# def course(request):
#   mv = cache.get('movie', 'has_expired')
#   if mv == 'has_expired':
#     cache.set('movie', 'RRR', 60)
#     mv = cache.get('movie')
#   return render(request, 'student/course.html', {'mv':mv})

# def course(request):
#   mv = cache.get_or_set('movie', 'The One', 60)
#   mv1 = cache.get_or_set('movie', 'The Harry', 60, version=2)
#   print(mv1)
#   return render(request, 'student/course.html', {'mv':mv})

def course(request):
  data = {'name':'Sonam', 'roll':101}
  cache.set_many(data, 30)
  # stu = cache.get_many(data)
  return render(request, 'student/course.html')

# def course(request):
#   cache.delete('movie', version=2)
#   return render(request, 'student/course.html')

# def course(request):
#   i = cache.incr('roll', delta=2)
#   print(i)
#   return render(request, 'student/course.html')

# def course(request):
#   cache.clear()
#   return render(request, 'student/course.html')
