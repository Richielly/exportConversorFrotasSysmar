# -*- coding: utf-8 -*-
import configparser

import pandas as pd
import os
import calendar

cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
class Read_file:
    def obter_ultimo_dia_mes(self, mes, ano):
        mes = int(mes)
        ano = int(ano)
        ultimo_dia = calendar.monthrange(int(ano), int(mes))[1]
        return f'{ultimo_dia:02d}/{mes:02d}/{ano}'

    def gerar_numero_sequencial(self, inicio=1):
        contador = inicio
        while True:
            yield contador
            contador += 1

    def escrever_arquivo_texto(self, nome_arquivo, linhas):
        # Verificar se o arquivo já existe
        if not os.path.exists(nome_arquivo):
            # Criar o arquivo caso ele não exista
            with open(nome_arquivo, 'w') as file:
                pass

        # Escrever as linhas no arquivo
        with open(nome_arquivo, 'w') as file:
            for linha in linhas:
                file.write(linha + '\n')
    def buscar_arquivo_hodometro_horimetro(self, pastas_iniciais, pasta_destino, codEntidade):
        reade_file = Read_file()
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        nome_arquivo = 'HodometroHorimetro.txt'
        txt = []
        try:
            controle = reade_file.gerar_numero_sequencial()
            for pasta_inicial in [pastas_iniciais]:
                for raiz, diretorios, arquivos in os.walk(pasta_inicial):
                    if nome_arquivo in arquivos:
                        caminho_arquivo = os.path.join(raiz, nome_arquivo)
                        # print(f'Arquivo encontrado: {caminho_arquivo}')
                        df = pd.read_csv(caminho_arquivo, sep="|", header=None, dtype="str", encoding='ansi')  # header=None se quiser colocar sem cabeçalho
                        df = df.fillna('')
                        df = df.astype(str)
                        df = df.get([1, 2, 3, 4, 6, 7, 8, 9])

                        competencia = df[3].iloc[0] #iloc pra tranformar series de pandas em formato python para fazer cast
                        ano = df[4].iloc[0]

                        frota = df[1].astype(int).iloc[0]
                        CdControle = next(controle)
                        CdTipoLancamento = 1  # 0=Manual/1=Expostação SimAm
                        DtLancamento = reade_file.obter_ultimo_dia_mes(competencia, ano)
                        VlrDeclarado = df[8].iloc[0].replace('.', ',')
                        DsNotaExplicativa = df[9].iloc[0]
                        CdControleSimam = df[2].iloc[0]
                        IsTrocaAcumulador = 1  # 0=Sim/1=Não
                        VlrAcumuladorInicial = df[6].iloc[0].replace('.', ',')
                        VlrAcumuladorFinal = df[7].iloc[0].replace('.', ',')
                        NovoValorAcumuladorInicial = ''
                        DtLeituraAcumulador = ''

                        txt.append(str(codEntidade)+'|'+str(frota)+'|'+str(CdControle)+'|'+str(CdTipoLancamento)+'|'+str(DtLancamento)+'|'+str(VlrDeclarado)+'|'+str(DsNotaExplicativa)+'|'\
                              +str(CdControleSimam)+'|'+str(IsTrocaAcumulador)+'|'+str(VlrAcumuladorInicial)+'|'+str(VlrAcumuladorFinal)+'|'+str(NovoValorAcumuladorInicial)+'|'+str(DtLeituraAcumulador))

            reade_file.escrever_arquivo_texto(pasta_destino+'VeiculoControleSimAm.txt', txt)
            return f'{pasta_destino}VeiculoControleSimAm.txt gerado com sucesso...'
        except TypeError as e:
            print(e)

    def buscar_arquivo_consumo(self, pastas_iniciais, pasta_destino, codEntidade):
        reade_file = Read_file()
        nome_arquivo = 'ConsumoCombustivel.txt'
        txt = []
        for pasta_inicial in [pastas_iniciais]:
            for raiz, diretorios, arquivos in os.walk(pasta_inicial):
                if nome_arquivo in arquivos:
                    caminho_arquivo = os.path.join(raiz, nome_arquivo)

                    df = pd.read_csv(caminho_arquivo, sep="|", header=None,dtype="str")  # header=None se quiser colocar sem cabeçalho
                    df = df.fillna('')
                    df = df.astype(str)

                    frota = df[2].astype(int).iloc[0]
                    NrSequencial = df[1].astype(int).iloc[0]
                    NrMes = df[5].iloc[0]  # iloc pra tranformar series de pandas em formato python para fazer cast
                    NrAno = df[6].iloc[0]
                    IdTipoCategoriaObjetoDespesa = df[3].iloc[0]
                    IdTipoObjetoDespesa = df[4].iloc[0]
                    NrQuantidade = df[7].iloc[0].replace('.', ',')
                    txt.append(str(codEntidade) + '|' + str(NrSequencial) + '|' + str(frota)+ '|' + str(NrMes) + '|' + str(NrAno) + '|' + str(IdTipoCategoriaObjetoDespesa)+ '|' + str(IdTipoObjetoDespesa) + '|' + str(NrQuantidade) + '|')

        reade_file.escrever_arquivo_texto(pasta_destino+'ConsumoCombustivel.txt', txt)
        return f'{pasta_destino}ConsumoCombustivel.txt gerado com sucesso...'

