from datetime import datetime

now = datetime.now()

# Formatar datetime com mascara
print(now.strftime("%d/%m/%Y %H:%M"))

# Conversao string para datetime
date_string = "20/07/2024 09:30"

parse_date = datetime.strptime(date_string, "%d/%m/%Y %H:%M")
print(parse_date)
