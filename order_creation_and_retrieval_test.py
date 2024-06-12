# Чаудхари Елена, 17-я когорта - Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data


# Автотест
def test_order_creation_and_retrieval():
    response = sender_stand_request.create_order(data.order_body)

    track_number = response.json()["track"]
    

    # Получение данных заказа по треку
    order_response = sender_stand_request.get_order(track_number)

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
