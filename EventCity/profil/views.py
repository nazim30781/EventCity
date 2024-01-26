from django.shortcuts import render, redirect
from django.views import View


class Profile(View):
   def get(self, request):
      profile = request.user.profile
      print(request)
      
      context = {
         'profile': profile
      }
      
      return render(request, 'profil/profile.html', context)
   
   

def change_logo(request):
   if request.method == 'POST':
      print(request.POST)
      print(request)
      img = request.FILES['logo']
      
      profile = request.user.profile
      profile.logo = img
      profile.save()
      return redirect('profile')
