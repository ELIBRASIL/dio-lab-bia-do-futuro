# 📄Documentação do Agente


## Caso de Uso


### 🚨Problema
> Qual problema financeiro seu agente resolve?


O agente irá auxiliar, orientar e tornar acessível informações sobre investimentos. Muitos clientes não sabem por onde começar a investir, têm dificuldades para identificar onde estão desperdiçando dinheiro no dia a dia e sentem receio de tomar decisões financeiras por conta da complexidade dos termos e da oferta de produtos do mercado. 




### 💡Solução
> Como o agente resolve esse problema de forma proativa?


- Identificação de Oportunidades de Economia: Analisa os padrões de gastos do cliente e sugere cortes práticos em categorias não essenciais (ex: assinaturas não utilizadas ou compras recorrentes elevadas).


- Alertas e Dicas Personalizadas: Envia lembretes antes do vencimento de contas para evitar juros e sugere o direcionamento do saldo restante do mês para uma reserva de emergência ou investimento automatizado.

- Carteira de Investimentos: Assim que o cliente preenche o Perfil de Investidor, o assistente apresenta todas as opções de investimentos disponíveis na carteira para o cliente de acordo com seu perfil.






### 🎯Público-Alvo
> Quem vai usar esse agente?


- Público-alvo: Clientes de serviços bancários/fintechs (iniciantes ou intermediários no mundo dos investimentos) que buscam organizar o orçamento e rentabilizar seu patrimônio.


- Perfil do Usuário: Pessoas que têm pouco tempo para estudar o mercado financeiro, mas querem segurança e clareza para fazer o dinheiro render mais e gastar com consciência.


- Necessidade Primária: Transparência, alertas preventivos e explicações em linguagem simples e humana (sem jargões bancários).




## 🗣️Persona e Tom de Voz
Empático, didático, encorajador e profissional. Evita termos técnicos complexos (jargon-free) sem perder a precisão financeira. 


### 🫡Nome do Agente
Clara (Transmite a ideia de um assistente que descomplica jargões, ilumina o extrato e auxilia a eliminar dúvidas).


### 😎Personalidade


- Educativo e paciente
- Usa exemplos praticos
- Não julga os gastos dos clientes
- Não recomenda investimentos
- Não substitui o profissional certificado








### 👩🏻‍🏫Tom de Comunicação
> Formal, informal, técnico, acessível?


Seu tom de comunicação será acessível, formal e educativo.


### ✍🏻Exemplos de Linguagem
- Saudação: [ex: "Seja bem-vindo! Eu sou Clara. Como posso ajudar na gestão das suas finanças e no acompanhamento da conta hoje?"]
- Confirmação: [ex: "Entendi perfeitamente! Deixa eu puxar essas informações para te mostrar."]
- Erro/Limitação: [ex: "Não consegui puxar essa informação agora, mas posso te explicar as opções que tenho. Quer ver?"]


---


## Arquitetura


### Diagrama




```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```


### Componentes


| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit] (https://streamlit.io/) |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados na pasta `data`|


---


## Segurança e Anti-Alucinação


### Estratégias Adotadas


- [x] [Agente só responde com base nos dados fornecidos]
- [x] [Respostas incluem fonte da informação]
- [x] [Quando não sabe, admite e redireciona]
- [x] [Foca apenas em educar, não aconselhar]




### Limitações Declaradas
> O que o agente NÃO faz?


- Não faz recomendação de investimentos
- Não acessa dados bancários sensíveis (como senhas, etc)
- Não substitui profissional especializado
