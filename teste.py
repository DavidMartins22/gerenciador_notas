# ==========================================
# --- test_notas.py ---
# ==========================================

import unittest

class TestSistemaNotas(unittest.TestCase):

    # Teste de aprovação normal
    def test_aprovacao(self):
        media = calcular_media([8.0, 7.0, 9.0])
        self.assertEqual(verificar_aprovacao(media), 'Aprovado')
    
    # Teste de reprovação normal
    def test_reprovacao(self):
        media = calcular_media([4.0, 5.0, 6.0])
        self.assertEqual(verificar_aprovacao(media), 'Reprovado')
    
    # Teste de lista vazia (edge case)
    def test_lista_vazia(self):
        media = calcular_media([])
        self.assertEqual(media, 0)
        
    # Teste de média mínima igual a zero
    def test_media_minima_zero(self):
        media = calcular_media([1.0, 2.0, 3.0])
        self.assertEqual(
            verificar_aprovacao(media, media_minima=0),
            'Aprovado'
        )

if __name__ == '__main__':
    unittest.main()