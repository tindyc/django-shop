import stripe

from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from basket.basket import Basket

@login_required
def BasketView(request):

    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51MpfHMF9njsegm9QSHEO7BauCm9jPhBzy7JQUpQFG7sKlOIjpVxNCbOAzaPFte64nQNDdihtfscz9xzA6PYAbIVH00aFkCu80F'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='gbp',
        metadata={'userid': request.user.id}
    )

    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})

