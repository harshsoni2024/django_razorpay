from http import client
from django.shortcuts import render
import razorpay
from .models import transaction
# Create your views here.
def payment_gateway(request):
    if request.method == "POST":
        name= request.POST.get("name")
        amount= int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_FnV7rymK4w4h44","TdkxsuCmcFFcOzmol4msjGpy"))
        payment = client.order.create(
            {
                'amount':amount,
                'currency':'INR',
                'payment_capture':'1'
                }
        )
        print(payment)
        transaction_obj = transaction(name = name, amount=amount, payment_id= payment['id'])
        transaction_obj.save()
        return render(request, 'payment_gateway.html', context={"payment":payment})

    return render(request, 'payment_gateway.html')

def payment_success(request):
    return render(request,'success.html')
