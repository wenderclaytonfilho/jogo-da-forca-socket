import socket

def main():
    host = 'localhost'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        print("Conectado ao servidor.")
        while True:
            data = s.recv(1024).decode()
            if "Parabéns" in data or "perdeu" in data:
                print(data)
                break
            print(data)
            letra = input("Digite uma letra: ")
            s.sendall(letra.encode())

if __name__ == "__main__":
    main()
