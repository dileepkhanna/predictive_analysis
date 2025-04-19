from django.shortcuts import render, redirect
from .models import ManagerModelRegister
from .models import MaterialDetails
from app_customer.models import CustomerInitiationForm
from django.db import IntegrityError
from django.contrib import messages
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import warnings
warnings.filterwarnings('ignore')


# Create your views here.
def manager_home(request):
    return render(request, 'manager/manager_home.html')


def manager_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['dob']
        address = request.POST['address']
        password = request.POST['password']
        try:
            ManagerModelRegister(username=username, email=email, contact=contact,
                                 date_of_birth=date_of_birth, address=address,
                                 password=password).save()
            messages.info(request, "manager successfully registered")
            return redirect('/manager_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/manager_register/')
    return render(request, 'manager/manager_sign.html')


def manager_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = ManagerModelRegister.objects.get(email=email, password=password)
            request.session['manager'] = r.email
            if r is not None:
                messages.info(request, 'Welcome to manager Page')
                return redirect('/manager_home/')
        except ManagerModelRegister.DoesNotExist as e:
            messages.info(request, 'Wrong Credentials')
            return redirect('/manager_login/')
    else:
        return render(request, 'manager/manager_sign.html')


def manager_logout(request):
    if 'manager' in request.session:
        request.session.pop('manager', None)
        messages.success(request, "manager Logout Success")
        return redirect('/')
    else:
        return redirect('/manager_home/')


def customer_initiation_table(request):
    ob = CustomerInitiationForm.objects.all()
    return render(request, 'manager/customer_initiation_table.html', {'ob': ob})


# def update(request, id):
#     ob = CustomerInitiationForm.objects.get(id=id)
#     if request.method == 'POST':
#         ob.customer_name = request.POST["name"]
#         ob.customer_email = request.POST["mail"]
#         ob.contact = request.POST["contact"]
#         ob.building_type = request.POST["building"]
#         ob.land_area = request.POST["area"]
#         ob.soil_type = request.POST["type"]
#         ob.soil_condition = request.POST["condition"]
#         ob.foundation = request.POST["foundation"]
#         ob.water = request.POST["water"]
#         ob.save()
#         return redirect('/manager_home/')
#     return render(request, 'manager/update.html', {'ob': ob})


def update1(request, id):
    ob = CustomerInitiationForm.objects.filter(id=id)
    return render(request, 'manager/update.html', {"ob": ob})


def content_update(request,customer_email):
    ob = CustomerInitiationForm.objects.get(customer_email=customer_email)
    print(customer_email)
    if request.method == 'POST':
        customer_name = request.POST["name"]
        customer_email = request.POST["mail"]
        contact = request.POST["contact"]
        building_type = request.POST["building"]
        land_area = request.POST["area"]
        soil_type = request.POST["type"]
        soil_condition = request.POST["condition"]
        foundation = request.POST["foundation"]
        water = request.POST["water"]
        ob.customer_name=customer_name
        ob.customer_email=customer_email
        ob.contact=contact
        ob.building_type=building_type
        ob.land_area=land_area
        ob.soil_type=soil_type
        ob.soil_condition=soil_condition
        ob.foundation=foundation
        ob.water=water
        ob.save()
    return redirect('/manager_home/')


def show_customer(request):
    ob = CustomerInitiationForm.objects.filter(send_customer=False)
    return render(request, 'manager/updated_table.html', {'ob': ob})


def send_customer(request, id):
    ob = CustomerInitiationForm.objects.get(id=id)
    ob.send_customer = True
    ob.save()
    messages.info(request, 'Successfully Sent Updated Content to Customer')
    return redirect('/manager_home/')


def material_details(request):
    return render(request, 'manager/material_details.html')


def material_details_form(request):
    if request.method == 'POST':
        cement = request.POST['cement']
        sand = request.POST['sand']
        aggregate = request.POST['aggregate']
        steel = request.POST['steel']
        paint = request.POST['paint']
        bricks = request.POST['bricks']
        tiles = request.POST['tiles']
        MaterialDetails(cement=cement, sand=sand, aggregate=aggregate, steel=steel,
                        paint=paint, bricks=bricks, tiles=tiles).save()
        messages.info(request, 'Materials Details Registered')
        return redirect('/manager_home/')
    return render(request, 'manager/manager_details.html')


def price_analyse(request):
    ob = CustomerInitiationForm.objects.filter(send_customer=True, request_estimation=True)
    return render(request, 'manager/price_output.html', {'ob': ob})


def algorithm(datas,r):
    print(datas)
    # data = pd.DataFrame(pd.read_excel("Construction Cost.xlsx"))
    # read_file = pd.read_excel("Construction Cost.xlsx")
    # read_file.to_csv("Construction Cost.csv", header=True, index=False)
    # data = pd.DataFrame(pd.read_csv("Construction Cost.csv"))
    data = pd.read_csv('Construction Cost.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]
    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = QuadraticDiscriminantAnalysis()
    model.fit(data_x, data_y)
    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])
    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


# a = algorithm([61, 1, 0, 148, 203, 0, 1, 160, 0, 0, 2, 1, 3])
# print(a)


def apply_algorithm(request, id):
    ob = CustomerInitiationForm.objects.get(id=id)
    r = ob.id
    input_value = []
    # da.save()
    a = ob.building_type
    b = ob.soil_type
    c = ob.soil_condition
    d = ob.foundation
    print(a)
    print(b)
    print(c)
    print(d)
    print(f'id: {r}')
    input_value.append(a)
    input_value.append(b)
    input_value.append(c)
    input_value.append(d)
    print(input_value)
    algo = algorithm(input_value,r)
    print(f'Cost: {algo}')
    CustomerInitiationForm.objects.filter(id=r).update(cost=algo)
    return redirect('/price_prediction/')


def price_prediction(request):
    ob = CustomerInitiationForm.objects.filter(price_send=False)
    return render(request, 'manager/price_prediction.html', {'ob': ob})


def send_cost(request, id):
    ob = CustomerInitiationForm.objects.get(id=id)
    ob.price_send = True
    ob.save()
    messages.info(request, 'Price Sent Successfully to Customer')
    return redirect('/price_prediction/')
