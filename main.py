import os
from tester import Tester

import sys
sys.path.append('tests')
from assignment1 import tests


SRC_DIR = "../0512182001_Fix_compile"
# SRC_DIR = "../0512182001"
# SRC_DIR = "src_files"


def main():
    tester = Tester(tests)
    dirs = sorted(os.listdir(SRC_DIR))
    for i, dir in enumerate(dirs, start=1):
        if(os.path.isdir(SRC_DIR+'/'+dir) == False):
            continue
        print("({:>3}/{:>3}) Testing student {}: ".format(i,len(dirs),dir), end='')
        tester.test(dir, os.path.join(SRC_DIR, dir))

    print("Creating report")
    tester.report_results()


if __name__ == "__main__":
    main()
