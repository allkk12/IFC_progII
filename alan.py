class Mobilia:
    def _init_ (self, nome= " ", função= " ", material= " ", quarto= None):
        self.nome= nome
        self.função= função
        self.material= material
        self.quarto= quarto

    def _repr_ (self):
        s= self.nome + "," + self.função + "," + self.material
        if self.quarto:
            s += str(self.quarto)
        return s
 
class Quarto:
    def _init_ (self, nome= " ", dimensões= " "):
        self.nome= nome
        self.dimensões= dimensões


class Casa:
    def _init_ (self, formato= " ", quarto= None):
        self.formato= formato
        self.quarto= quarto

    def _repr_ (self):
        q= self.quarto
        s1= self.formato + "," + [q]

t= Mobilia(nome="sofá", função="descanso", material="tecido")
print(t)

t1= Quarto(nome="banheiro", dimensões="5x6")
print(t1)

t2= Casa(formato="quadrado")
print(t2)