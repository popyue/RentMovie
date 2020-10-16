from django.shortcuts import render,redirect

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .task import order_created

# Create your views here.


def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
										movie=item['movie'],
										price=item['price'],
										quantity=item['quantity'])

			# clear the cart 
			cart.clear()
			print("11order id is {}".format(order.id))
			print("22request is {}".format(request))
			#order_create(order.id)
			request.session['order_id'] = order.id
			# redirect to the payment
			return redirect('payment:process')

	else:
		form = OrderCreateForm()
	return render(request,
				'orders/order/create.html',
				{'cart':cart, 'form':form})