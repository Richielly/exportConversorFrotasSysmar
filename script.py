import configparser

class Script:
    def query(self, codEntidade):
        cfg = configparser.ConfigParser()
        cfg.read('cfg.ini')
        motorista = cfg['DEFAULT']['motorista']
        fornecedor = cfg['DEFAULT']['fornecedor']

        return {
        'Cor' : f""" select count(*) from fro_cor """,

        'Marca' : f""" select count(*) from fro_mar """,

        'Especie' : f""" select distinct count(*) from fro_veic """

        # 'Modelo' : f""" select
        #                 v.veides ||'|'||
        #                 substring(m.mardes from 1 for 30) ||'|'||
        #                 case v.veinat
        #                 when 0 then 'NENHUM'
        #                 when 1 then 'VEÍCULOS DE PASSEIO E UTILITÁRIOS'
        #                 when 2 then 'CAMINHÕES'
        #                 when 3 then 'ÔNIBUS'
        #                 when 4 then 'MICROÔNIBUS'
        #                 when 5 then 'MOTOS'
        #                 when 50 then 'MOTONIVELADORA'
        #                 when 51 then 'PÁ CARREGADEIRA'
        #                 when 52 then 'TRATORES AGRÍCOLAS'
        #                 when 99 then 'OUTROS EQUIPAMENTOS'
        #                 when 999 then 'OUTROS TIPOS DE VEÍCULOS E EQUIPAMENTOS' end ||'|'||
        #                 case v.veinat
        #                 when 0 then '1'
        #                 when 1 then '2'
        #                 when 2 then '3'
        #                 when 3 then '4'
        #                 when 4 then '4'
        #                 when 5 then '1'
        #                 when 50 then '4'
        #                 when 51 then '4'
        #                 when 52 then '3'
        #                 when 99 then '1'
        #                 when 999 then '1' end ||'|'||
        #                 case v.veiodom
        #                 when 'K' then '1'
        #                 when 'H' then '2'
        #                 when 'N' then '' end ||'|'||
        #                 v.veitipcomb ||'|' as modelo
        #                 from fro_veic v
        #                 join FRO_FIPE fp on (fp.fipecod = v.veifipecod)
        #                 join fro_mar m on (m.marcod = fp.marcod) """,
        #
        # 'Motorista' : f""" select
        #              distinct
        #              {codEntidade} ||'|'||
        #              coalesce(cast(p.pescod as varchar), '')||'|'||
        #              '' ||'|'||
        #              coalesce(cast(p.pescod as varchar), '')||'|'||
        #              coalesce(cast(replace(replace(p.pescpfcnpj,'.',''),'-','') as varchar),'')||'|'||
        #              coalesce(cast(m.mothabreg as varchar), '') ||'|'||
        #              '1' ||'|'||
        #              coalesce(substring(cast(m.mothabdatpri as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatpri as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatpri as varchar) from 1 for 4), '') ||'|'||
        #              coalesce(substring(cast(m.mothabdatval as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatval as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatval as varchar) from 1 for 4), '') ||'|'||
        #              coalesce(substring(cast(m.mothabdatemis as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatemis as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatemis as varchar) from 1 for 4), '') ||'|' as motorista
        #              from public.fro_mot m
		# 			 join public.fro_pes p
		# 			   on p.pescod = m.motpescod
		# 			  union all
        #              select
        #              distinct
        #              {codEntidade} ||'|'||
        #              coalesce(cast(p.pescod as varchar), '')||'|'||
        #              '' ||'|'||
        #              coalesce(cast(p.pescod as varchar), '')||'|'||
        #              coalesce(cast(replace(replace(p.pescpfcnpj,'.',''),'-','') as varchar),'')||'|'
        #              ||'|'
        #              '1' ||'|'
        #              ||'|'
        #              ||'|'
        #              ||'|' as motorista
		#      from fro_abastecimentos a
		# 	 join fro_pes p
		# 			  on p.pescod = a.solicitantecodigo
	    #              and a.solicitantecodigo not in (select motpescod from fro_mot) """,
        #
        # 'MotoristaCategoriaCnh':f""" SELECT
        #                             {codEntidade} ||'|'||
        #                             m.motpescod ||'|'||
        #                             regexp_split_to_table(m.mothabcat, '') ||'|'
        #                             FROM public.fro_mot m
        #                             JOIN fro_pes p ON p.pescod = m.motpescod; """,
        #
        # 'Veiculo' : f""" SELECT
        #                 {codEntidade} ||'|'||
        #                 v.veicod ||'|'||
        #                 v.veicodbenpat ||'|'||
        #                 v.veiplaca ||'|'||
        #                 case veinat
        #                 when 0 then 'NENHUM'
        #                 when 1 then 'VEÍCULOS DE PASSEIO E UTILITÁRIOS'
        #                 when 2 then 'CAMINHÕES'
        #                 when 3 then 'ÔNIBUS'
        #                 when 4 then 'MICROÔNIBUS'
        #                 when 5 then 'MOTOS'
        #                 when 50 then 'MOTONIVELADORA'
        #                 when 51 then 'PÁ CARREGADEIRA'
        #                 when 52 then 'TRATORES AGRÍCOLAS'
        #                 when 99 then 'OUTROS EQUIPAMENTOS'
        #                 when 999 then 'OUTROS TIPOS DE VEÍCULOS E EQUIPAMENTOS' end ||'|'||
        #                 v.veides ||'|'||
        #                 v.veifipecod ||'|'||
        #                 coalesce(c.cordes,'1') ||'|'|| --incluir padrão
        #                 coalesce(v.veirenavam, '') ||'|'||
        #                 coalesce(v.veichassi, '') ||'|'||
        #                 '' ||'|'||
        #                 v.veianofab ||'|'||
        #                 v.veianomod ||'|'||
        #                 '1' ||'|'|| --sem dados na base padrão 1 campo obrigatório
        #                 regexp_replace(v.veiobs, '[\\n\\r]+', ' ', 'g' ) ||'|'||
        #                 coalesce(h.veihodhorsit, '2') ||'|'||
        #                 veitipvinc ||'|'||
        #                 v.veitipcomb ||'|'||
        #                 substring(cast(v.veidatsimam as varchar) from 9 for 2) ||'/'|| substring(cast(v.veidatsimam as varchar) from 6 for 2) ||'/'|| substring(cast(v.veidatsimam as varchar) from 1 for 4) ||'|'||
        #                 '1' ||'|'||
        #                 '1' ||'|'||
        #                 '1' ||'|'||
        #                 '1' ||'|'||
        #                 '2' ||'|'||
        #                 '1' ||'|' as Veiculo
        #                 FROM public.fro_veic v
        #                 left join fro_cor c on (c.corcod = v.veicorcod)
        #                 left join FRO_VEIC_HODHOR h on (h.veicod = v.veicod and v.veihodhorseqatu = h.veihodhorseq) """,
        #
        # 'Produto' : f""" select
        #                 case p.combdes
        #                     when 'GASOLINA' then 'COMBUSTÍVEL - GASOLINA'
        #                     when 'DIESEL' then 'COMBUSTÍVEL - DIESEL COMUM'
        #                     when 'DIESEL S-10' then 'COMBUSTÍVEL     -     DIESEL S-10'
        #                     when 'ETANOL' then 'COMBUSTÍVEL - ÁLCOOL (ETANOL)' else p.combdes end ||'|'||
        #                 case p.combcod
        #                     when '1' then '23401'
        #                     when '2' then '23402'
        #                     when '3' then '23403'
        #                     when '8' then '24595' else '' end ||'|'||
        #                 '1' ||'|'|| --Combustivel
        #                 '' ||'|'||
        #                 '' ||'|'||
        #                 1 ||'|' as Produto
        #                 from fro_comb p
        #                 union all
        #                 select distinct
        #                 substring (upper(i.iteetqdes) from 1 for 70 ) ||'|'||
        #                 '9999' ||'|'||
        #                 '3' ||'|'|| -- 1 Combustivel |2 Óleo/Lubrificante |3 Peças | 4 Serviços | 5 Pneus | 6 Acessorios
        #                 '' ||'|'||
        #                 '' ||'|'||
        #                 1 ||'|' --1 Ativo
        #                 from fro_man2 m2
        #                 join fro_iteetq i on (i.iteetqcod = m2.iteetqcod) """,
        #
        # 'VeiculoProduto' : f""" select
        #                         distinct
        #                         {codEntidade} ||'|'||
        #                         coalesce(cast(a.veicod as varchar), '') ||'|'||
        #                         case c.combcod
        #                             when '1' then '23401'
        #                             when '2' then '23402'
        #                             when '3' then '23403'
        #                             when '8' then '24595' else '' end ||'|'||
        #                         case c.combdes
        #                             when 'GASOLINA' then 'COMBUSTÍVEL - GASOLINA'
        #                             when 'DIESEL' then 'COMBUSTÍVEL - DIESEL COMUM'
        #                             when 'DIESEL S-10' then 'COMBUSTÍVEL     -     DIESEL S-10'
        #                             when 'ETANOL' then 'COMBUSTÍVEL - ÁLCOOL (ETANOL)' else c.combdes end ||'|' as veiculoProduto
        #
        #                         FROM public.fro_abastecimentos a
        #                         join fro_comb c on (c.combcod = a.combcod) """,
        #
        # 'MotoristaSituacaoCnh' : f""" SELECT
        #                             {codEntidade} ||'|'||
        #                             m.motpescod ||'|'||
        #                             DATE_PART('day',(SELECT CURRENT_DATE)) ||'/'|| DATE_PART('month',(SELECT CURRENT_DATE)) ||'/'|| DATE_PART('YEAR',(SELECT CURRENT_DATE)) ||'|'||
        #                             case motativo
        #                             when true then 1
        #                             else 2 end ||'|'||
        #                             '0' ||'|' as MotoridtaSitCnh
        #                             FROM public.fro_mot m
        #                             join fro_pes p on (p.pescod = m.motpescod) """,
        #
        # 'Abastecimento' : f""" SELECT
        #                         {codEntidade} ||'|'||
        #                         coalesce(cast(a.abastecimentocod as varchar), '') ||'|'||
        #                         coalesce(cast(a.veicod as varchar), '') ||'|'||
        #                         coalesce(v.veicodbenpat, '') ||'|'||
        #                         case a.combcod
        #                             when '1' then '23401'
        #                             when '2' then '23402'
        #                             when '3' then '23403'
        #                             when '8' then '24595' else '' end ||'|'||
        #                         case c.combdes
        #                             when 'GASOLINA' then 'COMBUSTÍVEL - GASOLINA'
        #                             when 'DIESEL' then 'COMBUSTÍVEL - DIESEL COMUM'
        #                             when 'DIESEL S-10' then 'COMBUSTÍVEL     -     DIESEL S-10'
        #                             when 'ETANOL' then 'COMBUSTÍVEL - ÁLCOOL (ETANOL)' else c.combdes end ||'|'||
        #                         case coalesce(cast(a.solicitantecodigo as varchar),'')
        #                             when '0' then '101' else coalesce(cast(a.solicitantecodigo as varchar),'101') end ||'|'||
        #                         coalesce(replace (cast(a.abastecimentovalorun as varchar), '.',','),'0') ||'|'||
        #                         coalesce(substring(cast(a.abastecimentodatahora as varchar) from 9 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 6 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 1 for 4) ||' '|| substring(cast(a.abastecimentodatahora as varchar) from 12 for 8),'') ||'|'||
        #                         coalesce(replace(cast(a.abastecimentoqtd as varchar), '.', ','),'') ||'|'||
        #                         coalesce(replace(cast(a.abastecimentovalorun * a.abastecimentoqtd as varchar),'.',','),'0') ||'|'||
        #                         '1' ||'|'|| --1 Completo
        #                         coalesce(REGEXP_REPLACE(cast(a.abastecimentodoc as varchar), '\D', '', 'g'), '') ||'|'||
        #                         coalesce(regexp_replace(a.abastecimentoobservacao, E'[\\n\\r]+', ' ', 'g' ),'') ||'|'||
        #                         case when a.forpescod = 0 then '99999999' else replace(coalesce(cast (a.forpescod as varchar),''),'.', '') end ||'|'||
        #                         coalesce(replace(replace(replace(p.pescpfcnpj, '.',''), '/',''), '-',''),'###') ||'|'||
        #                         coalesce(replace(cast (a.solicitantecodigo as varchar), '0', ''), '') ||'|'||
        #                         coalesce(REGEXP_REPLACE(cast(a.cccod as varchar), '\D', '', 'g'), '') ||'|'||
        #                         '' ||'|'||
        #                         case a.abastecimentodanificado
        #                             when 'S' then '2'
        #                             when 'N' then '1' else 1 end ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'||
        #                         {codEntidade} ||'|'||
        #                         {codEntidade} ||'|'||
        #                         coalesce(cast(a.abastecimentoempano as varchar), '') ||'|'||
        #                         coalesce(REGEXP_REPLACE(cast(a.abastecimentoempnum as varchar), '\D', '', 'g'), '') ||'|'||
        #                         coalesce(cast(a.abastecimentoempano as varchar), '') ||'|'||
        #                         {codEntidade} ||'|' as exportAbastecimento
        #                         FROM public.fro_abastecimentos a
        #                         join fro_veic v on (v.veicod = a.veicod and v.veiodom != 'N')
        #                         join fro_comb c on (c.combcod = a.combcod)
        #                         left join fro_pes p on (p.pescod = a.forpescod)
        #                         order by a.abastecimentocod """,
        #
        # 'EquipamentoConsumoCombustivel': f""" SELECT {codEntidade}||'|'||
        #                         ab.veicod||'|'||
        #                         TO_CHAR(ab.abastecimentodatahora, 'DD/MM/YYYY HH24:MI:SS')||'|'||
        #                         ve.veicodbenpat||'|'||
        #                         case co.combcod
        #                             when '1' then '23401'
        #                             when '2' then '23402'
        #                             when '3' then '23403'
        #                             when '8' then '24595' else '' end ||'|'||
        #                         case co.combdes
        #                             when 'GASOLINA' then 'COMBUSTÍVEL - GASOLINA'
        #                             when 'DIESEL' then 'COMBUSTÍVEL - DIESEL COMUM'
        #                             when 'DIESEL S-10' then 'COMBUSTÍVEL     -     DIESEL S-10'
        #                             when 'ETANOL' then 'COMBUSTÍVEL - ÁLCOOL (ETANOL)' else co.combdes end ||'|'||
        #                         replace(cast(ab.abastecimentoqtd as varchar), '.', ',')||'|'||
        #                         replace(cast(ab.abastecimentovalorun as varchar), '.', ',')||'|'||
        #                         replace(cast((ab.abastecimentoqtd * ab.abastecimentovalorun ) as varchar), '.', ',')||'|'||
        #                         {codEntidade}||'|'||
        #                         ab.abastecimentoempano||'|'||
        #                         ab.abastecimentoempnum||'|'||
		# 		                '' ||'|'||
        #                         {codEntidade}||'|'||
        #                         ab.abastecimentodoc||'|'||
        #                         pe.pescod||'|'||
        #                         translate (pe.pescpfcnpj, '.-/','')||'|'||
        #                         {codEntidade} ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'||
        #                         '' ||'|'
		#                         FROM fro_abastecimentos ab
		#                         join fro_veic ve
		#                             on ve.veicod = ab.veicod
		# 	                        and ve.veiodom = 'N'
		#                         join fro_comb co
		#                             on co.combcod = ab.combcod
		#                         join fro_pes pe
		#                             on pe.pescod = ab.forpescod """,
        #
        # 'Acumulador' : f""" SELECT
        #                     {codEntidade} ||'|'||
        #                     coalesce(cast(a.veicod as varchar), '') ||'|'||
        #                     coalesce(v.veicodbenpat, '') ||'|'||
        #                     coalesce(substring(cast(a.abastecimentodatahora as varchar) from 9 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 6 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 1 for 4) ||' '|| substring(cast(a.abastecimentodatahora as varchar) from 12 for 6),'') ||'#sec#|'||
        #                     '2' ||'|'|| --2 = Abastecimento
        #                     coalesce(cast(a.abastecimentocod as varchar), '') ||'|'||
        #                     coalesce(replace(cast(a.abastecimentokmhr as varchar), '.', ','),'0') ||'|'||
        #                     coalesce(replace(cast(a.abastecimentokmhr as varchar), '.', ','), '0') ||'|' as Acumulador
        #                     FROM public.fro_abastecimentos a
        #                     join fro_veic v on (v.veicod = a.veicod and v.veiodom != 'N')
        #                     join fro_comb c on (c.combcod = a.combcod)
        #                     union all
        #                     SELECT
        #                     {codEntidade} ||'|'||
        #                     coalesce(cast(s.veicod as varchar), '') ||'|'||
        #                     '' ||'|'||
        #                     coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 1 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
        #                     '3' ||'|'|| -- 3= Ordem de Serviço
        #                     '' ||'|'||
        #                     replace(cast(s.manveikmhr as varchar), '.',',') ||'|'||
        #                     replace(cast(s.manveikmhr as varchar), '.',',') ||'|'
        #                     from fro_man s """,
        #
        # 'VeiculoControleSimAm' : f""" select
        #                                 {codEntidade} ||'|'||
        #                                 coalesce(cast(csa.veicod as varchar), '') ||'|'||
        #                                 coalesce(cast(csa.veihodhorseq as varchar), '') ||'|'||
        #                                 1 ||'|'||
        #                                 coalesce(substring(cast(csa.veihodhordatcad as varchar) from 9 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 6 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 1 for 4), '') ||'|'||
        #                                 coalesce(replace(cast(csa.veihodhorkmhr as varchar), '.', ''), '0') ||'|'||
        #                                 coalesce(csa.veihodhormot, '') ||'|'||
        #                                 '' ||'|'||
        #                                 1 ||'|'||
        #                                 coalesce(replace(cast(csa.veihodhorkmhr as varchar), '.', ','),'0') ||'|'||
        #                                 coalesce(replace(cast(coalesce(csa.veihodhorkmhrfin, csa.veihodhorkmhr) as varchar), '.', ','),'0') ||'|'||
        #                                 coalesce(replace(cast(csa.veihodhorkmhr as varchar), '.', ','),'0') ||'|'||
        #                                 coalesce(substring(cast(csa.veihodhordatcad as varchar) from 9 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 6 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 1 for 4), '') ||'|'
        #                                 from FRO_VEIC_HODHOR csa
        #                                 order by csa.veicod, csa.veihodhorseq """,
        #
        # 'OrdemAbastecimento' : f""" SELECT
        #                             {codEntidade} ||'|'||
        #                             r.requisicaocod ||'|'||
        #                             r.veicod ||'|'||
        #                             r.reqforpescod ||'|'||
        #                             coalesce(replace(replace(replace(f.pescpfcnpj, '.',''), '/',''), '-',''),'{fornecedor}') ||'|'||
        #                             case coalesce(cast(r.pescod as varchar),'')
        #                             when '0' then '{motorista}' else coalesce(cast(r.pescod as varchar),'') end ||'|'||
        #                             coalesce(substring(cast(r.requisicaodata as varchar) from 9 for 2) ||'/'|| substring(cast(r.requisicaodata as varchar) from 6 for 2) ||'/'|| substring(cast(r.requisicaodata as varchar) from 1 for 4),'') ||'|'||
        #                             case c.combdes
        #                             when 'GASOLINA' then '23402'
        #                             when 'ETANOL' then '23401'
        #                             when 'DIESEL S-10' then '24595'
        #                             when 'DIESEL' then '23403' else '' end ||'|'||
        #                             '1' ||'|'|| --1 Completo
        #                             coalesce(replace(cast(r.requisicaoquantidade as varchar), '.', ','),'0,00') ||'|'||
        #                             coalesce(cast (a.abastecimentocod as varchar), '') ||'|'||
        #                             '' ||'|'||
        #                             0 ||'|'|| -- 0 = Sem Licitação
        #                             '' ||'|'||
        #                             '' ||'|'||
        #                             case cast(r.resppescod as varchar)
        #                                 when '0' then '' else cast(r.resppescod as varchar) end ||'|'||
        #                             coalesce(replace(replace(replace(p.pescpfcnpj, '.',''), '/',''), '-',''),'') ||'|'||
        #                             case cast(r.cccod as varchar)
        #                                 when '0' then '' else cast(r.cccod as varchar) end ||'|'||
        #                             coalesce(regexp_replace(r.requisicaoobservacao, E'[\\n\\r]+', ' ', 'g' ),'') ||'|'||
        #                             coalesce(replace(cast(r.requisicaokmhr as varchar), '.', ','),'') ||'|'||
        #                             coalesce(replace(cast(r.requisicaokmhr as varchar), '.', ','),'') ||'|'
        #                             FROM public.fro_requisicao r
        #                             left join public.fro_abastecimentos a on (a.abastecimentoreqcod = r.requisicaocod)
        #                             left join fro_pes f on (f.pescod = r.reqforpescod)
        #                             left join fro_pes p on (p.pescod = r.resppescod)
        #                             left join fro_comb c on (c.combcod = r.combcod)
        #                             order by r.requisicaocod """,
        #
        # 'VeiculoOrdemServico' : f""" select
        #                             {codEntidade} ||'|'||
        #                             s.mancod ||'|'||
        #                             s.veicod ||'|'||
        #                             '' ||'|'||
        #                             'Serviços Mecanico em Geral' ||'|'||
        #                             coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') ||'|'||
        #                             coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
        #                             coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 1 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
        #                             coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 2 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
        #                             coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 3 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
        #                             s.manobs ||'|'||
        #                             1 ||'|'|| -- 1-Sim
        #                             '' ||'|'||
        #                             '' ||'|'||
        #                             '' ||'|'||
        #                             l.ccdes ||'|'||
        #                             l.ccdes ||'|'||
        #                             l.ccdes ||'|'||
        #                             s.cccod ||'|'
        #                             from fro_man s
        #                             join fro_cc l on (l.cccod = s.cccod)
        #                             order by s.mancod """,
        #
        # 'VeiculoOrdemServicoProduto' : f""" select
        #                                     {codEntidade} ||'|'||
        #                                     m2.mancod ||'|'||
        #                                     '' ||'|'||
        #                                     substring (upper(i.iteetqdes) from 1 for 70 ) ||'|'||
        #                                     replace(cast(m2.maniteqtd as varchar),'.', ',') ||'|'||
        #                                     replace(cast(m2.maniteqtd * m2.manitevlruni as varchar), '.', ',') ||'|'||
        #                                     m2.maniteseq ||'|'||
        #                                     '' ||'|'||
        #                                     '' ||'|'
        #                                     from fro_man2 m2
        #                                     join fro_iteetq i on (i.iteetqcod = m2.iteetqcod) """

        }