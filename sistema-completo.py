"""
ZE_OS v3.5 // RETAIL_TERMINAL
Mercadinho do Seu Zé — Sistema Operacional de Varejo
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json, os, time, math
from datetime import datetime

# ── PERSISTÊNCIA ────────────────────────────────────────────────
ARQUIVO = "estoque.json"

ESTOQUE_INICIAL = {
    "ARROZ":            {"unidade": "5kg",             "preco": 15.00, "categoria": "MERCEARIA"},
    "FEIJÃO CARIOCA":   {"unidade": "1kg",             "preco":  6.00, "categoria": "MERCEARIA"},
    "AÇÚCAR":           {"unidade": "1kg",             "preco":  4.00, "categoria": "MERCEARIA"},
    "CAFÉ":             {"unidade": "500g",            "preco": 26.00, "categoria": "MERCEARIA"},
    "LEITE":            {"unidade": "1L",              "preco":  4.00, "categoria": "LATICÍNIOS"},
    "ÓLEO DE SOJA":     {"unidade": "900ml",           "preco":  6.00, "categoria": "MERCEARIA"},
    "MACARRÃO":         {"unidade": "500g",            "preco":  4.00, "categoria": "MERCEARIA"},
    "OVOS":             {"unidade": "cartela c/12",    "preco": 10.00, "categoria": "LATICÍNIOS"},
    "FRANGO":           {"unidade": "1kg",             "preco":  9.00, "categoria": "CARNES"},
    "PÃO FRANCÊS":      {"unidade": "1kg",             "preco": 12.00, "categoria": "PADARIA"},
    "MARGARINA":        {"unidade": "500g",            "preco":  7.00, "categoria": "LATICÍNIOS"},
    "FARINHA DE TRIGO": {"unidade": "1kg",             "preco":  5.00, "categoria": "MERCEARIA"},
    "TOMATE":           {"unidade": "1kg",             "preco":  6.00, "categoria": "HORTIFRUTI"},
    "BATATA":           {"unidade": "1kg",             "preco":  5.00, "categoria": "HORTIFRUTI"},
    "CEBOLA":           {"unidade": "1kg",             "preco":  4.00, "categoria": "HORTIFRUTI"},
    "SABÃO EM PÓ":      {"unidade": "1kg",             "preco": 12.00, "categoria": "LIMPEZA"},
    "PAPEL HIGIÊNICO":  {"unidade": "pacote 12 rolos", "preco": 15.00, "categoria": "HIGIENE"},
    "DETERGENTE":       {"unidade": "500ml",           "preco":  2.00, "categoria": "LIMPEZA"},
    "ÁGUA SANITÁRIA":   {"unidade": "1L",              "preco":  3.00, "categoria": "LIMPEZA"},
    "SABONETE":         {"unidade": "unidade",         "preco":  2.00, "categoria": "HIGIENE"},
}

def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    salvar_estoque(ESTOQUE_INICIAL)
    return dict(ESTOQUE_INICIAL)

def salvar_estoque(e):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(e, f, ensure_ascii=False, indent=2)

# ── PALETA ──────────────────────────────────────────────────────
C = {
    "bg":        "#121214",
    "panel":     "#1e1e26",
    "sidebar":   "#0d1117",
    "card":      "#191921",
    "card2":     "#16161e",
    "border":    "#1a2e1a",
    "border2":   "#0f2010",
    "green":     "#00ff88",
    "green_dim": "#00cc66",
    "green_dk":  "#004422",
    "green_pale":"#00ff8822",
    "cyan":      "#00d4ff",
    "cyan_dim":  "#0099bb",
    "red":       "#ff003c",
    "red_dim":   "#cc0030",
    "red_dk":    "#330010",
    "yellow":    "#ffb800",
    "yellow_dim":"#cc9200",
    "text":      "#c8d8c8",
    "text2":     "#6a8a6a",
    "text3":     "#3a4e3a",
    "white":     "#e8ffe8",
    "black":     "#080c08",
}

# badges por categoria
CAT_COLORS = {
    "MERCEARIA":  ("#00d4ff", "#001a22"),
    "LATICÍNIOS": ("#00ff88", "#002211"),
    "CARNES":     ("#ff003c", "#220010"),
    "HORTIFRUTI": ("#00ff88", "#001a0a"),
    "PADARIA":    ("#ffb800", "#221200"),
    "LIMPEZA":    ("#00ff88", "#001511"),
    "HIGIENE":    ("#00d4ff", "#001522"),
    "OUTROS":     ("#6a8a6a", "#0a100a"),
}

MONO  = ("Consolas", 10)
MONO_B= ("Consolas", 10, "bold")
MONO_S= ("Consolas", 9)
MONO_T= ("Consolas", 13, "bold")
MONO_H= ("Consolas", 18, "bold")
MONO_N= ("Consolas", 26, "bold")

# ── HELPERS ─────────────────────────────────────────────────────
def fr(pai, bg=None, **kw):
    return tk.Frame(pai, bg=bg or C["panel"], **kw)

def lb(pai, text="", tv=None, font=MONO, fg=None, bg=None, **kw):
    kw2 = dict(font=font, fg=fg or C["text"], bg=bg or C["panel"], **kw)
    if tv:
        return tk.Label(pai, textvariable=tv, **kw2)
    return tk.Label(pai, text=text, **kw2)

def entry(pai, var, **kw):
    defaults = dict(
        textvariable=var, font=MONO, fg=C["green"], bg=C["card2"],
        insertbackground=C["green"], relief="flat",
        highlightbackground=C["border"], highlightthickness=1,
        disabledbackground=C["card2"]
    )
    defaults.update(kw)
    return tk.Entry(pai, **defaults)

def hsep(pai, color=None, padx=0, pady=6):
    tk.Frame(pai, bg=color or C["border"], height=1).pack(fill="x", padx=padx, pady=pady)

def status_dot(pai, color=C["green"]):
    c = tk.Canvas(pai, width=8, height=8, bg=C["sidebar"], highlightthickness=0)
    c.pack(side="left", padx=(0, 6))
    c.create_oval(1, 1, 7, 7, fill=color, outline=color)
    return c

# ── MAIN ────────────────────────────────────────────────────────
class ZeOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ZE_OS v3.5 // RETAIL_TERMINAL")
        self.configure(bg=C["bg"])
        self.geometry("1200x740")
        self.minsize(1100, 680)

        self.estoque  = carregar_estoque()
        self.carrinho = []
        self._active  = "pdv"

        self._setup_styles()
        self._build_root()
        self._show("pdv")
        self._tick()

    # ── ROOT LAYOUT ─────────────────────────────────────────────
    def _build_root(self):
        # scanlines overlay via canvas (very subtle)
        self._sidebar = self._build_sidebar()
        self._content = fr(self, bg=C["bg"])
        self._content.pack(side="left", fill="both", expand=True)

    # ── STYLES ──────────────────────────────────────────────────
    def _setup_styles(self):
        s = ttk.Style(self)
        s.theme_use("clam")
        for name, fg_s, bg_s, hfg, hbg in [
            ("ZE",   C["green"], C["green_dk"], C["black"], C["green"]),
            ("Cart", C["green"], C["green_dk"], C["black"], C["green"]),
            ("Rel",  C["yellow"],"#332200",     C["black"], C["yellow"]),
        ]:
            s.configure(f"{name}.Treeview",
                background=C["panel"], foreground=C["text"],
                fieldbackground=C["panel"], rowheight=32,
                font=MONO, borderwidth=0, relief="flat")
            s.configure(f"{name}.Treeview.Heading",
                background=C["green"], foreground=C["black"],
                font=MONO_B, relief="flat", borderwidth=0,
                padding=(8, 6))
            s.map(f"{name}.Treeview",
                background=[("selected", bg_s)],
                foreground=[("selected", fg_s)])
        s.configure("ZE.Vertical.TScrollbar",
            background=C["card2"], troughcolor=C["bg"],
            arrowcolor=C["text3"], bordercolor=C["bg"],
            darkcolor=C["card2"], lightcolor=C["card2"], width=8)
        s.map("ZE.Vertical.TScrollbar",
            background=[("active", C["green_dk"])])

    # ── SIDEBAR ─────────────────────────────────────────────────
    def _build_sidebar(self):
        sb = tk.Frame(self, bg=C["sidebar"], width=220)
        sb.pack(side="left", fill="y")
        sb.pack_propagate(False)

        # top glow line
        tk.Frame(sb, bg=C["green"], height=1).pack(fill="x")

        # logo block
        logo = fr(sb, bg=C["sidebar"])
        logo.pack(fill="x", padx=18, pady=(20, 6))

        lb(logo, "ZE_OS", font=("Consolas", 22, "bold"),
           fg=C["green"], bg=C["sidebar"]).pack(anchor="w")
        lb(logo, "v3.5 // RETAIL_TERMINAL", font=("Consolas", 8),
           fg=C["text3"], bg=C["sidebar"]).pack(anchor="w")

        hsep(sb, color=C["border"], padx=18, pady=10)

        # nav
        self._nav_btns = {}
        self._nav_indicators = {}
        nav = fr(sb, bg=C["sidebar"])
        nav.pack(fill="x")

        items = [
            ("pdv",      "▸ PDV",        "[ PONTO_DE_VENDA ]"),
            ("estoque",  "▸ ESTOQUE",    "[ STOCK_DATABASE ]"),
            ("cadastro", "▸ CADASTRAR",  "[ ITEM_REGISTER  ]"),
            ("relatorio","▸ RELATORIO",  "[ SYS_REPORT     ]"),
        ]
        for key, label_short, label_long in items:
            row = tk.Frame(nav, bg=C["sidebar"], cursor="hand2")
            row.pack(fill="x", pady=1)

            indicator = tk.Frame(row, bg=C["sidebar"], width=3)
            indicator.pack(side="left", fill="y")

            btn_frame = tk.Frame(row, bg=C["sidebar"])
            btn_frame.pack(side="left", fill="both", expand=True, padx=(8, 12))

            lbl_top = lb(btn_frame, label_short, font=("Consolas", 9, "bold"),
                         fg=C["text3"], bg=C["sidebar"], anchor="w")
            lbl_top.pack(fill="x", pady=(8, 0))
            lbl_bot = lb(btn_frame, label_long, font=("Consolas", 8),
                         fg=C["text3"], bg=C["sidebar"], anchor="w")
            lbl_bot.pack(fill="x", pady=(0, 8))

            def make_cmd(k): return lambda: self._show(k)
            def make_enter(r, lt, lb_): return lambda e: self._nav_hover(r, lt, lb_, True)
            def make_leave(r, lt, lb_, k): return lambda e: self._nav_hover_out(r, lt, lb_, k)

            for w in [row, btn_frame, lbl_top, lbl_bot]:
                w.bind("<Button-1>", lambda e, k=key: self._show(k))
                w.bind("<Enter>", make_enter(row, lbl_top, lbl_bot))
                w.bind("<Leave>", make_leave(row, lbl_top, lbl_bot, key))

            self._nav_btns[key] = (row, lbl_top, lbl_bot)
            self._nav_indicators[key] = indicator

        hsep(sb, color=C["border"], padx=18, pady=10)

        # status block
        status = fr(sb, bg=C["sidebar"])
        status.pack(fill="x", padx=18, side="bottom", pady=14)

        status_dot(status)
        lb(status, "SISTEMA_ONLINE", font=("Consolas", 8),
           fg=C["green_dim"], bg=C["sidebar"]).pack(side="left")

        self._lbl_hora = lb(sb, "", font=("Consolas", 8),
                            fg=C["text3"], bg=C["sidebar"], anchor="w")
        self._lbl_hora.pack(side="bottom", fill="x", padx=18, pady=(0, 4))

        lb(sb, f"NODES: {len(self.estoque)} ITEMS",
           font=("Consolas", 8), fg=C["text3"], bg=C["sidebar"],
           anchor="w").pack(side="bottom", fill="x", padx=18, pady=(0, 2))

        tk.Frame(sb, bg=C["green"], height=1).pack(side="bottom", fill="x")
        return sb

    def _nav_hover(self, row, lt, lb_, active=True):
        if active:
            row.config(bg=C["green_pale"] if C["green_pale"] else C["border2"])
            lt.config(fg=C["green"], bg=C["sidebar"])
            lb_.config(fg=C["green_dim"], bg=C["sidebar"])

    def _nav_hover_out(self, row, lt, lb_, key):
        if key != self._active:
            row.config(bg=C["sidebar"])
            lt.config(fg=C["text3"], bg=C["sidebar"])
            lb_.config(fg=C["text3"], bg=C["sidebar"])

    def _nav_set_active(self, key):
        for k, (row, lt, lb_) in self._nav_btns.items():
            ind = self._nav_indicators[k]
            if k == key:
                row.config(bg=C["border2"])
                lt.config(fg=C["green"], bg=C["border2"])
                lb_.config(fg=C["green_dim"], bg=C["border2"])
                ind.config(bg=C["green"])
                for w in [row, lt, lb_]: w.config(bg=C["border2"])
                ind.config(bg=C["green"])
            else:
                row.config(bg=C["sidebar"])
                lt.config(fg=C["text3"], bg=C["sidebar"])
                lb_.config(fg=C["text3"], bg=C["sidebar"])
                ind.config(bg=C["sidebar"])

    def _show(self, key):
        self._active = key
        self._nav_set_active(key)
        for w in self._content.winfo_children():
            w.destroy()
        getattr(self, f"_tela_{key}")()

    def _tick(self):
        self._lbl_hora.config(
            text=datetime.now().strftime("SYS_TIME: %H:%M:%S\nDATE: %Y.%m.%d"))
        self.after(1000, self._tick)

    # ── PAGE HEADER ─────────────────────────────────────────────
    def _page_header(self, title, subtitle=""):
        wrap = fr(self._content, bg=C["bg"])
        wrap.pack(fill="x", padx=24, pady=(18, 0))

        left = fr(wrap, bg=C["bg"])
        left.pack(side="left")

        lb(left, f"// {title}", font=MONO_T, fg=C["green"], bg=C["bg"]).pack(anchor="w")
        if subtitle:
            lb(left, subtitle, font=MONO_S, fg=C["text3"], bg=C["bg"]).pack(anchor="w")

        right = fr(wrap, bg=C["bg"])
        right.pack(side="right")
        lb(right, datetime.now().strftime("%Y.%m.%d  %H:%M"),
           font=MONO_S, fg=C["text3"], bg=C["bg"]).pack(anchor="e")

        tk.Frame(self._content, bg=C["border"], height=1).pack(
            fill="x", padx=24, pady=(8, 0))

    # ══════════════════════════════════════════════════════════
    # TELA PDV
    # ══════════════════════════════════════════════════════════
    def _tela_pdv(self):
        self._page_header("PDV_TERMINAL", "PONTO DE VENDA // MODO OPERACIONAL")

        corpo = fr(self._content, bg=C["bg"])
        corpo.pack(fill="both", expand=True, padx=24, pady=14)
        corpo.columnconfigure(0, weight=58)
        corpo.columnconfigure(1, weight=42)
        corpo.rowconfigure(0, weight=1)

        # ── CATÁLOGO ────────────────────────────────────────
        left = fr(corpo, bg=C["panel"],
                  highlightbackground=C["border"], highlightthickness=1)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 10))

        # header catálogo
        ch = fr(left, bg=C["card2"])
        ch.pack(fill="x")
        tk.Frame(left, bg=C["green"], height=1).pack(fill="x")

        lb(ch, "  CATALOG_DB // PRODUTOS DISPONÍVEIS",
           font=MONO_B, fg=C["green"], bg=C["card2"],
           anchor="w").pack(side="left", pady=10)

        lb(ch, f"{len(self.estoque)} RECORDS  ",
           font=MONO_S, fg=C["text3"], bg=C["card2"]).pack(side="right", pady=10)

        # busca
        brow = fr(left, bg=C["panel"])
        brow.pack(fill="x", padx=14, pady=(10, 6))
        lb(brow, "SEARCH >", font=MONO_S, fg=C["text3"], bg=C["panel"]).pack(side="left", padx=(0,8))
        self._v_busca = tk.StringVar()
        self._v_busca.trace("w", lambda *a: self._pop_prod())
        e = entry(brow, self._v_busca)
        e.pack(fill="x", expand=True, ipady=6)
        e.bind("<FocusIn>",  lambda ev: e.config(highlightbackground=C["green"]))
        e.bind("<FocusOut>", lambda ev: e.config(highlightbackground=C["border"]))

        # tree
        tf = fr(left, bg=C["panel"])
        tf.pack(fill="both", expand=True, padx=14, pady=(0, 10))

        scr = ttk.Scrollbar(tf, style="ZE.Vertical.TScrollbar")
        scr.pack(side="right", fill="y")

        self._tree_prod = ttk.Treeview(
            tf, columns=("nome","cat","und","preco"),
            show="headings", style="ZE.Treeview",
            yscrollcommand=scr.set)
        scr.config(command=self._tree_prod.yview)

        for col, txt, w, anc, st in [
            ("nome","PRODUTO",   240,"w",True),
            ("cat", "CATEGORIA", 110,"w",False),
            ("und", "EMBAL.",    100,"w",False),
            ("preco","PREÇO",     90,"e",False),
        ]:
            self._tree_prod.heading(col, text=txt)
            self._tree_prod.column(col, width=w, anchor=anc, stretch=st)
        self._tree_prod.pack(fill="both", expand=True)
        self._tree_prod.bind("<Double-1>", lambda e: self._add())
        self._tree_prod.bind("<Return>",   lambda e: self._add())
        self._pop_prod()

        lb(left, "  ↵ ENTER ou DUPLO CLIQUE para adicionar ao carrinho",
           font=("Consolas", 8), fg=C["text3"], bg=C["panel"],
           anchor="w").pack(fill="x", padx=14, pady=(0, 8))

        # ── CARRINHO ────────────────────────────────────────
        right = fr(corpo, bg=C["panel"],
                   highlightbackground=C["border"], highlightthickness=1)
        right.grid(row=0, column=1, sticky="nsew")

        rh = fr(right, bg=C["card2"])
        rh.pack(fill="x")
        tk.Frame(right, bg=C["green"], height=1).pack(fill="x")

        lb(rh, "  CART_BUFFER // ITENS SELECIONADOS",
           font=MONO_B, fg=C["green"], bg=C["card2"],
           anchor="w").pack(side="left", pady=10)

        self._lbl_n_itens = lb(rh, "0 ITEMS  ",
                                font=MONO_S, fg=C["text3"], bg=C["card2"])
        self._lbl_n_itens.pack(side="right", pady=10)

        # tree carrinho
        cf = fr(right, bg=C["panel"])
        cf.pack(fill="both", expand=True, padx=14, pady=(10, 0))

        scr2 = ttk.Scrollbar(cf, style="ZE.Vertical.TScrollbar")
        scr2.pack(side="right", fill="y")

        self._tree_cart = ttk.Treeview(
            cf, columns=("nome","qtd","unit","sub"),
            show="headings", style="Cart.Treeview",
            yscrollcommand=scr2.set, height=8)
        scr2.config(command=self._tree_cart.yview)

        for col, txt, w, anc, st in [
            ("nome","PRODUTO",  155,"w",True),
            ("qtd", "QTD",       38,"center",False),
            ("unit","UNIT.",      80,"e",False),
            ("sub", "SUBTOTAL",   85,"e",False),
        ]:
            self._tree_cart.heading(col, text=txt)
            self._tree_cart.column(col, width=w, anchor=anc, stretch=st)
        self._tree_cart.pack(fill="both", expand=True)
        self._tree_cart.bind("<Delete>", lambda e: self._remover())

        lb(right, "  ⌦ DELETE para remover item",
           font=("Consolas", 8), fg=C["text3"], bg=C["panel"],
           anchor="w").pack(fill="x", padx=14, pady=(4, 0))

        # separador
        tk.Frame(right, bg=C["border"], height=1).pack(fill="x", padx=14, pady=10)

        # totais
        tot = fr(right, bg=C["panel"])
        tot.pack(fill="x", padx=14)

        def row_tot(txt, var, fg=C["text2"], big=False):
            r = fr(tot, bg=C["panel"])
            r.pack(fill="x", pady=2)
            lb(r, txt, font=MONO_S if not big else MONO_B,
               fg=fg, bg=C["panel"]).pack(side="left")
            lb(r, tv=var, font=MONO if not big else ("Consolas", 19, "bold"),
               fg=fg, bg=C["panel"]).pack(side="right")

        self._v_sub  = tk.StringVar(value="R$ 0,00")
        self._v_desc = tk.StringVar(value="R$ 0,00")
        self._v_tot  = tk.StringVar(value="R$ 0,00")

        row_tot("SUBTOTAL :", self._v_sub)
        row_tot("DESCONTO :", self._v_desc, fg=C["red"])

        tk.Frame(right, bg=C["border"], height=1).pack(fill="x", padx=14, pady=8)

        tr = fr(right, bg=C["panel"])
        tr.pack(fill="x", padx=14, pady=(0, 8))
        lb(tr, "TOTAL_DUE", font=MONO_B, fg=C["text3"], bg=C["panel"]).pack(side="left")
        lb(tr, tv=self._v_tot,
           font=("Consolas", 22, "bold"), fg=C["green"],
           bg=C["panel"]).pack(side="right")

        tk.Frame(right, bg=C["border"], height=1).pack(fill="x", padx=14, pady=(0, 8))

        # desconto
        drow = fr(right, bg=C["panel"])
        drow.pack(fill="x", padx=14, pady=(0, 8))
        lb(drow, "DESCONTO (R$) >", font=MONO_S, fg=C["text3"],
           bg=C["panel"]).pack(side="left")
        self._v_desc_in = tk.StringVar(value="0")
        self._v_desc_in.trace("w", lambda *a: self._recalc())
        de = entry(drow, self._v_desc_in, fg=C["yellow"], width=9, justify="right")
        de.pack(side="right", ipady=5)

        # botões
        bw = fr(right, bg=C["panel"])
        bw.pack(fill="x", padx=14, pady=(0, 14))

        tk.Button(bw, text="[ CONFIRMAR_VENDA ]", font=MONO_B,
                  fg=C["black"], bg=C["green"], activeforeground=C["black"],
                  activebackground=C["green_dim"], relief="flat", bd=0,
                  pady=12, cursor="hand2",
                  command=self._finalizar).pack(fill="x", pady=(0, 6))

        tk.Button(bw, text="[ LIMPAR_BUFFER ]", font=MONO_S,
                  fg=C["red"], bg=C["red_dk"], activeforeground=C["white"],
                  activebackground=C["red_dim"], relief="flat", bd=0,
                  pady=7, cursor="hand2",
                  command=self._limpar).pack(fill="x")

    def _pop_prod(self):
        f = self._v_busca.get().upper()
        for r in self._tree_prod.get_children():
            self._tree_prod.delete(r)
        for nome, d in self.estoque.items():
            if f in nome:
                self._tree_prod.insert("", "end", iid=nome, values=(
                    nome, d.get("categoria","—"),
                    d.get("unidade","—"),
                    f"R$ {d['preco']:.2f}".replace(".",",")))

    def _add(self):
        sel = self._tree_prod.selection()
        if not sel: return
        nome = sel[0]
        d = self.estoque[nome]
        for it in self.carrinho:
            if it["nome"] == nome:
                it["qtd"] += 1
                self._sync_cart()
                return
        self.carrinho.append({"nome": nome, "unidade": d["unidade"],
                               "preco": d["preco"], "qtd": 1})
        self._sync_cart()

    def _remover(self):
        sel = self._tree_cart.selection()
        if not sel: return
        self.carrinho = [i for i in self.carrinho if i["nome"] != sel[0]]
        self._sync_cart()

    def _sync_cart(self):
        for r in self._tree_cart.get_children():
            self._tree_cart.delete(r)
        for it in self.carrinho:
            sub = it["preco"] * it["qtd"]
            self._tree_cart.insert("", "end", iid=it["nome"], values=(
                it["nome"][:22], it["qtd"],
                f"R$ {it['preco']:.2f}".replace(".",","),
                f"R$ {sub:.2f}".replace(".",",")))
        self._recalc()

    def _recalc(self):
        sub = sum(i["preco"] * i["qtd"] for i in self.carrinho)
        try: desc = float(self._v_desc_in.get().replace(",","."))
        except: desc = 0
        desc  = max(0, min(desc, sub))
        total = sub - desc
        n     = sum(i["qtd"] for i in self.carrinho)
        self._lbl_n_itens.config(text=f"{n} ITEMS  ")
        self._v_sub.set(f"R$ {sub:.2f}".replace(".",","))
        self._v_desc.set(f"- R$ {desc:.2f}".replace(".",","))
        self._v_tot.set(f"R$ {total:.2f}".replace(".",","))

    def _limpar(self):
        self.carrinho.clear()
        self._sync_cart()

    def _finalizar(self):
        if not self.carrinho:
            messagebox.showwarning("CART_EMPTY", "Nenhum item no carrinho.")
            return
        try: desc = float(self._v_desc_in.get().replace(",","."))
        except: desc = 0
        sub   = sum(i["preco"] * i["qtd"] for i in self.carrinho)
        total = max(0, sub - desc)
        linhas = "\n".join(
            f"  {i['nome'][:26]:<28} {i['qtd']}x  R$ {i['preco']*i['qtd']:.2f}"
            for i in self.carrinho)
        msg = (f"{'━'*48}\n{linhas}\n{'━'*48}\n"
               f"  SUBTOTAL : R$ {sub:.2f}\n"
               f"  DESCONTO : R$ {desc:.2f}\n"
               f"  TOTAL    : R$ {total:.2f}\n{'━'*48}")
        if messagebox.askyesno("CONFIRM_TRANSACTION", f"Confirmar a venda?\n\n{msg}"):
            self._limpar()
            messagebox.showinfo("TX_COMPLETE",
                f"Venda finalizada com sucesso.\nTotal: R$ {total:.2f}")

    # ══════════════════════════════════════════════════════════
    # TELA ESTOQUE
    # ══════════════════════════════════════════════════════════
    def _tela_estoque(self):
        self._page_header("STOCK_DATABASE", f"INVENTÁRIO OPERACIONAL // {len(self.estoque)} REGISTROS")

        # stats strip
        strip = fr(self._content, bg=C["bg"])
        strip.pack(fill="x", padx=24, pady=(12, 0))

        precos = [d["preco"] for d in self.estoque.values()]
        total_v = sum(precos)
        media_v = total_v / len(precos) if precos else 0

        for titulo, valor, cor in [
            ("TOTAL_ITEMS", str(len(self.estoque)), C["green"]),
            ("AVG_PRICE",   f"R$ {media_v:.2f}",   C["cyan"]),
            ("MAX_PRICE",   f"R$ {max(precos):.2f}" if precos else "—", C["yellow"]),
            ("MIN_PRICE",   f"R$ {min(precos):.2f}" if precos else "—", C["text2"]),
        ]:
            c = tk.Frame(strip, bg=C["card2"],
                         highlightbackground=C["border"], highlightthickness=1)
            c.pack(side="left", expand=True, fill="both", padx=4, ipady=12)
            lb(c, titulo, font=("Consolas", 8), fg=C["text3"], bg=C["card2"]).pack(pady=(10,4))
            lb(c, valor, font=("Consolas", 16, "bold"), fg=cor, bg=C["card2"]).pack()
            lb(c, "", font=MONO_S, bg=C["card2"]).pack(pady=(0,10))

        # busca
        brow = fr(self._content, bg=C["bg"])
        brow.pack(fill="x", padx=24, pady=(12, 6))
        lb(brow, "FILTER >", font=MONO_S, fg=C["text3"], bg=C["bg"]).pack(side="left", padx=(0,8))
        self._v_best = tk.StringVar()
        self._v_best.trace("w", lambda *a: self._pop_est())
        e = entry(brow, self._v_best, bg=C["card2"])
        e.pack(side="left", ipady=6, fill="x", expand=True)
        e.bind("<FocusIn>",  lambda ev: e.config(highlightbackground=C["green"]))
        e.bind("<FocusOut>", lambda ev: e.config(highlightbackground=C["border"]))

        # tabela
        painel = fr(self._content, bg=C["panel"],
                    highlightbackground=C["border"], highlightthickness=1)
        painel.pack(fill="both", expand=True, padx=24, pady=(0, 20))

        tk.Frame(painel, bg=C["green"], height=1).pack(fill="x")

        scr = ttk.Scrollbar(painel, style="ZE.Vertical.TScrollbar")
        scr.pack(side="right", fill="y")

        self._tree_est = ttk.Treeview(
            painel, columns=("nome","cat","und","preco"),
            show="headings", style="ZE.Treeview",
            yscrollcommand=scr.set)
        scr.config(command=self._tree_est.yview)

        for col, txt, w, anc, st in [
            ("nome","PRODUTO",   300,"w",True),
            ("cat", "CATEGORIA", 150,"w",False),
            ("und", "EMBALAGEM", 160,"w",False),
            ("preco","PREÇO",    110,"e",False),
        ]:
            self._tree_est.heading(col, text=txt)
            self._tree_est.column(col, width=w, anchor=anc, stretch=st)
        self._tree_est.pack(fill="both", expand=True)
        self._pop_est()

    def _pop_est(self):
        f = self._v_best.get().upper() if hasattr(self,"_v_best") else ""
        for r in self._tree_est.get_children():
            self._tree_est.delete(r)
        for nome, d in self.estoque.items():
            if f in nome:
                self._tree_est.insert("", "end", values=(
                    nome, d.get("categoria","—"),
                    d.get("unidade","—"),
                    f"R$ {d['preco']:.2f}".replace(".",",")))

    # ══════════════════════════════════════════════════════════
    # TELA CADASTRO
    # ══════════════════════════════════════════════════════════
    def _tela_cadastro(self):
        self._page_header("ITEM_REGISTER", "CADASTRO DE PRODUTO // INPUT MATRIX")

        corpo = fr(self._content, bg=C["bg"])
        corpo.pack(fill="both", expand=True, padx=24, pady=14)
        corpo.columnconfigure(0, weight=40)
        corpo.columnconfigure(1, weight=60)
        corpo.rowconfigure(0, weight=1)

        # form
        form = fr(corpo, bg=C["panel"],
                  highlightbackground=C["border"], highlightthickness=1)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

        fh = fr(form, bg=C["card2"])
        fh.pack(fill="x")
        tk.Frame(form, bg=C["green"], height=1).pack(fill="x")

        lb(fh, "  NEW_ITEM_MATRIX",
           font=MONO_B, fg=C["green"], bg=C["card2"],
           anchor="w").pack(pady=10)

        self._v_c_nome  = tk.StringVar()
        self._v_c_und   = tk.StringVar()
        self._v_c_preco = tk.StringVar()
        self._v_c_cat   = tk.StringVar()

        def campo(icone, label_txt, var, hint=""):
            f = fr(form, bg=C["panel"])
            f.pack(fill="x", padx=18, pady=7)
            row = fr(f, bg=C["panel"])
            row.pack(fill="x")
            lb(row, icone, font=MONO_S, fg=C["green_dim"], bg=C["panel"]).pack(side="left", padx=(0,6))
            lb(row, label_txt, font=MONO_S, fg=C["text3"], bg=C["panel"]).pack(side="left")
            if hint:
                lb(row, hint, font=("Consolas", 8), fg=C["text3"], bg=C["panel"]).pack(side="right")
            e = entry(f, var)
            e.pack(fill="x", ipady=8, pady=(4, 0))
            e.bind("<FocusIn>",  lambda ev: e.config(highlightbackground=C["green"]))
            e.bind("<FocusOut>", lambda ev: e.config(highlightbackground=C["border"]))
            return e

        campo("#", "NOME_DO_PRODUTO *", self._v_c_nome)
        campo("◈", "EMBALAGEM", self._v_c_und, "ex: 1kg, 500ml")
        campo("$", "PREÇO_R$ *", self._v_c_preco)

        # categoria
        fc = fr(form, bg=C["panel"])
        fc.pack(fill="x", padx=18, pady=7)
        crow = fr(fc, bg=C["panel"])
        crow.pack(fill="x")
        lb(crow, "◉", font=MONO_S, fg=C["green_dim"], bg=C["panel"]).pack(side="left", padx=(0,6))
        lb(crow, "CATEGORIA", font=MONO_S, fg=C["text3"], bg=C["panel"]).pack(side="left")

        cats = ["MERCEARIA","LATICÍNIOS","CARNES","HORTIFRUTI",
                "PADARIA","LIMPEZA","HIGIENE","OUTROS"]
        self._v_c_cat.set(cats[0])
        om = tk.OptionMenu(fc, self._v_c_cat, *cats)
        om.config(font=MONO, fg=C["green"], bg=C["card2"],
                  activeforeground=C["black"], activebackground=C["green"],
                  relief="flat", highlightbackground=C["border"],
                  highlightthickness=1, bd=0, indicatoron=True)
        om["menu"].config(font=MONO, fg=C["green"], bg=C["card"],
                          activeforeground=C["black"],
                          activebackground=C["green"])
        om.pack(fill="x", ipady=5, pady=(4, 0))

        # feedback
        self._lbl_fb = lb(form, "", font=MONO_S, fg=C["green"], bg=C["panel"])
        self._lbl_fb.pack(padx=18, pady=(10, 0))

        tk.Button(form, text="[ REGISTER_ITEM ]", font=MONO_B,
                  fg=C["black"], bg=C["green"],
                  activeforeground=C["black"], activebackground=C["green_dim"],
                  relief="flat", bd=0, pady=12, cursor="hand2",
                  command=self._cadastrar).pack(fill="x", padx=18, pady=(10, 20))

        # lista
        lista = fr(corpo, bg=C["panel"],
                   highlightbackground=C["border"], highlightthickness=1)
        lista.grid(row=0, column=1, sticky="nsew")

        lh = fr(lista, bg=C["card2"])
        lh.pack(fill="x")
        tk.Frame(lista, bg=C["green"], height=1).pack(fill="x")
        lb(lh, "  REGISTERED_ITEMS // DATABASE",
           font=MONO_B, fg=C["green"], bg=C["card2"],
           anchor="w").pack(pady=10)

        scr = ttk.Scrollbar(lista, style="ZE.Vertical.TScrollbar")
        scr.pack(side="right", fill="y")

        self._tree_cad = ttk.Treeview(
            lista, columns=("nome","cat","preco"),
            show="headings", style="ZE.Treeview",
            yscrollcommand=scr.set)
        scr.config(command=self._tree_cad.yview)

        for col, txt, w, anc, st in [
            ("nome","PRODUTO",  260,"w",True),
            ("cat", "CATEGORIA",140,"w",False),
            ("preco","PREÇO",   100,"e",False),
        ]:
            self._tree_cad.heading(col, text=txt)
            self._tree_cad.column(col, width=w, anchor=anc, stretch=st)
        self._tree_cad.pack(fill="both", expand=True)
        self._refresh_cad()

    def _refresh_cad(self):
        for r in self._tree_cad.get_children():
            self._tree_cad.delete(r)
        for nome, d in self.estoque.items():
            self._tree_cad.insert("", "end", values=(
                nome, d.get("categoria","—"),
                f"R$ {d['preco']:.2f}".replace(".",",")))

    def _cadastrar(self):
        nome = self._v_c_nome.get().upper().strip()
        und  = self._v_c_und.get().strip()
        cat  = self._v_c_cat.get()
        ps   = self._v_c_preco.get().replace(",",".").strip()
        if not nome or not ps:
            self._lbl_fb.config(text="⚠ NOME e PREÇO são obrigatórios.", fg=C["red"])
            return
        try: preco = float(ps)
        except:
            self._lbl_fb.config(text="⚠ PREÇO inválido.", fg=C["red"])
            return
        ja = nome in self.estoque
        self.estoque[nome] = {"unidade": und or "—", "preco": preco, "categoria": cat}
        salvar_estoque(self.estoque)
        self._refresh_cad()
        acao = "UPDATED" if ja else "REGISTERED"
        self._lbl_fb.config(text=f"✔ {acao}: {nome}", fg=C["green"])
        self._v_c_nome.set(""); self._v_c_und.set(""); self._v_c_preco.set("")

    # ══════════════════════════════════════════════════════════
    # TELA RELATÓRIO
    # ══════════════════════════════════════════════════════════
    def _tela_relatorio(self):
        self._page_header("SYS_REPORT", "ANÁLISE OPERACIONAL // RELATÓRIO DO SISTEMA")

        # cards
        cards = fr(self._content, bg=C["bg"])
        cards.pack(fill="x", padx=24, pady=(14, 0))

        total  = len(self.estoque)
        precos = [d["preco"] for d in self.estoque.values()]
        media  = sum(precos) / total if total else 0
        mn, md = min(self.estoque.items(), key=lambda x: x[1]["preco"]) if self.estoque else ("—",{"preco":0})
        mx, mxd= max(self.estoque.items(), key=lambda x: x[1]["preco"]) if self.estoque else ("—",{"preco":0})

        for titulo, valor, sub, cor, bcor in [
            ("TOTAL_ITEMS",   str(total),              "REGISTROS NO SISTEMA",  C["green"],  C["green_dk"]),
            ("AVG_PRICE",     f"R$ {media:.2f}",       "MÉDIA GERAL",           C["cyan"],   "#001a22"),
            ("LOWEST_PRICE",  f"R$ {md['preco']:.2f}", mn[:18],                 C["green"],  C["green_dk"]),
            ("HIGHEST_PRICE", f"R$ {mxd['preco']:.2f}",mx[:18],                C["yellow"], "#221200"),
        ]:
            c = tk.Frame(cards, bg=bcor,
                         highlightbackground=cor, highlightthickness=1)
            c.pack(side="left", expand=True, fill="both", padx=5, ipady=14)
            tk.Frame(c, bg=cor, height=2).pack(fill="x")
            lb(c, titulo, font=("Consolas", 8, "bold"), fg=cor, bg=bcor).pack(pady=(12,4))
            lb(c, valor, font=("Consolas", 20, "bold"), fg=cor, bg=bcor).pack()
            lb(c, sub, font=("Consolas", 8), fg=C["text3"], bg=bcor).pack(pady=(4,12))

        # por categoria
        painel = fr(self._content, bg=C["panel"],
                    highlightbackground=C["border"], highlightthickness=1)
        painel.pack(fill="both", expand=True, padx=24, pady=(14, 20))

        ph = fr(painel, bg=C["card2"])
        ph.pack(fill="x")
        tk.Frame(painel, bg=C["green"], height=1).pack(fill="x")
        lb(ph, "  CATEGORY_BREAKDOWN // ANÁLISE POR CATEGORIA",
           font=MONO_B, fg=C["green"], bg=C["card2"],
           anchor="w").pack(pady=10)

        scr = ttk.Scrollbar(painel, style="ZE.Vertical.TScrollbar")
        scr.pack(side="right", fill="y")

        tree = ttk.Treeview(
            painel, columns=("cat","qtd","mn","mx","med"),
            show="headings", style="Rel.Treeview",
            yscrollcommand=scr.set)
        scr.config(command=tree.yview)

        for col, txt, w, anc, st in [
            ("cat","CATEGORIA", 180,"w",True),
            ("qtd","ITEMS",      80,"center",False),
            ("mn", "MENOR",     120,"e",False),
            ("mx", "MAIOR",     120,"e",False),
            ("med","MÉDIA",     120,"e",False),
        ]:
            tree.heading(col, text=txt)
            tree.column(col, width=w, anchor=anc, stretch=st)
        tree.pack(fill="both", expand=True)

        cats = {}
        for d in self.estoque.values():
            cat = d.get("categoria","OUTROS")
            cats.setdefault(cat, []).append(d["preco"])
        for cat, ps in sorted(cats.items()):
            tree.insert("", "end", values=(
                cat, len(ps),
                f"R$ {min(ps):.2f}".replace(".",","),
                f"R$ {max(ps):.2f}".replace(".",","),
                f"R$ {sum(ps)/len(ps):.2f}".replace(".",",")))

# ── ENTRY ───────────────────────────────────────────────────────
if __name__ == "__main__":
    ZeOS().mainloop()