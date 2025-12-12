import json
import os

# =============================================================================
# DADOS (BIBLIOTECA DE JOGOS)
# Agrupamos tudo em um único dicionário para facilitar a busca e expansão.
# =============================================================================

BIBLIOTECA_JOGOS = {
    "hollow knight": {
        "nome_formatado": "Hollow Knight",
        "conquistas": {
            "1": "Falsidade Derrotada", "2": "Homenagem às Formigas", "3": "Irmãs da Batalha",
            "4": "Acabando com o Traidor", "5": "Observador no Abismo", "6": "Domador de Almas",
            "7": "Mestre das Almas", "8": "Portador do Sonho", "9": "Despertar do Sonho",
            "10": "Herói de Hallownest", "11": "Coração Vazio", "12": "A Radiância",
            "13": "Verdade", "14": "Amigo dos Mineiros", "15": "Guardião Derrotado",
            "16": "O Coletor", "17": "Traidor Lorde", "18": "Defensor do Esterco",
            "19": "Uumuu", "20": "Cavaleiro da Colmeia", "21": "Orou & Mato",
            "22": "Cavaleiro das Sentinelas", "23": "Zote Derrotado", "24": "Princesa Grey Zote",
            "25": "O Amado Zote", "26": "Domador de Deuses", "27": "Deus da Guerra",
            "28": "Pantheon do Mestre", "29": "Pantheon do Artista", "30": "Pantheon do Sábio",
            "31": "Pantheon do Cavaleiro", "32": "Pantheon de Hallownest", "33": "Coração do Vazio",
            "34": "Ritual Completo", "35": "Evolução Completa", "36": "Mestre das Armas",
            "37": "Colecionador de Amuletos", "38": "Portador do Amuleto", "39": "Cartógrafo",
            "40": "Explorador", "41": "Caminho da Dor", "42": "Banimento da Trupe",
            "43": "Rei do Sonho", "44": "Cavaleiro Sombrio", "45": "Guardião do Coração",
            "46": "Amigo dos Sonhadores", "47": "Desafiante Perfeito", "48": "Testamento dos Deuses",
            "49": "Ascensão Divina", "50": "Mestre dos Amuletos", "51": "Guerreiro do Sonho",
            "52": "Escudo da Colmeia", "53": "Marcha do Mantis", "54": "Fúria do Caído",
            "55": "Espírito Vingativo", "56": "Espectro Uivante", "57": "Mergulho Desolador",
            "58": "Escuridão Descendente", "59": "Corte Ciclone", "60": "Grande Corte",
            "61": "Corte Avassalador", "62": "Sopro Sombrio", "63": "Final Verdadeiro"
        }
    },
    "elden ring": {
        "nome_formatado": "Elden Ring",
        "conquistas": {
            "1": "Elden Lord", "2": "Era das Estrelas", "3": "Senhor da Chama Frenética",
            "4": "Margit, o Agouro Caído", "5": "Godrick, o Enxertado", "6": "Lobo Vermelho de Radagon",
            "7": "Rennala, Rainha da Lua Cheia", "8": "Dragão Smarag", "9": "Radahn, o Flagelo das Estrelas",
            "10": "Rykard, Senhor da Blasfêmia", "11": "Godfrey, o Primeiro Lorde Prístino", "12": "Morgott, Rei dos Agouros",
            "13": "Gigante de Fogo", "14": "Maliketh, a Lâmina Negra", "15": "Godskin Duo",
            "16": "Hoarah Loux, Guerreiro", "17": "Radagon da Ordem Áurea", "18": "Besta Pristina de Elden",
            "19": "Malenia, a Lâmina de Miquella", "20": "Mohg, Senhor do Sangue", "21": "Dragão Lich Fortissax",
            "22": "Placidusax, Senhor Dragão", "23": "Espírito Ancestral", "24": "Espírito Ancestral Real",
            "25": "Avatar do Erdtree", "26": "Arma Lendária", "27": "Encantamento Lendário",
            "28": "Feitiçaria Lendária", "29": "Cinzas de Guerra Lendária", "30": "Talismã Lendário",
            "31": "Cinzas Espirituais Lendárias", "32": "Catedral de Mogh", "33": "Elevador de Dectus",
            "34": "Castelo Tempesvéu", "35": "A Capital Lyndell", "36": "Árvore de Miquella",
            "37": "Montanha dos Gigantes", "38": "Farum Azula em Ruínas", "39": "A Mesa-Redonda",
            "40": "A Runa da Morte", "41": "O Chamado da Chama", "42": "Restauração do Anel Prístino"
        }
    },
    "dark souls: remastered": {
        "nome_formatado": "Dark Souls: Remastered",
        "conquistas": {
            "1": "Derrote o Demônio do Asilo", "2": "Derrote Taurus Demon", "3": "Derrote Bell Gargoyles",
            "4": "Derrote Capra Demon", "5": "Derrote Gaping Dragon", "6": "Derrote Chaos Witch Quelaag",
            "7": "Derrote Iron Golem", "8": "Derrote Ornstein e Smough", "9": "Derrote Dark Sun Gwyndolin",
            "10": "Derrote Moonlight Butterfly", "11": "Derrote Great Grey Wolf Sif", "12": "Derrote Seath, o Imortal",
            "13": "Derrote Four Kings", "14": "Derrote Nito, Primeiro dos Mortos", "15": "Derrote Bed of Chaos",
            "16": "Derrote Demon Firesage", "17": "Derrote Centipede Demon", "18": "Derrote Pinwheel",
            "19": "Derrote Crossbreed Priscilla", "20": "Derrote Stray Demon", "21": "Derrote Gwyn, Lorde das Cinzas",
            "22": "Conecte o Fogo", "23": "Deixe o Fogo Apagar", "24": "Obtenha Arma de Fogo",
            "25": "Obtenha Arma Divina", "26": "Obtenha Arma Oculta", "27": "Todas as Armas Raras",
            "28": "Todos os Milagres", "29": "Todas as Magias", "30": "Todas as Piromancias",
            "31": "Todos os Milagres Ocultos", "32": "Todos os Feitiços Ocultos", "33": "Reforço Máximo de Arma Normal",
            "34": "Reforço Máximo de Arma Divina", "35": "Reforço Máximo de Arma de Fogo",
            "36": "Reforço Máximo de Arma Oculta", "37": "Juramento da Luz Solar", "38": "Juramento dos Darkwraith",
            "39": "Juramento do Caçador da Floresta", "40": "Juramento da Servidora do Caos",
            "41": "Juramento do Caminho do Dragão"
        }
    },
    "batman arkham asylum": {
        "nome_formatado": "Batman: Arkham Asylum",
        "conquistas": {
            "1": "Platinum Trophy", "2": "World's Greatest Detective", "3": "Perfect Knight",
            "4": "Born Free", "5": "Recurring Nightmare", "6": "Freeflow Combo 20", "7": "Freeflow Combo 40",
            "8": "Zsasz Cut Down To Size", "9": "Mano-a-Mano", "10": "Cryptic Investigator",
            "11": "Lateral Thinker", "12": "Mystery Solver", "13": "Conundrum Cracker",
            "14": "Mental Athlete", "15": "Riddle Resolver", "16": "Crack The E Nigma",
            "17": "Night Glider", "18": "Freeflow Perfection", "19": "Invisible Predator",
            "20": "Flawless Freeflow Fighter", "21": "Shocking Rescue", "22": "Malpractice Needs More Practice",
            "23": "Baneful Payback", "24": "Arkham Analyst", "25": "Crocodile Tears",
            "26": "Freakshow Rodeo", "27": "Predator Bronze", "28": "Resist The Fear",
            "29": "Catch!", "30": "Leave No Man Behind", "31": "Party Pooper", "32": "Freeflow Combo 5",
            "33": "Freeflow Combo 10", "34": "Rope-a-Dope-a-Dope", "35": "Predator Silver",
            "36": "Just What The Doctors Ordered", "37": "Daydreamer", "38": "Double Trouble",
            "39": "Solitary Confinement", "40": "Breaking and Entering", "41": "Predator Gold",
            "42": "Poisoned Ivy", "43": "Biggest Bang", "44": "Big Bang", "45": "Bigger Bang"
        }
    },
    "outlast 2": {
        "nome_formatado": "Outlast 2",
        "conquistas": {
            "1": "Omnipotent", "2": "Born Again", "3": "Sanctified", "4": "Preacher",
            "5": "Saint", "6": "Prophet", "7": "Messiah", "8": "Asahel",
            "9": "What God Has Joined", "10": "Babylon", "11": "Hang in there, Baby",
            "12": "Be Thou Clean", "13": "Golgatha", "14": "Sancti Sepulchri",
            "15": "Let No Man Put Asunder", "16": "Revelations", "17": "Bible Study",
            "18": "Ordination", "19": "The Road to Damascus", "20": "The Apostle Paul",
            "21": "Heal the Sick", "22": "Thoroughly Baptized", "23": "Them That Hath Ears",
            "24": "Slip and Slide", "25": "Proper Penance"
        }
    }
}

ARQUIVO_USUARIO = "progresso_usuario.json"
ARQUIVO_SUGESTOES = "sugestoes.txt"

# =============================================================================
# FUNÇÕES DE GERENCIAMENTO DE ARQUIVOS
# =============================================================================

def carregar_progresso():
    """Carrega o progresso do usuário do arquivo JSON. Se não existir, cria um novo."""
    if os.path.exists(ARQUIVO_USUARIO):
        try:
            with open(ARQUIVO_USUARIO, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de progresso. Criando novo.")
            return {}
    return {}

def salvar_progresso(dados):
    """Salva o progresso atual no arquivo JSON."""
    with open(ARQUIVO_USUARIO, "w") as f:
        json.dump(dados, f, indent=4)
    print("\n[!] Progresso salvo com sucesso!")

def salvar_sugestao_arquivo(sugestao):
    """Salva a sugestão do usuário em um arquivo de texto."""
    with open(ARQUIVO_SUGESTOES, "a") as f:
        f.write(f"{sugestao}\n")
    print("\n[!] Sugestão registrada no arquivo de sugestões. Obrigado!")

# =============================================================================
# FUNÇÕES DE LÓGICA DO JOGO
# =============================================================================

def exibir_conquistas(nome_jogo, dados_jogo):
    """Exibe todas as conquistas disponíveis para o jogo selecionado."""
    print(f"\n--- Todas as conquistas de {dados_jogo['nome_formatado']} ---")
    for key, value in dados_jogo['conquistas'].items():
        print(f"[{key}] {value}")

def gerenciar_conquistas_usuario(chave_jogo, dados_jogo, progresso_usuario):
    """Permite ao usuário marcar conquistas como concluídas."""
    nome_formatado = dados_jogo['nome_formatado']
    
    # Se o jogo não existe no progresso do usuário, inicializa uma lista vazia
    if chave_jogo not in progresso_usuario:
        progresso_usuario[chave_jogo] = []

    print(f"\n--- Gerenciar Conquistas: {nome_formatado} ---")
    print("Digite o NÚMERO da conquista para marcar/desmarcar (ou 'sair' para voltar).")
    
    while True:
        conquistas_feitas = progresso_usuario[chave_jogo]
        print(f"\nVocê já completou {len(conquistas_feitas)} de {len(dados_jogo['conquistas'])} conquistas.")
        
        escolha = input("Número da conquista (ou 'ver' para listar todas): ").lower()
        
        if escolha == 'sair':
            break
        
        if escolha == 'ver':
            exibir_conquistas(chave_jogo, dados_jogo)
            continue

        if escolha in dados_jogo['conquistas']:
            nome_conquista = dados_jogo['conquistas'][escolha]
            
            if escolha in conquistas_feitas:
                print(f"Removendo: {nome_conquista}")
                conquistas_feitas.remove(escolha)
            else:
                print(f"Adicionando: {nome_conquista}")
                conquistas_feitas.append(escolha)
            
            # Salva automaticamente após cada alteração
            progresso_usuario[chave_jogo] = conquistas_feitas
            salvar_progresso(progresso_usuario)
        else:
            print("Número de conquista inválido. Digite 'ver' para consultar os números.")

def comparar_progresso(chave_jogo, dados_jogo, progresso_usuario):
    """Mostra quais conquistas o usuário AINDA NÃO completou."""
    if chave_jogo not in progresso_usuario:
        print(f"\nVocê ainda não registrou nenhuma conquista para {dados_jogo['nome_formatado']}.")
        return

    feitas = set(progresso_usuario[chave_jogo])
    total_ids = set(dados_jogo['conquistas'].keys())
    
    faltantes = total_ids - feitas
    
    if not faltantes:
        print(f"\nPARABÉNS! Você platinou {dados_jogo['nome_formatado']}!")
    else:
        print(f"\n--- Faltam {len(faltantes)} conquistas para a platina ---")
        for id_conq in sorted(faltantes, key=lambda x: int(x)):
            print(f"[{id_conq}] {dados_jogo['conquistas'][id_conq]}")

# =============================================================================
# MENU PRINCIPAL
# =============================================================================

def main():
    progresso_usuario = carregar_progresso()
    
    while True:
        print("\n" + "="*50)
        print("RASTREADOR DE PLATINAS")
        print("="*50)
        
        # Cria uma lista formatada dos jogos disponíveis
        lista_nomes = [dados['nome_formatado'] for dados in BIBLIOTECA_JOGOS.values()]
        print(f"Jogos disponíveis: {', '.join(lista_nomes)}")

        escolha_usuario = input("\nQual jogo deseja acessar? (ou 'sair'): ").lower().strip()

        if escolha_usuario == "sair":
            print("Até a próxima caçada!")
            break

        # Verifica se o jogo existe no nosso dicionário
        if escolha_usuario in BIBLIOTECA_JOGOS:
            dados_jogo = BIBLIOTECA_JOGOS[escolha_usuario]
            
            while True:
                print(f"\n--- Menu: {dados_jogo['nome_formatado']} ---")
                print("1. Ver todas as conquistas")
                print("2. Gerenciar minhas conquistas (Salvar/Remover)")
                print("3. Ver o que falta para a Platina (Comparar)")
                print("4. Voltar ao menu principal")
                
                try:
                    opcao = int(input("Escolha uma opção: "))
                    
                    if opcao == 1:
                        exibir_conquistas(escolha_usuario, dados_jogo)
                    elif opcao == 2:
                        gerenciar_conquistas_usuario(escolha_usuario, dados_jogo, progresso_usuario)
                    elif opcao == 3:
                        comparar_progresso(escolha_usuario, dados_jogo, progresso_usuario)
                    elif opcao == 4:
                        break
                    else:
                        print("Opção inválida.")
                except ValueError:
                    print("Por favor, digite apenas números.")
        
        else:
            print("\nInfelizmente esse jogo não está na biblioteca.")
            if input("Deseja fazer uma sugestão (sim/não)? ").lower() == "sim":
                sugestao = input("Qual jogo devemos adicionar? ")
                salvar_sugestao_arquivo(sugestao)

if __name__ == "__main__":
    main()