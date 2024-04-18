from django import template
import calendar

register = template.Library()

traducoes_mes = {
    'January': 'Janeiro',
    'February': 'Fevereiro',
    'March': 'Março',
    'April': 'Abril',
    'May': 'Maio',
    'June': 'Junho',
    'July': 'Julho',
    'August': 'Agosto',
    'September': 'Setembro',
    'October': 'Outubro',
    'November': 'Novembro',
    'December': 'Dezembro'
}

traducoes_semana = {
    'Monday': 'Segunda-feira',
    'Tuesday': 'Terça-feira',
    'Wednesday': 'Quarta-feira',
    'Thursday': 'Quinta-feira',
    'Friday': 'Sexta-feira',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
}

@register.filter
def mes_extenso(numero):
    nome_mes = calendar.month_name[numero]
    return traducoes_mes.get(nome_mes, nome_mes)

@register.filter
def semana_extenso(numero):
    nome_semana = calendar.day_name[numero]
    return traducoes_semana.get(nome_semana, nome_semana)