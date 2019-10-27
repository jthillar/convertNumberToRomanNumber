#!/usr/bin/python
# -*-coding: utf-8 -*

import pandas as pd
import unittest
import romanNumbers

class RomanNumberTest(unittest.TestCase):

    def testConvertNumberToRomanNumber(self):

        df = pd.read_csv('arabe_romain.csv', encoding='utf-8', sep=';', dtype={'arabe':int, 'romain':str})
        for idx, row in df.iterrows():

            r = romanNumbers.convertNumberToRomanNumber(row['arabe'])
            self.assertEqual(r, row['romain'])

unittest.main()
