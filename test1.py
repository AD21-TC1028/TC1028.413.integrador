#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import fuzzy
import numeros


class Testprueba (unittest.TestCase):
    
    temperatura =[[10,20,30,40],
                  [20,30,40,50],
                  [30,40,50,60],
                  [40,50,60,70]]
    
    def test_fuzyy(self):
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,5),[0, 0, 0, 0])
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,25),[1, 0.5, 0, 0])
        self.assertEqual(fuzzy.calculo_membresia(self.temperatura,42),[0, 0.8, 1, 0.2])
    
    def test_pares(self):
        self.assertEqual(numeros.cuenta_pares([2,4,2,5,7,9,10]),4)
        self.assertEqual(numeros.cuenta_pares([6,3,5,4,6,7,9]),3)
        
    
if __name__ == '__main__':
    unittest.main()

