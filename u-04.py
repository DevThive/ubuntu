import os

def check_password_encryption():
    """
    /etc/shadow 파일에서 사용자 계정의 비밀번호 암호화 여부를 확인합니다.

    :return: 비밀번호 암호화 검사 결과 메시지
    """
    shadow_file = '/etc/shadow'
    
    if not os.path.exists(shadow_file):
        return f"파일이 존재하지 않습니다: {shadow_file}"

    encrypted_users = []
    non_encrypted_users = []

    with open(shadow_file, 'r') as file:
        for line in file:
            parts = line.split(':')
            if len(parts) > 1:
                username, password_hash = parts[0], parts[1]

                if password_hash in ['!', '*', '']:
                    # 비밀번호가 설정되지 않았거나, 계정이 비활성화됨
                    non_encrypted_users.append((username, "비밀번호 없음 또는 계정 비활성화"))
                elif password_hash.startswith('$'):
                    # 암호화된 비밀번호 (ex. $1$, $2a$, $5$, $6$ 등)
                    encrypted_users.append(username)
                else:
                    # 암호화되지 않은 비밀번호
                    non_encrypted_users.append((username, "암호화되지 않은 비밀번호"))

    result_message = "암호화된 비밀번호를 가진 사용자:\n"
    result_message += "\n".join(encrypted_users) + "\n\n"
    
    if non_encrypted_users:
        result_message += "암호화되지 않은 비밀번호를 가진 사용자 또는 비밀번호가 없는 사용자:\n"
        for user, reason in non_encrypted_users:
            result_message += f"{user}: {reason}\n"
    else:
        result_message += "모든 사용자의 비밀번호가 암호화되어 있습니다."

    return result_message

if __name__ == "__main__":
    result = check_password_encryption()
    print(result)
