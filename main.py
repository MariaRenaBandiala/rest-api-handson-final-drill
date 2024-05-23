import unittest
import warnings
from app import app  

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)

    def test_program_student_table(self):
        response = self.app.get("/program_student_table")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_program_table(self):
        response = self.app.get("/program_table")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_st_yr_table(self):
        response = self.app.get("/st_yr_table")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)  

    def test_student_record(self):
        response = self.app.get("/student_record")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list) 

    def test_year(self):
        response = self.app.get("/year")
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
