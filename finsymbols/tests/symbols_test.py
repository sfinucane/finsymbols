#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import glob
from unittest import TestCase, main
from six import string_types

def last_index(iterObj, value):
    if not iterObj:
        return None
    # find the first occurrence, if any
    pivot = iterObj.index(value)
    if not pivot:
        return None
    sub_iterObj = iterObj[pivot:]
    if len(sub_iterObj) <= 1:
        return pivot
    next_occurrence = last_index(sub_iterObj, value)
    return next_occurrence if next_occurrence else pivot


try:
    from finsymbols import symbols
except ImportError:
    # last_finsymbols = last_index(os.getcwd().split(os.path.sep), 'finsymbols')
    # print last_finsymbols
    # print pkg_path
    sys.path.append("")
    from finsymbols import symbols


class TestSizeOfList(TestCase):

    def test_sp500_size(self):
        sp500 = symbols.get_sp500_symbols()
        assert len(sp500) == 505, 'len gathered data: {}.\
         Expected len: 504'.format(len(sp500))

    def test_amex_not_null(self):
        amex = symbols.get_amex_symbols()
        assert len(amex) != 0, 'AMEX list is of size 0'

    def test_nyse_not_null(self):
        nyse = symbols.get_nyse_symbols()
        assert len(nyse) != 0, 'NYSE list is of size 0'

    def test_nasdaq_not_null(self):
        nasdaq = symbols.get_nasdaq_symbols()
        assert len(nasdaq) != 0, 'NASDAQ list is of size 0'

    def test_string_output(self):
        sp500 = symbols.get_sp500_symbols()
        company = sp500[0]

        assert isinstance(company['company'], string_types) == True, 'Company dict: {}.\
         Expected output to be string'.format(company)


if __name__ == '__main__':
    main()
