import os
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from . models import *
from django.urls import reverse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model 
from . forms import PostAdminForm
User = get_user_model()


##### Guide Single Page #####
def guide_singlepage(request,id):
    fltr = Order.objects.filter(id=id)
    order_user = Order.objects.filter(user_id = request.user.id ).order_by('-id')
    counts_user=0
    
    for x in order_user:
        if x.utesdiq == 1:
            counts_user +=1
            if x.gtesdiq == 1:
                counts_user -= 1
    return render(request,'main/guide_singlepage.html',{'fltr':fltr,'counts_user':counts_user})

##### Home Page #####

def index(request):
    
    img = CustomUser.objects.filter(id = request.user.id)
    say = Order.objects.all().count()
    sel = CustomUser.objects.raw("SELECT username FROM main_user WHERE main_user.choise == 'guide' ")
    order = Order.objects.all().select_related().order_by('-id')

    return render(request,'main/index.html',{'order':order,'sel':sel,'img':img,'say':say})

##### Tour Single Page #####
def tour_single_page(request,id):
    
    
   
    order = Order.objects.all().select_related().order_by('-id')
    img = CustomUser.objects.filter(id = request.user.id)
    fltr = Order.objects.filter(id = id )
    say = Order.objects.all().count()
   
  
    
    tour = Order.objects.filter(user_id_id = request.user.id).count()
    context = {'tour':tour,'say':say,'img':img,'fltr':fltr,'order':order,
     
     }
    return render(request , 'main/tour_single_page.html' , context)

##### Guide and User Profile #####
def profile_guide(request):
    img = CustomUser.objects.filter(id = request.user.id)
    
    order = Order.objects.all().order_by('-id')

    order_guide = Order.objects.filter(guide_id = request.user.id ).select_related().order_by('-id')
    counts_guide=0
    for x in order_guide:
        if x.utesdiq == 1:
            counts_guide +=1
            if x.gtesdiq == 1:
                counts_guide -= 1
                
    place = 3
    for x in order_guide:
        if x.gtesdiq == 1:
            place -= 1
            
    

    return render(request,'main/profile_guide.html',{'counts_guide':counts_guide,'order_guide':order_guide,
        'img':img,'order':order,'place':place})
    

##### Guide Order #####
def order(request):
    
    order = Order.objects.filter(guide_id=request.user.id).select_related()
    counts_guide=0
    for x in order:
        if x.utesdiq == 1:
            counts_guide +=1
            if x.gtesdiq == 1:
                counts_guide -= 1
   
    user = CustomUser.objects.all()
    return render(request , 'main/order.html' , {'order':order,'user':user,'counts_guide':counts_guide})

##### Block and Active Tour by Guide #####
def block_tour(request,id):
    order = Order.objects.get(id=id)

    
    order.active = 0
    order.save()
    
    return HttpResponseRedirect(reverse('profile_guide'))

def active_tour(request,id):
    
    order = Order.objects.get(id=id)
    
    order.active = 1
    order.save()
    
    return HttpResponseRedirect(reverse('profile_guide'))

##### Guide and User Settings #####
@login_required
def settings(request):
    img = CustomUser.objects.filter(id = request.user.id)
 
                
                
    userid = CustomUser.objects.get(id = request.user.id)
    return render(request, 'main/settings.html',{
    'userid':userid,'img':img})

def updateprofile(request,id):
    user = CustomUser.objects.get(id=id)

    if request.method == 'POST':
    
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        information = request.POST['information']

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.phone = phone
        user.information = information
        user.save()

    if request.method == 'POST' and 'foto' in request.FILES:
        foto=request.FILES['foto']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)

        user.img = uploaded_file_url

        user.save()
 
    if request.method == 'POST' and 'cover' in request.FILES:
        foto = request.FILES['cover']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)
        
        user.cover = uploaded_file_url

        user.save()

    return HttpResponseRedirect(reverse('settings'))

def updatepassword(request,id):
    user = CustomUser.objects.get(id=id)

    if request.method == 'POST':
        password = request.POST['password']
        new_password = request.POST['new_password']

        if user.check_password(password):
            if new_password == request.POST['new_passconf']:
                user.set_password(new_password)

                user.save()
            else:
                messages.warning(request,'Parollar uygun deyil')
        else:
            messages.warning(request,'Xahis Edirik Cari Parolu Daxil Edin')

    return HttpResponseRedirect(reverse('settings'))
    


def guide_post_page(request):
    guide = Guide.objects.filter(user_id = request.user.id).order_by('-id')
    guide_id = Guide.objects.all()

    form = PostAdminForm()

    return render(request, 'main/guide_post_page.html',{'form':form,'guide':guide,'guide_id':guide_id})

def add_guide(request):
    
    if request.method=='POST' :
        if 'foto' in request.FILES:
            foto=request.FILES['foto']
            fs = FileSystemStorage()
            filename=fs.save(foto.name,foto)
            uploaded_file_url=fs.url(filename)
        
        form = PostAdminForm()
        title = request.POST['title']
        description = request.POST['description']
        about = request.POST['about']
        duration = request.POST['duration']
        meeting_point = request.POST['meeting_point']
        transport = request.POST['transport']
        whats_included = request.POST['whats_included']
        price = request.POST['price']
        extra = request.POST['extra']
        restriction = request.POST['restriction']
        itinerary = request.POST['itinerary']
        # us_id = request.POST['us_id']
        # r = CustomUser.objects.get(id=us_id)
        insert = Guide( tesdiq=0,title=title,description=description,content=form,about=about,duration=duration,price=price,extra=extra,
                    meeting_point=meeting_point,transport=transport,whats_included=whats_included,
                    restriction=restriction,itinerary=itinerary,user_id = request.user.id,photo = uploaded_file_url
                        )
        insert.save()
        
        # s = int(request.POST['tour_id'])
        tour = Guide.objects.latest('id')
        ussave = Order(gtesdiq=0,guide_id=request.user.id,gstatus=0,utesdiq=0,tur_id=tour,
        guide_username=request.user.username,guide_photo = request.user.img,guide_cover = request.user.cover,
        guide_phone = request.user.phone,guide_information = request.user.information)
        ussave.save()
       
        
      
        
    return HttpResponseRedirect(reverse('profile_guide'))

def delete_guide(request,id):
    guide = Guide.objects.get(id=id)
    guide.delete()
    return HttpResponseRedirect(reverse('guide_post_page'))

def contact(request):
  
    template = loader.get_template('main/contact.html')
    return HttpResponse(template.render({},request))

def about(request):
   
    template = loader.get_template('main/about.html')
    return HttpResponse(template.render({},request))

def register_guide(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        information = request.POST['information']
        website = request.POST['website']

        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
    if request.method == 'POST' and 'foto' in request.FILES:
        foto=request.FILES['foto']
        fs = FileSystemStorage()
        filename=fs.save(foto.name,foto)
        uploaded_file_url=fs.url(filename)
        if password==confirm_password:
            if CustomUser.objects.filter(username=username).exists():
                messages.info(request, 'Bu istifadeci artiq movcuddur')
                return redirect('register_guide')
            elif CustomUser.objects.filter(email=email).exists():
                messages.info(request, 'Bu email artiq movcuddur')
                return redirect('register_guide')
            else:
                user = CustomUser.objects.create_user(img=uploaded_file_url,username=username, password=password, 
                                        email=email,phone=phone,information=information ,website=website,
                                        first_name=first_name, last_name=last_name , choise = 'guide')
                
                user.save()
                
                
                return redirect('login_guide')
        else:
            messages.info(request, 'Parollar uygun deyil')
            return redirect('register_guide')
            
    else:
        return render(request, 'main/register_guide.html')
    

def login_guide(request): 
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:

            auth.login(request,user)
            return redirect('profile_guide')
                 
        else:
            
            messages.info(request, 'Login ve ya parol yanlishdir')
            return redirect('login_guide')
        
    else:
        
        return render(request, 'main/login_guide.html' )
    
def logout_guide(request):
    auth.logout(request)
    return redirect('login_guide')
    

