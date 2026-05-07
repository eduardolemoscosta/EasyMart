from django.contrib.auth import get_user_model
from django.db import migrations


def create_admin_user(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')


def delete_admin_user(apps, schema_editor):
    User = get_user_model()
    User.objects.filter(username='admin').delete()

class Migration(migrations.Migration):
    dependencies = [
        ('products', '0003_produto_fornecedor'),
    ]

    operations = [
        migrations.RunPython(create_admin_user, delete_admin_user),
    ]
