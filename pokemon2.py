import random

# =========================================================
# Aula de Laboratório - Batalha Pokemon com Métodos (Python)
# Versão 3 (AVANÇADA): sobre a v2 (escolha de Pokemon +
# combustível por magia), adicionamos:
#   1) TIPOS e FRAQUEZAS: cada Pokemon tem um tipo, e golpes do
#      tipo vantajoso causam dano extra (ex: Fogo é super efetivo
#      contra Planta). O menu de escolha já mostra a fraqueza de
#      cada Pokemon antes de você decidir.
#   2) Pokemon adversário sorteado a cada partida (não só uma vez).
#   3) Loop "jogar novamente": ao final da batalha, o jogo pergunta
#      se você quer jogar outra partida, sem precisar reiniciar o
#      programa.
# =========================================================


# Tabela de vantagens de tipo: chave = tipo do golpe, valor = tipo
# que esse golpe é super efetivo contra (causa 50% de dano a mais).
TABELA_VANTAGENS = {
    "Fogo": "Planta",
    "Planta": "Água",
    "Água": "Fogo",
    "Elétrico": "Água",
}


Class Magia:
    """Representa um golpe/magia que um Pokemon pode usar."""
    def __init__(self, nome, poder, tipo, combustivel_maximo):
        self.nome = nome
        self.poder = poder
        self.tipo = tipo
        self.combustivel_maximo =  combustivel_maximo
        self.combustivel_atual = combsustivel_atual

    # Método sem retorno: monta o texto "3/5" para mostrar no menu
    def status_combustivel(self):
        if self.tem_combustivel
