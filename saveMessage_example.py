from cryptographyFramework import *

initializeWrite()
user = "Matue"
password = "30praum"
encryptedText = encryptMessage(user, password, "Foda-se o Hype, man, eu que sou o Hype")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "To suave não quero diploma")
saveNewLine(encryptedText)

