from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product, OrderCreation
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404


# Product CRUD
@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product = Product.objects.create(
            prodId=data['prodId'],
            category=data['category'],
            discount=data['discount'],
            imageId=data['imageId'],
            price=data['price'],
            productName=data['productName'],
            subCategory=data['subCategory'],
            tax=data['tax'],
            unit=data['unit']
        )
        return JsonResponse({'message': 'Product created successfully!', 'product': product.prodId})

@csrf_exempt
def get_product(request, prodId):
    product = get_object_or_404(Product, prodId=prodId)
    return JsonResponse({
        'prodId': product.prodId,
        'category': product.category,
        'discount': product.discount,
        'imageId': product.imageId,
        'price': product.price,
        'productName': product.productName,
        'subCategory': product.subCategory,
        'tax': product.tax,
        'unit': product.unit
    })

@csrf_exempt
def update_product(request, prodId):
    if request.method == 'PUT':
        data = json.loads(request.body)
        product = get_object_or_404(Product, prodId=prodId)
        product.category = data['category']
        product.discount = data['discount']
        product.imageId = data['imageId']
        product.price = data['price']
        product.productName = data['productName']
        product.subCategory = data['subCategory']
        product.tax = data['tax']
        product.unit = data['unit']
        product.save()
        return JsonResponse({'message': 'Product updated successfully!'})

@csrf_exempt
def delete_product(request, prodId):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, prodId=prodId)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully!'})

# Create Order
@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        try:
            order = OrderCreation.objects.create(
                orderId=data['orderId'],
                comments=data['comments'],
                contactNumber=data['contactNumber'],
                contactPerson=data['contactPerson'],
                customerId=data['customerId'],
                deliveryAddress=data['deliveryAddress'],
                deliveryLocation=data['deliveryLocation'],
                orderDate=data['orderDate'],
                status=data['status'],
                total=data['total']
            )
            return JsonResponse({"message": "Order created successfully", "orderId": order.orderId}, status=201)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)

# Get Order
def get_order(request, orderId):
    try:
        order = OrderCreation.objects.get(orderId=orderId)
        order_data = {
            "orderId": order.orderId,
            "comments": order.comments,
            "contactNumber": order.contactNumber,
            "contactPerson": order.contactPerson,
            "customerId": order.customerId,
            "deliveryAddress": order.deliveryAddress,
            "deliveryLocation": order.deliveryLocation,
            "orderDate": order.orderDate,
            "status": order.status,
            "total": order.total
        }
        return JsonResponse(order_data)
    except OrderCreation.DoesNotExist:
        return JsonResponse({"error": "Order not found"}, status=404)

# Update Order
@csrf_exempt
def update_order(request, orderId):
    if request.method == 'PUT':
        data = json.loads(request.body)
        
        try:
            order = OrderCreation.objects.get(orderId=orderId)
            order.comments = data.get('comments', order.comments)
            order.contactNumber = data.get('contactNumber', order.contactNumber)
            order.contactPerson = data.get('contactPerson', order.contactPerson)
            order.customerId = data.get('customerId', order.customerId)
            order.deliveryAddress = data.get('deliveryAddress', order.deliveryAddress)
            order.deliveryLocation = data.get('deliveryLocation', order.deliveryLocation)
            order.orderDate = data.get('orderDate', order.orderDate)
            order.status = data.get('status', order.status)
            order.total = data.get('total', order.total)
            order.save()

            return JsonResponse({"message": "Order updated successfully"})
        except OrderCreation.DoesNotExist:
            return JsonResponse({"error": "Order not found"}, status=404)
       
def delete_order(request, prodId):
    if request.method == 'DELETE':
        product = get_object_or_404(Product, prodId=prodId)
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully!'})

