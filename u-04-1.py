import os

def check_root_password_field(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('root:'):
                    fields = line.strip().split(':')
                    if len(fields) > 1 and fields[1] == 'x':
                        print("---------------------------------")
                        print("root의 두 번째 필드가 'x'입니다.")
                        print("---------------------------------")
                    else:
                        print("---------------------------------")
                        print("root의 두 번째 필드가 'x'가 아닙니다.")
                        print("---------------------------------")
                    break
            else:
                print("root 사용자 정보를 찾을 수 없습니다.")
    
    except FileNotFoundError:
        print("---------------------------------")
        print(f"{file_path} 파일이 존재하지 않습니다.")
        print("---------------------------------")
    except Exception as e:
        print("---------------------------------")
        print(f"오류 발생: {e}")
        print("---------------------------------")

def change_passwd_permissions():
    try:
        result = os.system('sudo chmod 640 /etc/passwd')
        if result == 0:
            print("권한이 성공적으로 변경되었습니다: /etc/passwd의 권한이 640으로 설정됨.")
        else:
            print("권한 변경 중 오류가 발생했습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

def check_password_file_rule(file):
    # 파일 권한 정보를 가져옴
    result = os.popen(f"ls -al {file}").read().strip()
    
    # 권한 부분 추출
    permissions = result.split()[0][1:]  # 첫 문자 '-'를 제외하고 권한 부분만 가져옴

    # 권한 확인
    if permissions == 'rw-r-----':
        print(f"{file} 파일의 권한이 rw-r-----으로 설정되어 있습니다.")
    else:
        print(f"{file} 파일의 권한이 rw-r-----이 아닙니다. 현재 권한: {permissions}")
        change_passwd_permissions()

def check_passwd_file():
    file_path = '/etc/passwd'
    
    if os.path.exists(file_path):
        print(f"{file_path} 파일이 존재합니다.")
        check_password_file_rule(file_path)
        check_root_password_field(file_path)
    else:
        print(f"{file_path} 파일이 존재하지 않습니다.")

# 함수 실행
check_passwd_file()
