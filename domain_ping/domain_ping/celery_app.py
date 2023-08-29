import os
from celery import Celery
from celery.schedules import crontab
from .settings import PING_TIME

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "domain_ping.settings")

app = Celery("domain_ping")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "update-debt-every-2-minutes": {
        "task": "domain.tasks.ping_domain",
        "schedule": crontab(minute=f"*/{PING_TIME}"),
    },
}
