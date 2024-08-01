from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate, logout
from django.contrib import messages
from cust.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from ladmin.models import Borrowing
from cust.models import customer



def home(request):
    if request.user.is_authenticated:
        user_id = request.session.get('_auth_user_id')
        if user_id:
            # Fetch the user object using the user_id
            user = User.objects.get(pk=user_id)
        return render(request,'cust/home.html',{'User': user})
        
    return render(request,'cust/home.html')

def contact(request):
    return render(request,'cust/contacts.html')

def logins(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(username=username,password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request,('Login Sucessful!!!'))
            return redirect('home')
        
        else:
            messages.success(request,('Login UNSucessful!!!'))
            return redirect('login')
    return render(request,'cust/login.html')


def logouts(request):
    logout(request)
    messages.success(request,("You've loged out sucessfully"))
    return redirect('home')




# register page 
def register(request):
    form=RegisterForm() 
    if request.method == 'POST':
        form=RegisterForm(request.POST) 
        print(form)
        if form.is_valid(): 
            
            form.save()
            

            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']

            # login

            user=authenticate(username=username, password=password)
            login(request, user) 
            messages.success(request, ('Reg success, logined in ..')) 
            return redirect('home')

        else:
            
            messages.success(request, ('Reg un success, try again..')) 
            return redirect('register')

    return render(request, 'cust/register.html', {'form':form})




@login_required
def user_borrowings(request):
    user = request.user.customer
    
    borrowings = Borrowing.objects.filter(user=user)
    return render(request, 'cust/borrow.html', {'borrowings': borrowings})


@login_required
def profile(request):
    user = request.user.customer  # Get the customer instance associated with the logged-in user
    borrowings = Borrowing.objects.filter(user=user)
    return render(request, 'cust/profilepage.html', {'borrowings': borrowings, 'user': request.user})

@login_required
def editpro(request,id):
    if request.method == 'POST':
        sname=request.POST.get('name')
        smobile=request.POST.get('mobile')
        
        
        
        sid=request.POST.get('id')
        if sid:
            store=customer.objects.get(id=sid)
            store.name=sname 
            store.mobile= smobile
          
            store.save()
            
            return redirect('profilepage')
        
        else:
            pass
    s=customer.objects.get(pk=id)
    return render(request,'cust/editprof.html',{'ser':s}) 