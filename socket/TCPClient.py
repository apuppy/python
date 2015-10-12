from socket import *
serverAddr = ('127.0.0.1',12000)
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(serverAddr)
sentence = input('Input lowercase sentense:')
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print('From server:',modifiedSentence.decode('utf-8'))
clientSocket.close()