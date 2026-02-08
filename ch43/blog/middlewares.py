from django.shortcuts import HttpResponse, render

def my_fun_middleware(get_response):
  print("One Time Initialization")

  def my_func(request):
    print("This is before view")
    response = get_response(request)
    print("This is after view")
    return response
  return my_func

# def my_fun_middleware(get_response):
#   print("One Time Initialization")

#   def my_func(request):
#     print("This is before view")
#     # response = HttpResponse("Response from my_fun_middleware")
#     response = render(request, 'blog/uc.html')
#     print("This is after view")
#     return response
#   return my_func

class MyClMiddleware:
  def __init__(self, get_response):
    self.get_response = get_response
    print("One Time Initialization")

  def __call__(self, request):
    print("This is before view")
    response = self.get_response(request)
    print("This is after view")
    return response
  
class MyMiddleware1:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time MyMiddleware1 Initialization")

 def __call__(self, request):
  print("This is MyMiddleware1 before view")
  response = self.get_response(request)
  print("This is MyMiddleware1 after view")
  return response

class MyMiddleware2:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time MyMiddleware2 Initialization")

 def __call__(self, request):
  print("This is MyMiddleware2 before view")
  response = self.get_response(request)
  print("This is MyMiddleware2 after view")
  return response

class MyMiddleware3:
 def __init__(self, get_response):
  self.get_response = get_response
  print("One Time MyMiddleware3 Initialization")

 def __call__(self, request):
  print("This is MyMiddleware3 before view")
  response = self.get_response(request)
  print("This is MyMiddleware3 after view")
  return response
  
# class MyProcessMiddleware:
#   def __init__(self, get_response):
#     self.get_response = get_response

#   def __call__(self, request):
#     response = self.get_response(request)
#     return response

#   def process_view(request, *args, **kwargs):
#     print("This is Process View -  Before View")
#     # return HttpResponse("This is before view")
#     return None


# class MyExceptionMiddleware:
#   def __init__(self, get_response):
#     self.get_response = get_response

#   def __call__(self, request):
#     response = self.get_response(request)
#     return response

#   def process_exception(self, request, exception):
#     print("Exception Occured")
#     msg = exception
#     class_name = exception.__class__.__name__
#     print(class_name)
#     print(msg)
#     return HttpResponse(msg)

# class MyTemplateResponseMiddleware:
#   def __init__(self, get_response):
#     self.get_response = get_response

#   def __call__(self, request):
#     response = self.get_response(request)
#     return response

#   def process_template_response(self, request, response):
#     print("Process Template Response From Middleware")
#     response.context_data['name'] = 'Sonam'
#     return response

