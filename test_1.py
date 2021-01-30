#! /usr/bin/python3
import unittest
import krak
import random




class StringMethods(unittest.TestCase):

    def test_f0(self):
      self.assertTrue(True)

    def test_f1_1(self):
        w = krak.f1(0)
        self.assertEqual(w, 0)

    def test_f1_2(self):
        w = krak.f1(1)
        self.assertEqual(w, 1)

    def test_f1_3(self):
        w = krak.f1(2)
        self.assertEqual(w, 4)

    def test_f1_4(self):
        w = krak.f1(2, 1)
        self.assertEqual(w, 5)

    def test_f1_5(self):
        w = krak.f1(2, 3)
        self.assertEqual(w, 7)

    def test_f2_1(self):
        c = krak.f2('ala')
        self.assertEqual(c, 'a')

    def test_f2_2(self):
        c = krak.f2([1, 2, 3])
        self.assertEqual(c, 1)

    def test_f2_3(self):
        c = krak.f2([])
        self.assertEqual(c, 'BUUUM')

    def test_f3_1(self):
        s = krak.f3(1)
        self.assertEqual(s, 'jeden')

    def test_f3_2(self):
        s = krak.f3(2)
        self.assertEqual(s, 'dwa')

    def test_f3_3(self):
        s = krak.f3(3)
        self.assertEqual(s, 'trzy')

    def test_f3_4(self):
        s = krak.f3(random.choice(range(4,1000)))
        self.assertEqual(s, 'other')

    def test_t4_1(self):
        t = krak.f4('ala')
        self.assertEqual(t, 'ala ma kota')

    def test_t4_2(self):
        t = krak.f4('kot')
        self.assertEqual(t, 'kot ma kota')

    def test_t4_3(self):
        t = krak.f4('kot', 'psa')
        self.assertEqual(t, 'kot ma kota i psa')

    def test_t4_4(self):
        t = krak.f4('kot', 'mysz')
        self.assertEqual(t, 'kot ma kota i mysz')

    def test_f5_1(self):
        r = krak.f5(0)
        self.assertEqual(r,[])

    def test_f5_2(self):
        r = krak.f5(1)
        self.assertEqual(r,[0])

    def test_f5_3(self):
        r = krak.f5(2)
        self.assertEqual(r,[0, 1])

    def test_f5_4(self):
        r = krak.f5(7)
        self.assertEqual(r,[0, 1, 2, 3, 4, 5, 6])

    def test_f5_5(self):
        r = krak.f5(7, 2)
        self.assertEqual(r,[0, 2, 4, 6])

    def test_f5_6(self):
        r = krak.f5(17, 2)
        self.assertEqual(r,[0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_f5_7(self):
        r = krak.f5(17, 5)
        self.assertEqual(r,[0, 5, 10, 15])

    def test_f6_1(self):
        s = krak.f6(1, '*')
        self.assertEqual(s,'*')

    def test_f6_2(self):
        s = krak.f6(7, '*')
        self.assertEqual(s,'*******')

    def test_f7_1(self):
        t = krak.f7('ala')
        self.assertEqual(t, 'slowo')

    def test_f7_2(self):
        t = krak.f7(1)
        self.assertEqual(t, 'cyfra')

    # def test_f7_3(self):
    #     t = krak.f7(<taaag>)
    #     self.assertEqual(t, 'tag poczatkowy')

    def test_f8_1(self):
        c = krak.f8('kot', 'ala ma kota')
        self.assertEqual(c, True)

    def test_f8_2(self):
        c = krak.f8('pies', 'ala ma kota')
        self.assertEqual(c, False)

    def test_f9_1(self):
        n = krak.f9(1, 2)
        self.assertEqual(n, 'dodatnie')

    def test_f9_2(self):
        n = krak.f9(-1, -2)
        self.assertEqual(n, 'ujemne')

    def test_f9_3(self):
        n = krak.f9(-1, 1)
        self.assertEqual(n, 'roznych znakow')

    def test_f9_4(self):
        n = krak.f9(-1, 0)
        self.assertEqual(n, 'jest zero')

    def test_f10_1(self):
        e = krak.f10(1, 1)
        self.assertEqual(e, 'rowne')

    def test_f10_2(self):
        e = krak.f10(1, 2)
        self.assertEqual(e, 'rozne')





if __name__ == '__main__':
  unittest.main()
