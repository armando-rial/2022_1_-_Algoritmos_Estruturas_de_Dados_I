from Cidade import Cidade
from Pessoa import Pessoa

c1 = Cidade("Porto Alegre")
#print("Cidade: ", c1.nome)
#c1.estado = "SC"

p1 = Pessoa("Adalto", "51 98765-4321", "Rua B", 2245.98, c1 )
#p1.salario = 2300.50
p1.cadastrar()

print("----------------------")

p2 = Pessoa()
p2.municipio = c1
p2.cadastrar()

c2 = Cidade("Florianópolis")
c2.estado = "SC"

p3 = Pessoa("Daniel", "48 22337788", "Av. A", 7500.0, c2)
p3.cadastrar()