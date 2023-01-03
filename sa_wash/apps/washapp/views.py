from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def dinosaur(request):
    return render(request, "dinosaur.html")

def wash1(request):
    return render(request, "wash1.html")

def wash2(request):
    return render(request, "wash2.html")

def order(request):
    return render(request, "order.html")

def QA(request):
    return render(request, "QA.html")

def contact(request):
    return render(request, "contact.html")

def order_detail(request):
    return render(request, "order_detail.html")

def QRcode(request):
    return render(request, 'QRcode.html')

def transmode1(request):
    return render(request, 'transmode1.html')

def transmode2(request):
    return render(request, 'transmode2.html')