import unittest
from CNF import CNF

class TestCNF(unittest.TestCase):
    def test_transform_model(self):
        cfg_file = 'model.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 37)

    def test_transform_model2(self):
        cfg_file = 'model2.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 13)

    def test_transform_model3(self):
        cfg_file = 'model3.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 27)

    def test_transform_model4(self):
        cfg_file = 'model4.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 23)

    def test_transform_model5(self):
        cfg_file = 'model5.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 32)

    def test_transform_model6(self):
        cfg_file = 'model6.txt'
        cnf_transformer = CNF(cfg_file)
        cnf_transformer.transform()
        self.assertEqual(len(cnf_transformer.P), 23)


if __name__ == '__main__':
    unittest.main()
