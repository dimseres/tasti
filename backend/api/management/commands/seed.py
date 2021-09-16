from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import os
from pathlib import Path
import json
from os import walk

from django.contrib.auth.hashers import make_password


# class Command(BaseCommand):
#     help = 'Closes the specified poll for voting'
#
#     def handle(self, *args, **options):
#         print(settings.FIXTURE_DIRS)
#         fixtures_data = []
#         for i in range(len(settings.FIXTURE_DIRS)):
#             fixture_files = []
#             filenames = next(walk(settings.FIXTURE_DIRS[i]), (None, None, []))[2]
#             for filename in filenames:
#                 with open(f"{settings.FIXTURE_DIRS[i]}{filename}", 'r') as file:
#                     data = json.load(file)


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('password', nargs='+', type=int)

    def handle(self, *args, **options):
        print("hased password: ", make_password(str(options['password'][0])))