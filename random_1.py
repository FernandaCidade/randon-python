import random

def main():
    # Fornece os limites de um intervalo de números e deixa o usuário adivinhar o número do computador até a suposição estiver correta.

    menor = int(input("Entre com o menor número: "))
    maior = int(input("Entre com o maior número: "))

    meuNumero = random.randint(menor,maior)

    count = 0

    while True:
        count += 1 
        numUsuario = int(input("Entre com seu chute: "))

        if numUsuario < meuNumero: 
            print("Muito pouco")
        
        elif numUsuario > meuNumero:
            print ("Muito longe")
        
        else: 
            print("Você conseguiu em ", count, " Tentativas! Apenas!")
            break



if __name__ == "__main__": 
        main()