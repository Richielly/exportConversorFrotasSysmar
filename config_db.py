import configparser
cfg = configparser.ConfigParser()
cfg.read('cfg.ini')
import fdb

query = {"produto":f"select codproduto, nome from PRODUTO where idtpcategobjetodesp = 1"}
class ConfigDB:
    def produtos(self, host=cfg['DEFAULT']['Host'], database=cfg['DEFAULT']['NomeBancoSequence'],
                  user=cfg['DEFAULT']['User'], port=cfg['DEFAULT']['Port'], password=cfg['DEFAULT']['Password']):
        result = []
        global query
        for seq, sql in query.items():
            try:
                dados_conexao = fdb.connect(host=host, database=database, user=user, port=int(port), password=password)
            except BaseException as e:
                return e, False
            cur = dados_conexao.cursor()

            cur.execute(sql)
            result.append(cur.fetchall())

            return result