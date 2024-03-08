import os
import unittest
import MySQLdb
import sqlalchemy
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.user import User


class TestHBNBCommand(unittest.TestCase):

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_create(self):
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            
            with self.assertRaises(sqlalchemy.exc.OperationalError):
                cons.onecmd('create User')
            
            clear_stream(cout)
            cons.onecmd('create User email="john25@gmail.com" password="123"')
            mdl_id = cout.getvalue().strip()
            
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(mdl_id))
            result = cursor.fetchone()
            
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            
            cursor.close()
            dbc.close()
    
    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')
    def test_db_show(self):
        with patch('sys.stdout', new=StringIO()) as cout:
            cons = HBNBCommand()
            obj = User(email="john25@gmail.com", password="123")
            
            dbc = MySQLdb.connect(
                host=os.getenv('HBNB_MYSQL_HOST'),
                port=3306,
                user=os.getenv('HBNB_MYSQL_USER'),
                passwd=os.getenv('HBNB_MYSQL_PWD'),
                db=os.getenv('HBNB_MYSQL_DB')
            )
            cursor = dbc.cursor()
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            result = cursor.fetchone()
            
            self.assertTrue(result is None)
            cons.onecmd('show User {}'.format(obj.id))
            self.assertEqual(cout.getvalue().strip(), '** no instance found **')
            
            obj.save()
            clear_stream(cout)
            cursor.execute('SELECT * FROM users WHERE id="{}"'.format(obj.id))
            
            cons.onecmd('show User {}'.format(obj.id))
            result = cursor.fetchone()
            
            self.assertTrue(result is not None)
            self.assertIn('john25@gmail.com', result)
            self.assertIn('123', result)
            self.assertIn('john25@gmail.com', cout.getvalue())
            self.assertIn('123', cout.getvalue())
            
            cursor.close()
            dbc.close()

    def test_help_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(f.getvalue().strip(), "Affiche la représentation sous forme de chaîne d'une instance")
            
    def test_quit_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            with self.assertRaises(SystemExit):
                HBNBCommand().onecmd("quit")

    def test_empty_line_present(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            self.assertEqual(f.getvalue(), "")

    def test_create_BaseModel_present(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(f.getvalue().strip(), "Crée une nouvelle instance de la classe spécifiée")
    
if __name__ == '__main__':
    unittest.main()
