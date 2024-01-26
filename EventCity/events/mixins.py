from .models import *
from django.views import View

class CategoryMixin:
   def get_categorys(self):
      return Category.objects.all()