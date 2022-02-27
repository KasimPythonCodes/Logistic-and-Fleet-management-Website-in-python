from django.urls import path,include
from app.views import*
from django.contrib.auth import views as auth_views

from app.forms import*
 

urlpatterns = [
    

    path('pick/', User_Pickup.as_view(),name='pick'),
    path('', home14,name='home'),

    path('privacy-&-policy.html/', privacy,name='privacy'),



    

    #models views end
    path('vgo-web.html/',  home1),
    path('success.html/',  success),

    path('term-&-condition.html/',  Term),

    # path('a/', home2),
    # path('b/', home3),
    path('vgo-blog/', home4),
    path('about-us-vgo/', home5),
    path('contact-us/', home6),
    path('Faqs/', home7),
    # path('g/', home8),
    path('tranpost/', home9),
    # path('i/', home10),
    path('Our-Team/', home11),
    path('fleet_management/', home12),
    path('logistic/', home13),

    

    path('sign/', Registration_User_Form.as_view() , name='sign'),
    # path('vender/', Vender_Profile.as_view() , name='vender'),


#start forms

    path('accounts/login/' , auth_views.LoginView.as_view(template_name='myhtml/login.html' ,
     authentication_form=LoginuserForm) , name='login'),
    path('logout/' , auth_views.LogoutView.as_view(next_page='login') , name='logout'),
    path('changepassword/' , auth_views.PasswordChangeView.
    as_view(template_name='myhtml/passwordchange.html',
    form_class=MypasswordchangeForm , success_url='/passwordchangedone/'),name="changepassword") ,
    path('passwordchangedone/'
    ,auth_views.PasswordChangeView.as_view(template_name=
    'myhtml/passwordchangedone.html' ),name="passwordchangedone"),

    path('password_reset/' , auth_views.PasswordResetView.as_view(
    template_name='myhtml/password_reset.html' , 
    form_class=Email_Check),name='password_reset'),

    path('password_reset/done' , auth_views.PasswordResetDoneView.as_view(
    template_name='myhtml/password_reset_done.html'),name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/' ,
    auth_views.PasswordResetConfirmView.as_view(
    template_name='myhtml/password_reset_confirm.html' , 
    form_class=Usersetpasswordform),name='password_reset_confirm'),

    path('password_reset_complete/' , auth_views.PasswordResetCompleteView.as_view(
    template_name='myhtml/password_complete.html'),name='password_reset_complete'),
    path('email/' , email_user , name="email")
#end forms

]