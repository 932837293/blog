from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.contrib import auth
from .models import userInfo,article,dynamic

from bookstore import models

def uploaded_file(f,filename):
    address = '/static/image/'+filename
    destination = open(address, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def book(request):
    #插入
    #userInfo.objects.create(username='admin',password='xixixi',nickname='林柯颖')
    #userInfo.objects.filter(username='admin').first().delete()
    #查询
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if islogin == True:
        users = userInfo.objects.filter(username=username).first()
        return render(request, 'MyMoment.html', context={'username': users.nickname, 'IsLogin': True})
    return render(request, 'MyMoment.html', context={'username': '最熟悉的陌生人'})


def index(request):
    return render(request, 'index.html', context={'username':'qsd'})

def log(request):
    return render(request, 'login.html', context={'username':'qsd'})



def reload(request):
    request.session.flush()
    return render(request, 'MyMoment.html',context={'username':'最熟悉的陌生人'})

def logout(request):
    request.session.flush()
    return render(request, 'login.html',context={'username':'最熟悉的陌生人'})

def home(request):
    return HttpResponse('Hello World!')

def test(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if islogin == True:
        users = userInfo.objects.filter(username=username).first()
        return render(request, 'test.html', context={'username': users.nickname,'IsLogin':True})
    return render(request, 'test.html',context={'username':'最熟悉的陌生人'})

def check(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if  islogin == True:
        users = userInfo.objects.filter(username=username).first()
        return render(request, 'test.html', context={'username': users.nickname, 'IsLogin': True})
    else:
        username = ''
        password = ''
        if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('pwd')
            if username =='' or password == '':
                return render(request, 'login.html', context={'pwderror': '不能为空'})
        users = userInfo.objects.filter(username = username).first()
        if users:
            if users.username == username and users.password != password:
                return render(request, 'login.html', context={'pwderror': '密码错误'})
            elif users.username != username:
                return render(request, 'login.html', context={'pwderror': '用户不存在'})
            elif users.username == username and users.password == password:
                request.session['username'] = users.username
                request.session['IsLogin'] = True
                return redirect('/test/')
                #return render(request, 'test.html', context={'username': users.nickname,'IsLogin':True})

        else:
            return  render(request, 'login.html', context={'pwderror': '用户不存在'})

def Mtest(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    articles = article.objects.all()
    dynamics = dynamic.objects.all().order_by('-aid')
    count = 0
    countd = 0
    for j in dynamics:
        countd += 1
    for i in articles:
        count += 1
    if islogin == True:
        users = userInfo.objects.filter(username=username).first()
        return render(request, 'MyMoment.html', context={'username': users.nickname,'IsLogin':True,'dynamiccount':countd,'articlecount':count})
    else:
        return render(request, 'MyMoment.html',context={'username':'最熟悉的陌生人','dynamiccount':countd,'articlecount':count})

def Mcheck(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if  islogin == True:
        users = userInfo.objects.filter(username=username).first()
        return render(request, 'MyMoment.html', context={'username': users.nickname, 'IsLogin': True})
    else:
        username = ''
        password = ''
        if request.method == 'POST':
            username = request.POST.get('name')
            password = request.POST.get('pwd')
            if username =='' or password == '':
                return render(request, 'login.html', context={'pwderror': '不能为空'})
        users = userInfo.objects.filter(username = username).first()
        if users:
            if users.username == username and users.password != password:
                return render(request, 'login.html', context={'pwderror': '密码错误'})
            elif users.username != username:
                return render(request, 'login.html', context={'pwderror': '用户不存在'})
            elif users.username == username and users.password == password:
                request.session['username'] = users.username
                request.session['IsLogin'] = True
                return redirect('/blog/MyWorld/')
                #return render(request, 'test.html', context={'username': users.nickname,'IsLogin':True})

        else:
            return  render(request, 'login.html', context={'pwderror': '用户不存在'})

def publish(request):
    return render(request,'publish.html')

def publishing(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if islogin == True:
        users = userInfo.objects.filter(username=username).first()
        articles = article.objects.all()
        count = 0
        for i in articles:
            count+=1
        title = request.POST.get('title')
        content = request.POST.get('content')

        time_now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        if title != '':
            article.objects.create(aid=str(count+1) , title=title, content=content, img_url='' ,time=time_now)

            return redirect('/blog/MyWorld/')
        else:
            return render(request, 'publish.html', context={'IsLogin':True,'pwderror': '请输入标题'})
    else:
        return render(request, 'World.html', context={'IsLogin':True,'pwderror': '请重新登录'})

def publishingdt(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    if islogin == True:
        users = userInfo.objects.filter(username=username).first()
        articles = dynamic.objects.all()
        count = 0
        for i in articles:
            count+=1
        content = request.POST.get('content')

        time_now = timezone.now().strftime("%Y-%m-%d %H:%M:%S")
        if content != '':
            dynamic.objects.create(aid=str(count+1),  content=content ,time=time_now)
            return redirect('/blog/MyWorld')
        else:
            return render(request, 'MyWorld.html', context={'IsLogin':True,'pwderror': '不可发表空内容'})
    else:
        return render(request, 'MyWorld.html', context={'pwderror': '请登录'})

def archive(request):
    islogin = request.session.get('IsLogin')
    username = request.session.get('username')
    articles = article.objects.all()
    return render(request,'archive.html',context={'IsLogin':islogin,'articles':articles})

def get_detail_page(request,article_id):
    articles = article.objects.all()
    for page in articles:
        if page.aid == article_id:
            curr_article = page
            return render(request, 'note.html', context={'curr_article': curr_article,
                                                        'article_content': curr_article.content})
    else:
        return HttpResponse('????')
    #section_list = curr_article.content.split('\n')
    #return render(request,'note.html',context={'curr_article':curr_article,'section_list':section_list,'article_content':curr_article.content})

def article_delete(request,article_id):
    islogin = request.session.get('IsLogin')
    if islogin:
        articletodelete = article.objects.filter(aid=article_id)
        articletodelete.delete()
        return redirect('/blog/MyWorld/')
    else:
        return redirect('/login/')

def MyWorld(request):
    username = request.session.get('username')
    islogin = request.session.get('IsLogin')
    articles = article.objects.all()
    users = userInfo.objects.filter(username=username).first()
    dynamics = dynamic.objects.all().order_by('-aid')
    count = 0
    countd = 0
    for j in dynamics:
        countd += 1
    for i in articles:
        count += 1
    content = request.POST.get('content')
    return render(request,'MyWorld.html',context={'IsLogin':islogin,'dynamics':dynamics,'user':users,'articlecount':count,'articles':articles,'dynamiccount':countd})

def search(request):
    text = request.POST.get('text')
    articles = article.objects.all()
    for articless in articles:
        if text == articless.title:
            print(text,articless.title)
            return redirect('/archive/note/'+str(articless.aid))
        else:
            print(text,articless.title)
    return redirect('/blog/MyWorld/')

def Register(request):
    return render(request,'Register.html')