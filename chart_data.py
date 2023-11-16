import flet as ft

name = "PieChart 2"


def build_chart(data_values):

    normal_radius = 50
    hover_radius = 60
    normal_title_style = ft.TextStyle(
        size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
    )
    hover_title_style = ft.TextStyle(
        size=22,
        color=ft.colors.WHITE,
        weight=ft.FontWeight.BOLD,
        shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
    )

    sections = []
    for value in data_values:
        section = ft.PieChartSection(
            value,
            title=f"{value}%",
            title_style=normal_title_style,
            # Definir a cor e outros atributos conforme necessário
        )
        sections.append(section)

    async def on_chart_event(e: ft.PieChartEvent):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = hover_radius
                section.title_style = hover_title_style
            else:
                section.radius = normal_radius
                section.title_style = normal_title_style
        await chart.update_async()

    chart = ft.PieChart(
        sections=sections,
        sections_space=0,
        center_space_radius=40,
        on_chart_event=on_chart_event,
        expand=True,
    )

    return chart