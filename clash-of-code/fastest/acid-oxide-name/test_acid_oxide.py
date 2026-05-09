import unittest

from acid_oxide_name import acid_oxide_name


class TestAcidOxideName(unittest.TestCase):
    def test_nonmetal_1_oxide_2(self):
        self.assertEqual(acid_oxide_name(1, "carbon", 2), "carbon dioxide")

    def test_nonmetal_2_oxide_3(self):
        self.assertEqual(acid_oxide_name(2, "sulfur", 3), "disulfur trioxide")

    def test_nonmetal_4_oxide_1(self):
        self.assertEqual(acid_oxide_name(4, "phosphorus", 1), "tetraphosphorus monoxide")

    def test_nonmetal_3_oxide_5(self):
        self.assertEqual(acid_oxide_name(3, "nitrogen", 5), "trinitrogen pentoxide")

    def test_nonmetal_5_oxide_4(self):
        self.assertEqual(acid_oxide_name(5, "chlorine", 4), "pentachlorine tetroxide")


if __name__ == "__main__":
    unittest.main()
