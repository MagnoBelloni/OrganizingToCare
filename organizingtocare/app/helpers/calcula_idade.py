from datetime import date, datetime

def CalcularIdade(data_nascimento):
    today = date.today()
    idade = today.year - data_nascimento.year - ((today.month, today.day) < (data_nascimento.month, data_nascimento.day))
    return idade

"""

Exemplo de uso:

data_e_hora_em_texto = '19990703'
data = datetime.strptime(data_e_hora_em_texto, '%Y%m%d').date()
CalcularIdade(data)

# melhoria futura, devolver ano, mês
# e dia de nascimento
"""