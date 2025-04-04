from django.test import TestCase
from .models import TodoItem

class TodoItemModelTest(TestCase):

    def setUp(self):
        TodoItem.objects.create(title="Test Todo", completed=False)

    def test_todo_item_creation(self):
        todo_item = TodoItem.objects.get(title="Test Todo")
        self.assertEqual(todo_item.title, "Test Todo")
        self.assertFalse(todo_item.completed)

    def test_todo_item_completed_status(self):
        todo_item = TodoItem.objects.get(title="Test Todo")
        todo_item.completed = True
        todo_item.save()
        self.assertTrue(todo_item.completed)