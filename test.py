# Write a test.py for testing the breakfast.py file.

try:
    import unittest
    from breakfast import app

except Exception as e:
    print("Some modules are missing {}".format(e))


class FlaskTest(unittest.TestCase):
    # Check for the response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()
