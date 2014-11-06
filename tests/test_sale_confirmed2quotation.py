#!/usr/bin/env python
# This file is part of sale_confirmed2quotation module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_depends, test_view


class SaleConfirmed2QuotationTestCase(unittest.TestCase):
    'Test Sale Confirmed to Quotation module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('sale_confirmed2quotation')

    def test0005views(self):
        'Test views'
        test_view('sale_confirmed2quotation')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        SaleConfirmed2QuotationTestCase))
    return suite
