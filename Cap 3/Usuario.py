# Criar um programa cadastroUsuario.py contendo os seguintes dados: nome, idade, cpf, identidade, nacionalidade, naturalidade, endereço,
# sexo, time de futebol e profissão. O mesmo deve ter tres saidas, uma pessoal (nome, idade, time de futebol) outra profissional
# nome, identidade, cpf e profissao) e por ultima, uma completa exibindo todos os dados.

print("INSIRA SEUS DADOS CONFORME FOR SOLICITADO")
Nome = input("Nome: ")
Idade = int(input("Idade: "))
CPF = int(input("CPF: "))
Identidade = int(input("Identidade: "))
Nacionalidade = input("Nacionalidade ")
Naturalidade = input("Naturalidade: ")
Endereço = input("Endereço: ")
Sexo = input("Sexo: ")
TimeFutebol = input("Seu time do coração: ")
Profissao = input("Profissão: ")

print("Dados pessoais: \n" "Nome:    %s \n" "Idade:   %s anos \n" "Torce para o %s \n" % (Nome, Idade, TimeFutebol))
print("Dados profissionais: \n" "Nome:        %s \n" "RG:          %d \n" "CPF:         %d \n" "Profissão:   %s \n" % (Nome, Identidade, CPF, Profissao ))
print("Dados completos: \n""Nome:            %s \n""Idade:           %d anos \n""CPF:             %d \n""RG:              %d \n""Nacionalidade:   %s \n"
      "Naturalidade:    %s \n""Endereço:        %s \n""Sexo:            %s \n""Torce para o %s \n"
      "Trabalha como %s \n" % (Nome, Idade, CPF, Identidade, Nacionalidade, Naturalidade, Endereço, Sexo, TimeFutebol, Profissao))