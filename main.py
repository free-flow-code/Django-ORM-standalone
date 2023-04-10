import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    passcards = Passcard.objects.all()
    newline = '\n'
    for passcard in passcards:
        print(f'owner_name: {passcard.owner_name}{newline}'
              f'passcode: {passcard.passcode}{newline}'
              f'created_at: {passcard.created_at}{newline}'
              f'is_active: {passcard.is_active}{newline}')
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
