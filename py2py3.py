#!/usr/bin/env python3

'''
Convert python2 to python3 code.

'''

import re
from autopep8 import fix_code
import sys


class Convert:

    def __init__(self, filepath):
        self.file = filepath
        
        if not self.file:
            self.print_help()
            
        with open(filepath, 'r') as pyfile:
            self.pycode = fix_code(pyfile.read())

    def print_help(self):
        print(f'./{sys.argv[0]} <file_path>')
        exit()

    def raise_deadlib_err(self):
        # to be implemented

    def to_py3(self):
        println = r'print\s(.*)'
        xrange_ = r'xrange\((.*?)\)'
        exception = r'(except\s[a-zA-Z]*),(\s.{1})'
        inputfunc = r'raw_input'
        nextfunc = r'(next\(\))'

        psub = {println: r'print(\1)', xrange_: r'range(\1)',
                exception: r'\1 as\2', inputfunc: 'input', nextfunc: r'__\1__'}

        for pattern, replacement in psub.items():
            self.pycode = re.sub(pattern, replacement, self.pycode)

        return self.pycode


if __name__ == "__main__":

    try:
        argv = sys.argv[1]
    except:
        argv = ''

    c = Convert(argv)
    py3code = c.to_py3()
    print(py3code)
