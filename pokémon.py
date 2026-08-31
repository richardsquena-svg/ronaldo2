import random
class pokemon:
  #Construtor da classe
  def_init_(self, nome, vida, ataque):
  self.nome=nome
  self.vida=vida
  self.ataque=ataque
  def ataque(self, inimigo):
    dano=random.randint(self, ataque // 2, self, ataque)
    print(self.nome, "atacou", inimigo.nome)
    print("dano", dano)
    inimigo.vida=inimigo.vida-dano
    if inimigo.vida < 0:
      inimigo.vida= 0
      print("vida de", inimigo.nome, ":", inimigo.vida)
      print()
      pikachu=pokemon("pikachu", 100, 30)
      charmander=pokemon("charmander", 110, 25)
      #batalha
      while pikachu.vida > 0 and charmandder.vida > 0:
        pikachu.atacar(charmander)
        if charmander.vida <= 0:
          print("charmander foi derrotado!")
          print("pikachu venceu!")
          break
          charmander.atacar(pikachu)
          if pikachu.vida <= 0:
            print("pikachu foi derrotado!")
            print("charmander venceu!")
            break
