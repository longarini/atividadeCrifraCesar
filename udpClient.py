from socket import *
serverName = "127.0.0.1"
serverPort = 13597
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("UDP Client\n")
while 1:
    message = input("Input message: ")
    if message == "exit":
        break

    messageCript = ""
    
    for c in message:
         cPlus = ord(c)
         if (cPlus + 5) > 255: 
            cPlus = (cPlus + 5) - 255
         else: 
            cPlus = cPlus + 5
         
         messageCript = messageCript + chr(cPlus)

    print(messageCript)
    clientSocket.sendto(bytes(messageCript,"utf-8"), (serverName, serverPort))
clientSocket.close()