from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('filterEvents', FilterEvents.as_view(), name='filterEvents'),
    path('', Index.as_view(), name='home'),
    
    path('createPersonEvent', CreatePersonEvent.as_view(), name='createPersonEvent'),
    path('createEvent', CreateEvent.as_view(), name='createEvent'),
    
    path('savePersonEvent', save, name='savePersonEvent'),
    path('saveEvent', save, name='saveEvent'),
    
    path('add', add_user, name='add_user_to_event'),
    
    
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)