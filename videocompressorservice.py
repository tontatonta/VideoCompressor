import socket

def send_request(command_number, file_name, output_file, address, port):
    request = f"{command_number} {file_name} {output_file}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((address, port))
        s.sendall(request.encode())
        data = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            data += chunk
        with open(output_file, "wb") as f:
            f.write(data)
        print(f"Video processed and downloaded successfully as {output_file}.")

if __name__ == "__main__":
    command_number = input("Enter the command number (1: Compress, 2: Change resolution, 3: Change the video aspect ratio, 4: Convert video to audio, 5: Create GIFs): ")
    file_name = input("Enter the file name to process: ")
    output_file = input("Enter the output file name: ")
    send_request(command_number, file_name, output_file, "localhost", 9050)