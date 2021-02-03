from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.demo),
    path('ShowShoes/<cid>',views.ShowShoes),
    path('ViewShoesDetails/<shoesid>',views.ViewShoesDetails),
    path('signup',views.signup),
    path('Login',views.Login),
    path('addToCart',views.addToCart),
    path('Logout',views.Logout),
    path('ShowCartItems',views.ShowCartItems),
    path('RemoveFromCart',views.RemoveFromCart),
    path('MakePayment',views.MakePayment),
    path('contact',views.contact),
]

