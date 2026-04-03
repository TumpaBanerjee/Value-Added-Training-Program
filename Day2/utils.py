def test_check_prime():
    test_cases=[(24,1),
                (151,0),
                (897765,1),
                (89,0),
                (173,0),
        ]
    pass_test_case=0
    fail_test_case=0
    for num,flag in test_cases:
        if check_prime(num)==flag:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_sum_of_digits():
    test_cases=[(100,1),(135,9),(3453,15),(89575,34),(321456,21)]
    pass_test_case=0
    fail_test_case=0
    for num,sum1 in test_cases:
        if sum_of_digits(num)==sum1:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_all_prime_sum():
    test_cases=[(10,15),
                (20,75),
                (100,1058),
                (60,438),
                (55,379),
        ]
    pass_test_case=0
    fail_test_case=0
    for num,sum1 in test_cases:
        if all_prime_sum(num)==sum1:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_calculate_factorial():
    test_cases=[(5,120),(4,24),(10,3628800),(7,5040),(13,6227020800)]
    pass_test_case=0
    fail_test_case=0
    for num,fact1 in test_cases:
        if calculate_factorial(num)==fact1:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")








