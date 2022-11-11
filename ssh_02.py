from  mail import NMail
import paramiko
import sys
import datetime
import time
import os

def sshExeCMD():
 for i in range(3):    
  ssh_client=paramiko.SSHClient()
  ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh_client.connect(hostname="10.10.13.41", port="22", username="root", password="1qaz!@#2WSX")
  except Exception as err:
      print("10.10.13.41 ssh failed")
      print(err)
      
      #info = err
      nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
      data = {
          "subject": "10.10.13.41 ssh failed"+str(nowTime),
          "content":  str(err),
          "receiver": "tecorigin_ops@tecorigin.com"
      }
      msg = NMail(username="suj@tecorigin.com", password="bsxiSF8odxR97Vkg")
      msg.send_email(data)
      #os.system('ipmitool -I lanplus -H 10.10.13.38 -U ADMIN -P Test@123 power  reset')
      break

      #sys.exit()
  stdin, stdout, stderr = ssh_client.exec_command("exit")
  time.sleep(5)
  print(str(stdout.read()))

if __name__ == '__main__':
  sshExeCMD()

