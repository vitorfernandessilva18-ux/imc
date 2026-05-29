def calcular_imc_metrico(peso, altura):
    # Se o usuário digitar a altura em centímetros (ex: 175), corrige para metros (1.75)
    if altura > 3:
        altura /= 100
    
    if peso <= 0 or altura <= 0:
        return None
        
    return peso / (altura ** 2)


def calcular_imc_imperial(libras, pes, polegadas):
    # Converte libras para kg (1 lb = 0.45359237 kg)
    peso_kg = libras * 0.45359237
    
    # Converte pés e polegadas para metros (1 polegada = 0.0254 metros)
    total_polegadas = (pes * 12) + polegadas
    altura_m = total_polegadas * 0.0254
    
    if peso_kg <= 0 or altura_m <= 0:
        return None
        
    return peso_kg / (altura_m ** 2)


def obter_categoria_e_cor(imc):
    # Códigos de cor ANSI para o terminal ficar bonito
    RESET = "\033[0m"
    AZUL = "\033[36m"
    VERDE = "\033[32m"
    LARANJA = "\033[33m"
    VERMELHO = "\033[31m"

    if imc < 18.5:
        return f"{AZUL}Abaixo do peso{RESET}"
    elif imc < 25:
        return f"{VERDE}Peso normal{RESET}"
    elif imc < 30:
        return f"{LARANJA}Sobrepeso{RESET}"
    else:
        return f"{VERMELHO}Obesidade{RESET}"


def main():
    print("=" * 30)
    print("   CALCULADORA DE IMC GLOBAL   ")
    print("=" * 30)
    print("1 - Sistema Métrico (kg / metros)")
    print("2 - Sistema Imperial (libras / pés e pol)")
    
    opcao = input("\nEscolha o sistema de unidades (1 ou 2): ").strip()
    
    try:
        if opcao == "1":
            peso = float(input("Digite o peso (kg): "))
            altura = float(input("Digite a altura (ex: 1.75 ou 175): "))
            imc = calcular_imc_metrico(peso, altura)
            
        elif opcao == "2":
            libras = float(input("Digite o peso (Libras - lbs): "))
            pes = float(input("Digite os Pés (ft): "))
            polegadas = input("Digite as Polegadas (in) [pressione Enter para 0]: ").strip()
            polegadas = float(polegadas) if polegadas else 0.0
            
            imc = calcular_imc_imperial(libras, pes, polegadas)
        else:
            print("\nOpção inválida!")
            return

        if imc is None:
            print("\n[Erro] Os valores inseridos devem ser maiores que zero.")
            return

        categoria = obter_categoria_e_cor(imc)
        print("\n" + "-" * 30)
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {categoria}")
        print("-" * 30)

    except ValueError:
        print("\n[Erro] Por favor, digite apenas números válidos.")


if __name__ == "__main__":
    main()