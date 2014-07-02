#!/data/project/yadkard/venv/bin/python
# -*- coding: utf-8 -*-

"""Test isbn.py module."""


import unittest

import isbn


class IsbnTest(unittest.TestCase):

    def test_is1(self):
        """not found in adinebook"""
        i = '9780349119168'
        o = isbn.Citation(i, pure = True)
        e = '* {{cite book|last=Adkins|first=Roy|title=The war for all the oceans : from Nelson at the Nile to Napoleon at Waterloo|publisher=Abacus|location=London|year=2007|isbn=9780349119168|ref=harv}}'
        self.assertIn(e, o.cite)

    def test_is2(self):
        """not found in ottobib"""
        i = '978-964-6736-71-9'
        o = isbn.Citation(i, pure = True)
        e = '* {{cite book|others=بدیل بن علی خاقانی (شاعر),  جهانگیر منصور (به اهتمام), and  بدیع الزمان فروزانفر (مقدمه)|title=دیوان خاقانی شروانی|publisher=نگاه|year=1389|isbn=978-964-6736-71-9|language=fa|ref={{sfnref|نگاه|1389}}'
        self.assertIn(e, o.cite)

    def test_is3(self):
        """exists in both"""
        i = '964-6736-34-3 '
        o = isbn.Citation(i)
        e = '* {{cite book|others=سحر معصومی (به اهتمام)|title=راز گل سرخ: نقد و گزیده شعرهای سهراب سپهری|publisher=نگاه|year=1386|isbn=964-6736-34-3|language=fa|ref={{sfnref|نگاه|1386}}'
        self.assertIn(e, o.cite)
        
    def test_is4(self):
        """unpure isbn10 not found in ottobib"""
        i = 'choghondar 964-92962-6-3 شلغم'
        o = isbn.Citation(i)
        e = '* {{cite book|last=حافظ|first=شمس الدین محمد|others= رضا نظرزاده (به اهتمام)|title=دیوان کامل حافظ همراه با فالنامه|publisher=دیوان|year=1385|isbn=964-92962-6-3|language=fa|ref=harv'
        self.assertIn(e, o.cite)



if __name__ == '__main__':
    unittest.main()
