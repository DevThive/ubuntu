import os

def check_passwd_file():
    file_path = '/etc/passwd'
    
    if os.path.exists(file_path):
        print(f"{file_path} 파일이 존재합니다.")
    else:
        print(f"{file_path} 파일이 존재하지 않습니다.")

# 파일 존재 확인 실행
check_passwd_file()
