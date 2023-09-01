from django.shortcuts import render,redirect
from django.http import HttpResponse
from.models import User,Contacts
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import Myusercreationform,contactForm
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from.utils import   get_random_activity
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required(login_url='login')
def contactList(request):
    user = User.objects.all()
    contacts = Contacts.objects.filter(user_id = request.user.id).order_by('first_name')
    q = request.GET.get('q', '') 
    contact = Contacts.objects.filter(
        Q(first_name__icontains=q) | Q(last_name__icontains=q),
        user_id=request.user.id
    ).order_by('first_name')
    search_string = request.GET.get('q', '')
    context = {'user': user, 'contacts': contacts, 'contact': contact,'search_string': search_string}
    return render(request,'contact_list.html',context)

def loginpage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request,user)
                return redirect('contactList')
            else:
                messages.error(request, 'Invalid email or password')

        except User.DoesNotExist:
            messages.error(request, 'User does not exist')


    context ={'page': page}
    return render(request,'login_register.html',context)

@login_required
def logoutuserpage(request):
    logout(request)
    return redirect('home')   

def signup(request):
    form = Myusercreationform()
    if request.method == 'POST':
        form = Myusercreationform(request.POST)
        if form.is_valid():
           user = form.save(commit = False) 
           user.username = user.username.lower()
           user.save()
           login(request, user)
           subject = 'welcome to PhoneBook!!'
           message = f'Hi {user.username}, thank you for registering in PhoneBook.'
           email_from = settings.EMAIL_HOST_USER
           recipient_list = [user.email]
           send_mail( subject, message, email_from, recipient_list )
           return redirect('home')
        else:
            messages.error (request, 'An error occurred while registering you')
    return render(request,'login_register.html', {'form':form})

@login_required
def createContact(request):
    form = contactForm()
    contact = Contacts.objects.all()
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user_id = request.user.id
            contact.save()
            return redirect('contactList')
        else:
            messages.error (request, 'An error occurred while adding the contact, please try again')
    context={'form':form}
    return render(request,'contact_create.html',context)

@login_required
def contactView(request, pk):
    contact = Contacts.objects.get(id=pk)
    form = contactForm()
    context = {'contact': contact, 'form': form}
    return render(request, 'contact_view.html', context)

@login_required
def add_to_favourite(request, pk):  # Renamed from 'add_favorite'
    contact = Contacts.objects.get(id=pk)
    if not contact.favourites:  # Corrected field name
        contact.favourites = True
        contact.save()
    return redirect('contacts', pk=pk)



@login_required
def remove_favorite(request, pk):
    contact = Contacts.objects.get(id=pk)
    if contact.favourites:
        contact.favourites = False
        contact.save()
    return redirect('contacts', pk=pk)


@login_required
def add_to_emergency(request, pk):  
    contact = Contacts.objects.get(id=pk)
    if not contact.Emergency:  
        contact.Emergency = True
        contact.save()
    return redirect('contacts', pk=pk)


@login_required
def remove_emergency(request, pk):
    contact = Contacts.objects.get(id=pk)
    if contact.Emergency:
        contact.Emergency = False
        contact.save()
    return redirect('contacts', pk=pk)



@login_required
def userprofile(request):
    user = User.objects.all()
    count = contacts = Contacts.objects.filter(user_id = request.user.id).count()
    context = {'user': user, 'count': count}
    return render(request, 'profile.html',context)


@login_required(login_url='/login')
def updateuser(request):
    user = request.user
    form = Myusercreationform(instance = user)
    if request.method == 'POST':
        form = Myusercreationform(request.POST, instance = user)
        if form.is_valid():
            form.save()
            return redirect('profile', pk = user.id)
    return render(request, 'update-user.html', {'form': form})


def delete_contact(request, contact_id):
    try:
        contact = Contacts.objects.get(id=contact_id, user_id=request.user.id)
        contact.delete()
    except Contacts.DoesNotExist:
        # Handle the case where the contact does not exist
        pass

    return redirect('contactList')  # Redirect back to the contact list


def custom_404(request, exception):
    activity = get_random_activity()
    return render(request, '404.html', {'activity': activity}, status=404)