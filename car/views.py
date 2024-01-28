from django.shortcuts import render, redirect
from django.views.generic import DetailView
from car.models import CarModel
from car.forms import CommentForm
# Create your views here.


class DetailCarView(DetailView):
    model = CarModel
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
    def post(self, request, *args, **kwargs):
        form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context  
