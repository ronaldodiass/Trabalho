#Ronaldo Dias Benedito = 11231102442
#Antonio Pedro dos Reis Neto = 11231101959
#Arthur Andrade Rodrigues = 11231102696

import os
import time
import json

class Aluno:
    def __init__(self, idade=0, altura=0.0, peso=0.0, nome="", rgm=0):
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.nome = nome
        self.rgm = rgm

    def imc(self):
        resultado = self.peso / (self.altura * self.altura)
        if resultado >= 40.0:
            return "Obesidade classe III"
        elif resultado >= 35.0:
            return "Obesidade classe II"
        elif resultado >= 30.0:
            return "Obesidade classe I"
        elif resultado >= 25.0:
            return "Excesso de Peso"
        elif resultado >= 18.5:
            return "Peso Normal"
        else:
            return "Abaixo do peso normal"

    def serializar(self):
        dic = {
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura,
            "peso": self.peso,
            "rgm": self.rgm
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def atualizarJSON(self, texto_json):
        dic = json.loads(texto_json)
        self.nome = dic.get("nome", "")
        self.idade = dic.get("idade", 0)
        self.altura = dic.get("altura", 0.0)
        self.peso = dic.get("peso", 0.0)
        self.rgm = dic.get("rgm", 0)

class Professor:
    def __init__(self, matricula="", nome="", idade=0, altura=0.0):
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def Serializar(self):
        dic = {
            "matricula": self.matricula,
            "nome": self.nome,
            "idade": self.idade,
            "altura": self.altura
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def AtualizarJSON(self, texto_json):
        dic = json.loads(texto_json)
        self.matricula = dic.get("matricula", "")
        self.nome = dic.get("nome", "")
        self.idade = dic.get("idade", 0)
        self.altura = dic.get("altura", 0.0)

    def __str__(self):
        return f"Matrícula: {self.matricula}, Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}"

class Disciplina:
    def __init__(self, codigo="", nome="", cargaHoraria=0, turma=0, notaMinima=0.0):
        self.codigo = codigo
        self.nome = nome
        self.cargaHoraria = cargaHoraria
        self.turma = turma
        self.notaMinima = notaMinima

    def Serializar(self):
        dic = {
            "codigo": self.codigo,
            "nome": self.nome,
            "cargaHoraria": self.cargaHoraria,
            "turma": self.turma,
            "notaMinima": self.notaMinima
        }
        texto_json = json.dumps(dic, indent=3)
        return texto_json

    def Deserializar(self, texto_json):
        dic = json.loads(texto_json)
        self.codigo = dic.get("codigo", "")
        self.nome = dic.get("nome", "")
        self.cargaHoraria = dic.get("cargaHoraria", 0)
        self.turma = dic.get("turma", 0)
        self.notaMinima = dic.get("notaMinima", 0.0)

class ModeloAcademico:
    def __init__(self):
        self.listaAlunos = []
        self.listaProfessores = []
        self.listaDisciplinas = []
        self.opcao = 1
        self.RecuperarAlunos()
        self.RecuperarProfessores()
        self.RecuperarDisciplinas()

    def SalvarAlunos(self):
        lista = [a.serializar() for a in self.listaAlunos]
        with open("alunos.json", 'w') as arquivo:
            json.dump(lista, arquivo, indent=3)
        print("Alunos salvos!")

    def RecuperarAlunos(self):
        self.listaAlunos.clear()
        try:
            with open("alunos.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    a = Aluno()
                    a.atualizarJSON(text)
                    self.listaAlunos.append(a)
        except FileNotFoundError:
            pass

    def SalvarProfessores(self):
        lista = [p.Serializar() for p in self.listaProfessores]
        with open("professores.json", 'w') as arquivo:
            json.dump(lista, arquivo, indent=3)
        print("Professores salvos!")

    def RecuperarProfessores(self):
        self.listaProfessores.clear()
        try:
            with open("professores.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    p = Professor()
                    p.AtualizarJSON(text)
                    self.listaProfessores.append(p)
        except FileNotFoundError:
            pass

    def SalvarDisciplinas(self):
        lista = [d.Serializar() for d in self.listaDisciplinas]
        with open("disciplinas.json", 'w') as arquivo:
            json.dump(lista, arquivo, indent=3)
        print("Disciplinas salvas!")

    def RecuperarDisciplinas(self):
        self.listaDisciplinas.clear()
        try:
            with open("disciplinas.json", 'r') as arquivo:
                lista_de_jsons_text = json.load(arquivo)
                for text in lista_de_jsons_text:
                    d = Disciplina()
                    d.Deserializar(text)
                    self.listaDisciplinas.append(d)
        except FileNotFoundError:
            pass
        
    def cadastrarAluno(self):
        idade = int(input("Digite a idade:"))
        altura = float(input("Digite a altura:"))
        peso = float(input("Digite o peso:"))
        nome = input("Digite o nome:")
        rgm = int(input("Digite o rgm:"))
        aluno = Aluno(idade, altura, peso, nome, rgm)
        self.listaAlunos.append(aluno)
        self.SalvarAlunos()
        return aluno


    def cadastrarProfessor(self):
        matricula = input("Digite a matrícula:")
        nome = input("Digite o nome:")
        idade = int(input("Digite a idade:"))
        altura = float(input("Digite a altura:"))
        professor = Professor(matricula, nome, idade, altura)
        self.listaProfessores.append(professor)
        self.SalvarProfessores()
        return professor

    def cadastrarDisciplina(self):
        codigo = input("Digite o código:")
        nome = input("Digite o nome:")
        cargaHoraria = int(input("Digite a carga horária:"))
        turma = int(input("Digite a turma:"))
        notaMinima = float(input("Digite a nota mínima:"))
        disciplina = Disciplina(codigo, nome, cargaHoraria, turma, notaMinima)
        self.listaDisciplinas.append(disciplina)
        self.SalvarDisciplinas()
        return disciplina

    def imprimirAlunos(self):
        print("|Alunos:")
        print("|Nome|Altura|Idade|Peso|RGM|")
        print("-------------------------------")
        for a in self.listaAlunos:
            print(a.nome, "|", a.idade, "|", a.altura, "|", a.peso, "|", a.rgm)
        print("-------------------------------")
        self.SalvarAlunos()

    def imprimirProfessores(self):
        print("|Professores:")
        print("|Matrícula|Nome|Idade|Altura|")
        print("-------------------------------")
        for p in self.listaProfessores:
            print(p.matricula, "|", p.nome, "|", p.idade, "|", p.altura)
        print("-------------------------------")
        self.SalvarProfessores()

    def imprimirDisciplinas(self):
        print("|Disciplinas:")
        print("|Código|Nome|Carga Horária|Turma|Nota Mínima|")
        print("-------------------------------")
        for d in self.listaDisciplinas:
            print(d.codigo, "|", d.nome, "|", d.cargaHoraria, "|", d.turma, "|", d.notaMinima)
        print("-------------------------------")
        self.SalvarDisciplinas()

    def Consulta_Peso(self):
        contador = 0
        for a in self.listaAlunos:
            if a.peso > 65:
                contador += 1
        print("Quantidade de alunos > 65 kg é: ", contador)
        for a in self.listaAlunos:
            if a.peso > 65:
                print("O aluno ", a.nome, " tem IMC: ", a.imc())
        self.SalvarAlunos()

    def removerAluno(self, rgm):
        for aluno in self.listaAlunos:
            if aluno.rgm == rgm:
                self.listaAlunos.remove(aluno)
                print(f"Aluno com RGM {rgm} removido.")
                self.SalvarAlunos()
                return
        print(f"Aluno com RGM {rgm} não encontrado.")
        self.SalvarAlunos()

    def removerProfessor(self, matricula):
        for professor in self.listaProfessores:
            if professor.matricula == matricula:
                self.listaProfessores.remove(professor)
                print(f"Professor com matrícula {matricula} removido.")
                self.SalvarProfessores()
                return
        print(f"Professor com matrícula {matricula} não encontrado.")
        self.SalvarProfessores()

    def removerDisciplina(self, codigo):
        for disciplina in self.listaDisciplinas:
            if disciplina.codigo == codigo:
                self.listaDisciplinas.remove(disciplina)
                print(f"Disciplina com código {codigo} removida.")
                self.SalvarDisciplinas()
                return
        print(f"Disciplina com código {codigo} não encontrada.")
        self.SalvarDisciplinas()

    def updateAluno(self, rgm):
        for aluno in self.listaAlunos:
            if aluno.rgm == rgm:
                print("Digite as novas informações do aluno:")
                aluno.idade = int(input("Nova idade:"))
                aluno.altura = float(input("Nova altura:"))
                aluno.peso = float(input("Novo peso:"))
                aluno.nome = input("Novo nome:")
                print(f"As informações do aluno com RGM {rgm} foram atualizadas.")
                self.SalvarAlunos()
                return
        print(f"Aluno com RGM {rgm} não encontrado.")
        self.SalvarAlunos()

    def updateProfessor(self, matricula):
        for professor in self.listaProfessores:
            if professor.matricula == matricula:
                print("Digite as novas informações do professor:")
                professor.nome = input("Novo nome:")
                professor.idade = int(input("Nova idade:"))
                professor.altura = float(input("Nova altura:"))
                print(f"As informações do professor com matrícula {matricula} foram atualizadas.")
                self.SalvarProfessores()
                return
        print(f"Professor com matrícula {matricula} não encontrado.")
        self.SalvarProfessores()

    def updateDisciplina(self, codigo):
        for disciplina in self.listaDisciplinas:
            if disciplina.codigo == codigo:
                print("Digite as novas informações da disciplina:")
                disciplina.nome = input("Novo nome:")
                disciplina.cargaHoraria = int(input("Nova carga horária:"))
                disciplina.turma = int(input("Nova turma:"))
                disciplina.notaMinima = float(input("Nova nota mínima:"))
                print(f"As informações da disciplina com código {codigo} foram atualizadas.")
                self.SalvarDisciplinas()
                return
        print(f"Disciplina com código {codigo} não encontrada.")
        self.SalvarDisciplinas()

def show_menu():
    
    print("|############################################################|")
    print("|                    OOP PYTHON                             | ")
    print("|############################################################|")
    print("")
    print("")
    print("1) Cadastrar Alunos")
    print("2) Imprimir Alunos")
    print("3) Consulta Alunos > 65 Kg:")
    print("4) Cadastrar Professor:")
    print("5) Imprimir Professores:")
    print("6) Cadastrar Disciplina:")
    print("7) Imprimir Disciplinas:")
    print("8) Remover Aluno:")
    print("9) Remover Professor:")
    print("10) Remover Disciplina:")
    print("11) Atualizar Aluno:")
    print("12) Atualizar Professor:")
    print("13) Atualizar Disciplina:")
    print("14) Sair")
    modelo.opcao = int(input("Qual é a sua opção? : "))

modelo = ModeloAcademico()

while modelo.opcao != 14:
    show_menu()

    if modelo.opcao == 1:
        modelo.cadastrarAluno()
        time.sleep(1)
    elif modelo.opcao == 2:
        modelo.imprimirAlunos()
        time.sleep(1)
    elif modelo.opcao == 3:
        modelo.Consulta_Peso()
        time.sleep(1)
    elif modelo.opcao == 4:
        modelo.cadastrarProfessor()
        time.sleep(1)
    elif modelo.opcao == 5:
        modelo.imprimirProfessores()
        time.sleep(1)
    elif modelo.opcao == 6:
        modelo.cadastrarDisciplina()
        time.sleep(1)
    elif modelo.opcao == 7:
        modelo.imprimirDisciplinas()
        time.sleep(1)
    elif modelo.opcao == 8:
        rgm = int(input("Digite o RGM do aluno a ser removido: "))
        modelo.removerAluno(rgm)
        time.sleep(1)
    elif modelo.opcao == 9:
        matricula = input("Digite a matrícula do professor a ser removido: ")
        modelo.removerProfessor(matricula)
        time.sleep(1)
    elif modelo.opcao == 10:
        codigo = input("Digite o código da disciplina a ser removida: ")
        modelo.removerDisciplina(codigo)
        time.sleep(1)
    elif modelo.opcao == 11:
        rgm = int(input("Digite o RGM do aluno a ser atualizado: "))
        modelo.updateAluno(rgm)
        time.sleep(1)
    elif modelo.opcao == 12:
        matricula = input("Digite a matrícula do professor a ser atualizado: ")
        modelo.updateProfessor(matricula)
        time.sleep(1)
    elif modelo.opcao == 13:
        codigo = input("Digite o código da disciplina a ser atualizada: ")
        modelo.updateDisciplina(codigo)
        time.sleep(1)
    elif modelo.opcao == 14:
        print("... SAINDO ... ")
        exit(0)
