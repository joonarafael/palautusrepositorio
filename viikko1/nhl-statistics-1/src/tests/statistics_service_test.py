import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_player_list(self):
        self.assertAlmostEqual(len(self.stats._players), 5)

    def test_search_existing_player(self):
        self.assertEqual(type(self.stats.search("Kurri")), Player)

    def test_search_nonexisting_player(self):
        self.assertEqual(self.stats.search("abc"), None)
    
    def test_search_team(self):
        self.assertAlmostEqual(len(self.stats.team("EDM")), 3)
    
    def test_top3(self):
        top_list = self.stats.top(3)

        self.assertAlmostEqual(len(top_list), 3)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Lemieux")
        self.assertEqual(top_list[2].name, "Yzerman")

        top_list = self.stats.top(3, SortBy.POINTS.value)

        self.assertAlmostEqual(len(top_list), 3)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Lemieux")
        self.assertEqual(top_list[2].name, "Yzerman")

    def test_top_goals(self):
        top_list = self.stats.top(3, SortBy.GOALS.value)

        self.assertAlmostEqual(len(top_list), 3)

        self.assertEqual(top_list[0].name, "Lemieux")
        self.assertEqual(top_list[1].name, "Yzerman")
        self.assertEqual(top_list[2].name, "Kurri")

    def test_top_assists(self):
        top_list = self.stats.top(3, SortBy.ASSISTS.value)

        self.assertAlmostEqual(len(top_list), 3)

        self.assertEqual(top_list[0].name, "Gretzky")
        self.assertEqual(top_list[1].name, "Yzerman")
        self.assertEqual(top_list[2].name, "Lemieux")