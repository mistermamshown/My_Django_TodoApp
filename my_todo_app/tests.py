from django.test import TestCase

# Create your tests here.

class TestTodo(TestCase):
    def test_my_todo_app(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
