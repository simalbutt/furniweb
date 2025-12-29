from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_order_confirmation_email(order):
    user = order.user
    items = order.items.all()

    subject = f"Order Confirmation - #{order.id}"
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [user.email]

    context = {
        "user": user,
        "order": order,
        "items": items,
    }

    html_content = render_to_string("emails/order_confirmation.html", context)
    text_content = (
        f"Thank you for your order #{order.id}. Total: Rs {order.total_amount}"
    )

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()
