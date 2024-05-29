import requests

# Ваш вебхук
webhook_url = ''

# ID вашего смарт-процесса
entity_type_id = 152  # Замените на ваш ID смарт-процесса
task_id = 95  # ID задачи, которую вы хотите получить

def get_task_details(webhook_url, entity_type_id, task_id):
    url = f'{webhook_url}crm.item.get'

    params = {
        'entityTypeId': entity_type_id,
        'id': task_id
    }

    response = requests.post(url, json=params)

    if response.status_code == 200:
        return response.json()['result']['item']
    else:
        print(f'Ошибка при получении подробной информации о задаче: {response.status_code}')
        print(response.json())
        return {}

# Получаем подробную информацию о задаче с ID 95
task_details = get_task_details(webhook_url, entity_type_id, task_id)

# Выводим подробную информацию о задаче
print(f"Подробная информация о задаче ID: {task_id}")
for field, value in task_details.items():
    print(f"{field}: {value}")



