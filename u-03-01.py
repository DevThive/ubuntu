import re
import os

def check_pam_tally_settings(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()

        # 설정 확인
        settings = [
            "auth required /lib/security/pam_tally.so deny=5 unlock_time=120",
            "no_magic_root",
            "account required /lib/security/pam_tally.so no_magic_root reset"
        ]

        for setting in settings:
            if setting not in content:
                print(f"설정 누락: {setting}")
                return False

        print("모든 설정이 정상적으로 포함되어 있습니다.")
        return True

    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return False
    except Exception as e:
        print(f"오류 발생: {e}")
        return False

# 사용 예시
file_path = '/etc/pam.d/common-account'  # 적절한 파일 경로로 수정하세요.
check_pam_tally_settings(file_path)
