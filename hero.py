class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        ataques = {
            'mago': 'magia',
            'guerreiro': 'espada',
            'monge': 'artes marciais',
            'ninja': 'shuriken'
        }
        ataque = ataques.get(self.tipo, 'ataque desconhecido')
        print(f'o {self.tipo} atacou usando {ataque}')

# Exemplo de uso
heroi1 = Heroi('Gandalf', 100, 'mago')
heroi1.atacar()

heroi2 = Heroi('Aragorn', 87, 'guerreiro')
heroi2.atacar()

heroi3 = Heroi('Master Roshi', 300, 'monge')
heroi3.atacar()

heroi4 = Heroi('Naruto', 17, 'ninja')
heroi4.atacar()
