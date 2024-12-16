
##client
import socket          # Import Python Standard Socket Library
import sys

print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555")

PORT = 5555          # Port Number of Server
    
try:
    # Create a Socket
    clientSocket = socket.socket()
    
    # Get my local host address
    localHost = socket.gethostname()
    
    print("\nAttempt Connection to: ", localHost, PORT)
    
    clientSocket.connect((localHost, PORT))
    
    # Sending message if there was a connection
    print("Socket Connected ...")
    print("Sending Message to Server")
    
    ###10 automated messages from client to server
    for i in range(1,11):
        msg= "Message" + str(i)
        print("Sending", msg)
        
        
        messageBytes = bytes(msg.encode("utf-8"))
        clientSocket.sendall(messageBytes)
    
        buffer = clientSocket.recv(2048)
        print(buffer)
    
    ##Letting user know that the 10 messages has been sent and the connection has ended
    print("All message has been sent, connection is closed")
    clientSocket.close()
    
except Exception as err:
    sys.exit(err)

            
