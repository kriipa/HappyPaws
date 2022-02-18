from itertools import product
from django.shortcuts import render, redirect
from cart.models import *
from customer.forms import *
from products import *
from checkout import *
from products.forms import *
from cart.forms import *
from checkout.forms import *
import datetime


def delete_shipping_order(request, pk):
    order = OrderProduct.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/owner-orders/')
    context = {}
    return render(request, 'owner/delete_shipping.html', context)

def delete_shipping_order(request, pk):
    order = OrderProduct.objects.get(id=pk)
    order.delete()
    return redirect('/owner-orders/')


def manageCustomer(request):
    customer = Customer.objects.all()
    context = {'customers': customer}
    return render(request, 'owner/manage_customer.html', context)


def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    user = request.user
    form = CustomerForm(request.POST)
    if request.method == 'POST':
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
        customer.reward_point = request.POST.get('reward_point')
        username = request.POST.get('username')
        password = request.POST.get('password')
        if password != customer.password:
            if username != customer.username:
                user.username = username
                user.set_password(password)
                user.save()
                customer.password = password
                customer.username = username
        customer.save()
        return redirect('/manage-customer/')
    context = {'form': form, 'customer': customer}
    return render(request, 'owner/updateCustomer.html', context)


# def deleteCustomer(request, pk):
#     customer = Customer.objects.get(id=pk)
#     if request.method == 'POST':
#         customer.delete()
#         return redirect('/manage-customer/')
#     context = {'customer': customer}
#     return render(request, 'owner/deleteCustomer.html', context)


def manageProduct(request):
    product = Product.objects.all()
    context = {'products': product}
    return render(request, 'owner/manageProduct.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    return redirect('/manage-customer/')

def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    category = Category.objects.all()
    form = ProductForm(request.POST, request.FILES)
    imageform = ImageForm(request.POST, request.FILES, instance=product)
    if request.method == 'POST':
        imageform = ImageForm(request.POST, request.FILES, instance=product)
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        category_id = request.POST.get('category')
        category_object = Category.objects.get(id=category_id)
        product.category = category_object
        
        product.save()
        imageform.save()
        return redirect('/manage-product/')  

    context = {'form': form, 'product': product, 'category': category, 'imageform': imageform}
    return render (request,'owner/updateproduct.html', context )

# def deleteProduct(request, pk):
#     product = Product.objects.get(id=pk)
#     if request.method == 'POST':
#         product.delete()
#         redirect('/manage-product/')
#     context= {'product': product}
    
#     return render(request, 'owner/deleteproduct.html', context)

def deleteProduct(request,pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("/manage-product/")

def createOrder(request):
    orderform = OrderForm()
    orderproductform = OrderProductForm()
    checkoutform = ShippingForm()
    customer = Customer.objects.all()
    product = Product.objects.all()
    if request.method == 'POST':
        orderform = OrderForm(request.POST)
        orderproductform = OrderProductForm(request.POST)
        checkoutform = ShippingForm(request.POST)
        orderCustomer = request.POST.get('customer')
        orderProduct = request.POST.get('item')
        orderStatus = request.POST.get('status')
        orderCustomer_object = Customer.objects.get(id=orderCustomer)
        orderProduct_object = Product.objects.get(id=orderProduct)
        order, created = Order.objects.get_or_create(
            customer=orderCustomer_object, order_completed=False, status=orderStatus, order_id=datetime.datetime.now().timestamp())
        order.save()
        order.order_placed = True
        orderQuantity = request.POST.get('quantity')
        orderProduct, created = OrderProduct.objects.get_or_create(
            order=order, item=orderProduct_object, quantity=orderQuantity)
        orderProduct.save()
        checkoutAddress = request.POST.get('address')
        checkoutCity = request.POST.get('city')
        Shipping.objects.create(
            customer=orderCustomer_object,
            order=order,
            city=checkoutCity,
            address=checkoutAddress,

        )
        return redirect('/owner-orders/')
    context = {'customer': customer, 'product': product}
    return render(request, 'owner/createorder.html', context)

def updateOrder(request, pk):
    orderform = OrderForm()
    orderproductform = OrderProductForm()
    checkoutform = ShippingForm()
    customer = Customer.objects.all()
    product = Product.objects.all()
    orderProduct = OrderProduct.objects.get(id=pk)
    order = Order.objects.get(id=orderProduct.order.id)
    shipping = Shipping.objects.get(order=order.id)
    orderProduct_item = Product.objects.get(id=orderProduct.item.id)   
    orderCustomer_object = Customer.objects.get(id=order.customer.id) 
    if request.method == 'POST':
        orderform = OrderForm(request.POST)
        orderproductform = OrderProductForm(request.POST)
        checkoutform = ShippingForm(request.POST)
        orderCustomer = request.POST.get('customer')
        orderItem = request.POST.get('item')
        orderStatus = request.POST.get('status')
        updateCustomer_object = Customer.objects.get(id=orderCustomer)
        updateProduct_object = Product.objects.get(id=orderItem)
        order.customer = updateCustomer_object
        order.status = orderStatus
        order.save()
        orderQuantity = request.POST.get('quantity')
        orderProduct.quantity = orderQuantity
        orderProduct.item = updateProduct_object
        orderProduct.save()
        checkoutAddress = request.POST.get('address')
        checkoutCity = request.POST.get('city')
        shipping.address = checkoutAddress
        shipping.city = checkoutCity
        shipping.save()
       
        return redirect('/owner-orders/')
    context = {'customer': customer, 'product': product, 
    'orderProduct': orderProduct,
    'order': order,
    'shipping': shipping,
    'orderProduct_item': orderProduct_item, 
    'orderCustomer': orderCustomer_object}
    return render(request, 'owner/updateOrder.html', context)

