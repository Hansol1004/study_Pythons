from typing import List, Union, Dict, Any

def perform_list_operations(list_a: List[Union[int, float]], list_b: List[Union[int, float]]) -> Dict[str, List[Any]]:
    """
    두 개의 숫자 리스트에 대해 요소별 사칙연산(+, -, *, /)을 수행하고 결과를 딕셔너리로 반환합니다.
    나눗셈 시 0으로 나누는 경우는 'division_error' 문자열로 처리됩니다.
    
    Args:
        list_a (List[Union[int, float]]): 첫 번째 숫자 리스트 (피연산자 A).
        list_b (List[Union[int, float]]): 두 번째 숫자 리스트 (피연산자 B).
        
    Returns:
        Dict[str, List[Any]]: 각 연산별 결과를 담은 리스트를 포함하는 딕셔너리.
    """
    
    # 성능과 가독성을 위해 zip()과 리스트 컴프리헨션을 사용합니다.
    
    # 덧셈 (Addition)
    addition_results = [a + b for a, b in zip(list_a, list_b)]
    
    # 뺄셈 (Subtraction)
    subtraction_results = [a - b for a, b in zip(list_a, list_b)]
    
    # 곱셈 (Multiplication)
    multiplication_results = [a * b for a, b in zip(list_a, list_b)]
    
    # 나눗셈 (Division) - 0으로 나누는 경우 'division_error' 처리 제약 조건 준수
    division_results = [
        a / b if b != 0 else 'division_error'
        for a, b in zip(list_a, list_b)
    ]
    
    return {
        "addition_results": addition_results,
        "subtraction_results": subtraction_results,
        "multiplication_results": multiplication_results,
        "division_results": division_results
    }

# --- 테스트 스크립트 ---

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 함수 실행: 모든 결과를 한 번에 계산
# 이 방식이 각 연산을 한 번의 루프로 처리하는 것보다 효율적입니다.
all_results = perform_list_operations(test_a, test_b)

# 테스트 실행: 개별 항목별로 입력값과 결과를 출력
print("--- 리스트 사칙연산 테스트 결과 ---")
print("입력 (a, b) => {add: 덧셈, sub: 뺄셈, mul: 곱셈, div: 나눗셈}")

for i in range(len(test_a)):
    a = test_a[i]
    b = test_b[i]
    
    # 개별 연산 결과를 추출
    results_for_pair = {
        'add': all_results['addition_results'][i],
        'sub': all_results['subtraction_results'][i],
        'mul': all_results['multiplication_results'][i],
        # 나눗셈 결과는 'division_error' 처리를 확인할 수 있습니다.
        'div': all_results['division_results'][i]
    }
    
    # 요청된 형식에 따라 출력
    print(f"{a}, {b} => {results_for_pair}")

# 0으로 나누는 경우 ('7, 0' 쌍) 결과 확인:
# 7, 0 => {'add': 7, 'sub': 7, 'mul': 0, 'div': 'division_error'}