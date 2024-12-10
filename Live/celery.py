from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définir le fichier de configuration Django par défaut
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_project.settings')

# Créer une instance de Celery
app = Celery('my_project')

# Charger la configuration depuis le fichier settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Charger automatiquement les tâches des applications Django
app.autodiscover_tasks()
