from django.shortcuts import render, redirect
from users.forms import LoginForm
from users.forms import SignupForm
from django.contrib.auth.models import User
from book.models import Favor
from django.contrib.auth import authenticate, login, logout

# Create your views here.
# 로그인
def login_view(request):
    # 기로그인 유저의 경우 추천도서목록으로 이동
    if request.user.is_authenticated: 
        return redirect("book:recommended_book")
    if request.method == "POST": 
        form = LoginForm(data = request.POST) 
        if form.is_valid(): 
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: 
                login(request, user) 
                return redirect("book:recommended_book")
            else: 
                form.add_error(None, "User information incorrect.")
        context = {"form" : form}
        return render(request, "users/login.html", context)
    else: 
        form = LoginForm() 
        context = {"form" : form}
        return render(request, "users/login.html", context)

# 회원가입
def signup_view(request):
    # 폼 입력값이 있는 경우 저장
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        # print(request.POST)
        # print(signup_form.is_valid())
        # print(signup_form.errors)
        if signup_form.is_valid():
            username = request.POST.get('username', None)
            password1 = request.POST.get('password1', None)
            password2 = request.POST.get('password2', None)
            genre =  request.POST.get('genre', None)
            # 비밀번호와 비밀번호확인 일치 여부 확인
            if password1 != password2:
                return render(request, "users/signup.html")
            else:
                # 유저 정보 저장
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                
                # 선호하는 장르 저장
                favor = Favor()
                favor.user_id = user
                favor.genre = genre
                favor.save()

                # 회원가입 후 로그인화면으로 이동
                return redirect("users:login")
        else:
            context = load_init.signup()
            return render(request, "users/signup.html", context)

    else:
        context = load_init.signup()
        return render(request, "users/signup.html", context)

# 로그아웃
def logout_view(request):
    logout(request) 
    return redirect("users:login")

# 초기 로드
class load_init():
    def signup():
        form = SignupForm()
        context = {
            "form" : form,
        }
        return context