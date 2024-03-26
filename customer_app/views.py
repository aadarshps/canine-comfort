from django.shortcuts import render,redirect

from accounts.models import *
from customer_app.forms import *
from staff_app.models import Report
from django.contrib.auth.decorators import login_required
# Create your views here.
def customer_home(request):
    return render(request,'customertemp/index.html')

@login_required(login_url='sign-in')
def boarding_view(request):
    if request.method == 'POST':
        form = BoardingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.customer_id = request.user.id
            form.save()
            return redirect('boarding-details')
    else:
        form = BoardingForm()
    return render(request, 'customertemp/boarding.html', {'form': form})

@login_required(login_url='sign-in')
def list_boarding_details(request):
    data = Boarding.objects.filter(customer=request.user,status="upcoming")
    return render(request, 'customertemp/boarding_detials.html',{'data':data})

@login_required(login_url='sign-in')
def updated_boarding_details(request):
    data = Boarding.objects.filter(customer=request.user).exclude(status="upcoming")
    return render(request, 'customertemp/boarding_detials_updated.html',{'data':data})

@login_required(login_url='sign-in')
def dog_add(request):
    if request.method == 'POST':
        form = DogForm(request.POST,request.FILES)
        if form.is_valid():
            form.instance.customer_id = request.user.id
            form.save()
            return redirect('dog-view-customer')
    else:
        form = DogForm()
    return render(request, 'customertemp/dog_add.html', {'form': form})

@login_required(login_url='sign-in')
def dog_view_customer(request):
    data = Dog.objects.filter(customer=request.user)
    return render(request,'customertemp/dog_view.html',{'data':data})

@login_required(login_url='sign-in')
def feeds_add(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.instance.customer_id = request.user.id
            form.save()
            return redirect('feeds-view-customer')
    else:
        form = FeedbackForm()
    return render(request, 'customertemp/feedback_add.html', {'form': form})

@login_required(login_url='sign-in')
def feeds_view_customer(request):
    data = Feedback.objects.filter(customer=request.user)
    return render(request,'customertemp/feedback_view.html',{'data':data})

@login_required(login_url='sign-in')
def staff_view_customer(request):
    staff = User.objects.filter(role=2)
    data = Userprofile.objects.filter(user__in=staff)
    return render(request, 'customertemp/staff_view.html',{'data':data})

@login_required(login_url='sign-in')
def list_reports_customer(request):
    data = Report.objects.filter(customer=request.user)
    return render(request, 'customertemp/report_detials.html',{'data':data})

