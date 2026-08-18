from stripe import StripeClient
from config.settings import STRIPE_API_KEY


client = StripeClient(STRIPE_API_KEY)

def create_stripe_course(course):
    """ Создаёт курс в страпе. """

    return client.v1.products.create({"name": course})


def create_stripe_price(amount, course):
    """ Создаёт сумму платежа в страпе. """

    response = course.id
    return client.v1.prices.create({
        "currency": "usd",
        "unit_amount": amount * 100,
        "product": response,
    })

def create_stripe_session(price):
    """ Создаёт сессию платежа в страпе. """

    response = price.id
    session = client.v1.checkout.sessions.create({
        "success_url": "http://127.0.0.1:8000/",
        "line_items": [{"price": response, "quantity": 1}],
        "mode": "payment",
    })
    return session.id, session.url
