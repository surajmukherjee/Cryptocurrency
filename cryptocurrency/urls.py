"""cryptocurrency URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from cryptocurrency import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from admin_app import views
from django.conf.urls.static import static
from cryptocurrency import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  url(r'^$', views.indexPage),
                  url(r'^verify/$', views.linkVerify),
                  url(r'^neonbutton/$', views.neonButton),
                  url(r'^coinsymbol/$', views.coin_symbol_data),
                  url(r'^final_login_page/$', views.final_login_page),
                  url(r'^final_signup_page/$', views.final_signup_page),
                  url(r'main_test/$', views.main_test)] \
              + static(settings.ICONS_URL, document_root=settings.ICONS_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.CSS_URL, document_root=settings.CSS_ROOT) \
              + static(settings.JAVASCRIPT_URL, document_root=settings.JAVASCRIPT_ROOT)
