from cryptographyFramework import *

initializeWrite()
user = "Fulano"
password = "1234"
encryptedText = encryptMessage(user, password, "Minha mensagem secreta!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Minha segunda mensagem secreta!")
saveNewLine(encryptedText)

