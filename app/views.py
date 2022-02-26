
from django.shortcuts import redirect, render 
from django.contrib import messages
from django.views import View
from app.forms import*
from django.core.mail import send_mail
from app.models import*
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


#######################


class  Registration_User_Form(View):
    def get(self , request):
      form=RegistrationFormUser()
      return render(request , 'myhtml/registration.html',{'form':form})

    def post(self , request):
        form=RegistrationFormUser(request.POST or None)
        if form.is_valid():
            messages.info(request, "Registration is Successfully Please Login!!")
            form.save()
            return redirect('/accounts/login/')
        return render(request, 'myhtml/registration.html' , {'form':form})    


###################

def email_user(request):
  send_mail(
        'VGO RIDES', 
        'Visit Link', 
        'kasim@veeaargroup.com',
        [],
        fail_silently=False
      )
    

#########################
class User_Pickup(View):
    def get(self,request):
      form=PICKUP_form_type()
      stu =Select_Goods.objects.all()
      print(stu)
      return render(request , 'user_pick_info.html' , {'form':form, 'stu':stu})
    def post(self , request):
      form=PICKUP_form_type(request.POST or None )
      if form.is_valid():
        # messages.info(request , "Success!!")
        form.save()
        form=PICKUP_form_type()
        return redirect('/success.html/')
      return render(request, 'user_pick_info.html',{'form':form })  
          


def success(request):
    return render(request, 'success.html')

def home1(request):
    return render(request, 'index.html')

def home4(request):
    return render(request, 'blog-single.html')  

def home5(request):
    return render(request, 'page-about-us.html')

def home6(request):
    return render(request, 'page-contact-us.html')

def home7(request):
    return render(request, 'page-faqs.html')

def home9(request):
    return render(request, 'service-single.html')

def privacy(request):
    return render(request, 'privacy.html')

def Term(request):
    return render(request, 'term.html')

def home11(request):
    return render(request, 'VGO-Family.html')

def home12(request):
    return render(request, 'fleet.html')

def home13(request):
    return render(request, 'logistics.html')    

