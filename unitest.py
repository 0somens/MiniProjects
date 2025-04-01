import unittest
import numpy as np

def calcular_van(descInicial, tasaDesc, flujos):
    """Calcula el VAN con NumPy."""
    n = len(flujos)
    van = -descInicial + np.sum(np.array(flujos) / (1 + tasaDesc) ** np.arange(1, n + 1))
    return van

class TestVANCalculator(unittest.TestCase):

    def test_proyecto_rentable(self):
        van = calcular_van(10000, 0.10, [3000, 3500, 4000, 4500, 5000])
        self.assertGreater(van, 0, "El VAN debería ser positivo (Rentable).")

    def test_proyecto_no_rentable(self):
        van = calcular_van(15000, 0.12, [2000, 2500, 3000, 3500])
        self.assertLess(van, 0, "El VAN debería ser negativo (No Rentable).")

    def test_proyecto_indiferente(self):
        van = calcular_van(8500, 0.08, [2500, 3000, 3600])
        self.assertAlmostEqual(van, 0, delta=0.1, msg="El VAN debería ser cercano a 0 (Indiferente).")

if __name__ == "__main__":
    unittest.main()
