# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20214 오승윤
# 프로젝트 주제: 사용자 중심 UI/UX 디자인 A/B 테스트 만족도 분석 및 마케팅 효율 검증기
# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# 우리 프로그램은 실행 후 사용자가 직접 입력하는 점수 데이터를 
# `test_data`라는 2차원 리스트에 누적하여 분석합니다.
# 처음에는 비어있는 리스트([])로 시작합니다.
#
# 현재 열의 의미 (2차원 리스트 구조):
# 0번 열: 가상 사용자 식별 번호 (User ID)
# 1번 열: 기존 디자인 (A안) 만족도 점수 (1~5점)
# 2번 열: 신규 디자인 (B안) 만족도 점수 (1~5점)
# ------------------------------------------------------------

test_data = []

# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 50)
    print("   UI/UX 디자인 A/B 테스트 분석 및 효율 검증기")
    print("   기존 디자인(A) vs 신규 디자인(B) 선호도 분석")
    print("=" * 50)


def input_scores(num_users):
    """사용자 수만큼 반복하여 A안, B안 점수를 입력받아 2차원 리스트를 만든다."""
    data_list = []
    print(f"\n--- 총 {num_users}명의 UI/UX 테스트 데이터를 입력받습니다 ---")
    
    for i in range(1, num_users + 1):
        print(f"\n[{i}번 가상 사용자 평가]")
        
        # input으로 받은 문자열을 숫자로 계산할 수 있게 int(정수형)로 변환
        a_score = int(input("기존 디자인(A안) 만족도 점수 (1~5점): "))
        b_score = int(input("신규 디자인(B안) 만족도 점수 (1~5점): "))
        
        # [사용자 식별 번호, A안 점수, B안 점수] 형태로 한 행을 만듦
        row = [i, a_score, b_score]
        
        # 만든 한 행(row)을 전체 표(data_list)에 추가(append)
        data_list.append(row)
        
    return data_list


def calculate_averages(data_list):
    """2차원 리스트를 반복문으로 돌며 A안과 B안의 총점 및 평균을 계산한다."""
    total_A = 0
    total_B = 0
    num_users = len(data_list)  # 총 참여 사용자 수

    # 반복문: 2차원 리스트의 모든 행(row)을 하나씩 꺼내며 점수 누적
    for row in data_list:
        # row[1]은 A안 점수, row[2]는 B안 점수
        total_A = total_A + row[1]
        total_B = total_B + row[2]

    # 평균 계산
    avg_A = total_A / num_users
    avg_B = total_B / num_users
    
    return avg_A, avg_B


def print_report(data_list, avg_A, avg_B):
    """전체 점수 현황 표와 최종 판정 결과를 출력한다."""
    print("\n" + "=" * 15 + " A/B TEST REPORT " + "=" * 15)
    print("사용자ID\tA안 점수\tB안 점수")
    print("-" * 45)
    
    # 반복문: 2차원 리스트에 누적된 내용을 표 형태로 출력
    for row in data_list:
        print(f"User {row[0]}\t{row[1]}점\t\t{row[2]}점")
    print("-" * 45)
    print(f"■ 최종 평균 만족도 -> A안: {avg_A:.2f}점 / B안: {avg_B:.2f}점")
    print("=" * 47)
    
    print( )
    # 조건문: 두 디자인의 평균 점수를 비교하여 최종 마케팅 가이드라인 판정
    if avg_B > avg_A:
        print("-> 결과: 신규 디자인(B안)의 만족도가 더 높습니다.")
        if (avg_B - avg_A) >= 1.0:
            print("💡 [추천] 신규 디자인 즉시 반영 및 전면 교체를 권장합니다!")
        else:
            print("💡 [추천] 신규 디자인 도입을 추천하나, 미세한 조정이 필요할 수 있습니다.")
    elif avg_A > avg_B:
        print("-> 결과: 기존 디자인(A안)의 만족도가 더 높거나 같습니다.")
        print("💡 [추천] 신규 디자인(B안) 도입을 보류하고, UI 수정을 재검토하세요.")
    else:
        print("-> 결과: 두 디자인의 만족도가 완벽히 동일합니다.")
        print("💡 [추천] 추가 데이터 수집 및 디자인 재테스트를 권장합니다.")


def main():
    show_intro()
    
    # 가상 사용자 수 입력 받기
    users_count = int(input("테스트에 참여할 사용자 수는 몇 명인가요?: "))
    
    # 1. 입력: 점수 입력받아 2차원 리스트 만들기
    my_data = input_scores(users_count)
    
    # 2. 처리: 평균 점수 계산하기
    average_A, average_B = calculate_averages(my_data)
    
    # 3. 출력: 최종 리포트 화면에 출력하기
    print_report(my_data, average_A, average_B)


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
main()