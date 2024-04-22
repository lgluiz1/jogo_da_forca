import flet as ft
from time import sleep
from random import choice

contado_verdadeiro = 6
letra_certa = 0

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 350
    page.window_width = 500
    page.window_bgcolor = ft.colors.WHITE
    page.scroll= True
        
    page.fonts = {"PressStart2P": "./fonts/PressStart2P.ttf"}
 # Função para iniciar o jogo
    def inicia(e):
        # Esconde os elementos iniciais
        jogo_inicio.width = 0
        jogo_inicio.height = 0
        botao.text = ""
        botao.icon = ""
        botao.expand = 0
        botao.width = 0
        logo.width = 0
        page.update()
        sleep(3)
        jogo_menu.width = 400
        jogo_menu.height = 300
        menu_opcoes.opacity = 0
        page.update()        
        sleep(3)
        menu_opcoes.width = 300
        menu_opcoes.height =300
        page.update()
        sleep(0.8)
        menu_opcoes.opacity = 1
        page.update()
    def animais(e):
        pass
    
    #Separação e formação das palavras separadas
    def modo_normal(e):
        jogo_menu.width = 0
        jogo_menu.height = 0
        menu_opcoes.opacity = 0
        page.update()
        sleep(3)
        jogo_modo_normal.width = 400
        jogo_modo_normal.height = 300
        page.update()
        sleep(2)
        contador.width = 250
        contador.height = 50
        page.update()
        teminal_teclado.width = 400
        teminal_teclado.height= 250
        sleep(3.5)
        page.update()
        sleep(1.5)
        teminal_teclado.opacity =1
        page.update()
        sleep(1.5)
        teminal_teclado.bgcolor = ft.colors.TRANSPARENT
        #teclado.control.content.color = ft.colors.BLACK
        page.update()
    
    def reinicia(e):
        global contado_verdadeiro, letra_certa, modo_normal_escolha
        # Redefinir as variáveis e configurações necessárias
        contado_verdadeiro = 6
        letra_certa = 0
        modo_normal_escolha = choice(modo_normal_lista).upper()

        # Redefinir o contador e outros elementos relevantes   

    def finalizar(e):
        derrota_01.opacity = 0
        derrota_02.opacity = 0
        derrota_03.opacity = 0
        for letters in terminal_forca:
            text = letters.content
            text.opacity=0
        sleep(1)
        page.update()
        jogo_modo_normal.width = 0
        jogo_modo_normal.height = 0        
        page.update()
        sleep(3)
        novo_jogo_reinicia.width = 300
        novo_jogo_reinicia.height = 150
        page.update()
        sleep(6)

        page.clean()
        # Redefina as variáveis ​​e configurações necessárias para reiniciar o aplicativo
        
        global contado_verdadeiro, letra_certa
        contado_verdadeiro = 6
        letra_certa = 0
        # Outras redefinições necessárias podem ser adicionadas aqui

        # Chame a função principal novamente para reiniciar o aplicativo
        main(page)

    modo_normal_lista = ["cacto", "tijolo", "druida", "xilogravura", "enigma", "futebol", "circo", "hamburguer", "jardim", "jornal", "bife", "xadrez", "enxame", "quimera", "carreta", "queijo", "sucesso", "paralama", "velocidade"]
    modo_normal_escolha = choice(modo_normal_lista).upper()
    terminal_forca = [ft.Container(
        content=ft.Text(value= letras, size=25, weight="bold", color=ft.colors.TRANSPARENT,text_align="center"),
        width=50,
        height=50,
        bgcolor= ft.colors.YELLOW,
        padding=2,
        border_radius= 10,
        opacity=1,
        border=ft.border.Border()
    )   for letras in modo_normal_escolha]

  # Criação dos elementos da interface
    botao = ft.ElevatedButton(text="Inicia Jogo", expand=1, icon="play_circle", on_click=inicia)
    logo = ft.Image(src="./img/logo.png", expand=3)
    botao_objetos = ft.ElevatedButton(text="Modo Normal", icon="sports_esports" , on_click=modo_normal)
    botao_animais = ft.ElevatedButton(text="Modo Animais" , icon="Pets", on_click= animais, disabled=True)
    

  # Contêiner para o botão de início do jogo, o logotipo e a palavra da forca
    menu_inicial = ft.Column(controls=[logo, botao], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment="center", spacing=20)
    menu_opcoes = ft.Column(controls=[
        ft.Row(controls=[ft.Text(value="Escolha Seu Modo de Jogo" , font_family="PressStart2P" ,color=ft.colors.YELLOW)], alignment="center",),
        ft.Row(controls=[ft.Text(value="Palavras Variadas" , font_family="PressStart2P" ,color=ft.colors.RED)], alignment="center",),
        ft.Row(controls=[botao_objetos],alignment="center"),
        ft.Row(controls=[ft.Text(value="Palavras tipos animais", font_family="PressStart2P",color=ft.colors.RED)],alignment="center",),
        ft.Row(controls=[botao_animais],alignment="center")
    ],  alignment="center",
        spacing=20,
        width=300,
        height=300)
    
    valor_contador = ft.Text(value="Você tem 6 chances", color=ft.colors.ORANGE_ACCENT, text_align="center",size=13,weight="bold",font_family="PressStart2P")
    loading_img = ft.Image(src="./img/loading.gif", width=150)
    carregador = ft.Row(controls=[loading_img], alignment="center")
    # Lista de letras do teclado
    derrota_01 = ft.Row(controls=[ft.Text(value="Você Perdeu", color=..., text_align="center",size=13,weight="bold",font_family="PressStart2P"),ft.Image(src="./img/crying-emoji-23.gif", height=25)],width=0,height=0,alignment="center")
    derrota_02 = ft.Row(controls=[ft.Text(value=f"Deseja Joga Novamente?", color=ft.colors.RED, text_align="center",size=13,weight="bold",font_family="PressStart2P")],width=0,height=0,alignment="center")  
    derrota_03 = ft.Row(controls=[ft.ElevatedButton(text="Tenta Novamente", on_click= finalizar)],width=0,height=0,alignment="center" )
    vitoria_01 = ft.Row(controls=[ft.Image(src="./img/3.png", width=200)],alignment="center",width= 0 ,height=0)
    vitoria_img_02 = ft.Row(controls=[ft.Image(src="./img/2.png",width=200)],alignment="center",width= 0 ,height=0)
    vitoria_img_03 = ft.Row(controls=[ft.Image(src="./img/1.png", width=200)],alignment="center",width= 0 ,height=0)
    vitoria_02 = ft.Row(controls=[ft.Text(value=f"Deseja Joga Novamente?", color=ft.colors.RED, text_align="center",size=13,weight="bold",font_family="PressStart2P")],width=0,height=0,alignment="center")  
    vitoria_03 = ft.Row(controls=[ft.ElevatedButton(text="Jogar Novamente", on_click= finalizar)],width=0,height=0,alignment="center" )

    def derrota():
        for contador in terminal_forca:
            text = contador.content
            text.color = ft.colors.RED
            page.update()
            text.color = ft.colors.WHITE
            page.update()
            sleep(1)
            text.color = ft.colors.RED
            page.update()
            text.color = ft.colors.WHITE
            page.update()
            text.color = ft.colors.RED
    def btn_click(e):
        global contado_verdadeiro
        global letra_certa  # Declarando a variável global
        # Configurações de operação do click teclado jogo
        valor_botao = e.control.content.value        
        e.control.bgcolor = "#C7FF8F"
        e.control.content.color = "#B5B5B5"
        e.control.disabled = True
        page.update()
        print(len(modo_normal_escolha))
        
        # Inicializa o contador fora do loop
        
        valor_clicado = False
        
        # Verificação de vogais do jogo
        for letters in terminal_forca:
            text = letters.content  # Acessa o texto dentro do contêiner
            
            # Modifica os atributos conforme necessário
            if text.value == valor_botao:
                letra_certa += 1
                valor_clicado = True
                text.color = ft.colors.RED
                page.update()

         
                # Verifica se a cor é diferente de "red"
        if valor_clicado == True:
            print(letra_certa)
            if len(modo_normal_escolha,) == letra_certa:
                teminal_teclado.opacity = 0
                contador.width = 0
                contador.height = 0
                page.update()
                sleep(1)
                jogo_modo_normal.height = 400
                teminal_teclado.width = 0
                teminal_teclado.height= 0
                jogo_modo_normal.image_src = "./img/confetti.gif"
                page.update()
                sleep(1)
                vitoria_03.height = 50
                vitoria_03.width = 300
                page.update()
                print("Voce Venceu")
                if contado_verdadeiro >= 3:
                    vitoria_01.width = 200
                    vitoria_01.height = 100
                    page.update()
                    print(f"primeiro If ganhou {contado_verdadeiro}")

                if contado_verdadeiro == 2:
                    vitoria_img_02.width = 300
                    vitoria_img_02.height = 100
                    page.update()
                    print(f"segundo If ganhou {contado_verdadeiro}")
                if contado_verdadeiro == 1:
                    vitoria_img_03.width = 300
                    vitoria_img_03.height = 100
                    page.update()
                    print(f"terceiro If ganhou {contado_verdadeiro}")
        else:
            contado_verdadeiro -= 1
            valor_contador.value = f"Você tem {contado_verdadeiro} chances"
            page.update()
            if contado_verdadeiro == 1:
                valor_contador.color = ft.colors.WHITE
                contador.bgcolor=ft.colors.RED_ACCENT
                sleep(1)
                valor_contador.value = f"Ultima chance"
                page.update()
            if contado_verdadeiro == 0:
                valor_contador.opacity = 0
                
                sleep(1)
                page.update()
                contador.width = 0
                contador.height = 0                
                page.update()
                sleep(1)
                page.update()
                teminal_teclado.opacity = 0
                derrota_01.height = 50
                derrota_01.width = 200
                page.update()
                sleep(1)
                teminal_teclado.width = 0
                teminal_teclado.height= 0
                jogo_modo_normal.height = 400
                page.update()
                derrota()
                page.update()
                derrota_02.width = 300
                derrota_02.height = 50                
                sleep(1)
                page.update()
                derrota_03.height = 50
                derrota_03.width = 300
                page.update()
            print("Nao")
            # Verifica se todas as cores são "red"
        
        

        

    teclado_letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]

    teclado = [ft.Container(
        content=ft.Text(value=btn.upper(), weight="bold", size=20,text_align="center", color=...),
        width= 50,
        height= 50,
        bgcolor="#7CFC00",
        border_radius=20,
        padding=7,
        on_click= btn_click,
        disabled=False
    )   for btn in teclado_letras]

    teminal_teclado = ft.Container(content=
                                   ft.Row(controls=teclado, 
                                          wrap=True,
                                          alignment="center"),
                                    width=0,
                                    height=0,
                                    animate=ft.animation.Animation(2000, "bounceOut"),
                                    opacity= 0,
                                    bgcolor="#7CFC00",
                                    border_radius= 10
                                    )
  
  
  # Contêiner principal do jogo
    jogo_inicio = ft.Container(
        content=menu_inicial,
        bgcolor="#7CFC00",
        padding=20,
        width=350,
        height=250,
        border_radius=10,
        animate=ft.animation.Animation(2000, "bounceOut"),
        
    )
    jogo_menu = ft.Container(
        content=menu_opcoes,
        bgcolor="#7CFC00",
        #image_src="./img/fundo_obj.png",
        padding=20,
        width=0,
        height=0,
        border_radius=10,
        animate=ft.animation.Animation(2000, "bounceOut"),
    )
    
    
    
    

    contador = ft.Container(
    content=ft.Column(
        controls=[ft.Row(controls=[valor_contador], alignment="center")],
        alignment="center"
    ),
    width=0,
    height=0,
    bgcolor=ft.colors.YELLOW_ACCENT,
    border_radius=50,
    opacity=1,
    animate=ft.animation.Animation(2000, "bounceOut")
)

    jogo_modo_normal = ft.Container(
    content=ft.Column(
        controls=[
            contador,  # Remova os colchetes extras
            vitoria_01,
            vitoria_img_02,
            vitoria_img_03,
            derrota_01,
            ft.Row(controls=terminal_forca, wrap=True, alignment="center", width="100%"),
            derrota_02,
            derrota_03,
            vitoria_03,
            
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment="center"
    ),
    bgcolor="#7CFC00",
    padding=25,
    width=0,
    height=0,
    border_radius=10,
    image_src= "",
    animate=ft.animation.Animation(2000, "bounceOut")
    )
    novo_jogo_reinicia = ft.Container(
    content=ft.Column(
        controls=[
            carregador            
        ],
        
    ),
    bgcolor="#7CFC00",
    
    width=0,
    height=0,
    border_radius=10,
    image_src= "",
    animate=ft.animation.Animation(2000, "bounceOut")
    )

    page.add(vitoria_img_02,novo_jogo_reinicia,jogo_inicio,jogo_menu,jogo_modo_normal,teminal_teclado)
ft.app(target=main)