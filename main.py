import os
from datetime import datetime
import django
from django.utils.timezone import localtime
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402
from datacenter.models import Visit


def get_duration(entered_at):
    time_now = localtime(timezone=None)
    delta = time_now - entered_at
    hours, remainder = divmod(delta.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds


def format_duration(hours, minutes, seconds):
    return f'{int(hours)}:{int(minutes)}:{int(seconds)}'


if __name__ == '__main__':
    #passcards = Passcard.objects.all()
    #newline = '\n'
    #active_passcards = Passcard.objects.filter(is_active=True)
    #print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    #print('Активных пропусков: ', len(active_passcards))
    #visits = Visit.objects.all()
    in_storage_users = Visit.objects.filter(leaved_at=None)
    for user in in_storage_users:
        print(user.passcard)
        timezone_entered_time = user.entered_at
        duration = get_duration(timezone_entered_time)
        print('Зашел в хранилище, время по Москве:', timezone_entered_time)
        print('Находится в хранилище: ', format_duration(*duration))
