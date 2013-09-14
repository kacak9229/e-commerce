from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')), 
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^media(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

    url(r'^$', 'products.views.home'),
    (r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/$', 'contact.views.contact'),
    url(r'^products/$', 'products.views.products'),
    url(r'^products/(?P<slug>[-\w]+)/$', 'products.views.product_single'),
    url(r'^products/(?P<slug>[-\w]+)/add$', 'cart.views.add'),
    url(r'^cart/$', 'cart.views.view'),
    url(r'^cart/delete$', 'cart.views.delete'),
    url(r'^checkout/$', 'checkout.views.checkout'),
)

