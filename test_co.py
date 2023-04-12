from app import*
from senha import*

def test_user ():
    assert True == first_letter("Alex")
    assert False == first_letter("alex")
    assert True == especial("Alex")
    assert False == especial("@Alex")
    assert True == espaco("Alex")
    assert False == espaco("Ale x")
    assert True == tamanho("Alex")
    assert False ==tamanho("Alexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
def test_i():
    assert True == lon("@Matue30praum")
    assert False == lon("@M30pra")
    assert True == esp("@Matue30praum")
    assert False == esp("Matue30praum")
    assert True == numero("@Matue30praum")
    assert False == numero("@Matueiiiipraum")
    assert True == verifica_letras("@Matue30praum")
    assert False == verifica_letras("@matue30praum")
    assert True == func("@Matue30praum")
    assert False == func("@matue30praum")


