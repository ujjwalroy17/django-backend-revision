from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def setcookie(request):
 response = render(request, 'student/setcookie.html')
#  response.set_cookie('pay_id', 'ppp123')
#  response.set_cookie('pay_id', 'ppp123', max_age=3600)
 response.set_cookie('pay_id', 'ppp123', expires=datetime.now(timezone.utc) + timedelta(days=2))
 return response

def getcookie(request):
#  pay_id = request.COOKIES['pay_id']
#  pay_id = request.COOKIES.get('pay_id')
 pay_id = request.COOKIES.get('pay_id', 'default_pay_id123')
 return render(request, 'student/getcookie.html',{'pay_id':pay_id})

def delcookie(request):
 response = render(request, 'student/delcookie.html')
 response.delete_cookie('pay_id')
 return response

def setsignedcookie(request):
 response = render(request, 'student/setsignedcookie.html')
 response.set_signed_cookie('token', 't123456', salt='tk')
 return response

def getsignedcookie(request):
#  token = request.get_signed_cookie('token', salt='tk')
 token = request.get_signed_cookie('token', default="guest_token123", salt='tk')
 return render(request, 'student/getsignedcookie.html',{'token':token})