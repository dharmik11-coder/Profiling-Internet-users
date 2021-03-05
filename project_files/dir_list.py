from os import listdir
import pandas as pd


def make_list(path):                                             #listing all files from given folder path
        for f in listdir(path):
            if not f.startswith('.') or f.startswith('~'):        #ignoring hidden files if any
                yield f




