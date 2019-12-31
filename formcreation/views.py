from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView,CreateView
from .models import data_of_user
from django.views.decorators.csrf import csrf_exempt
from .PayTm import Checksum
import random

MERCHANT_KEY='2SHq5!5JTnOr_iiq'
class Homepage(TemplateView):

    template_name="Homepage.html"


def Ffront(request):
    if request.method=="POST":
        global first,last,email,semester,address,zipcode,amount
        first=request.POST.get('first','')
        last=request.POST.get('last','')
        email=request.POST.get('email','')
        semester=request.POST.get('semester','')
        address=request.POST.get('address','')
        zipcode=request.POST.get('zipcode','')
        amount=request.POST.get('amount','')

        param_dict= {
            'MID':'QdSYxC64217640165409',
            'ORDER_ID':str(random.random()*100000),
            'TXN_AMOUNT':'500',
            'CUST_ID':'jonathandabreo24@gmail.com',
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
	        'CALLBACK_URL':'http://127.0.0.1:8000/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request,'paytm.html',{'param_dict':param_dict})


    else:
        return render(request, "Ffront.html")



@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            q =data_of_user(first=first,last=last,email=email,semester=semester,address=address,zipcode=zipcode,amount=amount)
            q.save()
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})
