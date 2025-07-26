from django.shortcuts import render, redirect
from .models import VendorModelRegister
from app_manager.models import MaterialDetails
from django.db import IntegrityError
from django.contrib import messages


# Create your views here.
def vendor_home(request):
    return render(request, 'vendor/vendor_home.html')


def vendor_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['dob']
        address = request.POST['address']
        password = request.POST['password']
        try:
            VendorModelRegister(username=username, email=email, contact=contact,
                                date_of_birth=date_of_birth, address=address,
                                password=password).save()
            messages.info(request, "vendor successfully registered")
            return redirect('/vendor_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/vendor_register/')
    return render(request, 'vendor/vendor_sign.html')


def vendor_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = VendorModelRegister.objects.get(email=email, password=password)
            request.session['vendor'] = r.email
            if r is not None:
                messages.info(request, 'Welcome to vendor Page')
                return redirect('/vendor_home/')
        except VendorModelRegister.DoesNotExist as e:
            messages.info(request, 'Wrong Credentials')
            return redirect('/vendor_login/')
    else:
        return render(request, 'vendor/vendor_sign.html')


def vendor_logout(request):
    if 'vendor' in request.session:
        request.session.pop('vendor', None)
        messages.success(request, "vendor Logout Success")
        return redirect('/')
    else:
        return redirect('/vendor_home/')


def received_material_details(request):
    ob = MaterialDetails.objects.filter(confirm=False)
    return render(request, 'vendor/received_material.html', {'ob': ob})


def send_to_supply(request, id):
    ob = MaterialDetails.objects.get(id=id)
    ob.confirm = True
    ob.save()
    messages.info(request, 'Successfully Sent to Provide Supply')
    return redirect('/vendor_home/')


def supply_materials(request):
    ob = MaterialDetails.objects.filter(confirm=True, send_from_vendor=False)
    return render(request, 'vendor/supply_materials.html', {'ob': ob})


def send_to_customer(request, id):
    if request.method == 'POST':
        supply_id = request.POST['supply_id']
        print(supply_id)
        print(id)
        ob = MaterialDetails.objects.get(id=id)
        ob.supply_id = supply_id
        ob.send_from_vendor = True
        ob.save()
        messages.info(request, 'Successfully added Supply id')
        return redirect('/vendor_home/')
    return render(request, 'vendor/supply_materials.html')


def view_details(request):
    ob = MaterialDetails.objects.filter(confirm=True, send_from_vendor=True)
    return render(request, 'vendor/view_details.html', {'ob': ob})
