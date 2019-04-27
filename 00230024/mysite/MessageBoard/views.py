from django.shortcuts import render
from .models import Commenter
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime, time


# Create your views here.
def index(request):
    commenter_list = Commenter.objects.order_by('-commenter_time')

    context = {
        'commenter_list': commenter_list
    }
    return render(request, 'MessageBoard/index.html', context)


# TODO 蜜汁bug，一直仍旧保持datetime.datetime.now()的格式，而不是格化式之后的
def postmessages(request):
    commenter = Commenter()
    commenter.commenter_content = request.POST['content']
    # commenter.commenter_time = datetime.datetime.now()
    # 格式化成20xx-03-20 11:45:39形式
    commenter.commenter_time = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    commenter.commenter_name = request.POST['name']
    commenter.save()

    return HttpResponseRedirect(reverse('MessageBoard:index'))
