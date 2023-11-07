from django.conf.urls import include, url
from django.contrib import admin

#For Serving MEDIAS UPLOADED
from django.conf import settings
from django.conf.urls.static import static
#END For Serving MEDIAS UPLOADED

urlpatterns = [
    # Examples:
    # url(r'^$', 'uimsproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^uimsapp/', include("uimsapp.urls", namespace='uimsapp')),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^$', 'uimsapp.views.home', name='home'),
    url(r'^login$', 'uimsapp.views.login', name='login'),
    url(r'^frontadmin/$', 'uimsapp.views.frontadmin', name='frontadmin'),
	url(r'^accounts/', include('registration.backends.default.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)