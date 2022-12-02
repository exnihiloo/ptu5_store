from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price)
    total = total.replace('.', '')
    # total = int(total)
    
    return render(request, 'payment/payment.html')




