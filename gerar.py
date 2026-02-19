import pyotp
import qrcode

# 1. Gerar uma chave secreta aleatória para o usuário (salve isso no seu Banco de Dados!)
secret = pyotp.random_base32()
print(f"Chave Secreta do Usuário: {secret}")

# 2. Criar o link que o Authy/Google Authenticator entende
auth_url = pyotp.totp.TOTP(secret).provisioning_uri(
    name="usuario@email.com",
    issuer_name="MeuSiteInc"
)

# 3. Gerar a imagem do QR Code
img = qrcode.make(auth_url)
img.save("meu_2fa_qrcode.png")