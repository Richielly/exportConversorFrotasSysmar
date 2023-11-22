import configparser
import os
import re
from datetime import datetime
class Util:

    def update_cfg(self, ini_name='cfg.ini', secao='DEFAULT', chave='CodEntidade', new=0):
        cfg = configparser.ConfigParser()
        cfg.read(ini_name)
        # Modifica um valor existente
        cfg.set(secao, chave, new)
        # Salva as alterações no arquivo de configuração
        with open(ini_name, 'w') as configfile:
            cfg.write(configfile)

    def create_file(self, filename, tipo='.ini'):
        cfg = configparser.ConfigParser()
        cfg.read('cfg.ini')
        dir = cfg['DEFAULT']['diretorioarquivos']
        file_dir_name = os.path.join(dir, filename + tipo)
        if not os.path.exists(file_dir_name):
            with open(file_dir_name, 'w') as file:
                file.write('[DEFAULT]' + '\n')
        return file_dir_name

    def atualizar_ou_criar_secao_config(self, nome_arquivo, secao, configuracoes):
        # Cria uma instância de ConfigParser
        config = configparser.ConfigParser()

        # Lê o arquivo de configuração existente, se ele existir
        config.read(nome_arquivo)

        # Adiciona a seção se ela não existir
        if not config.has_section(secao):
            config.add_section(secao)

        # Atualiza as configurações na seção
        config.set(secao, chave, valor)

        # Escreve as alterações no arquivo de configuração
        with open(nome_arquivo, 'w') as configfile:
            config.write(configfile)

    def listar_secoes(self, nome_arquivo):
        config = configparser.ConfigParser()
        config.read(nome_arquivo)
        return config.sections()

    def mostrar_configuracoes(self, nome_arquivo, secao):
        config = configparser.ConfigParser()
        config.read(nome_arquivo)

        if config.has_section(secao):
            return dict(config.items(secao))
        else:
            return None

    def obter_secao_configuracao(self, nome_arquivo):
        config = configparser.ConfigParser()
        config.read(nome_arquivo)

        configuracoes_simples = {}
        for secao in config.sections():
            # Assumindo que cada seção tem apenas uma configuração
            chave, valor = next(iter(config.items(secao)))
            configuracoes_simples[secao] = valor

        return configuracoes_simples

    def set_current_seconds(self, dt):
        current_seconds = datetime.now().second
        return dt.replace(second=current_seconds)

    def set_current_seconds_and_milliseconds_firebird(self, date_str):
        # Convertendo a string para um objeto datetime
        dt = datetime.strptime(date_str, '%d/%m/%Y %H:%M')

        # Obtendo os segundos e milissegundos atuais
        current_seconds = datetime.now().second
        current_microseconds = datetime.now().microsecond
        current_milliseconds = int(current_microseconds / 1000)

        # Atualizando o objeto datetime com os segundos e milissegundos atuais
        updated_dt = dt.replace(second=current_seconds, microsecond=current_milliseconds * 1000)

        # Formatando o objeto datetime para a string no formato desejado
        return updated_dt.strftime('%S.%f')[:-3]

    def extrair_data(self, texto):
        # Use expressões regulares para encontrar uma correspondência no formato "dd/mm/yyyy hh:mm"
        padrao = r'(\d{2}/\d{2}/\d{4} \d{2}:\d{2})'
        correspondencias = re.findall(padrao, texto)

        if correspondencias:
            # O primeiro item na lista de correspondências é a data sem segundos
            data_sem_segundos = correspondencias[0]

        return data_sem_segundos

