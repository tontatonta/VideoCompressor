## プログラム1: videocompressorservice.py

### 概要

このプログラムは、サーバーにリクエストを送信し、指定されたビデオファイルの処理結果を受け取ります。処理内容としては、ビデオの圧縮、解像度の変更、アスペクト比の変更、ビデオから音声への変換、GIFへの変換があります。

### 使い方

1. プログラムを実行します。
2. コマンド番号を入力します（1: 圧縮、2: 解像度変更、3: アスペクト比変更、4: ビデオから音声への変換、5: GIFへの変換）。
3. 処理したいビデオファイルの名前を入力します。
4. 処理結果の出力ファイル名を入力します。
5. サーバーアドレスとポート番号はデフォルトで設定されていますが、必要に応じて変更してください。

### 実行方法

1. ターミナルで次のコマンドを実行します。

### 注意事項

- サーバーアドレスとポート番号は適切に設定してください。

---

## プログラム2: videocompressorservice_server.py

### 概要

このプログラムは、指定されたサーバーアドレスとポート番号でリクエストを待ち受け、受け取ったリクエストに応じてビデオの処理を行います。処理内容は、ビデオの圧縮、解像度の変更、アスペクト比の変更、ビデオから音声への変換、GIFへの変換があります。

### 使い方

1. プログラムを実行します。
2. クライアントからのリクエストを待ちます。
3. リクエストを受け取り、指定された処理を行います。
4. 処理結果をクライアントに送信します。

### 実行方法

1. ターミナルで次のコマンドを実行します。

### 注意事項

- UNIXドメインソケットのパスは適切に設定してください。

---
