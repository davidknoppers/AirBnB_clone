#!/usr/bin/python3
"""
Tests the main console's functionality

"""
import sys
import unittest
from unittest import mock
from unittest.mock import create_autospec
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """"""
    def setUp(self):
        """setup method for Console Test Class"""
        self.mock_stdin = create_autospec(sys.stdin)
        self.mock_stdout = create_autospec(sys.stdout)

    def create(self, server=None):
        return HBNBCommand(stdin=self.mock_stdin, stdout=self.mock_stdout)

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_help(self):
        """test help command"""

    def test_exit(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("quit"))

    def test_EOF(self):
        """exit command"""
        cli = self.create()
        self.assertTrue(cli.onecmd("EOF"))

    def test_create_object(self):
        """test do_create"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('create'))
        self.assertEqual('** class name missing **',
                         fakeOutput.getvalue().strip())

    def test_show_object(self):
        """test do_show"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('show BaseModel'))
        self.assertEqual('** no instance found **',
                         fakeOutput.getvalue().strip())

    def test_destroy_object(self):
        """destroyerrr"""
        cli = self.create()
        bad_input = 'destroy BaseModel ChilledCow-ChanceTheRapper-98-98'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(bad_input))
        self.assertEqual('** no instance found **', '** no instance found **')

    def test_update(self):
        """test do_update"""
        cli = self.create()
        bad_input = 'update BaseModel ChilledCow-ChanceTheRapper-98-98 age'
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd(bad_input))
        self.assertEqual('** value missing **', '** value missing **')

    def test_all(self):
        """test do_all"""
        cli = self.create()
        with patch('sys.stdout', new=StringIO()) as fakeOutput:
            self.assertFalse(cli.onecmd('classname.all()'))
        self.assertEqual("** class doesn't exist **",
                         "** class doesn't exist **")

if __name__ == "__main__":
    unittest.main()
