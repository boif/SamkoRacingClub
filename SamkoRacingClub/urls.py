from datetime import datetime
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from SRC import views, forms
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('images/', views.images, name='images'),
    path('addimage/', views.addimage, name='addimage'),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.register, name='signup'),
    path('login/',
         LoginView.as_view
             (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year': datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)