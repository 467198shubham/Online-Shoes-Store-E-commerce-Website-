from django.shortcuts import render,HttpResponse,redirect
from Myadmin.models import Shoes,Category,UserInfo,MyCart,CardDetails,contact
# Create your views here.
def demo(request):
    allshoes=Shoes.objects.all()
    cats= Category.objects.all()
    return render(request,'master.html',{'shoe':allshoes,'cats':cats})
def contact(request):
    return render(request,'contact.html',{})
    
def ShowShoes(request,cid):
    allshoes=Shoes.objects.filter(category=cid)
    return render(request,'ShowShoes.html',{'shoe':allshoes})

def ViewShoesDetails(request,shoesid):  
    shoes=Shoes.objects.get(id=shoesid)
    return render(request,'ViewShoesDetails.html',{'shoes':shoes})
def addToCart(request):
    username=request.session.get("username",'Not set')
    if(request.method=="POST"):
        
        if(username=='Not set'):
            #if session is not created then redirect the user to home page.
            
            return redirect(Login)
        else:
           # return HttpResponse('Session is Created...')
           # add to product in cart
           shoesid=request.POST['shoesid']
           shoesName=request.POST['shoesName']
           price=request.POST['shoesprice']
           qty=request.POST['qty']
           user=UserInfo.objects.get(username=username)
           shoes=Shoes.objects.get(id=shoesid)
           try:
               cart=MyCart.objects.get(username=user,shoes=shoes)
           except:
               cart=MyCart()
               cart.username=UserInfo.objects.get(username=username)
               cart.shoes=Shoes.objects.get(id=shoesid)
               cart.qty=qty
               cart.save()    
               return HttpResponse('Added To Cart.....')
           else:
               return HttpResponse('Item already in cart')
def ShowCartItems(request):
     username=request.session.get("username",'Not set')
     if(username=='Not Set'):
         return render(Login)
     else:
         user=UserInfo.objects.filter(username=username)
         cartitems=MyCart.objects.filter(username=username)
         total=0
         for cart in cartitems:
             total+= cart.qty * cart.shoes.price
         request.session['Total'] = total
         return render(request, 'ShowCartItems.html',{'cartitems':cartitems})

def MakePayment(request):
    if(request.method=='GET'):
        return render(request,'MakePayment.html',{})
    else:
        cardno=request.POST['cardno']
        cvv=request.POST['cvv']
        expiry=request.POST['expiry']
    try:
        buyer=CardDetails.objects.get(cardno=cardno,cvv=cvv,expiry=expiry)     
        owner=CardDetails.objects.get(cardno='222',cvv="123",expiry="21/2021")  
        buyer.amount-=request.session['Total']   
        owner.amount+=request.session['Total']   
        buyer.save()
        owner.save()
        return HttpResponse('Payment Done Successfully....')
    except:
        return HttpResponse('Invalid Card Details')
    
def RemoveFromCart(request):
    if(request.method=="post"):
        cartid=request.post["cart_id"]
        c1=MyCart.objects.get(id=cartid)
        c1.delete()
        return redirect(ShowCartItems)
    
        
def signup(request):
    if(request.method=='GET'):
        return render(request,'signup.html')
    else:
        username=request.POST['Username']
        password=request.POST['Password']
        try:
            result=UserInfo.objects.get(username=username)
        except:
            user=UserInfo(username,password)
            user.save()
            return redirect(Login)
        else:
            return HttpResponse('This is already existing')
def contact(request):
     if(request.method=='GET'):
         return render(request,'contact.html')
     else:
         firstname=request.POST['firstname']
         lastname=request.POST['lastname']
         country=request.POST['country']
         subject=request.POST['subject']
     try:
         contacts=contact.objects.get(firstname=firstname,lastname=lastname,country=country,subject=subject)
     except:
         contacts.save()
         return redirect(demo)
def Login(request):
    if(request.method=='GET'):
        return render(request,'Login.html') 
    else:
        username=request.POST['Username']    
        password=request.POST['Password'] 
        try:
            user=UserInfo.objects.get(username=username,password=password)
           #store the information in  session
            request.session['username']=username
        except:
            return HttpResponse('Invalid Credential')
        else:
            return redirect(demo)   
def Logout(request):
    if(request.method=='GET'):
        del request.session['username']
        #Redirect to home page.
        return redirect(demo)
        