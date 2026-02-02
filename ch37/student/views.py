from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def setsession(request):
  request.session['fname'] = 'Aman'
  request.session['lname'] = 'Roy'
  # request.session.set_expiry(10) # value  in seconds
  # request.session.set_expiry(0) # sesssion expires when we close the browser
  return render(request, 'student/setsession.html')
 
def getsession(request):
  # first_name = request.session['fname']
  first_name = request.session.get('fname')
  last_name = request.session.get('lname')
  # first_name = request.session.get('fname','Guest')
  return render(request, 'student/getsession.html',{'first_name':first_name,'last_name':last_name})

def delsession(request):
  if 'lname' in request.session:
    del request.session['lname']
  return render(request, 'student/delsession.html')

def flushsession(request):
  request.session.flush()
  return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
  keys = request.session.keys()
  print(keys)
  items = request.session.items()
  print(items)
  age = request.session.setdefault('age',31)
  print(age)
  
  session_cookies_age = request.session.get_session_cookie_age()
  print("session cookie age",session_cookies_age) 
  
  expire_age = request.session.get_expiry_age()
  print("expire age",expire_age)
  
  expire_date = request.session.get_expiry_date()
  print("expire age",expire_date)
  
  expire_at_browser_close = request.session.get_expire_at_browser_close()
  print("expire_at_browser_close",expire_at_browser_close)
  
  return render(request, 'student/sessionmethodsinview.html')


def sessionclear(request):
  request.session.clear_expired()
  return render(request, 'student/sessionclear.html')

def sessionmethodsintemplate(request):
  keys = request.session.keys()
  items = request.session.items()
  return render(request, 'student/sessionmethodsintemplate.html',{'keys':keys,'items':items})

def settestcookie(request):
  request.session.set_test_cookie()
  return render(request, 'student/settestcookie.html')

def checktestcookie(request):
  print(request.session.test_cookie_worked())
  return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
  request.session.delete_test_cookie()
  return render(request, 'student/deltestcookie.html')
