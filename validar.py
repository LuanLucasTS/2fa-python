import pyotp

# Recupere a 'secret' que você salvou no banco de dados para esse usuário
user_secret = "ZVJRWXQAFRHU5HMWAZOZN6NFNBRZD4ET" # Exemplo

totp = pyotp.TOTP(user_secret)

# O código que o usuário digitou no seu site
codigo_digitado = input("Digite o código do seu app 2FA: ")

if totp.verify(codigo_digitado):
    print("Login autorizado! ✅")
else:
    print("Código inválido ou expirado. ❌")
