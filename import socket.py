import socket

def receive_message():
    
    received_message = b'Your secret message here'
    encryption_key = 'random_encryption_key'  
    decrypted_message = decrypt_message(received_message, encryption_key)
    print("Received Message:", decrypted_message)
    def notify_admin():
        
        pass

def decrypt_message(encrypted_message, encryption_key):
    
    return encrypted_message


receive_message()