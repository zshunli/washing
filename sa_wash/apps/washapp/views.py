from django.forms import forms
from django.shortcuts import render, redirect,HttpResponse, HttpResponseRedirect
from .models import price,order_detail,order
# from .forms import ODModelForm
from django.utils import timezone
import random, string, datetime
from datetime import time
import requests 
from loginapp.models import udata


# Create your views here.
# 小恐龍
def Level(hp):
    level=1
    if hp <= 10000000:
        level=9
    if hp <= 7000:
        level =8
    if hp <= 5000:
        level =7
    if hp <= 3000:
        level =6
    if hp <= 1000:
        level =5
    if hp <= 800:
        level =4
    if hp <= 500:
        level =3   
    if hp <= 300:
        level =2 
    if hp <= 150:
        level =1
    return level

def totalHP():
    totalHP=900
    return totalHP

def levelhp(level):
    if level==1:
        levelhp=300
    if level==2:
        levelhp=500
    if level==3:
        levelhp=800
    if level==4:
        levelhp=1000
    if level==5:    
        levelhp=3000
    if level==6:
        levelhp=5000
    if level==7:    
        levelhp=7000
    if level==8:
        levelhp=10000
    if level==9:
        levelhp=10000
    return levelhp

def HP(hp,h):
    Hp=h-hp
    return Hp

def percent(hp,h):
    p=int((hp / h)*100)
    return p

def imgurl(level):
    Imgurl="/static/images/dinosaur"+str(level)+".gif"
    return Imgurl

def dinosaur(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        hp=twpoint(request)
        LEVEL=Level(hp)
        levelimg=imgurl(LEVEL)
        h=levelhp(LEVEL)
        nextlevel=LEVEL+1
        Hpp=HP(hp,h)
        per=percent(hp,h)
        return render(request, "dinosaur.html",locals())

def twpoint(request):
    ordids=order.objects.filter(oUserid=request.session['UserID'])
    Wpoint=len(ordids)
    totalwpoint=Wpoint*150
    if udata.wpoint!=totalwpoint:
        udata.objects.filter(UID=request.session['UserID']).update(wpoint=totalwpoint)
    return totalwpoint
# 小恐龍


def wash1(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        return render(request, "wash1.html")

def wash2(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        return render(request, "wash2.html")

def transmode1(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method == 'POST':
            wash = request.POST.get('wash')
            spin = request.POST.get('spin')
            dry = request.POST.get('dry')
            fold = request.POST.get('fold')
            # print(wash+'/'+spin+'/'+dry+'/'+fold)
            return render(request, "transmode1.html", locals())
        elif request.method == 'GET':
            return render(request, 'transmode1.html')

def checkorder(request): #訂單產生存入資料表內
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method == "POST":
            wash = request.POST.get('wash')
            spin = request.POST.get('spin')
            dry = request.POST.get('dry')
            fold = request.POST.get('fold')
            card = request.POST.get('card')
            if len(card) == 16 and card.isdigit():
                credit='正確'
                transport = request.POST.get('transport')
                shop = request.POST.get('shop')
                # 顯示在頁面上的模式
                mode = wash+'、'+spin+'、'+dry+'、'+fold
                wash_num = request.POST.get('wash_num')
                wash_n=int(wash_num)
                prices=t_price(wash, dry, fold)
                carbon=t_carbon(wash, dry, fold) #改碳排量
                C_tax=carbon*3
                money=prices*wash_n
                point=t_point(wash, dry, fold)
                id=getordernum()
                qrcode1=getQR(id)
                qrcode2=getQR(id)
                expectedfinish=totaltime(wash,dry,fold)
                aft1 = ex1time(wash,dry,fold)
                aft2 = ex2time(wash,dry,fold)
                aft3 = ex3time(wash,dry,fold)
                aft4 = ex4time(wash,dry,fold)
                order_detail.objects.create(orderId=id,washmode=wash, spinmode=spin, drymode=dry, foldmode=fold,
                card=card, oTotal=money, oPoint=point,C_amount=carbon,oTransport=transport,sId=shop,wpoint=150,
                wash_num=wash_n, C_tax=C_tax, oSendcode=qrcode1, oReceivecode=qrcode2)
                order.objects.create(orderId=id,oUserid=request.session['UserID'])
            else:
                credit='錯誤'
                return render(request, 'transmode1.html', locals())
            return render(request, 'checkorder.html', locals())
        else:
            return render(request, 'checkorder.html', locals())

def finishorder(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method=='POST':
            finaltime=request.POST.get('finaltime')
            id=request.POST.get('id')
            if order_detail.objects.get(orderId=id):
                order_detail.objects.filter(orderId=id).update(finaltime=finaltime)
            else:
                print('重新訂單')
            return render(request, 'finishorder.html', locals())
        else:
            return render(request, 'finishorder.html')

def orderlist(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        ordids=order.objects.filter(oUserid=request.session['UserID']).order_by('-id')
        return render(request, "order.html", locals())

def orderdetail(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method == 'POST':
            ordid=request.POST.get('ordid')
            ords=order.objects.filter(orderId=ordid)
            ordts=order_detail.objects.filter(orderId=ordid)
            ordtime=order.objects.get(orderId=ordid)
            # print(type(ordtime.oFinish))
            if ordtime.oFinish is None:
                finishorder='還未完成'
                pay=False
                ddd='還未完成'
            else:
                finishorder=ordtime.oFinish
                pay=True
                ddd=pp()
            return render(request, "order_detail.html", locals())
        else:
            return HttpResponseRedirect("/wash/orderdetail")

def finish(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method == 'POST':
            ORDID=request.POST.get('ORDID')
            MEMID=request.session['UserID']
            # CDATE=request.POST.get('CDATE')
            POINT=request.POST.get('POINT')
            CARBON=request.POST.get('ctax')
            AMOUNT=request.POST.get('money')
            CDATE=order.objects.get(orderId=ORDID)
            nowtime=datetime.datetime.now()     
            # order.objects.filter(orderId=ORDID).update(oFinish=nowtime)

            dataa=requests.post('https://8aa3-2401-e180-8910-13-f557-3684-8108-3029.jp.ngrok.io/mymodels/mymodels/', data = {
                "T_ORDID": ORDID,#userID
                "T_MEMID": MEMID,#智慧喜＋之類的
                "T_CDATE": CDATE.oOrdertime,
                "T_GPOINT": POINT,
                "T_APPID": 12, #碳排放量（若你們沒有的話就一樣隨便打）
                "T_CARBON":CARBON,
                "T_AMOUNT":AMOUNT
            })

            # dataa=requests.post('https://5858-123-241-222-92.jp.ngrok.io/api/historyarticles/',data={
            # "ordid":ORDID,
            # "memid" :MEMID,
            # "appname" :12,
            # "c_amount":CARBON,
            # "gpoint" :POINT,
            # "amount" :AMOUNT,
            # "cdate" : CDATE.oOrdertime,
            # })

            print(dataa)
            # print(dataa.json())
            return render(request, 'finish.html', locals())


def QA(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        return render(request, "QA.html")

def contact(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        return render(request, "contact.html")

def QRcode(request):
    if 'UserID' not in request.session:
        return HttpResponseRedirect("/login_line")
    else:
        if request.method == 'POST':
            id=request.POST.get('id')
            qr=order_detail.objects.get(orderId=id)
            qrcode1=qr.oSendcode
            qrcode2=qr.oReceivecode
            return render(request, 'QRcode.html', locals())
        else:
            return render(request, 'QRcode.html', locals())

def transmode2(request):
    return render(request, 'transmode2.html')


def pp(): #訂單編號
    todaytime=datetime.datetime.now()
    re_date = todaytime.strftime('%Y%m%d%H%M%S')
    z =''.join(random.choice(string.ascii_letters) for x in range(2))
    y =''.join(random.choice(string.digits) for x in range(2))
    # res='ORDER'+'-'+re_date+'-'+y
    ddd=z+y
    return ddd

def getordernum(): #訂單編號
    todaytime=datetime.datetime.now()
    re_date = todaytime.strftime('%Y%m%d%H%M%S')
    z =''.join(random.choice(string.ascii_letters) for x in range(5))
    y =''.join(random.choice(string.digits) for x in range(3))
    # res='ORDER'+'-'+re_date+'-'+y
    res=z+y
    return res

def getQR(id): #QRcode
    y =''.join(random.choice(string.digits) for x in range(3))
    qrcode=id+'-'+y
    return qrcode

def totaltime(wash,dry,fold): #預計時間
    wmode=price.objects.get(modename=wash)
    dmode=price.objects.get(modename=dry)
    fmode=price.objects.get(modename=fold)
    t=wmode.ttime+dmode.ttime+fmode.ttime
    tdtime=datetime.datetime.now().replace(microsecond=0)
    nowtime = datetime.timedelta(minutes=t)
    aft=tdtime+datetime.timedelta(minutes=t)
    return aft 

def ex1time(wash,dry,fold): #時間選擇一
    aftime=totaltime(wash,dry,fold)
    aft1=aftime+datetime.timedelta(hours=1)
    return aft1 

def ex2time(wash,dry,fold): #時間選擇二
    aftime=totaltime(wash,dry,fold)
    aft2=aftime+datetime.timedelta(hours=2)
    return aft2 

def ex3time(wash,dry,fold): #時間選擇三
    aftime=totaltime(wash,dry,fold)
    aft3=aftime+datetime.timedelta(hours=3)
    return aft3 

def ex4time(wash,dry,fold): #時間選擇四
    aftime=totaltime(wash,dry,fold)
    aft4=aftime+datetime.timedelta(hours=4)
    return aft4 
    
def t_price(wash, dry, fold): #總金額含碳稅
    pwash = price.objects.get(modename=wash)
    pdry = price.objects.get(modename=dry)
    pfold = price.objects.get(modename=fold)
    totalp=50+(pwash.tprice+pdry.tprice+pfold.tprice)+3*(pwash.carbon+pdry.carbon+pfold.carbon)
    return totalp 

def t_carbon(wash, dry, fold): #總碳排量
    twash = price.objects.get(modename=wash)
    tdry = price.objects.get(modename=dry)
    tfold = price.objects.get(modename=fold)
    totalt=twash.carbon+tdry.carbon+tfold.carbon
    return totalt 

def t_point(wash, dry, fold): #總點數
    pwash = price.objects.get(modename=wash)
    pdry = price.objects.get(modename=dry)
    pfold = price.objects.get(modename=fold)
    totalpoint=20+pwash.point+pdry.point+pfold.point
    return totalpoint 