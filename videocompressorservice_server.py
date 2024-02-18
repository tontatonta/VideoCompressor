import socket
import ffmpeg

class VideoProcessor: #動画を変更するクラス
    def __init__(self):
        pass

    def compress_video(self, input_file, output_file, bitrate='1000k'):# 圧縮する関数
        (
            ffmpeg
            .input(input_file)
            .output(output_file, bitrate=bitrate)
            .run()
        )

    def change_resolution(self, input_file, output_file, resolution='720x480'): # 解像度を変更する関数
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vf=f"scale={resolution}")
            .run()
        )

    def change_aspect_ratio(self, input_file, output_file, aspect_ratio='1:1'): # アスペクト比を変更する関数
        (
            ffmpeg
            .input(input_file)
            .output(output_file, vf=f"setsar={aspect_ratio}")
            .run()
        )

    def convert_to_audio(self, input_file, output_file): # 音声ファイルへ変換する関数
        (
            ffmpeg
            .input(input_file)
            .output(output_file, acodec='mp3')
            .run()
        )

    def convert_to_gif(self, input_file, output_file, start_time, duration, fps=10): #gifへ変更する関数
        (
            ffmpeg
            .input(input_file, ss=start_time, t=duration)
            .output(output_file, vf=f"fps={fps}", pix_fmt='rgb24')
            .run()
        )



class Server:
    def __init__(self, address, port):
        self.address = address
        self.port = port
        self.processor = VideoProcessor()

    def handle_client(self, conn):
        request = conn.recv(1024).decode().split()
        command_number = request[0]
        file_name = request[1]
        output_file = request[2]
        if command_number == '1':
            self.process_video('compress', file_name, output_file)
        elif command_number == '2':
            self.process_video('change_resolution', file_name, output_file)
        elif command_number == '3':
            self.process_video('change_aspect_ratio', file_name, output_file)
        elif command_number == '4':
            self.process_video('convert_to_audio', file_name, output_file)
        elif command_number == '5':
            self.process_video('convert_to_gif', file_name, output_file)

        with open(output_file, "rb") as f:
            data = f.read()
            conn.sendall(data)

    def process_video(self, method, input_file, output_file):
        if method == 'compress':
            self.processor.compress_video(input_file, output_file)
        elif method == 'change_resolution':
            self.processor.change_resolution(input_file, output_file)
        elif method == 'change_aspect_ratio':
            self.processor.change_aspect_ratio(input_file, output_file)
        elif method == 'convert_to_audio':
            self.processor.convert_to_audio(input_file, output_file)
        elif method == 'convert_to_gif':
            self.processor.convert_to_gif(input_file, output_file, start_time=10, duration=5)

    def start(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.address, self.port))
            s.listen(1)
            print("Server is listening...")
            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    self.handle_client(conn)

if __name__ == "__main__":
    server = Server("localhost", 9050)
    server.start()
