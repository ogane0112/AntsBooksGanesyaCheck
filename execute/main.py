# src/main.py

def process_file_content(content):
    # ファイルの内容を処理する関数
    return content.upper()  # 例としてすべて大文字にする処理

def main():
    # 標準入力からすべての入力を読み取る
    content = input()
    result = process_file_content(content)
    print(result)

if __name__ == "__main__":
    main()
