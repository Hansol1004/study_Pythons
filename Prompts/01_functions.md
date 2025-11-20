## 문제

### 제작 프롬프트
```
당신은 30년 경력의 온라인 멘토링 전문가, Microsoft/VS Code Python 확장 개발자, Real Python/Talk Python To Me 등 기술 강좌 제작자, Pylance/Jupyter 등 주요 확장 프로그램 개발 기여자입니다.

아래의 상황을 해결하는 함수의 프롬프트를 제작하고, python 코드를 제작하려고함.

- 이 함수를 만들 때 제시하는 프롬프트를 반드시 json형식으로 출력

-프롬프트를 바탕으로, 실행되는 python 코드 제작

- 형식은 아래에 제시함.

[상황]

두 개의 숫자 리스트를 이용해 사칙연산(+, -, , /)을 수행하는 함수를 prompts/01_functions.*구현하시오.*
조건
테스트 데이터는 리스트(list) 로만 제공


테스트 데이터 개수는 10개


변수명은 소문자 + _ 조합


함수는 두 숫자를 입력받아 덧셈, 뺄셈, 곱셈, 나눗셈 결과를 모두 반환


0으로 나누는 경우는 "division_error" 반환



[형식]

# 테스트 리스트 (10개)
test_a = [10, 25, 40, 12, 7, 9, 16, 100, 3, 81]
test_b = [5, 5, 8, 3, 0, 3, 2, 4, 9, 9]

# 테스트 실행
for i in range(10):
    a = test_a[i]
    b = test_b[i]
    result = …
    print(f"{a}, {b} => {result}")

```

### json코드
```
{
    "function_name": "perform_list_operations",
    "description": "두 개의 숫자 리스트(list_a, list_b)를 입력받아 각 요소 쌍(list_a[i], list_b[i])에 대해 덧셈, 뺄셈, 곱셈, 나눗셈의 사칙연산을 수행하고 결과를 딕셔너리로 반환합니다. 이 함수는 사칙연산 수행 후, 결과를 개별 항목별로 출력하는 테스트 스크립트에서 활용됩니다.",
    "parameters": {
        "list_a": {
            "type": "List[Union[int, float]]",
            "description": "첫 번째 숫자 리스트 (피연산자 A)"
        },
        "list_b": {
            "type": "List[Union[int, float]]",
            "description": "두 번째 숫자 리스트 (피연산자 B)"
        }
    },
    "return_type": "Dict[str, List[Any]]",
    "output_structure": {
        "addition_results": "list_a[i] + list_b[i]의 결과 리스트",
        "subtraction_results": "list_a[i] - list_b[i]의 결과 리스트",
        "multiplication_results": "list_a[i] * list_b[i]의 결과 리스트",
        "division_results": "list_a[i] / list_b[i]의 결과 리스트 (list_b[i]가 0일 경우 'division_error' 문자열)"
    },
    "constraints": {
        "list_length": "list_a와 list_b의 길이는 동일해야 하며, 길이가 다를 경우 zip() 함수에 의해 짧은 리스트의 길이에 맞춰 연산이 수행됩니다.",
        "error_handling": "나눗셈 수행 시 list_b의 요소가 0일 경우, 파이썬 오류 대신 'division_error' 문자열을 반환하여 안전하게 처리해야 합니다."
    },
    "implementation_note": "성능과 가독성을 높이기 위해 Python의 내장 함수 zip()과 리스트 컴프리헨션을 사용하여 구현해야 합니다."
}
```