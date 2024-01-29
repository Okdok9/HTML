# Importando as bibliotecas necessárias
import requests
import json
import time
import random

# Definindo a url do jogo
url = "https://onabet.com/casino/game/2241819"

# Definindo a estratégia de aposta
valor_inicial = 10 # Valor inicial da aposta em reais
valor_maximo = 100 # Valor máximo da aposta em reais
valor_minimo = 5 # Valor mínimo da aposta em reais
momento_retirada = 2 # Momento de retirada da aposta em segundos

# Iniciando o loop principal
while True:
    # Fazendo a requisição ao site do jogo e obtendo os dados do avião
    resposta = requests.get(url)
    dados = json.loads(resposta.text)
    tempo_decolagem = dados["takeoff_time"] # Tempo de decolagem do avião em segundos
    tempo_pouso = dados["landing_time"] # Tempo de pouso do avião em segundos
    multiplicador = dados["multiplier"] # Multiplicador atual da aposta

    # Verificando se o avião está no ar
    if tempo_decolagem < time.time() < tempo_pouso:
        # Gerando um valor aleatório para a aposta entre o mínimo e o máximo
        valor_aposta = random.randint(valor_minimo, valor_maximo)

        # Enviando os dados da aposta para o site do jogo
        dados_aposta = {"bet_amount": valor_aposta, "game_id": 2241819}
        resposta_aposta = requests.post(url, data=dados_aposta)
        print(f"Apostei {valor_aposta} reais no avião.")

        # Esperando o momento de retirada da aposta
        time.sleep(momento_retirada)

        # Retirando a aposta do site do jogo
        dados_retirada = {"game_id": 2241819}
        resposta_retirada = requests.post(url, data=dados_retirada)
        print(f"Retirei a aposta no avião.")

        # Verificando o resultado da aposta
        resultado = json.loads(resposta_retirada.text)
        if resultado["status"] == "success":
            # A aposta foi bem sucedida
            valor_ganho = resultado["win_amount"] # Valor ganho na aposta em reais
            print(f"Ganhei {valor_ganho} reais na aposta.")
        else:
            # A aposta foi mal sucedida
            print(f"Perdi {valor_aposta} reais na aposta.")
    else:
        # O avião não está no ar
        print(f"O avião não está no ar. Aguardando a próxima rodada.")
        time.sleep(1) # Esperando um segundo para tentar novamente
