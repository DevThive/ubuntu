import os

def check_password_file_rule(file):
    # 파일 권한 정보를 가져옴
    result = os.popen(f"ls -al {file}").read()
    
    # 권한 부분 추출
    permissions = result.split()[0]

    # 권한 확인
    if permissions == 'rw-r-----':
        print(f"{file} 파일의 권한이 rw-r-----으로 설정되어 있습니다.")
    else:
        print(f"{file} 파일의 권한이 rw-r-----이 아닙니다. 현재 권한: {permissions}")

def check_passwd_file():
    file_path = '/etc/passwd'
    
    if os.path.exists(file_path):
        print(f"{file_path} 파일이 존재합니다.")
        check_password_file_rule(file_path)
    else:
        print(f"{file_path} 파일이 존재하지 않습니다.")

# 파일 존재 확인 실행
check_passwd_file()
