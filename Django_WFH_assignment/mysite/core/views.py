from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Speaker
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,CommentForm,SpeakerForm
from .models import Profile, Comment,Schedule
# Create your views here.
def home(request):
    speaker = Speaker.objects.all()
    schedule = Schedule.objects.all()
    comment = Comment.objects.all()
    return render(request, 'core/home.html', {'speaker':speaker, 'schedule':schedule, 'comment':comment})

def speaker_detail(request,slug):
    speaker = get_object_or_404(Speaker,slug=slug)
    return render(request, 'core/speaker_details.html',{'speaker':speaker})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form':form})
    

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def update_profile(request):
    profile = request.user.Profile
    form = ProfileUpdateForm(instance = profile)
    if request.method=='POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance = profile)
        if form.is_valid:
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'update_profile.html', {'form':form})


@login_required
def user_comment(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            comment, created = Comment.objects.update_or_create(
                profile=profile, 
                defaults={'text': text}  
            )
            
        
            return redirect('home')  
    else:
        form = CommentForm()

    return render(request, 'core/comment.html', {'form': form, 'profile': profile})

def add_speakers(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    else:
        form = SpeakerForm
    return render(request,'core/add_speaker.html',{'form':form})