from django.shortcuts import render
from myapp.models import Page, Post, Song
from django.contrib.auth.models import User

def home(request):
  return render(request, 'myapp/home.html')

def show_user_data(request):
  data1 = User.objects.all()
  data2 = User.objects.filter(email="raj@34example.com")
  data3 = User.objects.filter(mypage__pcat='tech')
  data4 = User.objects.filter(post__ptpublished='2026-02-13')
  data5 = User.objects.filter(song__sduration=4)
  return render(request, 'myapp/user.html', {'data1':data1, 'data2':data2, 'data3':data3, 'data4':data4, 'data5':data5})

def show_page_data(request):
  data1 = Page.objects.all()
  data2 = Page.objects.filter(pcat='Tech')
  data3 = Page.objects.filter(user__email='raj@example.com')
  return render(request, 'myapp/page.html', {'data1':data1, 'data2':data2, 'data3':data3})

def show_post_data(request):
  data1 = Post.objects.all()
  data2 = Post.objects.filter(ptpublished='2024-12-13')
  data3 = Post.objects.filter(user__username='raj')
  return render(request, 'myapp/post.html', {'data1':data1, 'data2':data2, 'data3':data3})

def show_song_data(request):
  data1 = Song.objects.all()
  data2 = Song.objects.filter(sduration=4)
  data3 = Song.objects.filter(user__username='sahil')
  return render(request, 'myapp/song.html', {'data1':data1, 'data2':data2, 'data3':data3})
