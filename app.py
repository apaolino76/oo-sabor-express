from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')

restaurante_praca.adicionar_bebida_no_cardapio(bebida_suco)
restaurante_praca.adicionar_prato_no_cardapio(prato_paozinho)

# restaurante_praca.receber_avaliacao('Gui', 10)
# restaurante_praca.receber_avaliacao('Lais', 8)
# restaurante_praca.receber_avaliacao('Emy', 5)

# restaurante_mexicano = Restaurante('mexican food', 'Mexicana')
# restaurante_mexicano.alternar_estado()
# restaurante_japones = Restaurante('Japa', 'Japonesa')

def main():
    # Restaurante.listar_restaurantes()
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()