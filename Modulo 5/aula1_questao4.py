#Blibioteca
from datetime import datetime

#Dados
d=datetime.now()
data=d.strftime('%d/%m/%Y')
hora=d.strftime('%H:%M')
print("Data: ", data)
print("Hora: ", hora)