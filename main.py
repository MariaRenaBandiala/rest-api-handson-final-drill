import unittest
import warnings
from app import app  

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_block_record(self):
        response = self.app.get("/block_record")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_program_record(self):
        response = self.app.get("/program_record")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_year_record(self):
        response = self.app.get("/year_record")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_student_block(self):
        response = self.app.get("/student_block")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_student_program(self):
        response = self.app.get("/student_program")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_student_year(self):
        response = self.app.get("/student_year")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_student_record(self):
        response = self.app.get("/student_record")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  


    def test_add_student_record(self):
        new_student = {
            "first_name": "Alice",
            "last_name": "Wonderland",
            "date_of_birth": "2002-01-01"
        }
        response = self.app.post("/student_record", json=new_student)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Student record added successfully", response.json["message"])

    def test_update_student_record(self):
        updated_student = {
            "first_name": "Alice",
            "last_name": "Wonder",
            "date_of_birth": "2002-01-01"
        }
        response = self.app.put("/student_record/1", json=updated_student)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Student record updated successfully", response.json["message"])

    def test_delete_student_record(self):
        response = self.app.delete("/student_record/1")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Student record deleted successfully", response.json["message"])

if __name__ == "__main__":
    unittest.main()
