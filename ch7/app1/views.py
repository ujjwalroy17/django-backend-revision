from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_django(request):
    # html = """<!DOCTYPE html>
    #     <html lang="en">
    #     <head>
    #     <meta charset="UTF-8">
    #     <title>Hello Django</title>
    #     </head>
    #     <body>

    #     <h1>Hello Django from App1</h1>

    #     </body>
    #     </html>
    #     """
    # return HttpResponse(html)
    return render(request,'app1/django.html')

def learn_drf(request):
    return render(request,'app1/drf.html')