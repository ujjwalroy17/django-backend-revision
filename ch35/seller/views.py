from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.decorators import login_and_role_required

# Create your views here.
@login_and_role_required('seller')
def seller_dashboard_view(request):
    return render(request,'seller/dashboard.html')