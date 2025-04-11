import unittest
from todo import ToDoList


class TestToDoList(unittest.TestCase):

    def setUp(self):
        self.todo = ToDoList()

    def test_add_task(self):
        self.todo.add_task("Buy groceries")
        self.assertIn("Buy groceries", self.todo.get_tasks())

    def test_add_empty_task_raises_error(self):
        with self.assertRaises(ValueError):
            self.todo.add_task("")

    def test_remove_task(self):
        self.todo.add_task("Walk the dog")
        self.todo.remove_task("Walk the dog")
        self.assertNotIn("Walk the dog", self.todo.get_tasks())

    def test_remove_nonexistent_task_raises_error(self):
        with self.assertRaises(ValueError):
            self.todo.remove_task("Nonexistent task")

    def test_get_tasks_returns_copy(self):
        self.todo.add_task("Read book")
        tasks = self.todo.get_tasks()
        tasks.append("New task")
        self.assertNotIn("New task", self.todo.get_tasks())

    def test_clear_tasks(self):
        self.todo.add_task("Do laundry")
        self.todo.clear_tasks()
        self.assertEqual(len(self.todo.get_tasks()), 0)


if __name__ == '__main__':
    unittest.main()
