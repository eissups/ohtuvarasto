import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

        self.varasto2= Varasto(0, 3)

        self.varasto3= Varasto(1, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_uudella_varastolla_oikea_saldo(self):
        self.assertAlmostEqual(self.varasto.saldo, 0)

        self.assertAlmostEqual(self.varasto3.saldo, 0) 

        self.assertAlmostEqual(self.varasto2.saldo, 0)                                                                                    
            

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_nega(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)


    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(saatu_maara, 8) 

    def test_ottaminen_negaa(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0) 

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_teksti(self):
        varasto4 = Varasto(12, 3)
        
        varasto4.lisaa_varastoon(6)
        # varastossa pitäisi olla tilaa 12 - 3 - 6 eli 3
        self.assertAlmostEqual(str(varasto4), "saldo = 9, vielä tilaa 3")


               