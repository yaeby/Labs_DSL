import sys
from CNF import CNF

if __name__ == '__main__':
    CFG = sys.argv[1] if len(sys.argv) > 1 else 'model.txt'
    cnf_transformer = CNF(CFG)
    cnf_transformer.transform()
