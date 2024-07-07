from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from datetime import datetime

data_de_teste = "2024-07-01"

parsed_data_de_teste = parse(data_de_teste)
print("\nData de teste:", parsed_data_de_teste)

date_relative = "next tuesday at 4pm"
parsed_date = parse(date_relative, fuzzy=True)
print("Data relativa (", date_relative, "):", parsed_date)

date1 = parse("2022-03-05")
date2 = parse("2022-03-10")
diff = relativedelta(date2, date1)
print("Diferença entre as datas:", diff.days)

current_date = datetime.now()
print("Data atual:", current_date)

daqui_sete_dias = current_date + relativedelta(days=7)
print("Data daqui a sete dias:", daqui_sete_dias)

daqui_uma_semana = current_date + relativedelta(weeks=1)
print("Data daqui a uma semana:", daqui_uma_semana)

daqui_um_mes = current_date + relativedelta(months=1)
print("Data daqui a um mês:", daqui_um_mes)

daqui_um_ano = current_date + relativedelta(years=1)
print("Data daqui a um ano:", daqui_um_ano.strftime("%Y-%m-%d"))

