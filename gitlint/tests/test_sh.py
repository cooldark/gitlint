# -*- coding: utf-8 -*-

try:
    # python 2.x
    from mock import patch, call, PropertyMock
except ImportError:
    # python 3.x
    from unittest.mock import patch, call, PropertyMock  # pylint: disable=no-name-in-module, import-error

from unittest2 import TestCase
from gitlint.sh import ShResult


class ShTests(TestCase):

    def test_equality_str(self):
        res = ShResult('example stdout', 'stderr', 0, [])
        self.assertEqual(res, 'example stdout')
        self.assertFalse(res == 'not the same')

    def test_equality_ustr(self):
        res = ShResult('This is å test', 'stderr', 0, [])
        self.assertEqual(res, u'This is å test')

