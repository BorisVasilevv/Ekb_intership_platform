# TravelRouteBuilder

## Описание запросов

```/travel_route ['POST']``` Принимает json вида:

```json
{
  "routes": [
    {
      "origin": "Москва",
      "destination": "Санкт-Петербург",
      "date": "2024-06-01",
      "preferred_transport": [1, 2]
    },
    {
      "origin": "Санкт-Петербург",
      "destination": "Москва",
      "date": "2024-06-03",
      "preferred_transport": [1]
    }
  ]
}
```

Возвращает json вида:
```json
{
  "routes": [
    {
      "origin": "Москва",
      "destination": "Санкт-Петербург",
      "transport": [
        {
          "transport_type":1,
          "price": 1500,
          "departure_datetime": "2024-06-01T06:00:00",
          "arrival_datetime": "2024-06-01T08:00:00"
        },
        {
          "transport_type":2,
          "price": 1000,
          "departure_datetime": "2024-06-01T07:00:00",
          "arrival_datetime": "2024-06-01T10:30:00"
        }
      ],
      "hotels": [
        {
          "name": "Отель А",
          "location": "Центральный район",
          "start_date": "2024-06-01",
          "end_date": "2024-06-03",
          "price": 2000
        },
        {
          "name": "Отель Б",
          "location": "Побережье",
          "start_date": "2024-06-01",
          "end_date": "2024-06-03",
          "price": 1500
        }
      ],
      "weather": {
        "temperature": 20,
        "wind_speed": 5,
        "precipitation": "дождь"
      }
    }
  ]
}
```
## Команды для разворота в docker

```docker build -t travel_route_builder_service .``` // создаем image проекта

```docker run -p 1488:1488 --name travel_route_builder_service travel_route_builder_service``` // создаем docker container
