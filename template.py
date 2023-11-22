import flet as ft
class Template:
    def tabela_analise(self, arquivo):

        tabela = ft.DataTable(
            divider_thickness=1,
            column_spacing=200,
            heading_row_color=ft.colors.BLACK12,
        columns=[
            ft.DataColumn(ft.Text("Arquivo")),
            ft.DataColumn(ft.Text("Linhas")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Cor')),
                    ft.DataCell(ft.Text(arquivo['Cor'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Marca')),
                    ft.DataCell(ft.Text(arquivo['Marca'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Especie')),
                    ft.DataCell(ft.Text(arquivo['Especie'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Modelo')),
                    ft.DataCell(ft.Text(arquivo['Modelo'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Motorista')),
                    ft.DataCell(ft.Text(arquivo['Motorista'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Motorista Categoria Cnh')),
                    ft.DataCell(ft.Text(arquivo['MotoristaCategoriaCnh'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Veiculo')),
                    ft.DataCell(ft.Text(arquivo['Veiculo'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Produto')),
                    ft.DataCell(ft.Text(arquivo['Produto'])),
                ],
            ),
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text('Veiculo x Produto')),
                    ft.DataCell(ft.Text(arquivo['VeiculoProduto'])),
                ],
            ),
        ],
    )
        tabela_2 = ft.DataTable(
            column_spacing=200,
            heading_row_color=ft.colors.BLACK12,
            columns=[
                ft.DataColumn(ft.Text("Arquivo")),
                ft.DataColumn(ft.Text("Linhas")),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Motorista Situação Cnh')),
                        ft.DataCell(ft.Text(arquivo['MotoristaSituacaoCnh'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Abastecimentos')),
                        ft.DataCell(ft.Text(arquivo['Abastecimento'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Equipamento Consumo de Combustivel')),
                        ft.DataCell(ft.Text(arquivo['EquipamentoConsumoCombustivel'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Acumulador')),
                        ft.DataCell(ft.Text(arquivo['Acumulador'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Controle SimAm')),
                        ft.DataCell(ft.Text(arquivo['VeiculoControleSimAm'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Ordens de Abastecimento')),
                        ft.DataCell(ft.Text(arquivo['OrdemAbastecimento'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Ordens de Serviço')),
                        ft.DataCell(ft.Text(arquivo['VeiculoOrdemServico'])),
                    ],
                ),
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text('Produto Ordem Servico')),
                        ft.DataCell(ft.Text(arquivo['VeiculoOrdemServicoProduto'])),
                    ],
                ),
            ],
        )
        return tabela, tabela_2
