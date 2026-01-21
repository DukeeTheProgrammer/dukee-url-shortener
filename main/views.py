from django.shortcuts import render, redirect
from .tools import generate_short_url
from django.http import JsonResponse
from .models import Link
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def home(request):
    return render(request, 'home.html')

@csrf_exempt
def generate_link(request):
    ip = request.META.get("REMOTE_ADDR")
    useragent = request.META.get("HTTP_USER_AGENT")
    data = json.loads(request.body)
    link=data.get("link")
    custom_name = data.get("custom_name")
    if not link:
        return JsonResponse({
            "success":False,
            "message":"Link is required"
            })
    shortened = generate_short_url() if not custom_name else custom_name
    linked_id = ip+useragent+link
    server = request.get_host()
    link_obj, created = Link.objects.get_or_create(
            ip=ip,
            main_link=link,
            shortened=shortened,
            useragent=useragent,
            link_id=linked_id
            )
    if link_obj:
         return JsonResponse({
                "success" : True,
                "message":f"Your shortened url has been generated for <' {link} '>",
                "url":server+"/"+link_obj.shortened
                })

    else:
        link_obj.save()
        return JsonResponse({
                "success" : True,
                "message":"Your shortened url was generated",
                "url":server+"/"+link_obj.shortened
                })
@csrf_exempt
def call_url(request, link):
    link = Link.objects.filter(shortened=link).first()
    if link:
        return redirect(link.main_link)
    else:
        return JsonResponse({
                "success":False,
                "message":"That Link was not found"
                })





