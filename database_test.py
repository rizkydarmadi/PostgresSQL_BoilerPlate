import unittest
from database import ConnectDB


class TestDatabase(unittest.TestCase):
    def test_is_correct(self):
        database = ConnectDB(path="config.json")
        self.assertEqual(
            ("postgresql", "postgres", "localhost", 5460, "account", "12qwaszx"),
            database.show(),
        )

    def test_session(self):
        database = ConnectDB(path="config.json")
        self.assertIsNotNone(database.session())


if __name__ == "__main__":
    unittest.main()
