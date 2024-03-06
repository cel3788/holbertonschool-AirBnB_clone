from main import Student
import unittest

class TestStudent(unittest.TestCase):

    def test_to_json_with_attrs(self):
        student = Student("John", "Doe", 25)
        json_data = student.to_json(["first_name", "age"])
        self.assertEqual(json_data, {"first_name": "John", "age": 25})

    def test_to_json_without_attrs(self):
        student = Student("Alice", "Smith", 30)
        json_data = student.to_json()
        self.assertEqual(json_data, {"first_name": "Alice", "last_name": "Smith", "age": 30})

if __name__ == '__main__':
    unittest.main()
