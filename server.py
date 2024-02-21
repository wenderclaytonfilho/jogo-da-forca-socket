import socket
import random 
def random_word():
    words = ["socket","redes","python",""]
    return words[random.randrange(0,3,1)]

def iniciar_jogo():
    palavra = random_word() 
    letras_reveladas = ['_'] * len(palavra)
    chances = 6
    return palavra, letras_reveladas, chances

def atualizar_letras(letra, palavra, letras_reveladas):
    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                letras_reveladas[i] = letra
        return letras_reveladas
    else:
        return letras_reveladas

def main():
    host = 'localhost'
    port = 65432

    palavra, letras_reveladas, chances = iniciar_jogo()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Aguardando conexão...")
        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            conn.sendall(f"{letras_reveladas} Chances restantes: {chances}".encode())
            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break
                letra = data.lower()
                letras_reveladas = atualizar_letras(letra, palavra, letras_reveladas)
                if '_' not in letras_reveladas:
                    conn.sendall("Parabéns! Você ganhou!".encode())
                    break
                elif chances == 0:
                    conn.sendall("Você perdeu! A palavra era: 'python'".encode())
                    break
                else:
                    if letra not in palavra:
                        chances -= 1
                    conn.sendall(f"{letras_reveladas} Chances restantes: {chances}".encode())

if __name__ == "__main__":
    main()
