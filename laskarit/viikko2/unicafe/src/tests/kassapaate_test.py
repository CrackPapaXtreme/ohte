import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
        self.maksukortti=Maksukortti(1000)
    
    def test_tarkista_init(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset, self.kassapaate.maukkaat,0)

    def test_kateisosto_maukkaat_ja_edulliset_ja_lkm_muuttuu(self):
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,(100240))
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,(100640))
        
    def test_kateinen_ei_riita_kassa_pysyy_samana(self):    
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset,0)
        self.assertEqual(self.kassapaate.maukkaat,0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100),100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100),100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,(100000))
    
    def test_maksukortilla_jos_tarpeeksi_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 3.60 euroa")
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        self.assertEqual(self.kassapaate.maukkaat,self.kassapaate.edulliset,1)
        self.assertEqual(self.kassapaate.kassassa_rahaa,(100000))

    def test_maksukortilla_jos_ei_tarpeeksi_rahaa(self):
        self.maksukortti.ota_rahaa(900)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),False)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,100)
        self.assertEqual(self.kassapaate.kassassa_rahaa,(100000))

    def test_kortille_lataaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 20.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa,101000)
        self.assertEqual(self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1),None)