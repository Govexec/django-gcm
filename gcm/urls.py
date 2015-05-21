from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^device/$', 'gcm.views.device', name='gcm-device'),
)
