from datetime import datetime

# Data e hora atual
atual = datetime.now()
s1 = atual.strftime("%d/%m/%Y")
# mm/dd/YY H:M:S
print("s1:", s1)
