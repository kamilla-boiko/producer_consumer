import random
from django.contrib.auth import get_user_model
from application.models import Order
from celery import shared_task


def generate_task_data():
    return {
        "task_id": random.randint(1000, 9999),
        "name": f"Task {random.choice(['A', 'B', 'C'])}",
        "description": f"Task description {random.randint(1, 10)}",
    }


@shared_task
def create_order():
    employees = list(get_user_model().objects.all())
    random_employee = random.choice(employees)

    task_data = generate_task_data()

    Order.objects.create(
        task_id=task_data["task_id"],
        name=task_data["name"],
        description=task_data["description"],
        employee=random_employee
    )
