class Aluno():
   def __init__(self, nome):
      self.nome = nome

class Aluno(Aluno):
   def __init__(self):
      self.nome = None


aluno = Aluno()
print(aluno.nome)

