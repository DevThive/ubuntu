import re


def check_password_policy(file_path='/etc/security/pwquality.conf'):
    """
    비밀번호 정책 파일을 읽고 복잡성 설정이 정상적인지 확인합니다.

    :param file_path: 비밀번호 정책 파일 경로
    :return: 정책 설정 검사 결과
    """
    # 설정 기본값
    policy = {
        "minlen": 8,  # 최소 길이
        "minclass": 3,  # 최소 클래스 (대문자, 소문자, 숫자, 특수 문자)
    }

    try:
        with open(file_path, 'r') as file:
            for line in file:
                # 주석 및 빈 줄 무시
                if line.strip().startswith('#') or not line.strip():
                    continue

                # 설정 항목 파싱
                match = re.match(r'(\w+)\s*=\s*(\d+)', line)
                if match:
                    key, value = match.groups()
                    policy[key] = int(value)

        # 정책 검증 로직
        results = []
        if policy['minlen'] < 8:
            results.append("비밀번호 최소 길이가 너무 짧습니다. (현재 설정: {})".format(policy['minlen']))
        if policy['minclass'] < 3:
            results.append("비밀번호는 최소 3가지 종류의 문자를 포함해야 합니다. (현재 설정: {})".format(policy['minclass']))

        if not results:
            return "비밀번호 복잡성 설정이 정상적으로 설정되었습니다."
        else:
            return "\n".join(results)

    except FileNotFoundError:
        return f"파일을 찾을 수 없습니다: {file_path}"
    except Exception as e:
        return f"정책 파일을 읽는 중 오류가 발생했습니다: {str(e)}"


# 예시 테스트
result = check_password_policy()
print(result)
