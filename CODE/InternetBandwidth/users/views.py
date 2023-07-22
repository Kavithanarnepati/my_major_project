from django.shortcuts import render, HttpResponse
from django.contrib import messages
from tenacity import retry_if_not_exception_message

from .forms import UserRegistrationForm
from .models import UserRegistrationModel
from django.conf import settings
import pandas as pd
import os


# Create your views here.
def UserRegister(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserRegistrationForm()
            return render(request, 'userregister.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'userregister.html', {'form': form})


def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'userlogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'userlogin.html', {})


# Create your views here.
def index1(request):
    return render(request, 'base.html')


def userbase(request):
    return render(request, 'users/UserHome.html')


def usrViewData(request):
    path = os.path.join(settings.MEDIA_ROOT, 'Punedata.csv')
    df = pd.read_csv(path)
    df = df.to_html(index=False)
    return render(request, 'users/viewDataset.html', {'data': df})


def usrEDAData(request):
    # from .utility.edaanalysis import startEda
    # obj = startEda()
    return render(request, 'users/edanalysis.html', {})


def usrMachineLearning(request):
    from .utility.MachineLearning import startProcess
    df_dt, dt_acc, rf_df, rf_acc, knn_df, knn_acc = startProcess()
    return render(request, 'users/usrMLResults.html',
                  {'df_dt': df_dt, 'dt_acc': dt_acc, 'rf_df': rf_df, 'rf_acc': rf_acc, 'knn_df': knn_df,
                   'knn_acc': knn_acc})


def usrPredictForm(request):
    path = os.path.join(settings.MEDIA_ROOT, 'Punedata.csv')
    df = pd.read_csv(path)
    lac = df['LAC'].values
    if request.method=='POST':
        from .utility.userPredictions import get_user_input
        lac = request.POST.get('laccode')
        result = get_user_input(lac)
        msg = f'In The LAC {lac} the Internet Consumption {result} GB (lacks)'

        return render(request, 'users/predictForm.html', {'lac': lac,'msg':msg})

    else:

        return render(request,'users/predictForm.html',{'lac': lac})