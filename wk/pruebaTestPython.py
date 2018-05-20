import unittest
import python_diario

class TestPythonSoftware(unittest.TestCase):
 
    def test_should_return_python_when_number_is_3(self):
        self.assertEqual('Python', python_diario.get_string(3))
 

if __name__ == '__main__': 
        unittest.main()

