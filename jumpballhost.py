import socket

HOST = '192.168.1.5'  # Listen on all interfaces
PORT = 12341

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2)  # Accept up to 2 clients

print(f"Server started. Waiting for players to connect on port {PORT}...")

players = []

while len(players) < 2:
    conn, addr = server_socket.accept()
    print(f"Player {len(players) + 1} connected from {addr}")
    players.append(conn)
    conn.sendall(str(len(players)).encode())

print("Both players connected. Game can begin!")

# Now keep the server running to maintain the connections
try:
    while True:
        for i, player in enumerate(players):
            try:
                data = player.recv(1024)
                if data:
                    print(f"Received from Player {i + 1}: {data.decode()}")
            except:
                continue
except KeyboardInterrupt:
    print("Server shutting down.")
finally:
    for p in players:
        p.close()
    server_socket.close()
