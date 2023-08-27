from django.db import models


class Domain(models.Model):
    domain_name = models.CharField("Ping", max_length=200, blank=False, null=False)
    ping_of_domain = models.TextField("Ping", blank=False, null=False)

    def __str__(self):
        return self.domain_name
