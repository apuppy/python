from socket import *
serverAddr = ('127.0.0.1',12000)
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(serverAddr)
serverSocket.listen(5)
print('The server is ready to receive')
while True:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024)
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence)
    connectionSocket.close()