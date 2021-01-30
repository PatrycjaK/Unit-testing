# Unit-testing
https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertIn

Unit tests exercises given by
lecturer

```
def test_f0(self):
    self.assertTrue(False)
```

---------------------------------------------------------------------

* f1 0 0
* f1 1 1
* f1 2 4
* f1 2,1  5
* f1 2,3  7
---------------------------------------------------------------------
* f2 ala a
* f2 [1,2,3] 1
* f2 [] BUUUUM
---------------------------------------------------------------------
* f3 1 jeden
* f3 2 dwa
* f3 3 trzy
* f3 random.choice(range(4,1000)) other
---------------------------------------------------------------------
* f4 ala "ala ma kota"
* f4 kot "kot ma kota"
* f4 kot,psa "kot ma kota i psa"
* f4 kot,mysz "kot ma kota i mysz"
---------------------------------------------------------------------
* f5 0 []
* f5 1 [0]
* f5 2 0,1
* f5 7 0,1,2,3,4,5,6
* f5 7,2 0,2,4,6
* f5 17,2 [0, 2, 4, 6, 8, 10, 12, 14, 16]
* f5 17,5 [0, 5, 10, 15]
---------------------------------------------------------------------
* f6 1,* "*"
* f6 7,* "*******"
---------------------------------------------------------------------
* f7  ala  slowo
* f7 1 cyfra
* f7 11111 liczba
* f7 11111 liczba_ze_znakiem
* f7 "Ala ma kota."  zdanie
* f7 <taaag>   tag poczatkowy
* f7 </taaag>   tag koncowy
---------------------------------------------------------------------
* f8 kot, ala ma kota  true
* f8 pies, ala ma kota  false
---------------------------------------------------------------------
* f9 1,2   dodatnie
* f9 -1,-2 ujemne
* f9 -1,1  roznych znakow
* f9 -1,0  jest zero
---------------------------------------------------------------------
* f10 1,1   rowne
* f10 1,2   rozne
