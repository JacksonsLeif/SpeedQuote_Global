import streamlit as st
import time
import math

# ==========================================
# 1. CONFIGURAÇÃO E MEMÓRIA
# ==========================================
st.set_page_config(page_title="SpeedQuote Global", page_icon="⚡", layout="wide")

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'current_page' not in st.session_state: st.session_state['current_page'] = 'Dashboard'
if 'dados_fornecedores' not in st.session_state: st.session_state['dados_fornecedores'] = None
if 'fornecedor_vencedor' not in st.session_state: st.session_state['fornecedor_vencedor'] = None

def change_page(page_name): st.session_state['current_page'] = page_name

# ==========================================
# 2. INJEÇÃO DE CSS GLOBAL
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #ffffff; }
    .neon-orb-purple { position: absolute; width: 500px; height: 500px; background: #8A2BE2; border-radius: 50%; filter: blur(180px); top: 0%; right: 10%; z-index: 0; opacity: 0.4; }
    .neon-orb-green { position: absolute; width: 400px; height: 400px; background: #00ff41; border-radius: 50%; filter: blur(150px); bottom: -10%; left: 10%; z-index: 0; opacity: 0.2; }
    
    .glass-box { background: rgba(20, 20, 20, 0.4); backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px); border: 1px solid rgba(255, 255, 255, 0.08); border-radius: 20px; padding: 40px; box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6); z-index: 1; position: relative; }
    .btn-main>button { width: 100% !important; background-color: #00ff41 !important; color: #050505 !important; font-weight: 900 !important; font-size: 1.1rem !important; border: none !important; border-radius: 10px !important; padding: 12px !important; transition: all 0.3s ease !important; }
    .btn-main>button:hover { background-color: #00cc33 !important; box-shadow: 0 0 20px rgba(0, 255, 65, 0.6) !important; transform: scale(1.02); }
    
    .nav-container { background: linear-gradient(90deg, #11071F, #050505, #0A140D); padding: 10px; border-bottom: 1px solid rgba(138, 43, 226, 0.3); border-radius: 10px; margin-bottom: 30px; box-shadow: 0 4px 15px rgba(0,0,0,0.5); z-index: 2; position: relative; }
    .nav-btn>button { background: transparent !important; color: #a0a0a0 !important; border: none !important; font-weight: bold !important; font-size: 1.1rem !important; transition: 0.3s !important; }
    .nav-btn>button:hover { color: #00ff41 !important; transform: translateY(-2px); }
    
    /* CSS DOS CARDS DA ARENA */
    .supplier-card { background: rgba(20, 20, 20, 0.8); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 15px; padding: 20px; text-align: center; position: relative; margin-bottom: 20px; }
    .price-tag { font-size: 2.5rem; font-weight: 900; margin: 15px 0; }
    .price-green { color: #00ff41; text-shadow: 0 0 15px rgba(0, 255, 65, 0.4); }
    .price-red { color: #ff3333; text-shadow: 0 0 15px rgba(255, 51, 51, 0.4); }
    .price-neutral { color: #ffffff; }
    .badge-win { position: absolute; top: -15px; right: -15px; background: #00ff41; color: #000; padding: 5px 15px; border-radius: 20px; font-weight: bold; font-size: 0.9em; box-shadow: 0 0 10px #00ff41; }
    .detail-row { display: flex; justify-content: space-between; border-bottom: 1px solid #333; padding: 8px 0; font-size: 0.9em; color: #ccc; }
    </style>
    <div class="neon-orb-purple"></div><div class="neon-orb-green"></div>
""", unsafe_allow_html=True)

# ==========================================
# 3. ROTEAMENTO DE TELAS
# ==========================================
if not st.session_state['logged_in']:
    spacer_left, col_sales, col_login, spacer_right = st.columns([0.5, 2.5, 1.5, 0.5])
    with col_sales:
        st.write("<br><br><br>", unsafe_allow_html=True)
        st.markdown('<h1 style="font-size: 3.5rem; font-weight: 900; background: linear-gradient(45deg, #b026ff, #00ff41); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">SPEEDQUOTE GLOBAL</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.4rem; color: #a0a0a0;">O primeiro Sourcing ERP do Brasil.</p>', unsafe_allow_html=True)
    with col_login:
        st.write("<br><br>", unsafe_allow_html=True)
        st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
        st.markdown("<h2 style='text-align: center;'>Acesse o Portal</h2><br>", unsafe_allow_html=True)
        email = st.text_input("E-mail corporativo", "admin@speedquote.com")
        senha = st.text_input("Senha", "1234", type="password")
        st.markdown("<div class='btn-main'>", unsafe_allow_html=True)
        if st.button("INICIAR SESSÃO"):
            st.session_state['logged_in'] = True
            st.rerun()
        st.markdown("</div></div>", unsafe_allow_html=True)

else:
    # NAV BAR
    st.markdown('<div class="nav-container">', unsafe_allow_html=True)
    n1, n2, n3, n4, n5 = st.columns([1, 1.5, 1.5, 1.5, 1.5])
    with n1: st.markdown("<span style='font-size: 1.5rem; font-weight: 900; background: linear-gradient(45deg, #b026ff, #00ff41); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>⚡ SQG</span>", unsafe_allow_html=True)
    st.markdown("<div class='nav-btn'>", unsafe_allow_html=True)
    with n2: 
        if st.button("🏠 Dashboard"): change_page('Dashboard')
    with n3: 
        if st.button("⚡ Ferramenta Free"): change_page('Auto-Format')
    with n4: 
        if st.button("⚔️ Arena Sourcing"): change_page('Arena')
    with n5: 
        if st.button("📦 Logística"): change_page('Logistica')
    st.markdown("</div></div>", unsafe_allow_html=True)
    
    if st.session_state['current_page'] == 'Dashboard':
        st.markdown("<h2>Bem-vindo de volta, Importador.</h2><br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        with c1: st.markdown("""<div class="glass-box" style="padding: 20px;"><h3 style="color:#00ff41;">1 / 5</h3><p>Cotações Free Usadas</p></div>""", unsafe_allow_html=True)
        with c2: 
            st.markdown("""<div class="glass-box" style="padding: 20px; border-color: #8A2BE2;"><h3>Projeto Atual</h3><p>Garrafas Térmicas 500ml</p></div>""", unsafe_allow_html=True)
            st.markdown("<div class='btn-main' style='margin-top: -15px;'>", unsafe_allow_html=True)
            if st.button("ABRIR ARENA"): change_page('Arena'); st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
        with c3: st.markdown("""<div class="glass-box" style="padding: 20px; border-color: #FFD700;"><h3 style="color:#FFD700;">Plano Enterprise</h3><p>Acesso total liberado.</p></div>""", unsafe_allow_html=True)

    # -----------------------------------------------------
    # ABA: ARENA SOURCING
    # -----------------------------------------------------
    elif st.session_state['current_page'] == 'Arena':
        st.markdown("<h2 style='color: #00ff41; border-bottom: 2px solid #8A2BE2; padding-bottom: 10px;'>⚔️ Arena de Comparação</h2>", unsafe_allow_html=True)
        
        if st.button("📥 Puxar Dados do Banco"):
            with st.spinner("Conectando com fornecedores..."):
                time.sleep(1)
                # ADICIONEI A VARIÁVEL 'pcs_ctn' (Peças por Caixa) AQUI!
                st.session_state['dados_fornecedores'] = [
                    {"nome": "Shenzhen Tech", "preco": 4.50, "moq": 500, "porto": "Shenzhen", "incoterm": "FOB", "cbm": 0.06, "pcs_ctn": 50},
                    {"nome": "Yiwu Plastics", "preco": 3.90, "moq": 1000, "porto": "Ningbo", "incoterm": "EXW", "cbm": 0.08, "pcs_ctn": 100},
                    {"nome": "Guangzhou Premium", "preco": 5.20, "moq": 200, "porto": "Guangzhou", "incoterm": "FOB", "cbm": 0.05, "pcs_ctn": 40}
                ]
        
        if st.session_state['dados_fornecedores']:
            dados = st.session_state['dados_fornecedores']
            precos = [f["preco"] for f in dados]
            preco_min, preco_max = min(precos), max(precos)
            
            st.write("<br>", unsafe_allow_html=True)
            cols = st.columns(3)
            
            for idx, fornecedor in enumerate(dados):
                with cols[idx]:
                    if fornecedor["preco"] == preco_min:
                        cor_preco, borda, badge = "price-green", "border: 2px solid #00ff41;", "<div class='badge-win'>🏆 MELHOR PREÇO</div>"
                    elif fornecedor["preco"] == preco_max:
                        cor_preco, borda, badge = "price-red", "border: 1px solid #ff3333;", ""
                    else:
                        cor_preco, borda, badge = "price-neutral", "border: 1px solid rgba(255,255,255,0.1);", ""
                    
                    st.markdown(f"""
                    <div class="supplier-card" style="{borda}">
                        {badge}
                        <h4 style="color: #8A2BE2;">{fornecedor['nome']}</h4>
                        <div class="price-tag {cor_preco}">US$ {fornecedor['preco']:.2f}</div>
                        <div class="detail-row"><span>MOQ:</span> <strong>{fornecedor['moq']} pcs</strong></div>
                        <div class="detail-row"><span>Caixa (PCS/CTN):</span> <strong>{fornecedor['pcs_ctn']} pcs</strong></div>
                        <div class="detail-row"><span>Vol/Caixa:</span> <strong>{fornecedor['cbm']} CBM</strong></div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    st.markdown("<div class='btn-main'>", unsafe_allow_html=True)
                    if st.button(f"✅ ESCOLHER {fornecedor['nome'].split()[0].upper()}", key=f"btn_{idx}"):
                        st.session_state['fornecedor_vencedor'] = fornecedor
                        change_page('Logistica')
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # ABA: HUB LOGÍSTICO (SIMULADOR DE CONTÊINER)
    # -----------------------------------------------------
    elif st.session_state['current_page'] == 'Logistica':
        st.markdown("<h2 style='color: #FFD700; border-bottom: 2px solid #8A2BE2; padding-bottom: 10px;'>📦 HUB Logístico</h2>", unsafe_allow_html=True)
        
        if not st.session_state['fornecedor_vencedor']:
            st.warning("⚠️ Você precisa escolher um fornecedor na 'Arena Sourcing' antes de calcular a logística.")
        else:
            f = st.session_state['fornecedor_vencedor']
            st.success(f"Fornecedor Selecionado: **{f['nome']}** | {f['pcs_ctn']} pcs/caixa | CBM por caixa: **{f['cbm']}**")
            
            st.markdown("<div class='glass-box'>", unsafe_allow_html=True)
            
            # Dividindo em duas colunas para ficar organizado
            col_qtd, col_tipo = st.columns(2)
            
            with col_qtd:
                qtd_desejada = st.number_input("Quantas unidades o cliente quer comprar?", min_value=1, value=f['moq'], step=100)
            
            with col_tipo:
                tipo_embarque = st.selectbox("Selecione o Tipo de Embarque", ["Contêiner 20'DC (33 CBM)", "Contêiner 40'HC (76 CBM)", "LCL (Carga Fracionada)"])
            
            # MATEMÁTICA CORRIGIDA: Qtd -> Caixas -> CBM
            caixas_totais = math.ceil(qtd_desejada / f['pcs_ctn']) # math.ceil arredonda sempre para cima, afinal não se envia meia caixa
            cbm_total = caixas_totais * f['cbm']
            
            st.write("<br>", unsafe_allow_html=True)
            st.markdown(f"### 📦 Caixas Totais (Master Cartons): <span style='color:#FFD700;'>{caixas_totais} caixas</span>", unsafe_allow_html=True)
            st.markdown(f"### 📏 Volume Total Calculado: <span style='color:#00ff41;'>{cbm_total:.2f} CBM</span>", unsafe_allow_html=True)
            
            # Lógica do Contêiner
            if tipo_embarque == "LCL (Carga Fracionada)":
                st.info("💡 Embarque LCL selecionado. O frete será cobrado por CBM avulso (Carga Consolidada).")
            else:
                # Define a capacidade com base no dropdown
                if "20'DC" in tipo_embarque: capacidade = 33.0
                elif "40'HC" in tipo_embarque: capacidade = 76.0
                
                porcentagem = (cbm_total / capacidade) * 100
                porcentagem_visual = 100 if porcentagem > 100 else porcentagem
                
                cor_barra = "#00ff41" if porcentagem <= 90 else "#ff3333" 
                
                st.markdown(f"""
                <div style="width: 100%; height: 50px; background-color: #222; border: 2px solid #555; border-radius: 5px; position: relative; overflow: hidden; margin-top: 10px; margin-bottom: 10px;">
                    <div style="width: {porcentagem_visual}%; height: 100%; background-color: {cor_barra}; box-shadow: 0 0 15px {cor_barra}; transition: width 1s ease-in-out;"></div>
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; font-weight: 900; font-size: 1.2rem; text-shadow: 1px 1px 2px black;">
                        {porcentagem:.1f}% Ocupado
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                if porcentagem > 100:
                    st.error(f"⚠️ Atenção: A carga ({cbm_total:.2f} CBM) estourou o limite do {tipo_embarque.split(' ')[1]}!")
                elif porcentagem < 50:
                    st.warning("💡 Dica: Muito espaço vazio! O frete unitário vai ficar caro. Sugira ao cliente comprar mais itens ou mudar para LCL.")
                
            st.markdown("</div>", unsafe_allow_html=True)