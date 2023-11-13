import os
import flet as ft
import time
import configparser
import script
import script_acacia
from random import randrange as r
from time import sleep
import util as utl
import psycopg2

import update_sequence, read_file, config_db

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
entidade = cfg['DEFAULT']['NomeEntidade']
empresa = 'Sysmar' #Acácia
sql_ini = 'script_sysmar.ini'
def pages(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_center()
    page.title = "Export Frotas "+str(empresa + entidade) + " V_3.0.1"
    progressBar = ft.ProgressBar(width=700, color=ft.colors.DEEP_ORANGE)

    def start(host='localhost', database=cfg['DEFAULT']['NomeBanco'], user=cfg['DEFAULT']['user'], password= cfg['DEFAULT']['password'], port = cfg['DEFAULT']['port'], comandos=''):

        if not os.path.exists(txt_local_arquivos.value):
            os.makedirs(txt_local_arquivos.value)

        try:
            dados_conexao = psycopg2.connect(
                host=host,
                database=database,
                user=user,
                password=password,
                port=port
            )

        except Exception as e:
            return e
        page.update()
        cur = dados_conexao.cursor()
        # page.add(txt_header)
        list_arquivos.clean()
        # page.add(progressBar)
        com_dados = 0
        sem_dados = 0
        step = 0
        while True:
            for comando in comandos:
                step+=1
                list_arquivos.update()
                list_arquivos.controls.append(ft.Text(f'{step}° Arquivo: ' + comando + ' iniciado em ' + time.strftime("%d/%m/%y %H:%M:%S"), size=16, color=ft.colors.GREEN))
                cur.execute(comandos[comando])
                result = cur.fetchall()
                arquivo = open(
                    txt_local_arquivos.value + comando + '_' + txt_entidade.value + '.txt', "w",
                    newline='', encoding='ANSI')

                for inf in result:
                    arquivo.write(str(inf[0]).replace('#sec#', str(r(0, 5)) + str(r(0, 9))) + '\n')
                if len(result) < 1:
                    list_arquivos.controls.append(ft.Text('  ❗ Finalizado em ' + time.strftime("%d/%m/%y %H:%M:%S"), size=16, color=ft.colors.ORANGE))
                    sem_dados+=1
                else:
                    list_arquivos.controls.append(ft.Text('  ✅ Finalizado em ' + time.strftime("%d/%m/%y %H:%M:%S"), size=16))
                    com_dados+=1
                for i in range(0, len(comandos)+1):
                    progressBar.value = step / len(comandos)
                    txt_header.value=(f'{step} arquivos Gerados [Com dado: {com_dados}/ Vazio: {sem_dados}]')
                    page.update()
                sleep(0.3)
                page.update()

            dados_conexao.close()
            cur.close()
            time.sleep(2)
            break
    def btn_click(e):
        # sqls = script.Script()
        # sqls = script_acacia.Script()
        # comandos = sqls.query(txt_entidade.value)
        comandos = utl.Util().obter_secao_configuracao(sql_ini)
        
        if not txt_database.value:
            txt_database.error_text = "Informe o caminho do Banco"
            page.update()
        else:
            page.update()
            txt_header.value = 'Sistema preparado para gerar arquivos...'
            database = txt_database.value
            utl.Util().update_cfg(new=txt_entidade.value)
            host= txt_host.value
            user= txt_user.value
            port= txt_port.value
            password= txt_password.value

            log = start(host=host, port=port, user=user, password=password, database=database, comandos=comandos)
            if log != None:
                list_arquivos.update()
                txt_header.value = log
                list_arquivos.controls.clear()
                progressBar.value=0
                progressBar.update()
                if not progressBar:
                    progressBar.update()

            page.update()
    def atualizar_sequence(e):
        atualiza = update_sequence.Update_sequence()
        list_sequencia.controls.clear()
        page.add(txt_header)
        if not txt_database_sequence.value:
            txt_database_sequence.error_text = "Informe o caminho do Banco"
            page.update()
        else:
            database_sequence = txt_database_sequence.value
            host_sequence = txt_host_sequence.value
            user_sequence = txt_user_sequence.value
            port_sequence = txt_port_sequence.value
            password_sequence = txt_password_sequence.value

            status, msg = atualiza.atualiza_sequence(host=host_sequence, port=port_sequence, user=user_sequence, password=password_sequence, database=database_sequence)
            if atualiza:
                atualizados = []
                for m in msg:
                    sleep(0.1)
                    if m[0] != None:
                        txt_header.value = "\n" + str(m[0])
                        page.update()
                        atualizados.append(str(m[0]))
                        list_sequencia.controls.append(ft.Text(f"✅ Sequência atualizada: {m[0]}", size=16))
            else:
                txt_header.value = "As sequências não foram atualizadas, verifique manualmente!\n " + str(msg)
            page.add(txt_header)
            txt_header.value = f"✅ Sequências atualizadas com sucesso"
            page.update()
    def gerar_arquivos_simam(e):
        list_arquivos.controls.clear()

        reade_file = read_file.Read_file()

        if not txt_caminho_arquivo_sim_am.value or not txt_caminho_arquivo_sim_am_destino.value:
            txt_header.value = " ⛔ Informe os caminhos de origem e destino dos arquivos."
            page.update()
        else:

            status_1 = reade_file.buscar_arquivo_hodometro_horimetro(txt_caminho_arquivo_sim_am.value + '/', txt_caminho_arquivo_sim_am_destino.value + '/',txt_entidade_arquivo_sim_am.value)
            status_2 = reade_file.buscar_arquivo_consumo(txt_caminho_arquivo_sim_am.value + '/', txt_caminho_arquivo_sim_am_destino.value + '/',txt_entidade_arquivo_sim_am.value)

            txt_header.value = 'Arquivo HodometroHorimetro ➡️' + str(status_1)+ '✅' + '\nArquivo Consumo ➡️' + str(status_2) +'✅'
            page.update()

    def config_produtos(e):
        host = 'localhost'
        database = cfg['DEFAULT']['NomeBanco']
        user = cfg['DEFAULT']['user']
        password = cfg['DEFAULT']['password']
        port = cfg['DEFAULT']['port']

        dados_conexao = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port
        )
        cur = dados_conexao.cursor()
        cur.execute(f""" select combcod, combdes from fro_comb """)
        result_origem = cur.fetchall()

        #Listar produtos na origem
        lista_produtos_oriegm = []
        for i in result_origem:
            lista_produtos_oriegm.append(i)

        produto_origem.value=lista_produtos_oriegm[0]
        produto_origem_2.value = lista_produtos_oriegm[1]
        produto_origem_3.value = lista_produtos_oriegm[2]
        produto_origem_4.value = lista_produtos_oriegm[3]
        page.update()
        if not txt_database_produtos.value:
            txt_database_produtos.error_text = "Informe o caminho do Banco"
            page.update()
        else:
            database_produtos = txt_database_produtos.value
            host_produtos = txt_host_produtos.value
            user_produtos = txt_user_produtos.value
            port_produtos = txt_port_produtos.value
            password_produtos = txt_password_produtos.value
            conf_db = config_db.ConfigDB()

            result = conf_db.produtos(host=host_produtos, port=port_produtos, user=user_produtos, password=password_produtos, database=database_produtos)

            drop_down_produto.options.clear()

            for i in result[0]:
                drop_down_produto.options.append(ft.dropdown.Option(i))
                drop_down_produto_2.options.append(ft.dropdown.Option(i))
                drop_down_produto_3.options.append(ft.dropdown.Option(i))
                drop_down_produto_4.options.append(ft.dropdown.Option(i))
                page.update()

            novo_produto.value = drop_down_produto.value
            novo_produto_2.value = drop_down_produto_2.value
            novo_produto_3.value = drop_down_produto_3.value
            novo_produto_4.value = drop_down_produto_4.value
            novo_produto.update()


    page.add(ft.Text(f"Exportador {empresa} para Sistema de Frotas", size=20, color='blue'))
    header_frotas = ft.Text("Gerador de Arquivos das Frotas", size=20, color='blue')
    txt_entidade = ft.TextField(label="Entidade", text_size=12, value=cfg['DEFAULT']['CodEntidade'], width=100, height=35, disabled=False, tooltip='Alterar o código de entidade, tambem altera o arquivo "cfg.ini"')
    txt_host = ft.TextField(label="Host", text_size=12, value=cfg['DEFAULT']['Host'], width=100, height=35)
    txt_user = ft.TextField(label="User", text_size=12, value=cfg['DEFAULT']['User'], width=250, height=35)
    txt_password = ft.TextField(label="Password", text_size=12, value=cfg['DEFAULT']['password'], width=130, height=35,password=True, can_reveal_password=True)

    txt_database = ft.TextField(label="Nome do Banco", value=cfg['DEFAULT']['NomeBanco'], text_size=12, height=40, width=200)
    txt_local_arquivos = ft.TextField(label="Caminho dos Arquivos gerados", value=cfg['DEFAULT']['DiretorioArquivos'], text_size=12, height=40, width=700)
    origem_destino = ft.Row([txt_database, txt_local_arquivos])
    txt_port = ft.TextField(label="Porta", text_size=12, value=cfg['DEFAULT']['port'], width=100, height=30)
    txt_header = ft.Text('Sistema preparado para gerar arquivos...')
    dados_banco = ft.Row([txt_entidade, txt_host, txt_port, txt_user, txt_password])
    btn_gerar_arquivos = ft.ElevatedButton("Gerar Arquivos", on_click=btn_click, icon=ft.icons.ADD_BOX)
    list_arquivos = ft.ListView(expand=1, spacing=2, padding=20, auto_scroll=True)
    list_sequencia = ft.ListView(expand=1, spacing=2, padding=20, auto_scroll=True)
    divisor = ft.Divider(height=2, thickness=3)
    header_simam = ft.Text("Gerador de Arquivos Sim Am", size=20, color='blue')
    txt_caminho_arquivo_sim_am = ft.TextField(label="Caminho do Arquivo SimAm", text_size=12, width=540, height=30)
    txt_caminho_arquivo_sim_am_destino = ft.TextField(label="Destino Arquivo SimAm", text_size=12, width=700, height=30)
    txt_entidade_arquivo_sim_am = ft.TextField(label="Entidade SimAm", value=cfg['DEFAULT']['codentidade'], text_size=12, height=30, width=150)
    dados_caminho_simAm = ft.Row([txt_entidade_arquivo_sim_am, txt_caminho_arquivo_sim_am])
    btn_gerar_arquivos_simam = ft.Row([ft.ElevatedButton("Gerar Arquivos do Sim Am", on_click=gerar_arquivos_simam, icon=ft.icons.PAGES)])
    header_sequence = ft.Text("Atualiza Sequências", size=20, color='blue')
    txt_host_sequence = ft.TextField(label="Host", text_size=12, value='localhost', width=100, height=40)
    txt_user_sequence = ft.TextField(label="User", text_size=12, value='sysdba', width=100, height=40)
    txt_password_sequence = ft.TextField(label="Password", text_size=12, value='masterkey', width=130, height=40,password=True, can_reveal_password=True)
    txt_database_sequence = ft.TextField(label="Caminho do Banco para nova sequência", value=cfg['DEFAULT']['NomeBancoSequence'], text_size=12, height=40, width=776)
    txt_port_sequence = ft.TextField(label="Porta", text_size=12, value=3050, width=100, height=40)
    dados_banco_sequencia = ft.Row([txt_host_sequence, txt_port_sequence, txt_user_sequence, txt_password_sequence])
    btn_atualizar_sequencia = ft.Row([ft.ElevatedButton("Atualizar Sequências", on_click=atualizar_sequence, icon=ft.icons.SETTINGS)])

    header_configuracoes = ft.Text("Configuração e manutenção de dados", size=20, color='blue')
    txt_host_produtos = ft.TextField(label="Host", text_size=12, value='localhost', width=100, height=40)
    txt_user_produtos = ft.TextField(label="User", text_size=12, value='sysdba', width=100, height=40)
    txt_password_produtos = ft.TextField(label="Password", text_size=12, value='masterkey', width=130, height=40,password=True, can_reveal_password=True)
    txt_database_produtos = ft.TextField(label="Caminho do Banco origem produtos",value=cfg['DEFAULT']['NomeBancoSequence'], text_size=12, height=40, width=776)
    txt_port_produtos = ft.TextField(label="Porta", text_size=12, value=3050, width=100, height=40)
    dados_banco_produtos = ft.Row([txt_host_produtos, txt_port_produtos, txt_user_produtos, txt_password_produtos])
    btn_buscar_produtos = ft.Row([ft.ElevatedButton("Buscar Produtos", on_click=config_produtos, icon=ft.icons.SEARCH)])
    drop_down_produto = ft.Dropdown(width=400)
    drop_down_produto_2 = ft.Dropdown(width=400)
    drop_down_produto_3 = ft.Dropdown(width=400)
    drop_down_produto_4 = ft.Dropdown(width=400)
    produto_origem = ft.Text(size=20)
    produto_origem_2 = ft.Text(size=20)
    produto_origem_3 = ft.Text(size=20)
    produto_origem_4 = ft.Text(size=20)
    novo_produto = ft.Text(size=20)
    novo_produto_2 = ft.Text(size=20)
    novo_produto_3 = ft.Text(size=20)
    novo_produto_4 = ft.Text(size=20)
    linha_produto = ft.Row([produto_origem, drop_down_produto, novo_produto])
    linha_produto_2 = ft.Row([produto_origem_2, drop_down_produto_2, novo_produto_2])
    linha_produto_3 = ft.Row([produto_origem_3, drop_down_produto_3, novo_produto_3])
    linha_produto_4 = ft.Row([produto_origem_4, drop_down_produto_4, novo_produto_4])

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Gerar Arquivos Frotas",
                icon=ft.icons.CAR_REPAIR,
                content=ft.Container(
                    content=ft.Column([header_frotas, divisor, dados_banco, origem_destino, btn_gerar_arquivos, txt_header,progressBar, list_arquivos]), alignment=ft.alignment.center,padding=15
                ),
            ),
            ft.Tab(
                text="Arquivos Sim Am",
                icon=ft.icons.SEARCH,
                content=ft.Container(
                    content=ft.Column([header_simam, divisor, dados_caminho_simAm,txt_caminho_arquivo_sim_am_destino, btn_gerar_arquivos_simam]), alignment=ft.alignment.center,padding=15
                ),
            ),
            ft.Tab(
                text="Atualizar Sequências",
                icon=ft.icons.SETTINGS,
                content=ft.Container(
                    content=ft.Column([header_sequence, divisor, dados_banco_sequencia, txt_database_sequence, btn_atualizar_sequencia, list_sequencia]), alignment=ft.alignment.center, padding=15
                ),
            ),
            ft.Tab(
                text="Configurações",
                icon=ft.icons.TABLE_VIEW,
                content=ft.Container(
                    content=ft.Column([header_configuracoes, divisor, dados_banco_produtos, txt_database_produtos, btn_buscar_produtos, linha_produto, linha_produto_2, linha_produto_3, linha_produto_4]), alignment=ft.alignment.center, padding=15
                ),
            ),
        ],
        expand=1,
    )

    page.add(t)
    # list_arquivos = ft.ListView(expand=1, spacing=2, padding=20, auto_scroll=True)

if __name__ == "__main__":
    # ft.app(port=3636, target=main, view=ft.WEB_BROWSER)
    ft.app(target=pages)

#  pyinstaller --name export_conversor_frotas_sysmar --onefile --icon=transferencia-de-dados.ico --noconsole main.py
# flet pack --name export_conversor_frotas_sysmar_V_0.2.2 --icon=transferencia-de-dados.ico main.py