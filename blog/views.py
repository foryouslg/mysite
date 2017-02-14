from django.shortcuts import render,HttpResponse
from blog.models import Navigation,Context
from django.core.paginator import Paginator,EmptyPage,InvalidPage,PageNotAnInteger
from datetime import datetime
from django.contrib.sessions.models import Session

# Create your views here.

#分页单位，几篇文章
PAGE_NUM = 5

def per_nex_page(page_id):
    per_page = int(page_id) - 1
    nex_page = int(page_id) + 1
    return per_page,nex_page

def navigation():
    nav = Navigation.objects.order_by()
    return nav

def detial_article(nav_id):
    nav_context = Navigation.objects.get(id=nav_id)
    all_article = nav_context.context_set.order_by('-create_time')
    return nav_context,all_article

def paginator(art,page_id):
    try:
        page = int(page_id)
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    paginator = Paginator(art,PAGE_NUM)
    try:
        articlelist = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        articlelist = paginator.page(1)
    articlelist.has_previous()
    articlelist.has_next()
    return articlelist

def homepaginator(request,page_id):
    #显示所有导航分类
    nav = navigation()
    #首页显示的文章内容(首页显示文章是不分类别的)
    home_article = Context.objects.order_by('-create_time')
    #显示page_id页的所有文章
    page_article = paginator(home_article,page_id)
    page = Paginator(home_article, PAGE_NUM)
    per_page, nex_page = per_nex_page(page_id)
    release = {
                'nav':nav,'page_article':page_article,'page_id':page_id,
                'page':page,'per_page':per_page,'nex_page':nex_page
               }
    return render(request,'blog/homepaginator.html',release)

def detailpaginator(request,nav_id,page_id):
    #显示所有导航分类
    nav = navigation()
    #首页显示的文章内容,共5个
    nav_context, all_article = detial_article(nav_id)

    page_article = paginator(all_article,page_id)
    page = Paginator(all_article, PAGE_NUM)
    nav_context = Navigation.objects.get(id=nav_id)
    per_page,nex_page = per_nex_page(page_id)
    release = {'nav':nav,'page_article':page_article,
                   'page':page,'nav_context':nav_context,
                   'per_page':per_page,'nex_page':nex_page
               }
    return render(request,'blog/detailpaginator.html',release)



def index(request):
    #显示所有导航分类
    nav = navigation()
    #首页显示的文章内容
    home_article = Context.objects.order_by('-create_time')
    #计算文章可以分多少页
    page = Paginator(home_article,PAGE_NUM)
    release = {'nav': nav, 'home_article': home_article, 'page': page}
    return render(request,'blog/index.html',release)

def detail(request,nav_id):
    # 显示所有导航分类
    nav = navigation()
    #所选导航的文章内容
    nav_context,all_article = detial_article(nav_id)

    page = Paginator(all_article,PAGE_NUM)
    release = {'nav':nav,'nav_context':nav_context,'all_article':all_article,'page':page}
    return render(request,'blog/detail.html',release)


def contextDetail(request,nav_id,context_id):
    nav = navigation()
    nav_context = Navigation.objects.get(id=nav_id)
    contextdetail = nav_context.context_set.get(id=context_id)


    #获取分类中的所有文章
    c = nav_context.context_set.all()
    art_id = []
    #将所有文章中的id存入一个列表中
    for i in c:
        art_id.append(i.id)
    #从新列表中获取文章id的排列,即当前文章在新列表中的位置
    now_id_index = art_id.index(int(context_id))
    #因为列表中第一个索引是0,所以当索引为0的时候,没有上一篇文章,即没有上一个id
    if now_id_index != 0:
        #当前文章在新列表中的位置减1就是上一篇文章
        i = now_id_index - 1
        #获取到上一篇文章的索引之后,获取该索引对应存储的文章id
        per_art_id = art_id[i]
        #将上一篇文章的id传入,获取该文章对象
        per_art = nav_context.context_set.get(id=per_art_id)
    else:
        #如果索引为0,即没有上一篇文章,将获取当前文章对象
        per_art = nav_context.context_set.get(id=context_id)
    if len(art_id) != now_id_index + 1:
        i = now_id_index + 1
        nex_art_id = art_id[i]
        nex_art = nav_context.context_set.get(id=nex_art_id)
    else:
        nex_art = nav_context.context_set.get(id=context_id)
    #per_art_id,nex_art_id = per_nex_art(context_id)
    request.session.set_expiry(60)
    request.session['sessionid'] = '123test'
    ll = request.session['sessionid']


    try:
        lll = request.COOKIES['sessionid']
        contextdetail.hits = contextdetail.hits
    except:
        contextdetail.hits += 1
        contextdetail.save()


    l = Session.objects.all()
    contextdetail.sessionid




    release = {
        'nav':nav,'nav_context':nav_context,
        'contextdetail':contextdetail,
        'per_art':per_art,'nex_art':nex_art,
        'hits':contextdetail.hits,
        'll':ll,
    }
    return render(request,'blog/context.html',release)

def aboutme(request):
    nav = navigation()
    #session = request.session.keys()


    if request.COOKIES:
        req = render(request,'blog/aboutme.html',{'nav':nav,'cookie':request.COOKIES})
    else:
        req = render(request,'blog/aboutme.html',{'nav':nav})
        req.set_cookie('cookie1',datetime.now())
    #cookie = request.COOKIES
    return req
    #return render(request,'blog/aboutme.html',{'nav':nav,'req':req})

def searchArt(request,*args):
    s = request.POST['*args']
    art = Context.objects.all().filter()
    pass