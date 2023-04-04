from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from chat.models import Message, Group
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from decouple import config


# @login_required
def group_chat(request, group_id):
    group = Group.objects.get(id=group_id)
    messages = Message.objects.filter(group=group).order_by('date')
    static_path = config('STATIC_PATH')
    style_path = config('STYLES_PATH')
    
    context = {
        'group': group,
        'messages': messages,
        'static_path': static_path,
        'style_path': style_path,
    }

    return render(request, 'group.html', context)

# @login_required
def chat_main_page(request):
    groups = Group.objects.all()
    static_path = config('STATIC_PATH')
    style_path = config('STYLES_PATH')
    context = {
        'groups': groups,
        'static_path': static_path,
        'style_path': style_path,
    }
    return render(request, 'chat_main_page.html', context)

# @login_required
# def send_message(request):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         group_id = request.POST.get('group_id')
#         sender = request.user
#         group = Group.objects.get(id=group_id)
#         message = Message.objects.create(group=group, sender=sender, content=content)
#         data = {'success': True}
#         return JsonResponse(data)
#     else:
#         data = {'success': False}
#         return JsonResponse(data)