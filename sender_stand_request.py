import configuration
import requests


# Создание заказа
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_ORDERS,
                         json=body)


# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response



