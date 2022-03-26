import unittest
from lib.loot import Loot


class TestLoot(unittest.TestCase):

    def test_loot_with_single_and_multiple_data(self):
        data = "20:35 Your deeds have been noticed and the following items " \
               "dropped by Scarlett Etzel are available in your reward chest:" \
               " a green gem, a giant shimmering pearl, a yellow gem, 2 berserk " \
               "potions, 7 ultimate mana potions, 26 supreme health potions, " \
               "5 platinum coins, an energy bar."
        loot = Loot(data)
        expected = {
            'berserk_potion': 2,
            'energy_bar': 1,
            'giant_shimmering_pearl': 1,
            'green_gem': 1,
            'platinum_coin': 5,
            'supreme_health_potion': 26,
            'ultimate_mana_potion': 7,
            'yellow_gem': 1
        }
        self.assertEqual(loot.item_counts, expected)

    def test_loot_one_item_single(self):
        data = "20:35 Your deeds have been noticed and the following items " \
               "dropped by Scarlett Etzel are available in your reward chest:" \
               " a green gem."
        loot = Loot(data)
        expected = {
            'green_gem': 1
        }
        self.assertEqual(loot.item_counts, expected)

    def test_fail_corrupted_keyword_data(self):
        # missing "chest: " keyword
        corrupted_data = "abcd e: a green gem."
        self.assertRaises(ValueError, Loot, corrupted_data)

    def test_fail_corrupted_keyword_dataa(self):
        # missing item name corrupted
        corrupted_data = "chest: 12, 13"
        self.assertRaises(ValueError, Loot, corrupted_data)
