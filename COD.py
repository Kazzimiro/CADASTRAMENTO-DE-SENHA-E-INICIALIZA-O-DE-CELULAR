# Cadastro da senha
senha_correta = input("Cadastre uma senha numérica de 4 dígitos: ")
while len(senha_correta) != 4 or not senha_correta.isdigit():
    print("Senha inválida. A senha deve conter exatamente 4 dígitos numéricos.")
    senha_correta = input("Cadastre uma senha numérica de 4 dígitos: ")
print("Senha cadastrada com sucesso!\n")

# Inicialização do celular com tentativas de senha
print("Bem-vindo ao celular!\n")
for tentativa in range(1, 4):  # 3 tentativas no total
    senha_inserida = input("Digite sua senha numérica: ")
    
    if senha_inserida == senha_correta:
        print("Bem-vindo.")
        break
    else:
        tentativas_restantes = 3 - tentativa
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você ainda tem {tentativas_restantes} tentativa(s) restante(s).\n")
        else:
            print("Senha incorreta. Seu celular foi bloqueado.")
            break
