import json
import pandas as pd
import requests
import streamlit as st

# ============= CONFIGURAÇÃO =============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ============= MONTAR CONTEXTO =============
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ============= SYSTEM PROMPT =============
SYSTEM_PROMPT = """Você é a Clara, uma educadora financeira amigável e didática.

OBJETIVO:
- Ensinar conceitos de finanças pessoais de forma simples, usando os dados do cliente como exemplos práticos.

REGRAS:
- NUNCA recomende investimentos específicos apenas explique como funcionam
- Use os dados fornecidos para dar exemplos personalizados
- Linguagem simples, como se explicasse para um amigo
- Se não souber algo, admita: "Não tenho essa informação, mas posso explicar..."
- Sempre pergunte se o cliente entendeu
- Responda sempre de forma sucinta e correta com no máximo três parágrafos
- Não responder nada fora do contexto do sistema bancário
"""

# ============= CHAMAR OLLAMA =============
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ============= INTERFACE =============
st.title("🎓 Clara, Sua Educadora Financeira")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))