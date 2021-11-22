from django.shortcuts import render, redirect
# 세션을 create 하기 위해 import, login 함수랑 이름 겹치면 안돼서 as로 호출
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    # 로그인이 되어있다면 아래 함수를 수행하기에 적합하지 않으므로 바로 redirect 한다.
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
    	# 첫번째 인자로 request 를 받아야 한다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 유효성 검사를 통과하면 세션을 create 해야 함 -> login()
            auth_login(request, form.get_user())
            # url 에 next 가 있을 때랑 없을때 결과가 다름
            return redirect(request.GET.get('next') or 'articles:index')
    else:
    	# 로그인에 필요한 빈 종이를 생성해서 lognin.html 에 전달
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)