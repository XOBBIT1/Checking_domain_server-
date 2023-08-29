import logging
import re
import subprocess
import threading

from .models import Domain
from domain_ping.celery_app import app

lock = threading.Lock()


def process_domain(domain_name):
    try:
        with lock:
            domain = Domain.objects.get(pk=domain_name.pk)
            domain_name = domain.domain_name
            domain.delete()

            ping_output_bytes = subprocess.check_output(["ping", domain_name])
            ping_output_text = ping_output_bytes.decode('cp866')
            average_match = re.search(r"Среднее = (\d+)", ping_output_text)

            new_domain = Domain(domain_name=domain_name, ping_of_domain=average_match.group(1))
            new_domain.save()

            logging.info(f"Успешно сохранен ping домена {domain_name}")
    except subprocess.CalledProcessError as e:
        logging.info(f"Ошибка при выполнении ping для {domain_name}: {e}")


@app.task
def ping_domain():
    domains = Domain.objects.all()

    threads = []
    for domain in domains:
        thread = threading.Thread(target=process_domain, args=(domain,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
