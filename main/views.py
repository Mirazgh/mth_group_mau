from django.shortcuts import render, redirect
from .forms import regform, login_form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import UserAnswer, Member
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def members(request):
    members = Member.objects.all()
    return render(request, 'main/members.html', {'members': members})

def login_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
    return render(request, 'registration/login.html', {})

def register(request):
    if request.method == 'POST':
        form = regform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/dashboard')
    else:
        form = regform()
    return render(request, 'registration/sign_up.html', {'form': form})

@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'main/dashboard.html', {})

@login_required(login_url='/login')
def exam(request):
    if request.method == "POST":
        user = request.user  # Assuming you have user authentication
        total_score = 0  # Initialize the total score
        for key, value in request.POST.items():
            if key.startswith('q'):
                total_score += int(value)  # Add the value to the total score

                # You can also store the answers in the database if needed
                UserAnswer.objects.create(user=user, question_text=key, answer=int(value))

        # Store the total score in the user's session
        request.session['total_score'] = total_score
        return redirect('/dashboard')
    # Render the HTML form with questions
    return render(request, 'main/exam.html')


@login_required(login_url='/login')
def display_user_answers(request):
    user = request.user  # Get the currently logged-in user
    user_answers = UserAnswer.objects.filter(user=user)
    total_score = sum([int(answer.answer) for answer in user_answers])
    exams = UserAnswer.objects.filter(user=user)
    return render(request, 'main/user_answers.html', {'user_answers': user_answers})





