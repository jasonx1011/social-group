"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    # url(r'^$', auth_views.LoginView.as_view(template_name='accounts/login.html'),
    #    name='home_login'),
    url(r'^test/$', views.TestPage.as_view(), name='test'),
    # url(r'^test/$', views.HomePage.as_view(), name='test'),
    # url(r'^test/$', RedirectView.as_view(url='http://127.0.0.1:8000/'), name='test'),
    url(r'^thanks/$', views.ThanksPage.as_view(), name='thanks'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^groups/', include('groups.urls', namespace='groups')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
