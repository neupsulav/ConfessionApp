from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from Confession.models import myconfessionmodel, feedbackmodel

# Create your views here.


def index(request):
    if request.user.is_anonymous:
        return render(request, 'login.html')

    return render(request, 'index.html')

    # if request.user.is_authenticated:
    #     return render(request, 'index.html')
    # else:
    #     return redirect('login')


def home(request):
    objects = myconfessionmodel.objects.all()
    if request.method == 'POST':
        searchvalue = request.POST.get('search')
        if searchvalue != '':
            objects = myconfessionmodel.objects.filter(
                tosendto__icontains=searchvalue)
    data = {
        'info': objects
    }
    return render(request, 'index.html', data)


def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')

        if username == '' or password == '':
            return render(request, 'login.html', {'error': True})

        user = authenticate(username=username, password=password)

        if user is not None:
            # try
            # objects = myconfessionmodel.objects.all()
            # data = {
            #     'info': objects
            # }
            return redirect('home')
        else:
            # messages.alert(request, 'Username or password is incorrect!')
            return render(request, 'login.html', {'noaccount': True})

    return render(request, 'login.html')


def signup(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Password doesn't match on both fields")
            return render(request, 'signup.html')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!!!")
            return render(request, 'signup.html')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists!!!")
            return render(request, 'signup.html')

        if fname == '' or lname == '' or username == '' or pass1 == '' or pass1 == '' or email == '':
            return render(request, 'signup.html', {'error': True})

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, "Account created successfully")
        return render(request, 'login.html')

    return render(request, "signup.html")


def logoutuser(request):
    logout(request)
    return render(request, 'login.html')


def myconfessions(request):
    if request.method == 'POST':
        towhom = request.POST.get('towhom')
        faculty = request.POST.get('faculty')
        confessiontext = request.POST.get('confessiontext')
        yourself = request.POST.get('yourself')

        if towhom == '' or faculty == '' or confessiontext == '':
            return render(request, 'myconfession.html', {'error': True})

        data = myconfessionmodel(tosendto=towhom, facultyis=faculty,
                                 confessionmsg=confessiontext, youridentification=yourself)
        data.save()
        return render(request, 'myconfession.html', {'success': True})

    return render(request, 'myconfession.html')


def feedback(request):
    if request.method == 'POST':
        text = request.POST.get('feedbacktext')
        name = request.POST.get('yourname')

        feedbackdata = feedbackmodel(
            feedbackdetails=text, feedbackprovider=name)
        feedbackdata.save()
        return render(request, 'feedback.html', {'success': True})
    return render(request, 'feedback.html')
