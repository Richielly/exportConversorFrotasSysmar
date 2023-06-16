import configparser

class Script:
    def query(self, codEntidade):
        cfg = configparser.ConfigParser()
        cfg.read('cfg.ini')

        return {
        'Cor' : f""" select cordes ||'|' from fro_cor """,

        'Marca' : f""" select substring(mardes from 1 for 30) ||'|' from fro_mar """,

        'Especie' : f""" select distinct
                    case veinat
                    when 0 then 'NENHUM'
                    when 1 then 'VEÍCULOS DE PASSEIO E UTILITÁRIOS'
                    when 2 then 'CAMINHÕES'
                    when 3 then 'ÔNIBUS'
                    when 4 then 'MICROÔNIBUS'
                    when 5 then 'MOTOS'
                    when 50 then 'MOTONIVELADORA'
                    when 51 then 'PÁ CARREGADEIRA'
                    when 52 then 'TRATORES AGRÍCOLAS'
                    when 99 then 'OUTROS EQUIPAMENTOS'
                    when 999 then 'OUTROS TIPOS DE VEÍCULOS E EQUIPAMENTOS' end ||'|'||
                    case veinat
                    when 0 then 'A'
                    when 1 then 'B'
                    when 2 then 'C'
                    when 3 then 'D'
                    when 4 then 'D'
                    when 5 then 'A'
                    when 50 then 'D'
                    when 51 then 'D'
                    when 52 then 'C'
                    when 99 then 'A'
                    when 999 then 'A' end ||'|'||
                    case veiodom
                    when 'K' then '1'
                    when 'H' then '2'
                    when 'N' then '' end ||'|'||
                    '' ||'|'||
                    '' ||'|' as Especie
                    from fro_veic """,

        'Modelo' : f""" select
                        v.veides ||'|'||
                        substring(m.mardes from 1 for 30) ||'|'||
                        case v.veinat
                        when 0 then 'NENHUM'
                        when 1 then 'VEÍCULOS DE PASSEIO E UTILITÁRIOS'
                        when 2 then 'CAMINHÕES'
                        when 3 then 'ÔNIBUS'
                        when 4 then 'MICROÔNIBUS'
                        when 5 then 'MOTOS'
                        when 50 then 'MOTONIVELADORA'
                        when 51 then 'PÁ CARREGADEIRA'
                        when 52 then 'TRATORES AGRÍCOLAS'
                        when 99 then 'OUTROS EQUIPAMENTOS'
                        when 999 then 'OUTROS TIPOS DE VEÍCULOS E EQUIPAMENTOS' end ||'|'||
                        case v.veinat
                        when 0 then '1'
                        when 1 then '2'
                        when 2 then '3'
                        when 3 then '4'
                        when 4 then '4'
                        when 5 then '1'
                        when 50 then '4'
                        when 51 then '4'
                        when 52 then '3'
                        when 99 then '1'
                        when 999 then '1' end ||'|'||
                        case v.veiodom
                        when 'K' then '1'
                        when 'H' then '2'
                        when 'N' then '' end ||'|'||
                        v.veitipcomb ||'|' as modelo
                        from fro_veic v
                        join FRO_FIPE fp on (fp.fipecod = v.veifipecod)
                        join fro_mar m on (m.marcod = fp.marcod) """,

        'Motorista' : f""" select
                            distinct
                            {codEntidade} ||'|'||
                            coalesce(cast(a.solicitantecodigo as varchar), '') ||'|'||
                            '' ||'|'||
                            coalesce(cast(m.motpescod as varchar), '') ||'|'||
                            lpad(cast(replace(replace(p.pescpfcnpj,'.',''),'-','') as varchar),11,'0') ||'|'||
                            coalesce(cast(m.mothabreg as varchar), '') ||'|'||
                            '1' ||'|'||
                            coalesce(substring(cast(m.mothabdatpri as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatpri as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatpri as varchar) from 1 for 4), '') ||'|'||
                            coalesce(substring(cast(m.mothabdatval as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatval as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatval as varchar) from 1 for 4), '') ||'|'||
                            coalesce(substring(cast(m.mothabdatemis as varchar) from 9 for 2) ||'/'|| substring(cast(m.mothabdatemis as varchar) from 6 for 2) ||'/'|| substring(cast(m.mothabdatemis as varchar) from 1 for 4), '') ||'|' as motorista
                            from public.fro_abastecimentos a
                            join public.fro_pes p on (p.pescod = a.solicitantecodigo)
                            left join public.fro_mot m on (m.motpescod = a.solicitantecodigo) """,

        'Veiculo' : f""" SELECT
                        {codEntidade} ||'|'||
                        v.veicod ||'|'||
                        v.veicodbenpat ||'|'||
                        v.veiplaca ||'|'||
                        case veinat
                        when 0 then 'NENHUM'
                        when 1 then 'VEÍCULOS DE PASSEIO E UTILITÁRIOS'
                        when 2 then 'CAMINHÕES'
                        when 3 then 'ÔNIBUS'
                        when 4 then 'MICROÔNIBUS'
                        when 5 then 'MOTOS'
                        when 50 then 'MOTONIVELADORA'
                        when 51 then 'PÁ CARREGADEIRA'
                        when 52 then 'TRATORES AGRÍCOLAS'
                        when 99 then 'OUTROS EQUIPAMENTOS'
                        when 999 then 'OUTROS TIPOS DE VEÍCULOS E EQUIPAMENTOS' end ||'|'||
                        v.veides ||'|'||
                        coalesce(c.cordes,'1') ||'|'|| --incluir padrão
                        coalesce(v.veirenavam, '') ||'|'||
                        coalesce(v.veichassi, '') ||'|'||
                        '' ||'|'||
                        v.veianofab ||'|'||
                        v.veianomod ||'|'||
                        '1' ||'|'|| --sem dados na base padrão 1 campo obrigatório
                        regexp_replace(v.veiobs, '[\\n\\r]+', ' ', 'g' ) ||'|'||
                        coalesce(h.veihodhorsit, '2') ||'|'||
                        veitipvinc ||'|'||
                        v.veitipcomb ||'|'||
                        substring(cast(v.veidatsimam as varchar) from 9 for 2) ||'/'|| substring(cast(v.veidatsimam as varchar) from 6 for 2) ||'/'|| substring(cast(v.veidatsimam as varchar) from 1 for 4) ||'|'||
                        '1' ||'|'||
                        '1' ||'|'||
                        '1' ||'|'||
                        '1' ||'|'||
                        '2' ||'|'||
                        '1' ||'|' as Veiculo
                        FROM public.fro_veic v
                        left join fro_cor c on (c.corcod = v.veicorcod)
                        left join FRO_VEIC_HODHOR h on (h.veicod = v.veicod and v.veihodhorseqatu = h.veihodhorseq) """,

        'Produto' : f""" select
                        p.combdes ||'|'||
                        p.combcod ||'|'||
                        '1' ||'|'|| --Combustivel
                        '' ||'|'||
                        '' ||'|'||
                        1 ||'|' as Produto
                        from fro_comb p
                        union all
                        select distinct
                        substring (upper(i.iteetqdes) from 1 for 70 ) ||'|'||
                        '9999' ||'|'||
                        '3' ||'|'|| -- 1 Combustivel |2 Óleo/Lubrificante |3 Peças | 4 Serviços | 5 Pneus | 6 Acessorios
                        '' ||'|'||
                        '' ||'|'||
                        1 ||'|' --1 Ativo
                        from fro_man2 m2
                        join fro_iteetq i on (i.iteetqcod = m2.iteetqcod) """,

        'VeiculoProduto' : f""" select
                                distinct
                                {codEntidade} ||'|'||
                                coalesce(cast(a.veicod as varchar), '') ||'|'||
                                coalesce(cast(a.combcod as varchar),'') ||'|'||
                                coalesce(c.combdes, '') ||'|' as veiculoProduto
                                FROM public.fro_abastecimentos a
                                join fro_comb c on (c.combcod = a.combcod) """,

        'MotoristaCategoriaCnh' : f""" SELECT
                                        {codEntidade} ||'|'||
                                        m.motpescod ||'|'||
                                        case m.mothabcat
                                        when 'A' then 'A'
                                        when 'B' then 'B'
                                        when 'C' then 'C'
                                        when 'D' then 'D'
                                        when 'E' then 'E'
                                        when 'AB' then 'B'
                                        when 'AC' then 'C'
                                        when 'AD' then 'D'
                                        when 'AE' then 'E' else 'A' end ||'|' as MotoristaCatCnh
                                        FROM public.fro_mot m
                                        join fro_pes p on (p.pescod = m.motpescod) """,

        'MotoristaSituacaoCnh' : f""" SELECT
                                    {codEntidade} ||'|'||
                                    m.motpescod ||'|'||
                                    DATE_PART('day',(SELECT CURRENT_DATE)) ||'/'|| DATE_PART('month',(SELECT CURRENT_DATE)) ||'/'|| DATE_PART('YEAR',(SELECT CURRENT_DATE)) ||'|'||
                                    case motativo
                                    when true then 1
                                    else 2 end ||'|'||
                                    '0' ||'|' as MotoridtaSitCnh
                                    FROM public.fro_mot m
                                    join fro_pes p on (p.pescod = m.motpescod) """,

        'Abastecimento' : f""" SELECT
                                {codEntidade} ||'|'||
                                coalesce(cast(a.abastecimentocod as varchar), '') ||'|'||
                                coalesce(cast(a.veicod as varchar), '') ||'|'||
                                coalesce(v.veicodbenpat, '') ||'|'||
                                coalesce(cast(a.combcod as varchar),'') ||'|'||
                                case c.combdes
                                when 'ALCOOL' then 'ALCOOL COMUM'
                                when 'DIESEL S10' then 'OLEO DIESEL S-10' else c.combdes end ||'|'||
                                case coalesce(cast(a.solicitantecodigo as varchar),'')
                                when '0' then '22732' else coalesce(cast(a.solicitantecodigo as varchar),'') end ||'|'||
                                coalesce(replace (cast(a.abastecimentovalorun as varchar), '.',','),'') ||'|'||
                                coalesce(substring(cast(a.abastecimentodatahora as varchar) from 9 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 6 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 1 for 4) ||' '|| substring(cast(a.abastecimentodatahora as varchar) from 12 for 8),'') ||'|'||
                                coalesce(replace(cast(a.abastecimentoqtd as varchar), '.', ','),'') ||'|'||
                                coalesce(replace(cast(a.abastecimentovalorun * a.abastecimentoqtd as varchar),'.',','),'') ||'|'||
                                '1' ||'|'|| --1 Completo
                                coalesce(replace(replace(coalesce(cast(a.abastecimentodoc as varchar),''),'/',''),'.', ''),'') ||'|'||
                                coalesce(regexp_replace(a.abastecimentoobservacao, E'[\n\r]+', ' ', 'g' ),'') ||'|'||
                                case when a.forpescod = 0 then '25149' else replace(coalesce(cast (a.forpescod as varchar),''),'.', '') end ||'|'||
                                coalesce(replace(replace(replace(p.pescpfcnpj, '.',''), '/',''), '-',''),'77488005000806') ||'|'||
                                coalesce(replace(cast (a.solicitantecodigo as varchar), '0', ''), '') ||'|'||
                                a.cccod ||'|'||
                                '' ||'|'||
                                case a.abastecimentodanificado
                                when 'S' then '2'
                                when 'N' then '1' else 1 end ||'|'||
                                '' ||'|'||
                                '' ||'|'||
                                '' ||'|'||
                                '' ||'|'||
                                {codEntidade} ||'|'||
                                {codEntidade} ||'|'||
                                coalesce(cast(a.abastecimentoempano as varchar), '') ||'|'||
                                coalesce(a.abastecimentoempnum, '') ||'|'||
                                coalesce(cast(a.abastecimentoempano as varchar), '') ||'|'||
                                39 ||'|' as exportAbastecimento
                                FROM public.fro_abastecimentos a
                                join fro_veic v on (v.veicod = a.veicod)
                                join fro_comb c on (c.combcod = a.combcod)
                                left join fro_pes p on (p.pescod = a.forpescod)
                                order by a.abastecimentocod """,

        'Acumulador' : f""" SELECT
                            {codEntidade} ||'|'||
                            coalesce(cast(a.veicod as varchar), '') ||'|'||
                            coalesce(v.veicodbenpat, '') ||'|'||
                            coalesce(substring(cast(a.abastecimentodatahora as varchar) from 9 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 6 for 2) ||'/'|| substring(cast(a.abastecimentodatahora as varchar) from 1 for 4) ||' '|| substring(cast(a.abastecimentodatahora as varchar) from 12 for 8),'') ||'|'||
                            '2' ||'|'|| --2 = Abastecimento
                            coalesce(cast(a.abastecimentocod as varchar), '') ||'|'||
                            replace(cast(a.abastecimentokmhr as varchar), '.', ',') ||'|'||
                            replace(cast(a.abastecimentokmhr as varchar), '.', ',') ||'|' as Acumulador
                            FROM public.fro_abastecimentos a
                            join fro_veic v on (v.veicod = a.veicod)
                            join fro_comb c on (c.combcod = a.combcod)
                            union all
                            SELECT
                            {codEntidade} ||'|'||
                            s.veicod ||'|'||
                            '' ||'|'||
                            coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 1 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
                            '3' ||'|'|| -- 3= Ordem de Serviço
                            '' ||'|'||
                            replace(cast(s.manveikmhr as varchar), '.',',') ||'|'||
                            replace(cast(s.manveikmhr as varchar), '.',',') ||'|'
                            from fro_man s """,

        'VeiculoControleSimAm' : f""" select
                                    {codEntidade} ||'|'||
                                    csa.veicod ||'|'||
                                    csa.veihodhorseq ||'|'||
                                    2 ||'|'||
                                    coalesce(substring(cast(csa.veihodhordatcad as varchar) from 9 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 6 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 1 for 4), '') ||'|'||
                                    replace(cast(csa.veihodhorkmhr as varchar), '.', '') ||'|'||
                                    coalesce(csa.veihodhormot, '') ||'|'||
                                    '' ||'|'||
                                    1 ||'|'||
                                    replace(cast(csa.veihodhorkmhr as varchar), '.', ',') ||'|'||
                                    replace(cast(coalesce(csa.veihodhorkmhrfin, csa.veihodhorkmhr) as varchar), '.', ',') ||'|'||
                                    replace(cast(csa.veihodhorkmhr as varchar), '.', ',') ||'|'||
                                    coalesce(substring(cast(csa.veihodhordatcad as varchar) from 9 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 6 for 2) ||'/'|| substring(cast(csa.veihodhordatcad as varchar) from 1 for 4), '') ||'|'
                                    from FRO_VEIC_HODHOR csa
                                    order by csa.veicod, csa.veihodhorseq """,

        'OrdemAbastecimento' : f""" SELECT
                                    {codEntidade} ||'|'||
                                    r.requisicaocod ||'|'||
                                    r.veicod ||'|'||
                                    r.reqforpescod ||'|'||
                                    coalesce(replace(replace(replace(f.pescpfcnpj, '.',''), '/',''), '-',''),'77488005000806') ||'|'||
                                    case coalesce(cast(r.pescod as varchar),'')
                                    when '0' then '22732' else coalesce(cast(r.pescod as varchar),'') end ||'|'||
                                    coalesce(substring(cast(r.requisicaodata as varchar) from 9 for 2) ||'/'|| substring(cast(r.requisicaodata as varchar) from 6 for 2) ||'/'|| substring(cast(r.requisicaodata as varchar) from 1 for 4),'') ||'|'||
                                    case c.combdes
                                    when 'OLEO' then '98714'
                                    when 'GASOLINA' then '115754'
                                    when 'ALCOOL' then '3'
                                    when 'DIESEL S10' then '1801'
                                    when 'DIESEL' then '116259' else '' end ||'|'||
                                    '1' ||'|'|| --1 Completo
                                    coalesce(replace(cast(r.requisicaoquantidade as varchar), '.', ','),'0,00') ||'|'||
                                    coalesce(cast (a.abastecimentocod as varchar), '') ||'|'||
                                    '' ||'|'||
                                    0 ||'|'|| -- 0 = Sem Licitação
                                    '' ||'|'||
                                    '' ||'|'||
                                    case cast(r.resppescod as varchar)
                                    when '0' then '' else cast(r.resppescod as varchar) end ||'|'||
                                    coalesce(replace(replace(replace(p.pescpfcnpj, '.',''), '/',''), '-',''),'') ||'|'||
                                    r.cccod ||'|'||
                                    coalesce(regexp_replace(r.requisicaoobservacao, E'[\\n\\r]+', ' ', 'g' ),'') ||'|'||
                                    coalesce(replace(cast(r.requisicaokmhr as varchar), '.', ','),'') ||'|'||
                                    coalesce(replace(cast(r.requisicaokmhr as varchar), '.', ','),'') ||'|'
                                    FROM public.fro_requisicao r
                                    left join public.fro_abastecimentos a on (a.abastecimentoreqcod = r.requisicaocod)
                                    left join fro_pes f on (f.pescod = r.reqforpescod)
                                    left join fro_pes p on (p.pescod = r.resppescod)
                                    left join fro_comb c on (c.combcod = r.combcod)
                                    order by r.requisicaocod """,

        'VeiculoOrdemServico' : f""" select
                                    {codEntidade} ||'|'||
                                    s.mancod ||'|'||
                                    s.veicod ||'|'||
                                    '' ||'|'||
                                    'Serviços Mecanico em Geral' ||'|'||
                                    coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') ||'|'||
                                    coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
                                    coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 1 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
                                    coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 2 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
                                    coalesce(substring(cast(s.mandat as varchar) from 9 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 6 for 2) ||'/'|| substring(cast(s.mandat as varchar) from 1 for 4), '') || ' 00:00:' ||lpad(substring(LPAD(cast(s.mancod + 3 as varchar),6,'0') from 6 for 1), 2, '0') ||'|'||
                                    s.manobs ||'|'||
                                    1 ||'|'|| -- 1-Sim
                                    '' ||'|'||
                                    '' ||'|'||
                                    '' ||'|'||
                                    l.ccdes ||'|'||
                                    l.ccdes ||'|'||
                                    l.ccdes ||'|'||
                                    s.cccod ||'|'
                                    from fro_man s
                                    join fro_cc l on (l.cccod = s.cccod)
                                    order by s.mancod """,

        'VeiculoOrdemServicoProduto' : f""" select
                                            {codEntidade} ||'|'||
                                            m2.mancod ||'|'||
                                            '' ||'|'||
                                            substring (upper(i.iteetqdes) from 1 for 70 ) ||'|'||
                                            replace(cast(m2.maniteqtd as varchar),'.', ',') ||'|'||
                                            replace(cast(m2.maniteqtd * m2.manitevlruni as varchar), '.', ',') ||'|'||
                                            m2.maniteseq ||'|'||
                                            '' ||'|'||
                                            '' ||'|'
                                            from fro_man2 m2
                                            join fro_iteetq i on (i.iteetqcod = m2.iteetqcod) """

        }