import unittest
from ..seed import Command
from django.test import TestCase


class TestStringMethods(TestCase):
    command = Command()

    def test_command_seed(self):
        # self.assertEqual('foo'.upper(), 'FOO')
        self.command.handle()
