import re 

def lon(senha):
    if len(senha)<=10:
        print("A senha deve ter mais de 10 caracteres")
        return False 
    else:
        return True 

def esp(senha):
    padrao = "^[a-zA-Z0-9_]*$"
    if re.match(padrao, senha):
        print("Erro. A string não possui caracteres especiais.")
        return False 
    else:
        return True 

def numero(senha):
    ca = False
    for can in senha:
        if can.isdigit():
            ca = True
            break
    if not ca:
        print("A senha deve conter ao menos um número")
        return False
    else:
        return True

def verifica_letras(senha):
    tem_maiuscula = False
    tem_minuscula = False

    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        elif letra.islower():
            tem_minuscula = True

    if tem_maiuscula and tem_minuscula:
        return True
    else:
        return False

def func(senha):
    if verifica_letras(senha):
        print("A senha foi salva!!!")
        return True 
    else:
        print("A senha deve conter ao menos uma letra maiúscula e uma letra minúscula.")
        return False 

def test_lon():
    assert lon("1234567890") == False
    assert lon("12345678901") == True
    assert lon("12345678901234567890") == True

def test_esp():
    assert esp("senha") == False
    assert esp("senha@") == True
    assert esp("Senha@1234") == True

def test_numero():
    assert numero("senha") == False
    assert numero("Senha") == False
    assert numero("Senha1") == True

def test_verifica_letras():
    assert verifica_letras("senha") == False
    assert verifica_letras("SENHA") == False
    assert verifica_letras("Senha") == True
    assert verifica_letras("sEnHa") == True

def test_func():
    assert func("senha") == False
    assert func("SENHA") == False
    assert func("Senha") == False
    assert func("Senha1") == True
    assert func("Senha@1234") == True

if __name__ == '__main__':
    senha = input("Insira sua senha: ")
    test_lon()
    test_esp()
    test_numero()
    test_verifica_letras()
    test_func()
