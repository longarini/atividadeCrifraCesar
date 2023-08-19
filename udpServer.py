from socket import *
serverPort = 13597
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("UDP server\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8")
    
    messageDecript = ""
    
    for c in text:
         cMinus = ord(c)
         if (cMinus - 5) < 0: 
            cMinus = (cMinus - 5) + 255
         else: 
            cMinus = cMinus - 5
         
         messageDecript = messageDecript + chr(cMinus)

    print("Received from Client: ", messageDecript)
