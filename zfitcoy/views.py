from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from zfitcoy.models import *
from django.shortcuts import render,redirect
from django.template.loader import get_template
from django.http import HttpResponse, request
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, message
from fitcoy.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User


def HOME(request):
    sers = Services.objects.all()
    new = Shop.objects.all().order_by('-id')
    ser = sers[:5]
    test = Team.objects.all()
    ab = About.objects.all()
    serm = Services.objects.all()
    if request.method == "POST":
        d = request.POST
        namee = d['em']
        Newsletter.objects.create(email=namee)
    d = {"ser":ser,"serm":serm,"test":test,"new":new,"ab":ab}
    return render(request, 'index.html',d)

def ABOUT(request):
    if request.method == "POST":
        d = request.POST
        namee = d['em']
        Newsletter.objects.create(email=namee)
    test = Team.objects.all()
    ab = About.objects.all()
    sers = Services.objects.all()
    ser = sers[:5]
    d = {"test":test,"ser":ser,"ab":ab}
    return render(request, 'about.html',d)

def SERVICES(request):
    if request.method == "POST":
        d = request.POST
        namee = d['em']
        Newsletter.objects.create(email=namee)
    serm = Services.objects.all()
    sers = Services.objects.all()
    ser = sers[:5]
    test = Team.objects.all()
    d = {"test":test,"ser":ser,"serm":serm}
    return render(request, 'services.html',d)

def APPOINTMENT(request):
    if request.method == "POST":
        if 'new' in request.POST:
            d = request.POST
            a = d['fname']
            b = d['femail']
            c = d['fmobile']
            k = d['fgender']
            e = d['time']
            f = d['freach']
            g = d['fdate']
            h = d['ftime']
            i = d['faddress']
            j = d['freason']
            Appointment.objects.create(name=a,email=b,mobile=c,gender=k,Time_of_day=e,Way_to_reach=f,date=g,time=h,Address=i,Reason_for_appointment=j)
            try:
                email = 'info.ujjainastrologer@gmail.com'
                subject = "Contact US Requests "
                content = "Astrology"
                msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
                d = {'cname': a,"cemail": b,"mobile": c,"gender":k,"tim":e,"reach":f,"date":g,"time":h,"address":i,"reason":j}
                html = get_template('email3.html').render(d)
                msg.attach_alternative(html, 'text/html')
                msg.send()
                return redirect('home')
            except:
                pass
        elif 'pos' in request.POST:
            d = request.POST
            namee = d['em']
            Newsletter.objects.create(email=namee)
            return redirect('home')
    test = Team.objects.all()
    sers = Services.objects.all()
    ser = sers[:5]
    d = {"test":test,"ser":ser}
    return render(request, 'appointment.html',d)

# def BLOG(request):
    
#     return render(request, 'blog.html')

def SHOP(request):
    sers = Services.objects.all()
    ser = sers[:5]
    if request.method == "POST":
        d = request.POST
        namee = d['em']
        Newsletter.objects.create(email=namee)
    pro = Shop.objects.all()
    new = Shop.objects.all().order_by('-id')
    d = {"pro":pro,"new":new,"ser":ser}
    return render(request, 'shop.html',d)

def CONTACT(request):
    sers = Services.objects.all()
    ser = sers[:5]
    if request.method == "POST":
        if 'new' in request.POST:
            d = request.POST
            namee = d['nam']
            emaill = d['email']
            msgg = d['msg']
            Contact.objects.create(name=namee,email=emaill,message=msgg)
            try:
                email = 'info.ujjainastrologer@gmail.com'
                subject = "Contact US Requests "
                content = "Astrology"
                msg = EmailMultiAlternatives(subject, f'{content}', EMAIL_HOST_USER, [f'{email}'])
                d = {'cname': namee,"cemail": emaill,"cmessage": msgg}
                html = get_template('email.html').render(d)
                msg.attach_alternative(html, 'text/html')
                msg.send()
                return redirect('home')
            except:
                pass
        elif 'pos' in request.POST:
            d = request.POST
            namee = d['em']
            Newsletter.objects.create(email=namee)
            return redirect('home')
        
    d={"ser":ser}
    return render(request, 'contact.html',d)

#####################################Dynamic pages ##############
def SERVICES_SINGLE(request,blo_id):
    if request.method == "POST":
        d = request.POST
        namee = d['em']
        Newsletter.objects.create(email=namee)
    sersingle = Services.objects.get(id=blo_id)
    sers = Services.objects.all()
    ser = sers[:5]
    d = {"sersingle":sersingle,"ser":ser}
    return render(request, 'services_single.html',d)

def RASHI_SINGLE(request,blon_id):
    sersingle = Rashi.objects.get(id=blon_id)
    d = {"sersingle":sersingle}
    return render(request, 'Rashisingle.html',d)