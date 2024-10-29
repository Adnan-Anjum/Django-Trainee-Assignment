# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Fruit

@receiver(post_save, sender=Fruit)
def log_fruit_creation(sender, instance, created, **kwargs):
    if created:
        print(f"Signal: A new fruit was added - {instance.name} ({instance.color})")