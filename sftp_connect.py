import pysftp
host = '10.105.92.120'
port = 22
username = 'sftp'
password= 'Password@123456789'
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

try:
  conn = pysftp.Connection(host=host,port=port,username=username, password=password,cnopts=cnopts)
  print("connection established successfully")
except(e):

  print('failed to establish connection to targeted server')