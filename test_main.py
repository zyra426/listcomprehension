from complete_main import create_hall_of_fame

run_cases = [
    ([
        (1, 1, True, False),
        (1, 2, True, True),
        (1, 3, True, False),
    ], ["Kelsier"])
]

submit_cases = run_cases + [
    ([
        (1, 1, True, False),
        (1, 2, True, True),
        (1, 3, True, False),
        (1, 4, True, True),
        (1, 5, True, False),
        (1, 6, True, True),
        (1, 7, True, True),
        (1, 8, True, True),
    ], ["Kelsier", "Sazed", "Dockson", "Breeze", "Lestibournes"]),
]


def test(input1, expected_output):
    print("---------------------------------")
    print(f"Input: {input1}")
    result = create_hall_of_fame(input1)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
