import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):
    def test_help_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertEqual(output, "Shows an individual instance of a class\n[Usage]: show <className> <objectId>")
    
    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_empty_line_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create_base_model_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 123")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 123")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_count_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 123 name 'John'")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_create_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_show_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_destroy_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_all_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_count_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            output = f.getvalue().strip()
            self.assertTrue(output)

    def test_help_update_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue().strip()
            self.assertTrue(output)

    # Test quit command
    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    # Test EOF command
    def test_EOF_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    # Test empty line command
    def test_empty_line_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    # Test create BaseModel command
    def test_create_base_model_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            # Add assertions for the expected output

  

if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
