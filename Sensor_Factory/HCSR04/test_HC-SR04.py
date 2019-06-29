#!/usr/bin/python

import HC_SR04

Sensor1 = HC_SR04.HCSR04(23, 24, 0.1)
Sensor1.Test()

#import unittest
#import calc

#lass TestCalc(unittest.TestCase):
    
#    def test_add(self):
#        self.assertEqual(calc.add(10, 5), 15)
#        self.assertEqual(calc.add(-1, 1), 0)
#        self.assertRaises(ValueError, calc.divide, 10, 0)

#if __name__ == '__main__':
#    unittest.main()
    
