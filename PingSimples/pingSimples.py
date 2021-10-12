import os ## Importa a biblioteca que integra os recurso do sistema operacional

print("#" * 60)
ip_ou_hodt = input("Digite o Ip ou host a ser verificado: ")
print("-" * 60)
os.system('ping -n 6 {}'. format(ip_ou_hodt))
print("-" * 60)