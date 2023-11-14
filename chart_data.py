
import flet as ft

class ChartData:
    def __init__(self, sections, center_space_radius=40, sections_space=0):
        self.sections = sections
        self.center_space_radius = center_space_radius
        self.sections_space = sections_space
        self.normal_radius = 50
        self.hover_radius = 60
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=22,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )

    async def on_chart_event(self, e: ft.PieChartEvent, chart: ft.PieChart):
        for idx, section in enumerate(chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        await chart.update_async()

    def create_chart(self):
        chart_sections = [
            ft.PieChartSection(
                value,
                title=f"{value}%",
                title_style=self.normal_title_style,
                color=color,
                radius=self.normal_radius,
            )
            for value, color in self.sections
        ]

        chart = ft.PieChart(
            sections=chart_sections,
            sections_space=self.sections_space,
            center_space_radius=self.center_space_radius,
            on_chart_event=self.on_chart_event,
            expand=True,
        )

        return chart
