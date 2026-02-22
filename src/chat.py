from search import search_prompt

def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return

    print("Digite 'sair' ou 'exit' para encerrar.")
    print("-" * 60)
    print()    
    while True:
        print("Faça sua pergunta:")
        question = input("\nPERGUNTA: ").strip()   
        
        if question.lower() in ['sair', 'exit', 'quit', 'q']:
            print("\nEncerrando chat!")
            break

        if not question:
            print("Por favor, digite uma pergunta válida.\n")
            continue  
        
        print("\n🔍 Buscando resposta...\n")
        resp = chain.invoke(question)

        print(f"RESPOSTA: {resp}")
        print("\n" + "-" * 60 + "\n")


if __name__ == "__main__":
    main()