# Funções

def maior2(x,y):
    if x > y:
        return x
    else:
        return y

def maior3(x,y,z):
    a = maior2(x,y)
    return maior2(a,z)

def maior4(x,y,z,h):
    a = maior3(x,y,z)
    return maior2(a,h)

def maior5(a,b,c,d,e):
    x = maior4(a,b,c,d)
    return maior2(x,e)

# Testes

import unittest

class TestStringMethods(unittest.TestCase):
    def test_2(self):
        self.assertEqual(maior2(1,2),2)
        self.assertEqual(maior2(4,2),4)
        self.assertEqual(maior2(-1,-2),-1)
        self.assertEqual(maior2(-1,2),2)

    def test_3(self):
        self.assertEqual(maior3(1,2,3),3)
        self.assertEqual(maior3(4,2,1),4)
        self.assertEqual(maior3(-1,-2,-3),-1)
        self.assertEqual(maior3(-1,2,1),2)

    def test_4(self):
        self.assertEqual(maior4(1,2,3,4),4)
        self.assertEqual(maior4(4,2,1,0),4)
        self.assertEqual(maior4(-1,-2,-3,-4),-1)
        self.assertEqual(maior4(-1,2,0,1),2)

    def test_5(self):
        self.assertEqual(maior5(1,2,3,4,5),5)
        self.assertEqual(maior5(4,2,1,0,1),4)
        self.assertEqual(maior5(-1,-2,-3,-5,-6),-1)
        self.assertEqual(maior5(-1,2,5,6,9),9)    
 
# Chamadas

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()