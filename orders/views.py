from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart

def order_create(request):
    # Создание объекта корзины, привязанного к текущему сеансу
    cart = Cart(request)
    
    if request.method == 'POST':
        # Создание формы с данными из POST-запроса
        form = OrderCreateForm(request.POST)
        
        if form.is_valid():
            # Сохранение нового заказа
            order = form.save()
            
            # Создание элементов заказа для каждого товара в корзине
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # Очистка корзины
            cart.clear()
            
            # Отображение страницы подтверждения заказа
            return render(request,
                          'orders/order/created.html',
                          {'order': order})
    
    else:
        # Если запрос не POST, создается пустая форма
        form = OrderCreateForm()
    
    # Отображение страницы создания заказа с корзиной и формой
    return render(request,
                  'orders/order/create.html',
                  {'cart': cart, 'form': form})
