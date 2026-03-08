import streamlit as st

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="SpeedQuote Global", page_icon="⚡", layout="wide")

# Inicializando a "Memória" do site (Session State)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# ==========================================
# 2. INJEÇÃO DE CSS (VISUAL GLOBAL)
# ==========================================
st.markdown("""
    <style>
    /* Fundo escuro geral do site */
    .stApp {
        background-color: #050505;
        color: #ffffff;
    }

    /* Luzes Neon de Fundo */
    .neon-orb-purple {
        position: absolute; width: 500px; height: 500px; background: #8A2BE2;
        border-radius: 50%; filter: blur(180px); top: 0%; right: 10%;
        z-index: 0; opacity: 0.4; animation: pulse 8s infinite alternate;
    }
    .neon-orb-green {
        position: absolute; width: 400px; height: 400px; background: #00ff41;
        border-radius: 50%; filter: blur(150px); bottom: -10%; left: 10%;
        z-index: 0; opacity: 0.2;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.3; }
        100% { transform: scale(1.1); opacity: 0.5; }
    }

    /* Textos da Landing Page */
    .sales-title { font-size: 3.8rem; font-weight: 900; background: linear-gradient(45deg, #b026ff, #00ff41); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 0px; line-height: 1.1; z-index: 1; position: relative; }
    .sales-subtitle { font-size: 1.4rem; color: #a0a0a0; margin-top: 10px; margin-bottom: 40px; z-index: 1; position: relative; }
    .bullet-point { font-size: 1.1rem; margin-bottom: 20px; color: #e0e0e0; z-index: 1; position: relative; line-height: 1.5; }
    
    /* Caixa de Vidro (Fase 1 e Dashboard) */
    .glass-box {
        background: rgba(20, 20, 20, 0.4); backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px; padding: 40px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6);
        z-index: 1; position: relative;
    }

    /* Botão Verde Padrão */
    .stButton>button {
        width: 100% !important; background-color: #00ff41 !important; color: #050505 !important;
        font-weight: 900 !important; font-size: 1.1rem !important; border: none !important;
        border-radius: 10px !important; padding: 12px !important; transition: all 0.3s ease !important;
    }
    .stButton>button:hover { background-color: #00cc33 !important; box-shadow: 0 0 20px rgba(0, 255, 65, 0.6) !important; transform: scale(1.02); }

    /* ========================================= */
    /* CSS NOVO: DASHBOARD (FASE 2)              */
    /* ========================================= */
    
    /* Barra de Navegação Superior (Solid Header) */
    .nav-bar {
        background: linear-gradient(90deg, #11071F, #050505, #050505, #0A140D);
        padding: 15px 30px; border-bottom: 1px solid rgba(138, 43, 226, 0.3);
        border-radius: 10px; margin-bottom: 30px; display: flex; gap: 30px; align-items: center;
        position: relative; z-index: 2; box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .nav-item { color: #a0a0a0; font-size: 1.1rem; font-weight: 600; cursor: pointer; transition: 0.3s; }
    .nav-item.active { color: #00ff41; text-shadow: 0 0 10px rgba(0,255,65,0.4); }
    
    /* Cards do Dashboard */
    .dash-card {
        background: rgba(20, 20, 20, 0.6); border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 15px; padding: 25px; height: 100%; transition: transform 0.3s;
        position: relative; z-index: 1;
    }
    .dash-card:hover { transform: translateY(-5px); border-color: rgba(138, 43, 226, 0.4); box-shadow: 0 10px 20px rgba(0,0,0,0.5); }
    .dash-title { font-size: 1.2rem; font-weight: bold; color: #ffffff; margin-bottom: 10px; }
    .dash-value { font-size: 2.8rem; font-weight: 900; color: #8A2BE2; margin-bottom: 5px; }
    
    /* Esconder o aviso chato de "Press Enter" dos campos de texto */
    div[data-testid="InputInstructions"] > span:nth-child(1) { visibility: hidden; }
    </style>

    <div class="neon-orb-purple"></div>
    <div class="neon-orb-green"></div>
""", unsafe_allow_html=True)

# ==========================================
# 3. O "CÉREBRO" DO APP (MUDANÇA DE TELAS)
# ==========================================

if not st.session_state['logged_in']:
    # ---------------------------------------------------------
    # TELA 1: PORTA DE ENTRADA (LANDING PAGE)
    # ---------------------------------------------------------
    spacer_left, col_sales, col_login, spacer_right = st.columns([0.5, 2.5, 1.5, 0.5])

    with col_sales:
        st.write("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<p class="sales-title">SPEEDQUOTE GLOBAL</p>', unsafe_allow_html=True)
        st.markdown('<p class="sales-subtitle">Não faça planilhas. Faça negócios.</p>', unsafe_allow_html=True)
        st.markdown('<p class="bullet-point">⚡ <b>Mapeamento Automático:</b> Traduza e formate dados crus em cotações padronizadas em segundos.</p>', unsafe_allow_html=True)
        st.markdown('<p class="bullet-point">🔗 <b>Smart Link:</b> Esqueça arquivos no WeChat. Envie links interativos para a China e receba os preços direto no painel.</p>', unsafe_allow_html=True)
        st.markdown('<p class="bullet-point">📦 <b>Hub Logístico:</b> Calcule o espaço no container (CBM) e evite prejuízos de <i>Inland Freight</i> antes de fechar o pedido. <span style="color:#FFD700; font-size:1.2em;">🔒</span></p>', unsafe_allow_html=True)
        st.markdown('<p class="bullet-point">🇧🇷 <b>Módulo Brasil:</b> Sugestão de HS Code Universal e estimativa integrada de impostos para nacionalização. <span style="color:#FFD700; font-size:1.2em;">🔒</span></p>', unsafe_allow_html=True)

    with col_login:
        st.write("<br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center; margin-bottom: 15px;'>Acesse o Portal</h2>", unsafe_allow_html=True)
        
        # O novo subtítulo com "Sign Up"
        st.markdown("<p style='text-align: center; color: #a0a0a0; font-size: 0.9em; margin-bottom: 25px;'><b>Login</b> &nbsp;|&nbsp; <a href='#' style='color: #8A2BE2; text-decoration: none;'>Sign Up</a></p>", unsafe_allow_html=True)
        
        email = st.text_input("E-mail corporativo", placeholder="voce@suaempresa.com")
        senha = st.text_input("Senha", type="password", placeholder="••••••••")

        if st.button("INICIAR SESSÃO"):
            if email and senha:
                # O Truque: Troca a memória para 'Verdadeiro' e recarrega a página na hora
                st.session_state['logged_in'] = True
                st.rerun()
            else:
                st.error("Preencha o e-mail e a senha para entrar.")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    # ---------------------------------------------------------
    # TELA 2: DASHBOARD PRINCIPAL (PÓS-LOGIN)
    # ---------------------------------------------------------
    
    # Menu Superior Neon (Solid Header)
    st.markdown("""
        <div class="nav-bar">
            <span style="font-size: 1.5rem; font-weight: 900; background: linear-gradient(45deg, #b026ff, #00ff41); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-right: 20px;">⚡ SQG</span>
            <span class="nav-item active">🏠 Dashboard</span>
            <span class="nav-item">⚡ Auto-Format</span>
            <span class="nav-item">🔗 Smart Link <span style="color:#FFD700; font-size:0.8em;">🔒</span></span>
            <span class="nav-item">📦 Logística <span style="color:#FFD700; font-size:0.8em;">🔒</span></span>
        </div>
    """, unsafe_allow_html=True)
    
    # Cabeçalho de Boas-vindas e Botão de Sair (Logout)
    col_texto, col_botao = st.columns([8, 1])
    with col_texto:
        st.markdown("<h2 style='margin-bottom: 20px;'>Bem-vindo de volta, Importador.</h2>", unsafe_allow_html=True)
    with col_botao:
        if st.button("Sair da Conta"):
            st.session_state['logged_in'] = False
            st.rerun()

    # Os 3 Cards Inferiores (A Vitrine de Ferramentas)
    c1, c2, c3 = st.columns(3)

    # CARD 1: O Hodômetro de Cotações (Gatilho Free)
    with c1:
        st.markdown("""
        <div class="dash-card">
            <div class="dash-title">📊 Uso da Conta (Plano Free)</div>
            <div class="dash-value" style="color: #00ff41;">1 <span style="font-size: 1.2rem; color: #a0a0a0;">/ 5</span></div>
            <p style="color: #a0a0a0; font-size: 0.9em;">Cotações gratuitas utilizadas neste mês.</p>
            <div style="width: 100%; background-color: #222; height: 8px; border-radius: 5px; margin-top: 20px;">
                <div style="width: 20%; background-color: #00ff41; height: 100%; border-radius: 5px; box-shadow: 0 0 10px #00ff41;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # CARD 2: Ação Rápida (Formatação)
    with c2:
        st.markdown("""
        <div class="dash-card" style="border-color: rgba(0, 255, 65, 0.4); background: rgba(0, 255, 65, 0.05);">
            <div class="dash-title">🚀 Ação Rápida</div>
            <p style="color: #e0e0e0; font-size: 0.95em; margin-bottom: 20px;">Sua equipe de compras está aguardando os preços. Inicie uma formatação de planilha agora.</p>
        </div>
        """, unsafe_allow_html=True)
        # Botão real colocado por cima via Streamlit para ter funcionalidade de clique
        st.write("") # Espaçador
        if st.button("⚡ NOVA COTAÇÃO AUTOMÁTICA"):
            st.info("A engrenagem do Sourcing Automático será ligada na Fase 3!")

    # CARD 3: A Isca Premium (Mapa Borrado)
    with c3:
        st.markdown("""
        <div class="dash-card" style="padding: 0; overflow: hidden; border-color: rgba(255, 215, 0, 0.4);">
            <div style="filter: blur(5px); opacity: 0.3; height: 100%; background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/China_edcp_location_map.svg/500px-China_edcp_location_map.svg.png'); background-size: cover; background-position: center;">
            </div>
            
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center; width: 90%;">
                <h3 style="color: #FFD700; margin-bottom: 5px;">🔒 Módulo Premium</h3>
                <p style="font-size: 0.9em; color: #fff;">Calcule o CBM e evite surpresas com Frete Inland.</p>
                <button style="background: #FFD700; color: #000; border: none; padding: 10px 20px; border-radius: 5px; font-weight: 900; cursor: pointer; margin-top: 10px;">DESBLOQUEAR PLANO</button>
            </div>
        </div>
        """, unsafe_allow_html=True)