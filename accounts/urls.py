
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    # path('admin/', admin.site.urls),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
# ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

