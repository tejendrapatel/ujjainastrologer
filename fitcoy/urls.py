
from django.contrib import admin
from django.urls import path
from zfitcoy.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include
urlpatterns = [
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('admin/', admin.site.urls),
    path('',HOME,name= 'home'),
    path('about',ABOUT,name= 'about'),
    path('services',SERVICES,name= 'services'),
    path('appointment',APPOINTMENT,name= 'appointment'),
    # path('blog',BLOG,name= 'blog'),
    path('shop',SHOP,name= 'shop'),
    path('contact',CONTACT,name= 'contact'),
    ################dynamic pages ############
    path('Service/<int:blo_id>/',SERVICES_SINGLE, name='services_single'),
    path('rashi/<int:blon_id>/',RASHI_SINGLE, name='Rashi_single'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
