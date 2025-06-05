from Class.ManagerGioco import GameManager
from Class.App_state import Access, Settings, Placing, Match, LoserScreen, WinnerScreen
import streamlit as st
import time
#streamlit run Battleship.py

st.set_page_config(
    page_title='Battaglia Navale',
    page_icon='⚓',
    layout = ['centered','wide'][0], #Alterna 0 e 1 per scegliere il layout
    menu_items = {'About': "# This is a header. This is an *extremely* cool app!"}
)
st.logo(r"C:\Users\PICARO\Desktop\Unisa\3-2\Progettazione_del_software\Progetto_BN\Codice\logo.png")
if "GM" not in st.session_state:
    st.session_state.GM = GameManager()
    st.session_state.country_generate = False
    st.session_state.attesa = 0
    
# Se l'applicazione è in Access state
if st.session_state.GM.app_state().get_state() is Access:
    c1, c2 = st.columns([5,1])
    with c1:
        st.write("# 1941 - Il caos sfocia in mare")
        st.write('_By Francesco Picaro_')
    with c2:
        st.image(r"C:\Users\PICARO\Desktop\Unisa\3-2\Progettazione_del_software\Progetto_BN\Codice\logo.png", width=150)
    st.write("""
             In un mondo in cui l'attacco a Pearl Harbor ha segnato l'inizio di una *nuova era*,
             e quello di una guerra lontana da ogni immaginazione, tutti i paesi si scontrano
             in un gioco di **strategia e astuzia**, riuscirai a tenere il passo con i tuoi avversari?
             
             Il gioco è semplice: ***piazza*** le tue navi, ***attacca*** quelle degli avversari e cerca di affondarle tutte.
             Una classica battaglia navale, ma con un tocco di modernità, o meglio, strategia.
             
             Tutti i paesi che sono in guerra hanno flotte diverse, ma sopratutto, ***armi*** diverse.
             """)
    st.markdown("""
                ### Arsenale
                
                **Bomba Atomica:** Annienta un'area di **2x2 caselle**. Il colpo di grazia per la flotta nemica!

                **Radar:** Scandaglia un'area di **3x3 caselle** e rivela quante navi si nascondono. Conosci il tuo nemico, affondalo con precisione!

                **Attacco a Sorpresa:** Ottieni **2 turni consecutivi**. Sferra un doppio attacco e prendi il tuo avversario alla sprovvista!

                **Mina Sottomarina:** Posiziona una trappola invisibile in mare. Se l'avversario la bombarda entro 10 turni, ottieni un **Attacco a Sorpresa**. Un'astuta vendetta!

                **Flotta d'Emergenza:** Proteggi una tua nave. Se affonda entro 10 turni, **piazzi una nuova nave 1x1 in uno spot casuale**. Una seconda chance inaspettata per sorprendere l'avversario!
                """)
    
    if st.button("Vai alle Impostazioni", key="settings-btn"):
        st.session_state.GM.app_state().go_to_settings()
        st.rerun()

# Se l'applicazione è in Settings state   
if st.session_state.GM.app_state().get_state() is Settings:
    st.write("## Impostazioni")
    st.write("Qui puoi configurare le tue preferenze di gioco.")
    
    if not st.session_state.country_generate:
        with st.spinner("Costruzione delle flotte in corso..."):
            time.sleep(st.session_state.attesa)  # Simula un caricamento
            st.session_state.GM.create_countries()
            st.session_state.country_generate = True
    
    with st.form("settings-form"):
        st.write("Impostazioni di gioco:")
        n = st.slider("Dimensioni della griglia", min_value=8, max_value=10, value=10, step=2)
        difficulty = st.selectbox("Difficoltà", options=["Facile", "Normale", "Difficile"], index=1)
        
        st.session_state.player_country = st.selectbox("Scegli il tuo paese", options=st.session_state.GM.get_countries(), index=0)
        st.session_state.AI_country = st.selectbox("Scegli il paese dell'avversario", options=st.session_state.GM.get_countries(), index=1)
        
        submitted = st.form_submit_button("Salva Impostazioni e piazza le Navi")
        if submitted:
            st.session_state.GM.setup_settings(n, difficulty, st.session_state.player_country, st.session_state.AI_country)
            st.success("Impostazioni salvate con successo!")
            st.session_state.GM.app_state().go_to_placing()
            st.session_state.piazzamento_ai = False
            st.session_state.ship_to_place = st.session_state.GM.get_country(st.session_state.player_country).get_navy().still_alive()
            st.session_state.placing_ship = 0
            st.rerun()


# Se l'applicazione è in Placing state
if st.session_state.GM.app_state().get_state() is Placing:
    st.write("## Piazzamento Navi")
    st.write("Qui puoi piazzare le tue navi sul campo di battaglia.")
    if not st.session_state.piazzamento_ai:
        with st.spinner("Piazzamento delle navi avversarie in corso..."):
            time.sleep(st.session_state.attesa)  # Simula un caricamento
            st.session_state.GM.riempimento_navi_ai(st.session_state.GM.ai_country.get_navy())
            st.session_state.piazzamento_ai = True
            
    st.dataframe(st.session_state.GM.get_player_grid().df())
    if st.session_state.placing_ship < st.session_state.ship_to_place:
        ship = st.session_state.GM.player_country.get_navy().ships[st.session_state.placing_ship]
        with st.form("placing-form"):
            st.write("Piazza le tue navi")
            st.write("Navi ancora da piazzare: ", st.session_state.ship_to_place - st.session_state.placing_ship)
            st.write("La nave da piazzare ha dimensione", ship.dim())
            c1, c2, c3 = st.columns([1, 1, 2])
            rows, cols = st.session_state.GM.get_player_grid().xy()
            with c1:
                col = st.selectbox("Colonna", options=cols, index=0)
            with c2:
                row = st.selectbox("Riga", options=rows, index=0)
            with c3:
                orientation = st.selectbox("Orientamento", options=["Orizzontale", "Verticale"], index=0)
                orientation = 0 if orientation == "Orizzontale" else 1
            
            submitted = st.form_submit_button("Piazza Nave")
            if submitted:
                if st.session_state.GM.controlla_posizione_nave_player(ship, row, col, orientation):
                    st.session_state.GM.posiziona_nave_player(ship, row, col, orientation)
                    st.toast("Nave piazzata con successo!")
                    st.session_state.placing_ship += 1
                    st.rerun()
                else:
                    st.toast("Posizione non valida! Riprova.")
            
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Torna alle Impostazioni", key="settings-btn back"):
            st.session_state.GM.app_state().go_to_settings()
            st.rerun()
    with col2:
        if st.session_state.placing_ship == st.session_state.ship_to_place:
            if st.button("Inizia la Partita", key="match-btn"):
                st.session_state.GM.app_state().go_to_match()
                st.rerun()
        else:
            st.warning("Devi piazzare tutte le tue navi prima di iniziare la partita.")
            
# Se l'applicazione è in Match state
if st.session_state.GM.app_state().get_state() is Match:
    st.write("## Partita in Corso")
    st.write("Qui puoi attaccare le navi nemiche e cercare di affondarle.")
    
    st.write("Turno attuale:", st.session_state.GM.turno())
    st.write("Lunghezza della partita:", st.session_state.GM.len_Match())
    
    st.write("### Griglia AI")
    st.write("Numero di navi ancora non affondate dell'avversario:", st.session_state.GM.get_country(st.session_state.AI_country).get_navy().still_alive())
    st.dataframe(st.session_state.GM.get_ai_grid().df())
    st.write("---")
    st.write("### Griglia del Giocatore")
    st.dataframe(st.session_state.GM.get_player_grid().df())
    
    if st.session_state.GM.turno() == "AI":
        st.session_state.GM.play_turn()
        st.rerun()
        
    else:
        rows, cols = st.session_state.GM.get_ai_grid().xy()
        c1, c2, c3 = st.columns([3, 3, 1])
        with c1:
            col = st.selectbox("Colonna", options=cols, index=0)
        with c2:
            row = st.selectbox("Riga", options=rows, index=0)
        with c3:
            armi_disponibili = st.session_state.GM.get_country(st.session_state.player_country).get_arsenal().still_usable()
            if armi_disponibili:
                use_weapon = st.checkbox("Attacco con Arma", key="weapon-checkbox", value=True)
            else:
                st.write("Armi terminate")
        
        
        if armi_disponibili:
            nomi_armi_disponibili = [w.type() for w in armi_disponibili]
            name_weapon = st.radio("Scegli un'arma", options=nomi_armi_disponibili, index=0, disabled = not use_weapon)
            weapon = armi_disponibili[nomi_armi_disponibili.index(name_weapon)]
        else:
            use_weapon = False
        
        
        attack = st.button("Attacca")
        if attack:
            # Se stai per usare un'arma
            if use_weapon:
                if weapon.type() == "Bomba Atomica":
                    if st.session_state.GM.griglia_ai.check_attack(row, col, 2):
                        weapon.use(st.session_state.GM.griglia_ai, (row, col))
                        st.session_state.GM.play_turn()
                    else:
                        st.toast("Posizione per arma non valida")
                        time.sleep(1.5)
                        
                elif weapon.type() == "Radar":
                    if st.session_state.GM.griglia_ai.check_attack(row, col, 3):
                        n = weapon.use(st.session_state.GM.griglia_ai, (row, col))
                        st.toast(f"Navi trovate: {n}")
                        time.sleep(3)
                        st.session_state.GM.play_turn()
                    else:
                        st.toast("Posizione per arma non valida")
                        time.sleep(1.5)
                        
                elif weapon.type() == "Attacco a sorpresa":
                    weapon.use(st.session_state.GM.turn_counter)
                    st.session_state.GM.play_turn()
                    
                elif weapon.type() == "Mina sottomarina":
                    cella = st.session_state.GM.griglia_player.cell(row, col)
                    if not cella.occupied() and not cella.hitted():
                        weapon.set_trap(st.session_state.GM.turn_counter, cella)
                        st.session_state.GM.play_turn()
                    else:
                        st.toast("Posizione per arma non valida")
                        time.sleep(1.5)
                        
                elif weapon.type() == "Flotta d'emergenza":
                    cella = st.session_state.GM.griglia_player.cell(row, col)
                    if cella.occupied() and not cella.hitted():
                        weapon.set_trap(st.session_state.GM.turn_counter, cella)
                        st.session_state.GM.play_turn()
                        st.toast(f"Allarme piazzato in ({col}, {row})")
                        time.sleep(1.5)
                    else:
                        st.toast("Posizione per arma non valida")
                        time.sleep(1.5)
                
                st.rerun()
            else:
                st.session_state.GM.play_turn((row, col))
                st.rerun()
    
    if st.session_state.GM.check_match_end():
        if st.session_state.GM.player_country.get_navy().end():
            st.session_state.GM.app_state().go_to_LoserScreen()
            st.rerun()
        elif st.session_state.GM.ai_country.get_navy().end():
            st.session_state.GM.app_state().go_to_WinnerScreen()
            st.rerun()
                            
    if st.button("Termina la Partita", key="loser-btn"):
            st.session_state.GM.app_state().go_to_LoserScreen()
            st.rerun()
    
    
# Se l'applicazione è in LoserScreen state
if st.session_state.GM.app_state().get_state() is LoserScreen:
    st.write("## Hai Perso")
    st.write("La tua flotta è stata annientata. Riprova!")
    st.write("La partita è durata", st.session_state.GM.len_Match(), "turni")
    st.session_state.country_generate = False
    
    st.write("Stato finale della tua griglia")
    
    st.write("Stato finale della griglia avversaria")
    
    if st.button("Torna alle impostazioni per una nuova partita", key="settings-btn loss"):
        st.session_state.GM.app_state().go_to_settings()
        st.rerun()
        

# Se l'applicazione è in WinnerScreen state
if st.session_state.GM.app_state().get_state() is WinnerScreen:
    st.balloons()
    st.write("## Hai Vinto!")
    st.write("La tua strategia ha prevalso. Congratulazioni!")
    st.write("Complimenti hai vinto in ben", st.session_state.GM.len_Match(), "turni!")
    st.session_state.country_generate = False
    
    if st.button("Torna alle impostazioni per una nuova partita", key="settings-btn win"):
        st.session_state.GM.app_state().go_to_settings()
        st.rerun()