import os

class Analisador:
    def __init__(self):
        self.caminho = ""
        
        self.iniciar()

    def limpa_terminal(self):
        """Limpa o terminal de acordo com o sistema operacional."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def iniciar(self):
        """Inicializa o sistema de análise de dados."""
        print(f"==================================\n"
               " Analise de dados do INEP por CSV \n"
               "==================================\n")

        arquivo = input(f"Digite o nome do arquivo CSV: ")

        try: 
            self.caminho = f"data/{arquivo}.csv";

            if not os.path.exists(self.caminho):
                raise FileNotFoundError()

            print(f"\nArquivo '{arquivo}' selecionado!\n")

            print("[1] - Analisar o arquivo")
            print("[2] - Visualizar dashboard")
            print("[3] - Executar tudo")
            print("[4] - Limpar dados")
            print("[5] - Sair\n")

            opcao = input("O que deseja fazer? ")

            match opcao: 
                case "1":
                    self.limpa_terminal()
                    self.analisar_arquivo()
                case "2":
                    print("Limpar dados selecionado!")
                case "3":
                    print("Visualizar dashboard selecionado!")
                case "4":
                    print("Executar tudo selecionado!")
                case "5":
                    print("Saindo do programa...")
                case _:
                    print("Opção inválida. Por favor, escolha uma opção válida.")

        except FileNotFoundError:
            print(f"\nArquivo '{arquivo}' não encontrado. Verifique o nome e tente novamente.\n")

    def analisar_arquivo(self):
        """Função para analisar o arquivo CSV."""
        print("Analisando o arquivo...")

Analisador()