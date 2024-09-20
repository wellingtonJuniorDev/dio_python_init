# pip install pytz

import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Europe/Oslo'))

print(data)

data_sao_paulo = datetime.now(pytz.timezone('America/Sao_Paulo'))

print(data_sao_paulo)
