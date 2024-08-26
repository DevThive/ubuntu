import re

def check_password_complexity(file_path='/etc/login.defs'):
    """
    비밀번호 복잡성 정책 파일을 읽고 복잡성 설정이 정상적인지 확인합니다.

    :param file_path: 비밀번호 정책 파일 경로
    :return: 정책 설정 검사 결과
    """
    # 설정 기본값
    policy = {
        "PASS_MIN_LEN": None,  # 최소 길이
        "MIN_SPECIAL_CHARS": None,  # 최소 특수 문자 사용 횟수
        "MIN_LOWERCASE": None,  # 최소 소문자 사용 횟수
        "MIN_UPPERCASE": None,  # 최소 대문자 사용 횟수
    }

    vulnerability_messages = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 주석 및 빈 줄 무시
                if line.strip().startswith('#') or not line.strip():
                    continue

                # 설정 항목 파싱
                match = re.search(r'^\s*PASS_MIN_LEN\s+(\d+)', line)
                if match:
                    policy['PASS_MIN_LEN'] = int(match.group(1))

                match = re.search(r'^\s*MIN_SPECIAL_CHARS\s+(\d+)', line)
                if match:
                    policy['MIN_SPECIAL_CHARS'] = int(match.group(1))

                match = re.search(r'^\s*MIN_LOWERCASE\s+(\d+)', line)
                if match:
                    policy['MIN_LOWERCASE'] = int(match.group(1))

                match = re.search(r'^\s*MIN_UPPERCASE\s+(\d+)', line)
                if match:
                    policy['MIN_UPPERCASE'] = int(match.group(1))

        # 주석 처리 여부 확인
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip().startswith('#'):
                    if 'PASS_MIN_LEN' in line:
                        vulnerability_messages.append("비밀번호 최소 길이 설정이 주석 처리되어 있습니다.")
                    if 'MIN_SPECIAL_CHARS' in line:
                        vulnerability_messages.append("비밀번호 특수 문자 최소 개수 설정이 주석 처리되어 있습니다.")
                    if 'MIN_LOWERCASE' in line:
                        vulnerability_messages.append("비밀번호 소문자 최소 개수 설정이 주석 처리되어 있습니다.")
                    if 'MIN_UPPERCASE' in line:
                        vulnerability_messages.append("비밀번호 대문자 최소 개수 설정이 주석 처리되어 있습니다.")

        # 정책 검증
        if policy['PASS_MIN_LEN'] is None:
            vulnerability_messages.append("비밀번호 최소 길이 설정이 없습니다.")
        elif policy['PASS_MIN_LEN'] < 8:
            vulnerability_messages.append("비밀번호 최소 길이는 8자 이상이어야 합니다. (현재 설정: {})".format(policy['PASS_MIN_LEN']))

        if policy['MIN_SPECIAL_CHARS'] is None:
            vulnerability_messages.append("비밀번호 특수 문자 최소 개수 설정이 없습니다.")
        elif policy['MIN_SPECIAL_CHARS'] < 2:
            vulnerability_messages.append("비밀번호는 최소 2개의 특수 문자를 포함해야 합니다. (현재 설정: {})".format(policy['MIN_SPECIAL_CHARS']))

        if policy['MIN_LOWERCASE'] is None:
            vulnerability_messages.append("비밀번호 소문자 최소 개수 설정이 없습니다.")
        elif policy['MIN_LOWERCASE'] < 1:
            vulnerability_messages.append("비밀번호는 최소 1개의 소문자를 포함해야 합니다. (현재 설정: {})".format(policy['MIN_LOWERCASE']))

        if policy['MIN_UPPERCASE'] is None:
            vulnerability_messages.append("비밀번호 대문자 최소 개수 설정이 없습니다.")
        elif policy['MIN_UPPERCASE'] < 1:
            vulnerability_messages.append("비밀번호는 최소 1개의 대문자를 포함해야 합니다. (현재 설정: {})".format(policy['MIN_UPPERCASE']))

        # 결과 출력
        if vulnerability_messages:
            return "\n".join(vulnerability_messages)
        else:
            return "비밀번호 복잡성 설정이 정상적으로 설정되었습니다."

    except FileNotFoundError:
        return f"파일을 찾을 수 없습니다: {file_path}"
    except Exception as e:
        return f"정책 파일을 읽는 중 오류가 발생했습니다: {str(e)}"


# 예시 테스트
result = check_password_complexity()
print(result)
