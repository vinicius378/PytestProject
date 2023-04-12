
import re

def first_letter(usuario):
    if usuario[0].isupper():
        return True 
    else:
        return False

def especial(usuario):
    padrao = "^[a-zA-Z0-9_\s]*$"
    if re.match(padrao, usuario):
        return True 
    else:
        return False

def espaco(usuario):
    if ' ' in usuario:
        return False 
    else:
        return True 

def tamanho(usuario):
    if len(usuario) <= 30:
       return True 
    else:
        return False 

def validar_usuario(usuario):
    erros = []
    if not first_letter(usuario):
        erros.append("A primeira letra deve ser maiúscula.")
    if not especial(usuario):
        erros.append("A string possui caracteres especiais.")
    if not espaco(usuario):
        erros.append("Há um espaço na string.")
    if not tamanho(usuario):
        erros.append("O usuário excede o número de 30 caracteres.")
        
    if len(erros) == 0:
        print("Usuário salvo!!")
        return True 
    else:
        print("Erro. O usuário é inválido por causa dos seguintes motivos:")
        for erro in erros:
            print("- " + erro)
        return False 