from celery import current_app as current_celery_app
from celery.result import AsyncResult
from project.config import settings

# Notes:

# create_celery is a factory function that configures and then returns a Celery app instance.
# Rather than creating a new Celery instance, we used current_app so that shared tasks will work as expected.
# celery_app.config_from_object(settings, namespace="CELERY") means all celery-related configuration keys should be prefixed with CELERY_. For example, to configure the broker_url, we should use CELERY_BROKER_URL


def create_celery():
    celery_app = current_celery_app
    celery_app.config_from_object(settings, namespace="CELERY")

    return celery_app


def get_task_info(task_id):
    """
    return task info according to the task_id
    """
    task = AsyncResult(task_id)
    state = task.state

    if state == "FAILURE":
        error = str(task.result)
        response = {
            "state": task.state,
            "error": error,
        }
    else:
        response = {
            "state": task.state,
        }
    return response
