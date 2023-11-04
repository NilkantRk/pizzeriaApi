# In pizzeria_app/views.py

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pizza, Order
from .serializer import PizzaSerializer, OrderSerializer
from .tasks import change_order_status


# to create order

@api_view(['POST'])
def create_order(request):
    if request.method == 'POST':
        pizzas_data = request.data.get('pizzas')
        if pizzas_data:
            order = Order.objects.create(status='Placed')
            for pizza_data in pizzas_data:
                pizza_data['order'] = order.id  # Associate the pizza with the order
                pizza_serializer = PizzaSerializer(data=pizza_data)
                if pizza_serializer.is_valid():
                    pizza = pizza_serializer.save()
                    order.pizzas.add(pizza)  # Add the pizza to the order
                else:
                    order.delete()
                    
                    return Response(pizza_serializer.errors, status=400)
                
            change_order_status.delay(order.id)  # Asynchronously call the Celery task 

            return Response({'message': 'Order placed successfully!','order_id':order.id }, status=201)
            
        else:
            return Response({'error': 'No pizzas provided.'}, status=400)

    return Response({'error': 'Invalid request method.'}, status=400)



# tack the order that is placed

@api_view(['GET'])
def track_order(request, order_id):
    
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response({'error': 'Order does not exist.'}, status=404)

    serializer = OrderSerializer(order)
    return Response(serializer.data)
    
