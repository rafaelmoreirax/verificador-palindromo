import unicodedata

def normalizar(texto):
    # Remove acentos e caracteres especiais
    texto = ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )
    # Remove espaços e deixa minúsculo
    return ''.join(c.lower() for c in texto if c.isalnum())

def eh_palindromo(texto):
    texto_norm = normalizar(texto)
    return texto_norm == texto_norm[::-1]

def main():
    print("=== Verificador de Palíndromos ===")
    while True:
        entrada = input("Digite uma palavra ou frase (ou 'sair' para encerrar): ").strip()
        if entrada.lower() == 'sair':
            print("Até a próxima!")
            break
        if not entrada:
            print("Por favor, digite algo.")
            continue
        if eh_palindromo(entrada):
            print("✅ É um palíndromo!\n")
        else:
            print("❌ Não é um palíndromo.\n")

if __name__ == "__main__":
    main()
