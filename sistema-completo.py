import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# ── ARQUIVO DE DADOS ────────────────────────────────────────────
ARQUIVO = "estoque.json"

ESTOQUE_INICIAL = {
    "ARROZ":            {"unidade": "5kg",             "preco": 15.00},
    "FEIJÃO CARIOCA":   {"unidade": "1kg",             "preco":  6.00},
    "AÇÚCAR":           {"unidade": "1kg",             "preco":  4.00},
    "CAFÉ":             {"unidade": "500g",            "preco": 26.00},
    "LEITE":            {"unidade": "1L",              "preco":  4.00},
    "ÓLEO DE SOJA":     {"unidade": "900ml",           "preco":  6.00},
    "MACARRÃO":         {"unidade": "500g",            "preco":  4.00},
    "OVOS":             {"unidade": "cartela c/12",    "preco": 10.00},
    "FRANGO":           {"unidade": "1kg",             "preco":  9.00},
    "PÃO FRANCÊS":      {"unidade": "1kg",             "preco": 12.00},
    "MARGARINA":        {"unidade": "500g",            "preco":  7.00},
    "FARINHA DE TRIGO": {"unidade": "1kg",             "preco":  5.00},
    "TOMATE":           {"unidade": "1kg",             "preco":  6.00},
    "BATATA":           {"unidade": "1kg",             "preco":  5.00},
    "CEBOLA":           {"unidade": "1kg",             "preco":  4.00},
    "SABÃO EM PÓ":      {"unidade": "1kg",             "preco": 12.00},
    "PAPEL HIGIÊNICO":  {"unidade": "pacote 12 rolos", "preco": 15.00},
    "DETERGENTE":       {"unidade": "500ml",           "preco":  2.00},
    "ÁGUA SANITÁRIA":   {"unidade": "1L",              "preco":  3.00},
    "SABONETE":         {"unidade": "unidade",         "preco":  2.00},
}

def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    salvar_estoque(ESTOQUE_INICIAL)
    return ESTOQUE_INICIAL.copy()

def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, ensure_ascii=False, indent=2)

# ── CORES / TEMA ────────────────────────────────────────────────
BG         = "#0a0a0a"
BG2        = "#111111"
BG3        = "#1a1a1a"
VERDE      = "#00ff41"
VERDE_DIM  = "#00aa2a"
VERDE_DARK = "#003310"
CINZA      = "#333333"
CINZA2     = "#222222"
TEXTO      = "#cccccc"
TEXTO2     = "#888888"
BRANCO     = "#ffffff"
VERMELHO   = "#ff3333"
AMARELO    = "#ffcc00"

FONTE_TITLE = ("Courier New", 18, "bold")
FONTE_MONO  = ("Courier New", 11)
FONTE_MONO_B= ("Courier New", 11, "bold")
FONTE_SMALL = ("Courier New", 9)
FONTE_BIG   = ("Courier New", 13, "bold")

# ── APP ─────────────────────────────────────────────────────────
class Mercadinho:
    def __init__(self, root):
        self.root = root
        self.root.title("MERCADINHO DO SEU ZÉ // SISTEMA v1.0")
        self.root.configure(bg=BG)
        self.root.geometry("900x640")
        self.root.resizable(False, False)

        self.estoque = carregar_estoque()
        self.tela_atual = None

        self._construir_header()
        self._construir_nav()
        self._construir_corpo()
        self._construir_statusbar()

        self.mostrar_tela("dashboard")

    # ── HEADER ──────────────────────────────────────────────────
    def _construir_header(self):
        header = tk.Frame(self.root, bg=BG, pady=10)
        header.pack(fill="x", padx=20, pady=(15, 0))

        esq = tk.Frame(header, bg=BG)
        esq.pack(side="left")

        tk.Label(esq, text="[ MERCADINHO DO SEU ZÉ ]",
                 font=FONTE_TITLE, fg=VERDE, bg=BG).pack(anchor="w")
        tk.Label(esq, text=">> sistema de estoque e vendas // powered by terminal",
                 font=FONTE_SMALL, fg=TEXTO2, bg=BG).pack(anchor="w")

        dir_ = tk.Frame(header, bg=BG)
        dir_.pack(side="right")

        self.lbl_hora = tk.Label(dir_, text="", font=FONTE_SMALL, fg=VERDE_DIM, bg=BG)
        self.lbl_hora.pack(anchor="e")
        self.lbl_qtd = tk.Label(dir_, text="", font=FONTE_SMALL, fg=TEXTO2, bg=BG)
        self.lbl_qtd.pack(anchor="e")
        self._atualizar_hora()

        sep = tk.Frame(self.root, bg=VERDE, height=1)
        sep.pack(fill="x", padx=20, pady=(8, 0))

    def _atualizar_hora(self):
        agora = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
        self.lbl_hora.config(text=f">> {agora}")
        self.lbl_qtd.config(text=f"produtos no estoque: {len(self.estoque)}")
        self.root.after(1000, self._atualizar_hora)

    # ── NAV ─────────────────────────────────────────────────────
    def _construir_nav(self):
        nav = tk.Frame(self.root, bg=BG2, pady=6)
        nav.pack(fill="x", padx=20, pady=(8, 0))

        self.btns_nav = {}
        abas = [
            ("dashboard", "[ INÍCIO ]"),
            ("estoque",   "[ ESTOQUE ]"),
            ("cadastro",  "[ CADASTRAR ]"),
            ("venda",     "[ VENDER ]"),
        ]
        for chave, texto in abas:
            b = tk.Button(
                nav, text=texto,
                font=FONTE_MONO_B, fg=TEXTO2, bg=BG2,
                activeforeground=VERDE, activebackground=BG2,
                relief="flat", bd=0, padx=14, pady=4, cursor="hand2",
                command=lambda c=chave: self.mostrar_tela(c)
            )
            b.pack(side="left", padx=2)
            self.btns_nav[chave] = b

        sep = tk.Frame(self.root, bg=CINZA, height=1)
        sep.pack(fill="x", padx=20, pady=(6, 0))

    def _nav_highlight(self, ativa):
        for chave, btn in self.btns_nav.items():
            if chave == ativa:
                btn.config(fg=VERDE, bg=VERDE_DARK)
            else:
                btn.config(fg=TEXTO2, bg=BG2)

    # ── CORPO ───────────────────────────────────────────────────
    def _construir_corpo(self):
        self.corpo = tk.Frame(self.root, bg=BG)
        self.corpo.pack(fill="both", expand=True, padx=20, pady=10)

    def mostrar_tela(self, nome):
        for w in self.corpo.winfo_children():
            w.destroy()
        self._nav_highlight(nome)
        self.tela_atual = nome

        if nome == "dashboard": self._tela_dashboard()
        elif nome == "estoque": self._tela_estoque()
        elif nome == "cadastro": self._tela_cadastro()
        elif nome == "venda": self._tela_venda()

    # ── STATUS BAR ──────────────────────────────────────────────
    def _construir_statusbar(self):
        sep = tk.Frame(self.root, bg=VERDE, height=1)
        sep.pack(fill="x", padx=20)
        bar = tk.Frame(self.root, bg=BG, pady=4)
        bar.pack(fill="x", padx=20)
        self.status = tk.Label(bar, text=">> sistema online. aguardando comando...",
                               font=FONTE_SMALL, fg=VERDE_DIM, bg=BG, anchor="w")
        self.status.pack(side="left")

    def set_status(self, msg, cor=VERDE_DIM):
        self.status.config(text=f">> {msg}", fg=cor)

    # ── TELA: DASHBOARD ─────────────────────────────────────────
    def _tela_dashboard(self):
        f = tk.Frame(self.corpo, bg=BG)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="// PAINEL PRINCIPAL", font=FONTE_BIG,
                 fg=VERDE, bg=BG).pack(anchor="w", pady=(10, 20))

        cards = tk.Frame(f, bg=BG)
        cards.pack(fill="x")

        total_produtos = len(self.estoque)
        menor = min(self.estoque.items(), key=lambda x: x[1]["preco"]) if self.estoque else None
        maior = max(self.estoque.items(), key=lambda x: x[1]["preco"]) if self.estoque else None

        dados_cards = [
            ("PRODUTOS\nCADASTRADOS", str(total_produtos), VERDE),
            ("MENOR\nPREÇO", f"R$ {menor[1]['preco']:.2f}\n{menor[0]}" if menor else "-", AMARELO),
            ("MAIOR\nPREÇO", f"R$ {maior[1]['preco']:.2f}\n{maior[0]}" if maior else "-", VERMELHO),
        ]

        for titulo, valor, cor in dados_cards:
            card = tk.Frame(cards, bg=BG3, bd=0, relief="flat",
                            highlightbackground=cor, highlightthickness=1)
            card.pack(side="left", expand=True, fill="both", padx=6, ipady=16, ipadx=10)
            tk.Label(card, text=titulo, font=FONTE_SMALL, fg=TEXTO2, bg=BG3).pack()
            tk.Label(card, text=valor, font=("Courier New", 15, "bold"),
                     fg=cor, bg=BG3).pack(pady=6)

        tk.Label(f, text="\n// ACESSO RÁPIDO", font=FONTE_MONO_B,
                 fg=TEXTO2, bg=BG).pack(anchor="w", pady=(24, 8))

        btns = tk.Frame(f, bg=BG)
        btns.pack(anchor="w")

        self._btn_acao(btns, "[ + CADASTRAR PRODUTO ]", VERDE,     lambda: self.mostrar_tela("cadastro"))
        self._btn_acao(btns, "[ $ REGISTRAR VENDA ]",   AMARELO,   lambda: self.mostrar_tela("venda"))
        self._btn_acao(btns, "[ = VER ESTOQUE ]",        TEXTO2,   lambda: self.mostrar_tela("estoque"))

        self.set_status("dashboard carregado.")

    def _btn_acao(self, pai, texto, cor, cmd):
        tk.Button(pai, text=texto, font=FONTE_MONO_B,
                  fg=cor, bg=BG3, activeforeground=BRANCO,
                  activebackground=CINZA, relief="flat", bd=0,
                  padx=18, pady=8, cursor="hand2", command=cmd
                  ).pack(side="left", padx=(0, 10))

    # ── TELA: ESTOQUE ───────────────────────────────────────────
    def _tela_estoque(self):
        f = tk.Frame(self.corpo, bg=BG)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="// ESTOQUE COMPLETO", font=FONTE_BIG,
                 fg=VERDE, bg=BG).pack(anchor="w", pady=(10, 12))

        # busca
        busca_frame = tk.Frame(f, bg=BG)
        busca_frame.pack(fill="x", pady=(0, 8))
        tk.Label(busca_frame, text="BUSCAR:", font=FONTE_SMALL,
                 fg=TEXTO2, bg=BG).pack(side="left", padx=(0, 6))
        self.var_busca = tk.StringVar()
        self.var_busca.trace("w", lambda *a: self._filtrar_estoque())
        entry_busca = tk.Entry(busca_frame, textvariable=self.var_busca,
                               font=FONTE_MONO, fg=VERDE, bg=BG3,
                               insertbackground=VERDE, relief="flat",
                               highlightbackground=CINZA, highlightthickness=1, width=30)
        entry_busca.pack(side="left")

        # tabela
        cols = ("produto", "unidade", "preco")
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Hacker.Treeview",
                         background=BG2, foreground=TEXTO,
                         fieldbackground=BG2, rowheight=26,
                         font=("Courier New", 10))
        style.configure("Hacker.Treeview.Heading",
                         background=BG3, foreground=VERDE,
                         font=("Courier New", 10, "bold"), relief="flat")
        style.map("Hacker.Treeview",
                  background=[("selected", VERDE_DARK)],
                  foreground=[("selected", VERDE)])

        frame_tree = tk.Frame(f, bg=BG)
        frame_tree.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(frame_tree, bg=BG3, troughcolor=BG,
                              activebackground=VERDE, relief="flat")
        scroll.pack(side="right", fill="y")

        self.tree = ttk.Treeview(frame_tree, columns=cols, show="headings",
                                  style="Hacker.Treeview",
                                  yscrollcommand=scroll.set)
        scroll.config(command=self.tree.yview)

        self.tree.heading("produto", text="PRODUTO")
        self.tree.heading("unidade", text="EMBALAGEM")
        self.tree.heading("preco",   text="PREÇO (R$)")
        self.tree.column("produto", width=340)
        self.tree.column("unidade", width=200)
        self.tree.column("preco",   width=120, anchor="e")
        self.tree.pack(fill="both", expand=True)

        self._filtrar_estoque()
        self.set_status(f"estoque carregado. {len(self.estoque)} produto(s).")

    def _filtrar_estoque(self):
        busca = self.var_busca.get().upper().strip() if hasattr(self, "var_busca") else ""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for nome, dados in self.estoque.items():
            if busca in nome:
                self.tree.insert("", "end", values=(
                    nome,
                    dados["unidade"],
                    f"R$ {dados['preco']:.2f}"
                ))

    # ── TELA: CADASTRO ──────────────────────────────────────────
    def _tela_cadastro(self):
        f = tk.Frame(self.corpo, bg=BG)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="// CADASTRAR PRODUTO", font=FONTE_BIG,
                 fg=VERDE, bg=BG).pack(anchor="w", pady=(10, 20))

        form = tk.Frame(f, bg=BG3, highlightbackground=CINZA,
                        highlightthickness=1)
        form.pack(anchor="w", ipadx=30, ipady=24)

        def campo(label_text, var):
            row = tk.Frame(form, bg=BG3)
            row.pack(fill="x", pady=8, padx=20)
            tk.Label(row, text=label_text, font=FONTE_MONO, fg=TEXTO2,
                     bg=BG3, width=22, anchor="w").pack(side="left")
            e = tk.Entry(row, textvariable=var, font=FONTE_MONO,
                         fg=VERDE, bg=BG, insertbackground=VERDE,
                         relief="flat", highlightbackground=CINZA,
                         highlightthickness=1, width=28)
            e.pack(side="left")
            return e

        self.v_nome  = tk.StringVar()
        self.v_und   = tk.StringVar()
        self.v_preco = tk.StringVar()

        campo("NOME DO PRODUTO :", self.v_nome)
        campo("EMBALAGEM       :", self.v_und)
        campo("PREÇO (R$)      :", self.v_preco)

        # feedback
        self.lbl_feedback = tk.Label(form, text="", font=FONTE_MONO,
                                     bg=BG3, fg=VERDE)
        self.lbl_feedback.pack(pady=(4, 0))

        tk.Button(form, text="[ CADASTRAR ]", font=FONTE_MONO_B,
                  fg=BRANCO, bg=VERDE_DARK, activeforeground=BRANCO,
                  activebackground=CINZA, relief="flat", bd=0,
                  padx=20, pady=8, cursor="hand2",
                  command=self._cadastrar).pack(pady=(16, 0))

        self.set_status("preencha os campos e clique em cadastrar.")

    def _cadastrar(self):
        nome  = self.v_nome.get().upper().strip()
        und   = self.v_und.get().strip()
        preco_str = self.v_preco.get().strip().replace(",", ".")

        if not nome or not und or not preco_str:
            self.lbl_feedback.config(text="!! preencha todos os campos.", fg=VERMELHO)
            self.set_status("campos incompletos.", VERMELHO)
            return

        try:
            preco = float(preco_str)
        except ValueError:
            self.lbl_feedback.config(text="!! preço inválido.", fg=VERMELHO)
            self.set_status("preço inválido.", VERMELHO)
            return

        ja_existe = nome in self.estoque
        self.estoque[nome] = {"unidade": und, "preco": preco}
        salvar_estoque(self.estoque)

        msg = f"produto atualizado: {nome}" if ja_existe else f"produto cadastrado: {nome}"
        self.lbl_feedback.config(text=f">> {msg}", fg=VERDE)
        self.set_status(msg, VERDE)
        self.v_nome.set("")
        self.v_und.set("")
        self.v_preco.set("")

    # ── TELA: VENDA ─────────────────────────────────────────────
    def _tela_venda(self):
        f = tk.Frame(self.corpo, bg=BG)
        f.pack(fill="both", expand=True)

        tk.Label(f, text="// REGISTRAR VENDA", font=FONTE_BIG,
                 fg=VERDE, bg=BG).pack(anchor="w", pady=(10, 12))

        top = tk.Frame(f, bg=BG)
        top.pack(fill="both", expand=True)

        # lista de produtos
        esq = tk.Frame(top, bg=BG)
        esq.pack(side="left", fill="both", expand=True, padx=(0, 12))

        tk.Label(esq, text="SELECIONE O PRODUTO:", font=FONTE_SMALL,
                 fg=TEXTO2, bg=BG).pack(anchor="w", pady=(0, 4))

        style = ttk.Style()
        style.configure("Venda.Treeview",
                         background=BG2, foreground=TEXTO,
                         fieldbackground=BG2, rowheight=24,
                         font=("Courier New", 10))
        style.configure("Venda.Treeview.Heading",
                         background=BG3, foreground=AMARELO,
                         font=("Courier New", 10, "bold"), relief="flat")
        style.map("Venda.Treeview",
                  background=[("selected", VERDE_DARK)],
                  foreground=[("selected", VERDE)])

        frame_tree = tk.Frame(esq, bg=BG)
        frame_tree.pack(fill="both", expand=True)

        scroll = tk.Scrollbar(frame_tree, bg=BG3, troughcolor=BG,
                              activebackground=VERDE, relief="flat")
        scroll.pack(side="right", fill="y")

        self.tree_venda = ttk.Treeview(frame_tree, columns=("prod","und","preco"),
                                        show="headings", style="Venda.Treeview",
                                        yscrollcommand=scroll.set)
        scroll.config(command=self.tree_venda.yview)
        self.tree_venda.heading("prod",  text="PRODUTO")
        self.tree_venda.heading("und",   text="EMBAL.")
        self.tree_venda.heading("preco", text="PREÇO")
        self.tree_venda.column("prod",  width=220)
        self.tree_venda.column("und",   width=120)
        self.tree_venda.column("preco", width=90, anchor="e")
        self.tree_venda.pack(fill="both", expand=True)
        self.tree_venda.bind("<<TreeviewSelect>>", self._selecionar_produto)

        for nome, dados in self.estoque.items():
            self.tree_venda.insert("", "end", values=(
                nome, dados["unidade"], f"R$ {dados['preco']:.2f}"
            ))

        # painel direito
        dir_ = tk.Frame(top, bg=BG3, highlightbackground=CINZA,
                         highlightthickness=1, width=260)
        dir_.pack(side="right", fill="y", ipadx=16, ipady=16)
        dir_.pack_propagate(False)

        tk.Label(dir_, text="// DETALHES DA VENDA", font=FONTE_SMALL,
                 fg=VERDE, bg=BG3).pack(pady=(12, 16))

        self.lbl_prod_sel = tk.Label(dir_, text="nenhum produto\nselecionado",
                                      font=FONTE_MONO, fg=TEXTO2, bg=BG3,
                                      justify="center")
        self.lbl_prod_sel.pack(pady=(0, 12))

        tk.Label(dir_, text="QUANTIDADE:", font=FONTE_SMALL,
                 fg=TEXTO2, bg=BG3).pack(anchor="w", padx=14)
        self.v_qtd = tk.StringVar(value="1")
        tk.Entry(dir_, textvariable=self.v_qtd, font=FONTE_BIG,
                 fg=AMARELO, bg=BG, insertbackground=AMARELO,
                 relief="flat", highlightbackground=CINZA,
                 highlightthickness=1, width=8, justify="center"
                 ).pack(padx=14, pady=4)

        self.lbl_total = tk.Label(dir_, text="TOTAL:\nR$ 0.00",
                                   font=("Courier New", 14, "bold"),
                                   fg=VERDE, bg=BG3)
        self.lbl_total.pack(pady=16)

        self.v_qtd.trace("w", lambda *a: self._calcular_total())

        tk.Button(dir_, text="[ REGISTRAR VENDA ]", font=FONTE_MONO_B,
                  fg=BRANCO, bg=VERDE_DARK, activeforeground=BRANCO,
                  activebackground=CINZA, relief="flat", bd=0,
                  padx=12, pady=8, cursor="hand2",
                  command=self._registrar_venda).pack(pady=(4, 0))

        self.lbl_venda_fb = tk.Label(dir_, text="", font=FONTE_SMALL,
                                      bg=BG3, fg=VERDE, wraplength=220,
                                      justify="center")
        self.lbl_venda_fb.pack(pady=8)

        self._produto_selecionado = None
        self.set_status("selecione um produto da lista para iniciar a venda.")

    def _selecionar_produto(self, event):
        sel = self.tree_venda.selection()
        if not sel:
            return
        valores = self.tree_venda.item(sel[0], "values")
        nome = valores[0]
        dados = self.estoque.get(nome)
        if not dados:
            return
        self._produto_selecionado = {"nome": nome, "dados": dados}
        self.lbl_prod_sel.config(
            text=f"{nome}\n{dados['unidade']}\nR$ {dados['preco']:.2f}",
            fg=BRANCO
        )
        self._calcular_total()
        self.set_status(f"produto selecionado: {nome}")

    def _calcular_total(self):
        if not self._produto_selecionado:
            return
        try:
            qtd = int(self.v_qtd.get())
            preco = self._produto_selecionado["dados"]["preco"]
            total = preco * qtd
            self.lbl_total.config(text=f"TOTAL:\nR$ {total:.2f}")
        except ValueError:
            self.lbl_total.config(text="TOTAL:\n---")

    def _registrar_venda(self):
        if not self._produto_selecionado:
            self.lbl_venda_fb.config(text="!! selecione um produto.", fg=VERMELHO)
            return
        try:
            qtd = int(self.v_qtd.get())
            if qtd <= 0:
                raise ValueError
        except ValueError:
            self.lbl_venda_fb.config(text="!! quantidade inválida.", fg=VERMELHO)
            return

        nome  = self._produto_selecionado["nome"]
        dados = self._produto_selecionado["dados"]
        total = dados["preco"] * qtd

        self.lbl_venda_fb.config(
            text=f">> venda registrada!\n{qtd}x {nome}\nTotal: R$ {total:.2f}",
            fg=VERDE
        )
        self.set_status(f"venda: {qtd}x {nome} = R$ {total:.2f}", VERDE)

# ── MAIN ────────────────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = Mercadinho(root)
    root.mainloop()