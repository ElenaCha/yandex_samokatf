# Финальный проект Яндекс Практикум - тестирование приложения Яндекс Самокат
1. Тестирование функциональности веб-приложения. Необходимо протестировать функциональность «Сделать заказ».
2. Ретест багов в мобильном приложении.
3. Регрессионное тестирование мобильного приложения по готовым тест-кейсам.
4. Работа с базой данных
Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).

SELECT c.login, COUNT(o.track)         
FROM "Couriers" AS c 
INNER JOIN "Orders" AS o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login;

Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

SELECT track,
	CASE
	 WHEN finished = true THEN 2
	 WHEN canсelled = true THEN -1
	 WHEN "inDelivery" = true THEN 1
	 ELSE 0
    END AS status
FROM "Orders";

5. Автоматизация теста к API
Теперь автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Шаги автотеста:
Выполнить запрос на создание заказа.
Сохранить номер трека заказа.
Выполнить запрос на получения заказа по треку заказа.
Проверить, что код ответа равен 200.
- Для запуска тестов должны быть установлены пакеты pytest и requests
- Запуск всех тестов выполянется командой pytest# YandexSamokat
