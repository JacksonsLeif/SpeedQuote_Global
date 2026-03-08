import streamlit as st

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="SpeedQuote Global", page_icon="⚡", layout="wide")

# ==========================================
# 2. INJEÇÃO DE CSS (O VISUAL CYBER-PREMIUM E GLASSMORPHISM)
# ==========================================
st.markdown("""
    <style>
    /* Fundo escuro geral do site */
    .stApp {
        background-color: #050505;
        color: #ffffff;
    }

    /* Luzes Neon de Fundo (Efeito Blur simulando a Framer) */
    .neon-orb-purple {
        position: absolute;
        width: 500px;
        height: 500px;
        background: #8A2BE2; /* Roxo Neon */
        border-radius: 50%;
        filter: blur(180px);
        top: 0%;
        right: 10%;
        z-index: 0;
        opacity: 0.4;
        animation: pulse 8s infinite alternate;
    }
    .neon-orb-green {
        position: absolute;
        width: 400px;
        height: 400px;
        background: #00ff41; /* Verde Hacker */
        border-radius: 50%;
        filter: blur(150px);
        bottom: -10%;
        left: 10%;
        z-index: 0;
        opacity: 0.2;
    }

    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.3; }
        100% { transform: scale(1.1); opacity: 0.5; }
    }

    /* Textos de Vendas (Lado Esquerdo) */
    .sales-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: linear-gradient(45deg, #b026ff, #00ff41);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        line-height: 1.1;
        z-index: 1;
        position: relative;
    }
    .sales-subtitle {
        font-size: 1.4rem;
        color: #a0a0a0;
        margin-top: 10px;
        margin-bottom: 40px;
        z-index: 1;
        position: relative;
    }
    .bullet-point {
        font-size: 1.1rem;
        margin-bottom: 20px;
        color: #e0e0e0;
        z-index: 1;
        position: relative;
        line-height: 1.5;
    }

    /* A Mágica do Vidro Translúcido na Caixa de Login (Mirando na 2ª Coluna) */
    [data-testid="column"]:nth-of-type(2) {
        background: rgba(20, 20, 20, 0.4) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 20px !important;
        padding: 40px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6) !important;
        z-index: 1;
        margin-top: 20px;
    }

    /* Estilo das caixinhas de digitar Email e Senha */
    .stTextInput>div>div>input {
        background-color: rgba(0, 0, 0, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    .stTextInput>div>div>input:focus {
        border-color: #8A2BE2 !important;
        box-shadow: 0 0 15px rgba(138, 43, 226, 0.4) !important;
    }

    /* O Botão de Login (Verde Neon) */
    .stButton>button {
        width: 100% !important;
        background-color: #00ff41 !important;
        color: #050505 !important;
        font-weight: 900 !important;
        font-size: 1.2rem !important;
        letter-spacing: 1px;
        border: none !important;
        border-radius: 10px !important;
        padding: 12px !important;
        transition: all 0.3s ease !important;
        margin-top: 20px !important;
    }
    .stButton>button:hover {
        background-color: #00cc33 !important;
        box-shadow: 0 0 20px rgba(0, 255, 65, 0.6) !important;
        transform: scale(1.02);
    }
    </style>

    <div class="neon-orb-purple"></div>
    <div class="neon-orb-green"></div>
""", unsafe_allow_html=True)

# ==========================================
# 3. ESTRUTURA VISUAL (TELA DIVIDIDA)
# ==========================================

# Criamos 4 colunas: as das pontas são vazias para centralizar o conteúdo na tela
spacer_left, col_sales, col_login, spacer_right = st.columns([0.5, 2.5, 1.5, 0.5])

# --- LADO ESQUERDO: A Página de Vendas ---
with col_sales:
    st.write("<br><br><br>", unsafe_allow_html=True) # Dá um espaço do topo
    st.markdown('<p class="sales-title">SPEEDQUOTE GLOBAL</p>', unsafe_allow_html=True)
    st.markdown('<p class="sales-subtitle">Não faça planilhas. Faça negócios.</p>', unsafe_allow_html=True)

    st.markdown('<p class="bullet-point">⚡ <b>Mapeamento Automático:</b> Traduza e formate dados crus em cotações padronizadas em segundos.</p>', unsafe_allow_html=True)
    st.markdown('<p class="bullet-point">🔗 <b>Smart Link:</b> Esqueça arquivos no WeChat. Envie links interativos para a China e receba os preços direto no painel.</p>', unsafe_allow_html=True)
    st.markdown('<p class="bullet-point">📦 <b>Hub Logístico:</b> Calcule o espaço no container (CBM) e evite prejuízos de <i>Inland Freight</i> antes de fechar o pedido. <span style="color:#FFD700; font-size:1.2em;">🔒</span></p>', unsafe_allow_html=True)
    st.markdown('<p class="bullet-point">🇧🇷 <b>Módulo Brasil:</b> Sugestão de HS Code Universal e estimativa integrada de impostos para nacionalização. <span style="color:#FFD700; font-size:1.2em;">🔒</span></p>', unsafe_allow_html=True)

# --- LADO DIREITO: A Caixa de Vidro (Login) ---
with col_login:
    st.write("<br><br>", unsafe_allow_html=True) # Alinha a caixa com o texto da esquerda
    st.markdown("<h2 style='text-align: center; margin-bottom: 25px;'>Acesse o Portal</h2>", unsafe_allow_html=True)

    # Campos do Streamlit
    email = st.text_input("E-mail corporativo", placeholder="voce@suaempresa.com")
    senha = st.text_input("Senha", type="password", placeholder="••••••••")

    # Botão de ação principal
    if st.button("INICIAR SESSÃO"):
        if email and senha:
            # Por enquanto é só um aviso visual. Na Fase 2 isso vai destravar o site!
            st.success("Acesso validado! Carregando o Dashboard...")
        else:
            st.error("Preencha o e-mail e a senha para entrar.")

    # Link discreto embaixo do botão
    st.markdown("<p style='text-align: center; margin-top: 20px; font-size: 0.9em; color: #a0a0a0;'>Quer testar a plataforma? <a href='#' style='color: #8A2BE2; text-decoration: none;'>Fale com um especialista</a></p>", unsafe_allow_html=True)