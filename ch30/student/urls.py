from django.urls import path
from student.views import Home,Profile
urlpatterns = [
    path('home/',Home, name="Home"),
    # path('profile/<my_id>',Profile, name="Profile"),
    # path('profile/<int:my_id>',Profile, name="Profile"),
    # path('profile/<slug:title>',Profile, name="Profile"),
    # path('profile/<str:title>',Profile, name="Profile"),
    path('profile/<int:my_class>/<int:my_id>',Profile, name="Profile"),

]