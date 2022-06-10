from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L993GJlq2jGOSsnMIaPUB6JkQ1vwjoDONbgWYlicJCqwDNWhLXQbzoWV8mf0LIpAlvztSzBNesqS4pL5VBZzjbH00kgTl7fjw',
        'client_secret': 'sk_test_51L993GJlq2jGOSsnl277whoCiuqr8NZVTKc1VmyCx2w3BITtZX29lViQ60mMZQVyQCxCtn9h3iqFOeoHLj2Fnfdv00slRUYCNg',
    }

    return render(request, template, context)
