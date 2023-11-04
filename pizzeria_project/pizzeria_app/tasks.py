from celery import shared_task
from time import sleep
from .models import Order

# asyncronus task to track order 
# for the testing purpose the time laps is kept only 5 seconds

@shared_task
def change_order_status(order_id):
    order = Order.objects.get(pk=order_id)
    # print("change_order_status called")
    sleep(10)
    order.status = 'Accepted'
    order.save(update_fields=['status'])
    sleep(50)
    order.status = 'Preparing'
    order.save(update_fields=['status'])
    sleep(120)
    order.status = 'Dispatched'
    order.save(update_fields=['status'])
    sleep(120)
    order.status = 'Delivered'
    order.save(update_fields=['status'])


