import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "module3.settings")

application = get_wsgi_application()

# 🔽 ADD THIS BLOCK
try:
    from django.core.management import call_command
    call_command("migrate", interactive=False)
except Exception as e:
    print("Migration error:", e)
