from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('add_guide/',views.add_guide,name='add_guide'),
    path('guide_post_page',views.guide_post_page,name='guide_post_page'),

    
    # Register and login Guide
    path("logout_guide/", views.logout_guide, name="logout_guide"),
    path("register_guide/", views.register_guide, name="register_guide"),
    path("login_guide/", views.login_guide, name="login_guide"),
    
    path("delete_guide/<int:id>", views.delete_guide, name="delete_guide"),
    path("tour_single_page/<int:id>", views.tour_single_page, name="tour_single_page"),
    



    path("order/", views.order, name="order"),
    
    
    path("profile_guide/", views.profile_guide, name="profile_guide"),
    
    path("settings/", views.settings, name="settings"),
    
    path('settings/updateprofile/<int:id>',views.updateprofile,name='updateprofile'),

    path('settings/updatepassword/<int:id>',views.updatepassword,name='updatepassword'),
    
    path('profile_guide/block_tour/<int:id>',views.block_tour,name='block_tour'),
    
    path('profile_guide/active_tour/<int:id>',views.active_tour,name='active_tour'),
    
    path("guide_singlepage/<int:id>", views.guide_singlepage, name="guide_singlepage"),
    
    path("contact/", views.contact, name="contact"),
    
    path("about/", views.about, name="about"),






]