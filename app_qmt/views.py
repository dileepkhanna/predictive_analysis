from django.shortcuts import render, redirect
from .models import QMTModelRegister
from app_manager.models import MaterialDetails
from django.db import IntegrityError
from django.contrib import messages
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import TheilSenRegressor
import warnings
warnings.filterwarnings('ignore')


# Create your views here.
def qmt_home(request):
    return render(request, 'qmt/qmt_home.html')


def qmt_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        date_of_birth = request.POST['dob']
        address = request.POST['address']
        password = request.POST['password']
        try:
            QMTModelRegister(username=username, email=email, contact=contact,
                                  date_of_birth=date_of_birth, address=address,
                                  password=password).save()
            messages.info(request, "qmt successfully registered")
            return redirect('/qmt_login/')
        except IntegrityError as e:
            messages.info(request, "Email already exists")
            return redirect('/qmt_register/')
    return render(request, 'qmt/qmt_sign.html')


def qmt_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            r = QMTModelRegister.objects.get(email=email, password=password)
            request.session['qmt'] = r.email
            if r is not None:
                messages.info(request, 'Welcome to qmt Page')
                return redirect('/qmt_home/')
        except QMTModelRegister.DoesNotExist as e:
            messages.info(request, 'Wrong Credentials')
            return redirect('/qmt_login/')
    else:
        return render(request, 'qmt/qmt_sign.html')


def qmt_logout(request):
    if 'qmt' in request.session:
        request.session.pop('qmt', None)
        messages.success(request, "qmt Logout Success")
        return redirect('/')
    else:
        return redirect('/qmt_home/')


def send_to_analyse(request):
    ob = MaterialDetails.objects.filter(send_to_analyse=False)
    return render(request, 'qmt/send_to_analyse.html', {'ob': ob})


def click_to_send(request, id):
    ob = MaterialDetails.objects.get(id=id)
    ob.send_to_analyse = True
    ob.save()
    messages.info(request, "Material Details Sent to Analyse")
    return redirect('/send_to_analyse/')


def qmt_material_details(request):
    ob = MaterialDetails.objects.filter(send_to_analyse=True)
    return render(request, 'qmt/qmt_material_details.html', {'ob': ob})


def algo(datas,r):
    print(datas)
    # data = pd.DataFrame(pd.read_excel("Land.xlsx"))
    # read_file = pd.read_excel("Land.xlsx")
    # read_file.to_csv("Land.csv", header=True, index=False)
    data = pd.DataFrame(pd.read_csv("Land.csv"))
    # data = pd.read_csv('Land.csv')
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

    model = TheilSenRegressor()
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


def apply_algo(request, id):
    ob = MaterialDetails.objects.get(id=id)
    r = ob.id
    input_value = []
    # da.save()
    a = ob.cement
    b = ob.sand
    c = ob.aggregate
    d = ob.steel
    e = ob.paint
    f = ob.bricks
    g = ob.tiles
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(f'id: {r}')
    input_value.append(a)
    input_value.append(b)
    input_value.append(c)
    input_value.append(d)
    input_value.append(e)
    input_value.append(f)
    input_value.append(g)
    print(input_value)
    algor = algo(input_value,r)
    print(f'Land: {algor}')
    MaterialDetails.objects.filter(id=r).update(land=algor)
    messages.success(request, 'Analysing done, Land area found successfully')
    return redirect('/qmt_home/')


def desired_land(request):
    ob = MaterialDetails.objects.all()
    return render(request, 'qmt/desired_land.html', {'ob': ob})
