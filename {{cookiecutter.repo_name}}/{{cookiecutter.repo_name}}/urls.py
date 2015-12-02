from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^', include('core.urls')),
    url(r'^gallery/', include('magicgallery.urls')),
    url(r'^frontend/', include('frontend.urls')),

    url(r'^magiccontent/', include('magiccontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.textimagecontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.formattedtextimagecontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.imagecontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.iconcontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.dividertextcontent.urls')),
    url(r'^magiccontent/', include('magiccontent.contrib.background.urls')),
    url(r'^magiccontent/', include('magiccontentnavigation.urls')),
    url(r'^menuitem/', include('magiccontentnavigation.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
