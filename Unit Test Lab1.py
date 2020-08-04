import unittest
import Lab1CNYT
import math

class TestLab1CNYT(unittest.TestCase):
    
    def test_suma(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(Lab1CNYT.suma(c1,c2), [4,6])

    def test_resta(self):
        c1 = [3,4]
        c2 = [1,2]
        self.assertEqual(Lab1CNYT.resta(c1,c2), [2,2])

    def test_producto(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(Lab1CNYT.producto(c1,c2), [-5,10])

    def test_division(self):
        c1 = [1,2]
        c2 = [3,4]
        self.assertEqual(Lab1CNYT.division(c1,c2), [0.44,0.08])

    def test_modulo(self):
        c1 = [1,2]
        self.assertEqual(Lab1CNYT.modulo(c1), math.sqrt(5))

    def test_cart_pol(self):
        c1 = [1,1]
        self.assertEqual(Lab1CNYT.cart_pol(c1),[1.4142135623730951, 45.0])

    def test_pol_cart(self):
        c1 = [1.4142135623730951, 45.0]
        self.assertEqual(Lab1CNYT.pol_cart(c1),[1,1])

    def test_fase(self):
        c1 = [1,2]
        self.assertEqual(Lab1CNYT.fase(c1),63.43494882292201)
        
if __name__ == '__main__':
    unittest.main()

