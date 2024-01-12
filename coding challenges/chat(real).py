import socket
import hashlib
import hmac
from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipherSuite = Fernet(key)


def server():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('localhost', 1234))
    serverSocket.listen(1)
    print("Server listening on port 1234...")
    clientSocket, clientAddress = serverSocket.accept() 
    print("Connected with client:", clientAddress)

    encryptedMessage = clientSocket.recv(1024)
    decryptedMessage = cipherSuite.decrypt(encrypted_message)
    hashValue = decryptedMessage[:128]
    message = decrypted_message[128:]
    sha512 = hashlib.sha512()
    sha512.update(message)
    calculatedHash = sha512.hexdigest()
    if calculatedHash == hashValue.decode():
        print('Integrity verification successful')
    else:
        print('Integrity verification failed')
    responseMessage = 'Response from server'
    responseHash = hmac.new(key, responseMessage.encode(), hashlib.sha1).hexdigest()
    response = responseHash + responseMessage
    encryptedResponse = cipherSuite.encrypt(response.encode())
    connection.send(encryptedResponse)
    connection.close()



def client():
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect(('localhost', 1234))
    print("Connected to server...")
    
    message = 'Hello from client'
    messageHash = hmac.new(key, message.encode(), hashlib.sha1).hexdigest()
    message = messageHash + message
    encryptedMessage = cipherSuite.encrypt(message.encode())
    clientSocket.send(encryptedMessage)
    encryptedResponse = clientSocket.recv(1024)
    decryptedResponse = cipherSuite.decrypt(encryptedResponse)
    hashValue = decryptedResponse[:40]
    response = decryptedResponse[40:]
    calculatedHash = hmac.new(key, response, hashlib.sha1).hexdigest()
    if calculated_hash == hashValue.decode():
        print('Integrity verification successful')
        print('Response:', response.decode())
    else:
        print('Integrity verification failed')
    client_socket.close() 



server()
client()
