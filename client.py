import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
  while True:
    try:
      message = client.recv(1024).decode('ascii')
      if message == "NICK":
        client.send(nickname.encode('ascii'))
      else:
        print(message)
  except:
    print("An error ocurred!")
    client.close()
    break

def write():
  while True:
    message = f'{nickname}: {input("")}'
    client.send(message.encode('ascii'))

receice_thread = threading.Thread(target=receive)
receice_thread.start()

write_thread = threading.Thread(target=wite)
write_thread.start()