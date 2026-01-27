import requests
import pandas as pd
# from util import chave_api # Removido comentário para teste

# Simulação da chave e URL
chave = "SUA_CHAVE"
url = f'https://economia.awesomeapi.com.br/json/last/USD-BRL,BTC-BRL,EUR-BRL,GBP-BRL'
resposta = requests.get(url).json()
print(resposta)
# 1. Criamos uma lista vazia para armazenar os dados
dados_para_dataframe = []

for par_moeda, dados in resposta.items():
    dados_para_dataframe.append({
        'par_moeda': par_moeda,                  # USDBRL, BTCBRL...
        'moeda': dados['code'],                  # USD, BTC...
        'moeda_destino': dados['codein'],        # BRL
        'nome': dados['name'],
        'preco_compra': float(dados['bid']),
        'preco_venda': float(dados['ask']),
        'max_dia': float(dados['high']),
        'min_dia': float(dados['low']),
        'variacao': float(dados['varBid']),
        'variacao_pct': float(dados['pctChange']),
        'timestamp': int(dados['timestamp']),
        'data_coleta': dados['create_date']
    })

# 3. Criamos o DataFrame de uma vez só, fora do loop
df = pd.DataFrame(dados_para_dataframe)

print("\n--- Dados recolhidos   --")
print(df)