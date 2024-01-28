from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from author.forms import SignUp, ChangeUserForm
from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from purchase.models import PurchaseClass
# Create your views here.


def signUp(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'SignUp Successfully!')
            return redirect('login')
    else:
        form = SignUp()
    return render(request, 'signUp.html', {'form':form, 'type':'SignUp'})
    

class UserLoginView(LoginView):
    template_name = 'signUp.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request, 'Logged is successfully!')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request, 'Logged information incorrect!')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        user_id = self.request.user.id
        purchase_obj = PurchaseClass.objects.filter(user=user_id)
        context['cars'] = purchase_obj
        return context

@login_required
def profile(request):
    purchase_obj = PurchaseClass.objects.filter(user=request.user.id)
    return render(request, 'profile.html', {'cars':purchase_obj})

@login_required
def edit(request):
    if request.method == 'POST':
        form = ChangeUserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile') 
    else:
        form = ChangeUserForm(instance=request.user)
        return render(request, 'signUp.html', {'form':form, 'type' : 'Edit Your Profile'})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')