from django.contrib import admin
from django.urls import path, include
from . import views as mainViews

from django.conf import settings
from django.conf.urls.static import static

import searches.views as searchViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.index, name='main-home'),
    path('about/', mainViews.about, name='main-about'),
    path('contact/', mainViews.contact, name='main-contact'),
    path('blog/', include('appBlog.urls')),

    path('search/', searchViews.search),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
