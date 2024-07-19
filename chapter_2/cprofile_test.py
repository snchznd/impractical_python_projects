"""A module to analyze the performance of palingrams.py"""

import cProfile
import palingrams

if __name__ == '__main__' :
    cProfile.run('palingrams.main()')
