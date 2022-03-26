import unittest
from lib.session import Session


class TestSession(unittest.TestCase):

    def test_session_success(self):
        #all damages are in the range of +- 10%
        damages = [
            (10258, 9900, 10000),
            (5500, 4800, 5000),
            (15700, 14000, 15000)
        ]
        for over, under, actual in damages:
            self._assert_damage_helper(over, actual)
            self._assert_damage_helper(under, actual)

    def test_session_corrupted_data(self):
        session_raw = """
        Damagee: 12
        """
        self.assertRaises(ValueError, Session, session_raw)

    def test_session_no_classification(self):
        session_raw = """
        Damage: 1000
        """
        with self.assertRaises(ValueError) as e:
            Session(session_raw)
        self.assertEqual(str(e.exception), 'No damage classification found')

    def _assert_damage_helper(self, damage: int, classification):
        session_raw = """
        Damage: {s}
        """
        session = Session(session_raw.format(s=damage))
        self.assertEqual(session.actual_damage, damage)
        self.assertEqual(session.damage_classification, classification)
