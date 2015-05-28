# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from gcm.models import Device, Group

@csrf_exempt
def device(request):
    """
    Register device

    Args:
        reg_id - reg id from android app
        device_id - unique device id
        group - device group slug
    """
    device_id = request.POST.get('device_id', None)
    if device_id:
        device, created = Device.objects.get_or_create(dev_id=device_id)
        device.reg_id = request.POST.get('reg_id')
        if request.POST.get("is_active", "true") == "true":
            device.is_active = True
        else:
            device.is_active = False

        group_slug = request.POST.get("group", None)
        if group_slug:
            try:
                device.group = Group.objects.get(slug=group_slug)
            except:
                return HttpResponseBadRequest()
        
        device.save()

        return HttpResponse()
    else:
        return HttpResponseBadRequest()
