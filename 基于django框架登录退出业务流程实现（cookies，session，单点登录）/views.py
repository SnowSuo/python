from django.shortcuts import render ,redirect
from django.http import HttpResponse


# Create your views here.
#创建全局列表
listaccount=[]
#跳转网站首页
def index(request):
    return render(request,'index.html')
#定义一个函数用于写入cookie数据
# def setcookies(request,company):
#     #设置重定向地址
#     req=redirect('/app/index/')
#     #设置cookies
#     req.set_cookie('company',company)
#     print('成功保存cookies数据....')
#     #响应客户端
#     return req
# #定义一个函数获取cookies数据
# def getcookies(request):
#     #
#     value=request.COOKIES.get('company',None)
#     #
#     return render(request,'index.html',{'company':value})
# #加密写入cookies
# def setsaltcookies(request,language):
#     #设置重定向跳转路径
#     req=redirect('/app/index/')
#     #使用salt中的值进行混淆加密后存放到cookies中
#     req.set_signed_cookie('language',language,salt='abc')
#     print('成功保存cookies数据....')
#     #响应客户端
#     return req
# #解密cookies中
# def getsaltcookies(request):
#     #获取cookies中的值
#     value=request.get_signed_cookie('language',None,salt='abc')
#     #响应客户端
#     return render(request,'index.html',{'language':value})
#设置home页面
def home(request):
    #获取session数据
    account=request.session.get('account',None)
    print('account: {0}'.format(account))
    if not account:
        return redirect('/app/login/')
    else:
        return render(request,'home.html',{'account':account})

#登陆业务处理
def login(request):
    if request.POST:
        #接收用户数据
        account=request.POST.get('account',None)
        password=request.POST.get('password',None)
        print('account:{0} password{1}'.format(account,password))
        #判断用户账号是否已在登录列表中
        if account in listaccount:
            print('账户已经登录在线')
        else:

            #业务处理
            if account=='admin' and password=='123':
                #将账户信息追加至列表
                listaccount.append(account)
                print('账户信息成功添加至列表')
                #设置响应路径
                rep=redirect('/app/home')
                #将登陆账号加密到cooike中
                rep.set_signed_cookie('account',account, salt='www.baidu')
                print('登录成功后加密写入cookie中')
                #登录成功后，将用户账号写入session中
                request.session['account']=account
                print('登录成功后写入session')
                return rep
            else:
                return render(request,'login.html',{'message':'账号密码错误'})
            pass
    else:
        #从cookie中获取account的值
        account=request.get_signed_cookie('account',None,salt='www.baidu')
        #判断account是否存在，决定是否不填数据
        if account:
            return render(request,'login.html',{'account':account})
        else:
            return render(request,'login.html')      
#退出
def logout(request):
    #删除当前登陆者session的信息
    del request.session['account']
    listaccount.pop()
    print('删除当前登录者信息')
    return redirect('/app/login/')

# #写入数据到session会话中
# def setSessions(request,username):
#     #写入session
#     request.session['username']=username
#     print('用户名称写到session中')
#     return redirect('/app/index/')
# #获取session中的数据
# def getSessions(request):
    value=request.session.get('username',None)
    return HttpResponse('session:{0}'.format(value))
#跳转至login登录界面
def gotoLogin(request):
    return redirect('/app/login/')
