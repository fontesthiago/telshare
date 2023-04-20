#importando módulos
import os, shutil, logging, socket


#configuração de log, para consulta após instalação
logging.basicConfig(level=logging.INFO, filename="install.log", format="%(asctime)s - %(levelname)s - %(message)s")
logging.info(f"\n\n\nINSTALAÇAO INICIADA NO COMPUTADOR:   {socket.gethostname()}")


#define o local de instalação
installationdirectory = 'c:\windows'


#Copia o script para a pasta destino da instalação
try:
    shutil.copy2('SharingConnection.ps1', installationdirectory)
    logging.info('arquivo de script foi copiado')
except:
    logging.info('arquivo de script NÃO foi copiado')


#tenta criar a tarefa que será iniciada junto com o usuário
try:
    os.popen(rf'schtasks /create /sc ONLOGON /ru System /tr {installationdirectory}\sharingconnection.ps1 /tn smed\SharingConnection')
    logging.info('Tarefa criada')

except:
    logging.info('Tarefa criada')




"""
documentação para criação de tarefas:
https://learn.microsoft.com/pt-br/windows-server/administration/windows-commands/schtasks-create


"""