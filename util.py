import configparser
import os
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

    def create_file(self, filename):
        cfg = configparser.ConfigParser()
        cfg.read('cfg.ini')
        dir = cfg['DEFAULT']['diretorioarquivos']
        file_dir_name = os.path.join(dir, filename + '.ini')
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
        for chave, valor in configuracoes.items():
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


import script

# t = Util()
# new_arquivo_ini = 'script_sysmar.ini'

# print(t.create_file(filename=file_name))
# t.atualizar_ou_criar_secao_config(nome_arquivo=new_arquivo_ini, secao=, configuracoes={'script':})

# sqls = script.Script()
# comandos = sqls.query(446)
# for secao, script in comandos.items():
#     print(secao)
#     t.atualizar_ou_criar_secao_config(nome_arquivo=new_arquivo_ini, secao=secao, configuracoes={'script':str(script)})
# print(t.listar_secoes(new_arquivo_ini))
# print(t.mostrar_configuracoes(new_arquivo_ini, )['script'])

# print(t.obter_configuracoes_simples(new_arquivo_ini))
