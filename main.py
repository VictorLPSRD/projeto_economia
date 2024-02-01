# Framework kivy e kivymd para c5ia estrutura do app.
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.theming import ThemeManager
from kivy.config import Config
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup
Config.set('graphics', 'resizable', False)

# Biblioteca sqllite3 permite ao desenvolvedor interagir com bancos de dados.
# Biblioteca request usada para fazer solicitações HTTP, facilitando a interação com APIs da web e a obtenção de recursos da internet.
import sqlite3
import requests

# Estrutura do front. 
KV = """
ScreenManager:
    id: screen_manager


    Telaentrda:
    Telalogin:
    Telacadastro:
    TelaControlGasto:
    Telaprincipal:
    Telafinancas:
    TelaistalGasto:
    TelaP2:
    Telauser:
    Telarecuperasenha:
    tela_Ipva:



<Telaentrda>:
    name: 'Telaentrada'

    Image:
        source: './src/img/inicial.png'
        size_hint: (3.0, 3.0)
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }  
    
    MDRoundFlatIconButton:
        text: "Claro/Escuro"
        pos_hint: {'center_x': 0.8, 'center_y': 0.95}
        on_release: app.troca_tema()
       

    MDIconButton:
        icon: "chevron-right"
        user_font_size: "35sp"
        pos_hint: {"center_x": .5, "center_y": .12}      
        on_press: app.root.current = 'Telalogin'   
                
<Telalogin>:
    name: 'Telalogin'

    Image:
        source: './src/img/login.png'
        size_hint: (3.0, 3.0)
        pos_hint: {'center_x': 0.5, 'center_y': 0.75 }  

    MDTextField:
        
        id: usuario
        adaptive_size: True
        hint_text: "Usuário"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.50}
        size_hint_x: 0.8
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        
        id: senha
        adaptive_size: True
        hint_text: "Senha"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.38}
        size_hint_x: 0.8
        password: True
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color

    MDRoundFlatIconButton:
        adaptive_size: True
        text: "Entrar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.20 }
        on_press: app.check_credentials()

    MDRoundFlatIconButton:
        adaptive_size: True
        text: "Registrar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10 }
        on_release:
            root.manager.transition.direction = "down"
            root.manager.current = 'Telacadastro'

    MDRectangleFlatIconButton:
        adaptive_size: True
        text: "Recupera senha"
        line_color: 0,0,0,0
        pos_hint: {'center_x': 0.24, 'center_y': 0.30 }
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = 'Telarecuperasenha'


<Telacadastro>:
    name: 'Telacadastro'
   
    MDLabel:
        adaptive_size: True
        text: "Registra !"
        font_style: "H5"
        bold: True
        size_hint: (0.5, 0.8)
        pos_hint: {'center_x': 0.5, 'center_y': .80}
        halign: "center"
        theme_text_color: "Custom"
        text_color: 1, 0, 0, 1  
  
    MDTextField:

        id: usuario_cadastro
        hint_text: "Usuário"
        adaptive_size: True  
        pos_hint: {'center_x': 0.5, 'center_y': 0.70}  
        size_hint_x: 0.8
        icon_right_color: app.theme_cls.primary_color


        

    MDTextField:
        adaptive_size: True
        id: nascimneto
        hint_text: "Data dd/mm/yyyy "
        helper_text: "Insira uma data dd/mm/aaaa válida"
        pos_hint: {'center_x': 0.5, 'center_y': 0.60} 
        size_hint_x: 0.8
        validator: "date"
        date_format: "dd/mm/yyyy"
        date_interval: None, "01/01/2100"
        icon_right: "calendar-range"  
        icon_right_color: app.theme_cls.primary_color

    MDTextField:

        id: email_cadastro
        hint_text: "Email"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.50}  
        size_hint_x: 0.8
        helper_text:"user@gmail.com"
        validator: "email"
        icon_right: "email"  
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        id: senha_cadastro
        hint_text: "Senha"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.40}  
        size_hint_x: 0.8
        password: True
        max_text_length: 20
        icon_right: "lock"  
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        id: c_senha_cadastro
        hint_text: "Confirme Senha"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.30}  
        size_hint_x: 0.8
        password: True
        max_text_length: 20
        icon_right: "lock"  
        icon_right_color: app.theme_cls.primary_color


    MDRoundFlatIconButton:
        text: "Cadastrar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10 }  
        adaptive_size: True
        on_press: app.conectar()  

    MDRectangleFlatIconButton
        adaptive_size: True
        icon: "arrow-left"
        text: " VOLTAR"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "Telalogin" 


<Telarecuperasenha>:
    name:'Telarecuperasenha'

    MDLabel:
        text: 'Recupera Conta'
        font_style:"H5"
        bold: True
        pos_hint: {'center_x': 0.75, 'center_y': 0.82}

    MDRectangleFlatIconButton
        adaptive_size: True
        icon: "arrow-left"
        text: " VOLTAR"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "Telalogin" 

    MDTextField:
        adaptive_size: True
        id: email_recu
        hint_text: "Email"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.30}  
        size_hint_x: 0.8
        mode:"rectangle"
        helper_text:"user@gmail.com"
        validator: "email"
        icon_right: "email"  
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        id: usuario_recu
        hint_text: "Usuário"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.56}
        size_hint_x: 0.8
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        helper_text: "Coloque o nome de usuario que muda. !"
    
    MDTextField:
        id: senha_recu
        hint_text: "Senha"
        password: True
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.43}
        size_hint_x: 0.8
        icon_right: "lock"
        icon_right_color: app.theme_cls.primary_color
        helper_text: "Coloque a senha que deseja mudar. !"

    MDRoundFlatIconButton:
        text: "recuperando"
        pos_hint: {'center_x': 0.5, 'center_y': 0.17 }  
        adaptive_size: True
        on_press: app.recupera_conta()  

<Telaprincipal>: 
    name: 'Telaprincipal'

    MDLabel:
        text: "Moedas Globais"
        icon: 'earth'
        theme_icon_color: "Custom"
        icon_color: "green"
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.7, 'center_y':0.90}

    MDIcon:
        icon: "earth"
        theme_text_color: "Custom"
        text_color: 0, 1, 0, 1  
        pos_hint: {"center_x": 0.85, "center_y": .90}


    MDLabel:
        text: "Criptomoedas"
        icon: 'earth'
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.7, 'center_y':0.55}

    MDIcon:
        icon: "bitcoin"
        size_hint: 0.5,0.5
        theme_text_color: "Custom"
        text_color: 0.8, 0.6, 0.0, 1
        pos_hint: {"center_x": 0.85, "center_y": .55}


    MDFloatingActionButton
        adaptive_size: True
        icon: 'finance'
        pos_hint: {'center_x': 0.2, 'center_y':0.1}
        
    MDFloatingActionButton
        adaptive_size: True
        icon: 'home-circle'
        pos_hint: {'center_x': 0.5, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "TelaP2"

    MDFloatingActionButton
        adaptive_size: True
        icon: 'account'
        pos_hint: {'center_x': 0.8, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "Telauser"

<TelaP2>:   
    name: 'TelaP2' 
    
    MDRectangleFlatIconButton
        icon: "chart-bar"
        adaptive_size: True
        text: "IPVA"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6 }
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = 'IPVA'

    MDRectangleFlatIconButton
        icon: "plus-circle-multiple"
        adaptive_size: True
        text: "Finanças"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5 }
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = 'TelaFinancas'
    
    MDRectangleFlatIconButton
        icon: "book-account-outline"
        adaptive_size: True
        text: "Histórico das Finanças"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4 }
        on_release:
            root.manager.transition.direction = "up"
            root.manager.current = 'TelaistalGasto'


    # botoes de movimentação
    MDFloatingActionButton
        text: 'News'
        adaptive_size: True
        icon: 'finance'
        pos_hint: {'center_x': 0.2, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "Telaprincipal"

    MDFloatingActionButton
        adaptive_size: True
        icon: 'home-circle'
        pos_hint: {'center_x': 0.5, 'center_y':0.1}

    MDFloatingActionButton
        adaptive_size: True
        icon: 'account'
        pos_hint: {'center_x': 0.8, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "Telauser"

<Telauser>: 
    name: 'Telauser'

    Image:
        source: './src/img/user.png'
        size_hint: (1.5, 1.5)
        pos_hint: {'center_x': 0.5, 'center_y': 0.8 }  
    

    # botoes de movimentação
    MDFloatingActionButton
        adaptive_size: True
        icon: 'finance'
        pos_hint: {'center_x': 0.2, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "Telaprincipal"

    MDFloatingActionButton
        adaptive_size: True
        icon: 'home-circle'
        pos_hint: {'center_x': 0.5, 'center_y':0.1}
        on_release:
            root.manager.transition.direction = "right"
            root.manager.current = "TelaP2"

    MDFloatingActionButton
        adaptive_size: True
        icon: 'account'
        pos_hint: {'center_x': 0.8, 'center_y':0.1}

    MDRectangleFlatIconButton:
        adaptive_size: True
        text: "Sair"
        line_color: 0,0,0,0
        pos_hint: {'center_x': 0.28, 'center_y': 0.40 }
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = 'Telalogin'


<TelaFinancas>: 
    name: 'TelaFinancas'


    MDLabel:
        text: "Finanças"
        font_style: 'H5'
        bold: True
        size_hint: 0.7,0.7
        adaptive_size: True
        pos_hint: {"center_x": 0.5, "center_y": .8}


    MDTextField:

        id: nome_gasto
        hint_text: "Nome da finança"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.60}  
        size_hint_x: 0.8
        text_color: 1, 1, 1, 1 
        icon_right: "account"  
        icon_right_color: app.theme_cls.primary_color

    MDTextField:
        id: data_gasto
        hint_text: "Data dd/mm/yyyy "
        helper_text: "Insira uma data dd/mm/aaaa válida"
        pos_hint: {'center_x': 0.5, 'center_y': 0.50} 
        size_hint_x: 0.8
        validator: "date"
        date_format: "dd/mm/yyyy"
        date_interval: None, "01/01/2100"
        text_color: 1, 1, 1, 1 
        icon_right: "calendar-range"  
        icon_right_color: app.theme_cls.primary_color


    MDTextField:
        id: valor
        hint_text: "Valor do gasto"  
        pos_hint: {'center_x': 0.5, 'center_y': 0.40}  
        size_hint_x: 0.8
        max_text_length: 20
        text_color: 1, 1, 1, 1 
        icon_right: "lock"  
        icon_right_color: app.theme_cls.primary_color


    MDRoundFlatIconButton:
        text: "Cadastrar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10 }  
        adaptive_size: True
        on_press: app.registro_financas()  

    MDRectangleFlatIconButton
        adaptive_size: True
        icon: "arrow-left"
        text: " VOLTAR"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "TelaP2" 


<TelaistalGasto>: 
    name: 'TelaistalGasto'

    MDScrollView:
        size_hint: (0.5, None)
        height: root.height
    
    MDLabel:
        text: "Nome"
        pos_hint: {'center_x': 0.15, 'center_y': 0.87 }  
        adaptive_size: True
        

    MDLabel:
        text: "Valor"
        pos_hint: {'center_x': 0.50, 'center_y': 0.87 }  
        adaptive_size: True

    MDLabel:
        text: "Data"
        pos_hint: {'center_x': 0.80, 'center_y': 0.87 }  
        adaptive_size: True
            

    MDRectangleFlatIconButton
        adaptive_size: True
        icon: "arrow-left"
        text: " VOLTAR"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "TelaP2" 

    MDRoundFlatIconButton:
        text: "Listar"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10 }  
        adaptive_size: True
        on_press: app.lista_gasto()

<tela_Ipva>: 
    name: 'IPVA'

    MDRectangleFlatIconButton
        adaptive_size: True
        icon: "arrow-left"
        text: " VOLTAR"
        pos_hint: {'center_x': 0.2, 'center_y': 0.95}
        on_release:
            root.manager.transition.direction = "left"
            root.manager.current = "TelaP2"

    
    MDLabel:
        text: " Calcula o valor do IPVA"
        icon: 'earth'
        theme_icon_color: "Custom"
        icon_color: "green"
        font_style: 'H5'
        bold: True
        pos_hint: {'center_x': 0.7, 'center_y':0.88}

        
    
    MDLabel:
        text: "Informe o valor venal do veículo:"
        icon: 'earth'
        theme_icon_color: "Custom"
        icon_color: "green"
        pos_hint: {'center_x': 0.55, 'center_y':0.80}

    MDTextField:
        
        id: valor_venal
        adaptive_size: True
        hint_text: "valor_venal"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.73}
        size_hint_x: 0.8
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color

    
    MDLabel:
        text: "Informe a alíquota do estado (em percentual):"
        icon: 'earth'
        theme_icon_color: "Custom"
        icon_color: "green"
        pos_hint: {'center_x': 0.55, 'center_y':0.62}

    MDLabel:
        text: "OBS: Utilizar ponto ao inves de virgula"
        icon: 'earth'
        theme_icon_color: "Custom"
        icon_color: "green"
        pos_hint: {'center_x': 0.58, 'center_y':0.58}

    MDTextField:
        
        id: aliquota_estado
        adaptive_size: True
        hint_text: "aliquota_estado"
        mode:"rectangle"
        pos_hint: {'center_x': 0.5, 'center_y': 0.50}
        size_hint_x: 0.8
        icon_right: "account"
        icon_right_color: app.theme_cls.primary_color

    MDRoundFlatIconButton:
        text: "Calcular"
        pos_hint: {'center_x': 0.5, 'center_y': 0.10 }  
        adaptive_size: True
        on_press: app.ipva() 
            
"""
# Criação de class para gera novas telas.

class tela_Ipva(MDScreen):
    pass

class Telaentrda(MDScreen):
    pass

class Telalogin(MDScreen):
    pass
 
class Telacadastro(MDScreen):
    pass

class Telarecuperasenha(MDScreen):
    pass

class TelaMenu(MDScreen):
    pass

class TelaControlGasto(MDScreen):
    pass

class TelaistalGasto(MDScreen):
    pass

class Telaprincipal(MDScreen):
    pass

class TelaCotacao(MDScreen):
    pass

class Telafinancas(MDScreen):
    pass

class TelaConverte(MDScreen):
    pass

class TelaP2(MDScreen):
    pass

class Telauser(MDScreen):
    pass


class MainApp(MDApp):
    theme_cls = ThemeManager()

    def build(self):
        self.Telalogin = Builder.load_string(KV)
        self.theme_cls.theme_style_switch_animation = True
        self.theme_cls.theme_style = "Dark" 
        self.theme_cls.primary_palette="Red"
        Window.size = (350, 580)

        return self.Telalogin
    
    def troca_tema(self):

        self.theme_cls.theme_style = (
            "Dark" if self.theme_cls.theme_style == "Light" else "Light"
        )
    
    def conectar(self):
        # Conectar ao banco de dados SQLite3
        conn = sqlite3.connect('usuario.db')
        cursor = conn.cursor()

        # Obtendo dados dos campos de entrada da tela de cadastro !
        usuario_cadastrado = self.Telalogin.get_screen('Telacadastro').ids.usuario_cadastro.text
        nascimento = self.Telalogin.get_screen('Telacadastro').ids.nascimneto.text
        email_cadastrado = self.Telalogin.get_screen('Telacadastro').ids.email_cadastro.text
        senha_cadastrada = self.Telalogin.get_screen('Telacadastro').ids.senha_cadastro.text
        senha_confirmada = self.Telalogin.get_screen('Telacadastro').ids.email_cadastro.text

        # Inserir dados no banco de dados
        cursor.execute("""
            INSERT INTO usuarios(nome, nascimento, email, senha, con_senha)
            VALUES (?,?, ?, ?, ?)""", (usuario_cadastrado, nascimento, email_cadastrado, senha_cadastrada, senha_confirmada))
        
        # Mensagem de castro feito com sucesso !
        cadastro=Label(text='Cadastro bem-sucedido,', pos=(15, -170))
        aviso=Label(text=' volte para tela de login !', pos=(15, -190))
        screen = self.root.get_screen('Telacadastro')
        screen.add_widget(cadastro)
        screen.add_widget(aviso)

        # Apagando as Label depois de um tempo.
        Clock.schedule_once(lambda dt: screen.remove_widget(cadastro), 10)
        Clock.schedule_once(lambda dt: screen.remove_widget(aviso), 10)

        # Limpa dados da tela de Cadastro !
        self.Telalogin.get_screen('Telacadastro').ids.usuario_cadastro.text = ("")  
        self.Telalogin.get_screen('Telacadastro').ids.nascimneto.text = ("")  
        self.Telalogin.get_screen('Telacadastro').ids.email_cadastro.text = ("")
        self.Telalogin.get_screen('Telacadastro').ids.senha_cadastro.text = ("")
        self.Telalogin.get_screen('Telacadastro').ids.email_cadastro.text = ("")

        # Confirmar as alterações e fechar a conexão
        conn.commit()
        conn.close()

    def recupera_conta(self):

        # Obtendo os dados dos campos de entrada da tela recupera usuario!
        usuario_recu = self.Telalogin.get_screen('Telarecuperasenha').ids.usuario_recu.text
        senha_recu = self.Telalogin.get_screen('Telarecuperasenha').ids.senha_recu.text
        email_recu = self.Telalogin.get_screen('Telarecuperasenha').ids.email_recu.text

        print(f"{usuario_recu,senha_recu,email_recu}")

        # Conectando ao banco de dados
        conn = sqlite3.connect('usuario.db')
        cursor = conn.cursor()

        # Executando a consulta SQL para atualizar os dados do usuário
        cursor.execute("""
        UPDATE usuarios
        SET nome = ?,
            senha = ?
        WHERE email = ?
    """, (usuario_recu, senha_recu, email_recu))

        # Mensagem de castro feito com sucesso !
        aviso1=MDLabel(text='Dados atualizados com sucesso,', pos=(55, -240))
        aviso2=MDLabel(text='Você já pode entra na sua conta,', pos=(50, -260))
        aviso3=MDLabel(text='com as novas credencias !', pos=(50, -280))
        screen = self.root.get_screen('Telarecuperasenha')
        screen.add_widget(aviso1)
        screen.add_widget(aviso2)
        screen.add_widget(aviso3)
        
        # Commit para salvar as alterações no banco de dados
        conn.commit()

        # Fechar a conexão com o banco de dados
        conn.close()


    def check_credentials(self):
        # Obtenha os valores dos campos de entrada de usuário e senha que ficam no Telalogin 
        usuario_input = self.Telalogin.get_screen('Telalogin').ids.usuario.text
        senha_input = self.Telalogin.get_screen('Telalogin').ids.senha.text

        conn = sqlite3.connect('usuario.db')
        cursor = conn.cursor()

        # Limpe os campos da tela de login !
        self.Telalogin.get_screen('Telalogin').ids.usuario.text = ''
        self.Telalogin.get_screen('Telalogin').ids.senha.text = ''

        cursor.execute("""SELECT * FROM usuarios WHERE nome = ? AND senha = ?""", (usuario_input, senha_input))
        

        result = cursor.fetchone()
        
        try:
            if result:
                # Credenciais corretas, mude para a tela 'Telaprincipal'
                self.Telalogin.get_screen('Telalogin').manager.current = "Telaprincipal"

                # Pegando os dados do usuario.
                conn = sqlite3.connect('usuario.db')
                cursor = conn.cursor()

                cursor.execute("""SELECT nome, email, nascimento FROM usuarios WHERE nome = ? AND senha = ?""", (usuario_input, senha_input))
                result = cursor.fetchone()

                nome,email,nascimento = result

                #jogando na tela de usuario
                erro=MDLabel(text=f'usuario: {nome}\nNascimento: {nascimento}\nEmail: {email}', pos=(40, 65))
                screen = self.root.get_screen('Telauser')
                screen.add_widget(erro)

                conn.commit()
                conn.close()

                # pegando dados da tabela usuario
                conn = sqlite3.connect('usuario.db')
                cursor = conn.cursor()

                # Pegando soma dos gastos 
                cursor.execute("""SELECT SUM(valor_gasto) FROM financeiro""")
                
                resultados = cursor.fetchall()
                # Colocando essa soma na tela user.
                screen = self.root.get_screen('Telauser')

                #Adicionando e criando uma label para coloca na tela user.
                soma=resultados
                soma = f'Gasto total: {soma}'
                soma = MDLabel(text=soma, pos=(39,25))
                screen.add_widget(soma)
            
         

            else :
                # Credenciais incorretas, você pode exibir uma mensagem de erro
                erro = Label(text='Credenciais incorretas.', pos=(30, 40))
                screen = self.root.get_screen('Telalogin')
                screen.add_widget(erro)

                # Configura um temporizador para remover o widget de erro após 20 segundos
                Clock.schedule_once(lambda dt: screen.remove_widget(erro), 20)

                conn.close()

        except  sqlite3.Error as e: 
            # Em caso de erro no SQLite, exibir um pop-up de alerta
            texto = f"Erro na função credentials {e}"
            popup = Popup(title='Alerta', content=Label(text=texto), size_hint=(None, None), size=(300, 200))
            popup.open()  # Abre o pop-up

    def dismiss_popup(self, instance):
        # Método para fechar o pop-up
        instance.parent.parent.dismiss()

    def registro_financas(self):
        try:
            conn = sqlite3.connect('usuario.db')
            cursor = conn.cursor()

            # Obtendo dados dos campos de entrada da tela de Financas !
            nome_gasto = self.Telalogin.get_screen('TelaFinancas').ids.nome_gasto.text
            valor_gasto = self.Telalogin.get_screen('TelaFinancas').ids.valor.text
            data_gasto = self.Telalogin.get_screen('TelaFinancas').ids.data_gasto.text
        
            print(nome_gasto)
            print(valor_gasto)
            print(data_gasto)
        
            # Inserir dados no banco de dados
            cursor.execute("""
                INSERT INTO financeiro(nome_gasto, valor_gasto, data)
                VALUES (?,?,?)""", (nome_gasto , valor_gasto, data_gasto))


            conn.commit()
            conn.close()
        except  sqlite3.Error as e:
             # Em caso de erro no SQLite, exibir um pop-up de alerta
            texto = f"Erro na função credentials {e}"
            popup = Popup(title='Alerta', content=Label(text=texto), size_hint=(None, None), size=(300, 200))
            popup.open()  # Abre o pop-up

    def lista_gasto(self):
        try:
            conn = sqlite3.connect('usuario.db')
            cursor = conn.cursor()

            cursor.execute("""SELECT nome_gasto, valor_gasto, data FROM financeiro""")
            resultados = cursor.fetchall()
            espaço = 190

            # Verifique se há resultados antes de prosseguir
            if resultados:
                screen = self.root.get_screen('TelaistalGasto')
                
                for resultado in resultados:

                    # Adicione 20 ao valor de espaço para a próxima iteração
                    espaço -= 22

                    # Aqui você pode acessar os dados específicos da linha
                    nome_gasto, valor_gasto, data = resultado

                    # Crie o rótulo MDLabel com os dados desejados
                    texto = f'{nome_gasto}'
                    texto1 = f'{valor_gasto}'
                    texto2 = f'{data}'
                    text = MDLabel(text=texto, pos=(30, espaço))
                    text1 = MDLabel(text=texto1, pos=(160, espaço))
                    text2 = MDLabel(text=texto2, pos=(250, espaço))
                    
                    # Adicione o rótulo à tela
                    screen.add_widget(text)
                    screen.add_widget(text1)
                    screen.add_widget(text2)

                    
            else:
                print("Nenhum resultado encontrado.")
                erro = Label(text="Nenhum resultado encontrado.", pos=(30, 40))
                screen = self.root.get_screen('TelaistalGasto')
                screen.add_widget(erro)

                # Configura um temporizador para remover o widget de erro após 20 segundos
                Clock.schedule_once(lambda dt: screen.remove_widget(erro), 20)

            conn.close()

        except sqlite3.Error as e:
            print(f"Erro na função credentials {e} ")
            popup = Popup(title='Alerta', content=Label(text=texto), size_hint=(None, None), size=(300, 200))
            popup.open()  # Abre o pop-up

    def on_start(self):
        self.pegando_dados()  # Chamando a função para obter os dados

    def ipva(self):
        try:
            # Pegando os dados da tela de 'IPVA'.
            aliquota = self.Telalogin.get_screen('IPVA').ids.valor_venal.text
            valor_venal = self.Telalogin.get_screen('IPVA').ids.aliquota_estado.text
            # Trocando a tipagem dos dados para fazer calculo.
            valor_venal = float(valor_venal)
            aliquota = float(aliquota)
            ipva = valor_venal * (aliquota / 100)
            # Exibindo a informação 
            c_ipva = Label(text=f"O valor do IPVA a ser pago é: R$ {ipva} $.", pos=(10,-140),bold=True)
            screen = self.root.get_screen('IPVA')
            screen.add_widget(c_ipva)

        except:
            erro = Label(text=f"Coloque os valores nos campos", pos=(10,-140),bold=True)
            screen = self.root.get_screen('IPVA')
            screen.add_widget(erro)

             # Configura um temporizador para remover o widget de erro após 5 segundos
            Clock.schedule_once(lambda dt: screen.remove_widget(erro), 5)

            
        
        
 
    def pegando_dados(self):
        # Retorna atualizações a cada 30 minutos !
        url = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL,GBP-BRL,JPY-BRL,BTC-BRL,RUB-BRL,BTC-BRL,ETH-BRL,XRP-BRL,LTC-BRL,DOGE-BRL')
        url_format = url.json()

        dolar_hoje = url_format['USDBRL']['bid']
        dolar_variação = url_format['USDBRL']['varBid']
        label = MDLabel(text=f"*Cotação do Dólar hoje: {dolar_hoje} Variação: {dolar_variação}",pos=(20, 180),font_style='Caption')

        euro_hj = url_format['EURBRL']['bid']
        euro_variação = url_format['EURBRL']['varBid']
        label1 = MDLabel(text=f"*Cotação do Euro hoje: {euro_hj} Variação: {euro_variação}",pos=(20, 160),font_style='Caption')

        peso_hj = url_format['ARSBRL']['bid']
        peso_variação = url_format['ARSBRL']['varBid']
        label2 = MDLabel(text=f"*Cotação do pesso hoje: {peso_hj} Variação: {peso_variação}",pos=(20, 140),font_style='Caption')

        libra_hj = url_format['GBPBRL']['bid']
        libra_variação= url_format['GBPBRL']['varBid']
        label3 = MDLabel(text=f"*Cotação do Libra hoje: {libra_hj} Variação: {libra_variação}",pos=(20, 120),font_style='Caption')

        rublo_hj = url_format['RUBBRL']['bid']
        rublo_variação= url_format['RUBBRL']['varBid']
        label4 = MDLabel(text=f"*Cotação do Rublo Russo hoje: {rublo_hj} Variação: {rublo_variação}",pos=(20, 90),font_style='Caption')

        bit_hj = url_format['BTCBRL']['bid']
        bit_variação= url_format['BTCBRL']['varBid']
        label5 = MDLabel(text=f"*Cotação do Bitcoin hoje: {bit_hj} Variação: {bit_variação}",pos=(20, -20),font_style='Caption')

        eth_hj = url_format['ETHBRL']['bid']
        eth_variação= url_format['ETHBRL']['varBid']
        label6 = MDLabel(text=f"*Cotação do Ethereum hoje: {eth_hj} Variação: {eth_variação}",pos=(20, -40),font_style='Caption')

        xrp_hj = url_format['XRPBRL']['bid']
        xrp_variação= url_format['XRPBRL']['varBid']
        label7 = MDLabel(text=f"*Cotação do Ripple hoje: {xrp_hj} Variação: {xrp_variação}",pos=(20, -60),font_style='Caption')

        LTC_hj = url_format['LTCBRL']['bid']
        LTC_variação= url_format['LTCBRL']['varBid']
        label8 = MDLabel(text=f"*Cotação do Litecoin hoje: {LTC_hj} Variação: {LTC_variação}",pos=(20, -80),font_style='Caption')

        DOG_hj = url_format['DOGEBRL']['bid']
        DOG_variação= url_format['DOGEBRL']['varBid']
        label9 = MDLabel(text=f"*Cotação do Dogecoin hoje: {DOG_hj} Variação: {DOG_variação}",pos=(20, -110),font_style='Caption')

        # Adicionando as labels à TelaPrincipal
        screen = self.root.get_screen('Telaprincipal')
        screen.add_widget(label)
        screen.add_widget(label1)
        screen.add_widget(label2)
        screen.add_widget(label3)
        screen.add_widget(label4)
        screen.add_widget(label5)
        screen.add_widget(label6)
        screen.add_widget(label7)
        screen.add_widget(label8)
        screen.add_widget(label9)

if __name__ == '__main__':
    MainApp().run()