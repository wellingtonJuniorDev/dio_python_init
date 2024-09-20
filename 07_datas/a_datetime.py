from datetime import date, datetime, time, timedelta

data = date(2024,9,20)
print(data)

data_hora = datetime(2024,9,20, 8,50,30)
print(datetime.today())

hora = time(10,20,0)
print(hora)

# operacoes timedelta https://docs.python.org/pt-br/3/library/datetime.html#datetime.timedelta
tipo_carro = 'G' # P,M,G
tempo_p = 30
tempo_m = 45
tempo_g = 60

data_atual = datetime.now()

if tipo_carro=='P':
    data_estimada = data_atual + timedelta(minutes= tempo_p)
    print(f"chegou às {data_atual} e fica pronto às {data_estimada}")

elif tipo_carro=='M':
    data_estimada = data_atual + timedelta(minutes= tempo_m)
    print(f"chegou às {data_atual} e fica pronto às {data_estimada}")

else:
    data_estimada = data_atual + timedelta(minutes= tempo_g)
    print(f"chegou às {data_atual} e fica pronto às {data_estimada}")
    
print(date.today() - timedelta(days=1))

calculo_time = datetime(2024,9,20,9,10) - timedelta(hours=1)
print(calculo_time.time())

