from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, CreateView, DetailView
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# from django.http import JsonResponse
# import json

from .mixins import *

from .forms import *
from .service import *
from .models import *


class Index(CategoryMixin, ListView):
   template_name = 'events/index.html'
   model = PersonEvent
   context_object_name = 'PersonEvents'
   cat_list = []
    
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['events'] = Event.objects.filter(city=self.request.user.profile.city)
      context['profile'] = self.request.user.profile
      return context
   
   
class FilterEvents(CategoryMixin, ListView):
   template_name='events/index.html'
   context_object_name = 'events'
   
   def get_queryset(self):
      queryset = Event.objects.filter(cat__in=self.request.GET.getlist('category'), city=self.request.user.profile.city)
      return queryset
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['profile'] = self.request.user.profile
      
      return context
   
    
class CreateEvent(CreateView):
   form_class = EventForm
   template_name = 'events/create_event.html'
   
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['cats'] = Category.objects.all()
      return context
   
   def get_initial(self, **kwargs):
      initial = super(CreateEvent, self).get_initial(**kwargs)
      initial.update({
			'creater': self.request.user.profile,
		})
      return initial
   
   def get_success_url(self):
      return reverse_lazy('home')
   
   
class CreatePersonEvent(CreateEvent):
   form_class = PersonEventForm
   template_name = 'events/create_person_event.html'   


def save(request):
   if request.method == "POST":
      title = request.POST.get('title')
      description = request.POST.get('description')
      date = request.POST.get('date')
      city = request.POST.get('city')[:-1]
      address = request.POST.get('address')
      cat = Category.objects.get(title=request.POST.get('elastics'))
      
      varios = request.POST.get('type')
      
      if varios == 'Person':
         PersonEvent(title=title, description=description, date=date, city=city, address=address, cat=cat, creater=request.user.profile).save()
      elif varios == 'Event':
         Event(title=title, description=description, date=date, city=city, address=address, cat=cat, creater=request.user.profile).save()
   return redirect('home')


@csrf_exempt
def add_user(request):
   profile = request.user.profile
   event = Event.objects.get(pk=request.POST.get('pk'))
   
   event.users.add(profile)
   
   return redirect('home')