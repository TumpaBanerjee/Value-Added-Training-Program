def test_insurance_provider(function):
    test_cases=[(1,'M',40,1),
                (0,'M',30,0),
                (0,'F',30,1),
                (5,'F',30,-1),
                (1,1,30,1)
        ]
    pass_test_case=0
    fail_test_case=0
    for mar,sex,age,eligible in test_cases:
        if function(mar,sex,age)==eligible:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")



def test_scholarship_amount_function(function):
    test_cases=[(90,102000,'C',200000.0),
                (60,102000,'C',100000.0),
                (60,400000,'C',0),
                (60,200000,'C',100000.0),
                (80,200000,'G',50000.0),
                (80,200000,'T',100000.0),
                (80,200000,'G',50000.0)
        ]
    pass_test_case=0
    fail_test_case=0
    for marks,income,cast,payable in test_cases:
        if function(marks,income,cast)==payable:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==7:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")


