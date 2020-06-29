import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                print(line)
                if line[6] == 'True':
                    lte_exist = True
                else:
                    lte_exist = False
                phone = Phone(name=line[1], price=line[3], image=line[2], release_date=line[4], lte_exists=lte_exist,
                              slug=slugify(line[1]))
                phone.save()
                # TODO: Добавьте сохранение модели
                # pass
