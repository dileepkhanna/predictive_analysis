from django.shortcuts import render, redirect
from .models import CustomerModelRegister
from .models import CustomerInitiationForm
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.
def customer_home(request):
    return render(request, 'customer/customer_home.html')


def customer_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['dob']
        address = request.POST['address']
        password = request.POST['password']
        try:
            CustomerModelRegister(username=username, email=email, contact=contact,
                                  date_of_birth=date_of_birth, address=address,
                                  password=password).save()
            messages.info(request, "Customer successfully registered")
            return redirect('/customer_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/customer_register/')
    return render(request, 'customer/customer_sign.html')


def customer_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = CustomerModelRegister.objects.get(email=email, password=password)
            request.session['customer'] = r.email
            if r is not None:
                messages.info(request, 'Welcome to Customer Page')
                return redirect('/customer_home/')
        except CustomerModelRegister.DoesNotExist as e:
            messages.info(request, 'Wrong Credentials')
            return redirect('/customer_login/')
    else:
        return render(request, 'customer/customer_sign.html')


def customer_logout(request):
    if 'customer' in request.session:
        request.session.pop('customer', None)
        messages.success(request, "Customer Logout Success")
        return redirect('/')
    else:
        return redirect('/customer_home/')


def customer_initiation_form(request):
    ob = CustomerModelRegister.objects.all()
    if request.method == 'POST':
        customer_name = request.POST['name']
        customer_email = request.POST['mail']
        contact = request.POST['contact']
        building_type = request.POST['building']
        land_area = request.POST['area']
        soil_type = request.POST['type']
        soil_condition = request.POST['condition']
        foundation = request.POST['foundation']
        water = request.POST['water']
        CustomerInitiationForm(customer_name=customer_name, customer_email=customer_email, contact=contact,
                               building_type=building_type, land_area=land_area, soil_type=soil_type,
                               soil_condition=soil_condition, foundation=foundation, water=water).save()
        messages.info(request, "Customer Initiation Form registered successfully")
        return redirect('/customer_home/')
    return render(request, 'customer/customer_initiation_form.html', {'ob': ob})


def customer_updated_table(request):
    ob = CustomerInitiationForm.objects.filter(send_customer=True, request_estimation=False)
    return render(request, 'customer/customer_updated_table.html', {'ob': ob})


def request_estimation(request, id):
    ob = CustomerInitiationForm.objects.get(id=id)
    ob.request_estimation = True
    ob.save()
    messages.info(request, 'Details Sent to Manager for getting Estimation')
    return redirect('/customer_home/')


def receive_estimation(request):
    ob = CustomerInitiationForm.objects.filter(accept_work=False)
    return render(request, 'customer/receive_estimation.html', {'ob': ob})


def accept_work(request, id):
    ob = CustomerInitiationForm.objects.get(id=id)
    ob.accept_work = True
    ob.save()
    messages.info(request, 'Work Accepted By Customer')
    return redirect('/customer_home/')
