from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Tafera para enviar notificações de email  quando forem feitos pedidos
    """

    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have succesfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@shop_project.com', [order.email])
    return mail_sent
