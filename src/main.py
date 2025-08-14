import flet as ft
import os

def main(page: ft.Page):
    file_picker = ft.FilePicker()
    page.overlay.append(file_picker)

    class BotaoTema:
        def __init__(self, botao, page, texto, tela, area_arquivos, info_arquivo, linha_divisoria, botao_upload, text_button, icone_select):
            self.icone_do_botao = icone_select
            self.texto_do_botao = text_button
            self.botao_upload = botao_upload
            self.info_arquivo = info_arquivo
            self.linha_divisoria = linha_divisoria
            self.area_arquivos = area_arquivos
            self.botao = botao
            self.tela = tela
            self.texto = texto
            self.page = page
            self.tema_escuro = True

        def alternar_tema(self, e):

            # Light mode
            if self.tema_escuro:
                # Mudança das cores dos elementos do APP
                self.tela.bgcolor = "#9BA8AB"

                self.area_arquivos.bgcolor = "#CCD0CF"
                self.linha_divisoria.content.color = '#778183'
                self.info_arquivo.content.color = ft.Colors.BLACK
                self.botao_upload.bgcolor = "#A1A8AA"

                self.icone_do_botao.color = '#06141B'
                self.texto_do_botao.color = '#06141B'

                self.botao.icon = ft.Icons.MODE_NIGHT
                self.botao.icon_color = '#06141B'
                self.botao.tooltip = 'Modo Escuro'
                self.botao.rotate = ft.Rotate(3.14)
                self.texto.content.color = "#06141B"
                self.tema_escuro = False

            # Dark Mode
            else:
                # Mudança das cores dos elementos do APP
                self.tela.bgcolor = "#06141B"

                self.area_arquivos.bgcolor = "#11212D"
                self.linha_divisoria.content.color = '#050F15'
                self.info_arquivo.content.color = ft.Colors.WHITE
                self.botao_upload.bgcolor = '#0E1B25'

                self.icone_do_botao.color = 'white'
                self.texto_do_botao.color = 'white'

                self.botao.icon = ft.Icons.SUNNY
                self.botao.icon_color = '#ECE360'
                self.botao.tooltip = 'Modo Claro'
                self.botao.rotate = ft.Rotate(-3.14)
                
                self.texto.content.color = 'white'
                self.tema_escuro = True
            # Atualiza as mudanças para ficarem visíveis
            self.page.update()

    # Define a função com o nome correto e parâmetro adequado
    def arquivo_selecionado(e: ft.FilePickerResultEvent):
        if e.files:
            file = e.files[0]
            info_arquivo.content.value = f'Arquivo selecionado: {file.name}'
        else:
            info_arquivo.content.value = 'Nenhum arquivo selecionado.'
        info_arquivo.update()

    # Configuração da página...
    fonte_fira = os.path.join(os.path.dirname(__file__), 'assets', 'FiraCode-Medium.ttf')
    fonte_inter = os.path.join(os.path.dirname(__file__), 'assets', 'Inter.ttf')

    page.fonts = {
        "Fira Code": fonte_fira,
        "Inter": fonte_inter
    }

    page.title = 'Conversor de Arquivos'
    page.window.width = 500
    page.window.height = 700
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 0
    page.margin = 0

    thememode = ft.IconButton(
        icon=ft.Icons.SUNNY, icon_color="#ECE360",
        animate_rotation=ft.Animation(600, 'easeOut')
    )

    texto = ft.Container(
        padding=ft.padding.only(top=30),
        content=
            ft.Text(
                value='Selecione o seu arquivo:',  
                font_family="Fira Code", size=17,
            )  
        )
    
    # - Elementos separados para o controle de cores na alteração de tema
    # - Adicionados ao botao_upload
    icone_select = ft.Icon(ft.Icons.FILE_OPEN, color='white')
    text_button = ft.Text(
                    value='Selecionar',
                    color='white',
                    font_family='Inter'
                    )
    
    botao_upload = ft.ElevatedButton(
            bgcolor="#0E1B25",
            content=ft.Container(
                margin=ft.margin.only(left=15),
                content=ft.Row(
                    controls=[icone_select, text_button]
                )
            ),
            width=150,
            height=50,
            on_click=lambda _: file_picker.pick_files(
                allow_multiple=False,
                file_type=ft.FilePickerFileType.ANY
        )
    )
    

    info_arquivo = ft.Container(
        padding=20,
        margin=ft.margin.only(top=30),
        content=ft.Text(
            value='Nenhum arquivo selecionado.',
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
            color=ft.Colors.WHITE,
            font_family='Inter',
            size=15,
        ),
    )

    linha_divisoria = ft.Container(
        width=445,
        margin=ft.margin.only(top=10),
        content=ft.Divider(thickness=1.5, color="#06141B")
    )

    area_arquivos = ft.Container(
        width=440,
        height=550,
        bgcolor="#11212D",
        border_radius=20,
        alignment=ft.alignment.top_center,
        animate=ft.Animation(500, 'easeInOut'),
        shadow=ft.BoxShadow(
            blur_radius=100,
            color=ft.Colors.BLACK54,
            offset=ft.Offset(3, 3)
        ),
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                texto,
                linha_divisoria,
                info_arquivo,
                ft.Container(
                    margin=ft.margin.only(top=260),
                    content=botao_upload
                )
            ]
        )
    )

    card = ft.Container(
        content=ft.Row(
            controls=[area_arquivos],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

    tela = ft.Container(
        bgcolor="#06141B",
        expand=True,
        animate=ft.Animation(500, 'easeInOut'),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    alignment=ft.alignment.top_right,
                    padding=ft.padding.only(bottom=15, right=20),
                    content=thememode,
                ),
                card,
            ]
        )
    )

    page.add(tela)
    
    # Cria a instância do BotaoTema antes de configurar o file_picker
    botao = BotaoTema(thememode, page, texto, tela, area_arquivos, info_arquivo, linha_divisoria, botao_upload, text_button, icone_select)
    
    # Configura o file_picker com a função correta
    file_picker.on_result = arquivo_selecionado
    
    thememode.on_click = botao.alternar_tema
    page.update()

ft.app(target=main)