from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

import datetime
import MySQLdb

from .models import Slide, Featured, Page, Post, Cate

# Create your views here.

def hello(request):
    return HttpResponse("Hello django!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    context = {}
    context['title'] = 'Home'
    context['sliders'] = Slide.objects.all()
    context['featureds_items'] = Featured.objects.filter(featured_type=1)
    context['featureds_ads'] = Featured.objects.filter(featured_type=2)
    return render(request, 'home.html', context)

def posts(request):
    context = {}
    context['title'] = 'Posts'



    context['data'] = [
            {
                "id": 1,
                "title": "经典的歌曲永远不会过时，经典的演绎永远难以忘怀",
                "source": "今日头条",
                "publish": "2016-11-18",
                "images": ["http://www.test.com/img/p1.jpg"]
            },
            {
                "id": 2,
                "title": "微信又增加3大逆天功能，忍不住提醒你们记得更新",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p2.jpg"]
            },
            {
                "id": 3,
                "title": "历史上死的比岳飞还憋屈的十位战神级人物，第十位真的太惨了",
                "source": "搜狐网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p4.jpg", "http://www.test.com/img/p5.jpg", "http://www.test.com/img/p6.jpg"]
            },
            {
                "id": 4,
                "title": "中国男篮为什么落后于世界水平，看球员的身体就知道了",
                "source": "新浪网",
                "publish": "2016-11-16",
                "images": []
            },
            {
                "id": 5,
                "title": "氢弹威力巨大为何多国放弃？唯独中国保存下来？",
                "source": "百度网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p2.jpg", "http://www.test.com/img/p3.jpg", "http://www.test.com/img/p6.jpg"]
            },
            {
                "id": 6,
                "title": "爆笑动物：猴子和狗打架，猴子输了不服气欲拿棍棒再战",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": []
            },
            {
                "id": 7,
                "title": "人到40血管易堵，吃什么可以清血管？",
                "source": "今日头条",
                "publish": "2016-11-18",
                "images": ["http://www.test.com/img/p3.jpg"]
            },
            {
                "id": 8,
                "title": "医生教你三个动作，快速清肠排毒，人人可学！",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p4.jpg"]
            },
            {
                "id": 9,
                "title": "快递员的真实工资有多少？",
                "source": "搜狐网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p1.jpg", "http://www.test.com/img/p2.jpg", "http://www.test.com/img/p4.jpg"]
            },
            {
                "id": 10,
                "title": "诸葛亮一生最信任的人，也是对他最忠诚的人，武力值不输关羽张飞",
                "source": "新浪网",
                "publish": "2016-11-16",
                "images": []
            },
            {
                "id": 11,
                "title": "我国成功完成世界上又一超级工程，它让缅甸到中国不超过一分钟",
                "source": "百度网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p3.jpg"]
            },
            {
                "id": 12,
                "title": "自己创业开公司，真的很难吗",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p5.jpg"]
            },
            {
                "id": 13,
                "title": "三峡大坝的水为什么射向空中？中国人的智慧美国人也只能干看着",
                "source": "今日头条",
                "publish": "2016-11-18",
                "images": ["http://www.test.com/img/p1.jpg"]
            },
            {
                "id": 14,
                "title": "马云：我对钱没兴趣，天猫和淘宝未来30年可能会被死掉",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p6.jpg"]
            },
            {
                "id": 15,
                "title": "盘点世界上最“离奇”的几个越狱事件",
                "source": "搜狐网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p4.jpg", "http://www.test.com/img/p2.jpg", "http://www.test.com/img/p1.jpg"]
            },
            {
                "id": 16,
                "title": "不孝有三，无后为大，另外两个是啥？",
                "source": "新浪网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p1.jpg"]
            },
            {
                "id": 17,
                "title": "十种人最容易猝死，教你了解猝死前的6个征兆",
                "source": "百度网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p3.jpg"]
            },
            {
                "id": 18,
                "title": "为什么很多成功男人有情人？",
                "source": "腾讯网",
                "publish": "2016-11-16",
                "images": ["http://www.test.com/img/p2.jpg"]
            }
        ]
    return render(request, 'posts.html', context)

def post(request, id):
    try:
        id = int(id)
    except ValueError:
        raise Http404()
    html = "<html><body>This is the post: %s.</body></html>" % id
    return HttpResponse(html)

def about(request):
    context = {}
    context['title'] = 'About'
    context['content'] = 'About Page content ...'
    context['type'] = 2
    return render(request, 'about.html', context)

def profile(request):
    t = Template("<html><body><h2>This is {{ name }} profile")
    c = Context({'name': 'ken'})
    html = t.render(c)
    return HttpResponse(html)
