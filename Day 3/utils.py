def test_odd_pos_sum(function):
    test_cases=[([0,1,2,3,4,5],9),
                ([0,-1,2,-3,4,5],1),
                ([10,23,11,-21,23,45,67,-2,6],45),
                ([4,5,3,8,9,10,2],23),
                ([-3,-12,-4,-22,-67,-21,-11],-55),
        ]
    pass_test_case=0
    fail_test_case=0
    for lst,s in test_cases:
        if function(lst)==s:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_odd_sum(function):
    test_cases=[([0,1,2,3,4,5],9),
                ([0,-1,2,-3,4,5],1),
                ([10,23,11,-21,23,45,67,-2,6],148),
                ([4,5,3,8,9,10,2],17),
                ([-3,-12,-4,-22,-67,-21,-11],-102),
        ]
    pass_test_case=0
    fail_test_case=0
    for lst,s in test_cases:
        if function(lst)==s:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_product_search(function):
    test_cases=[(({'computer':20000,'laptop':50000,'Mouse':500,'Keyboard':300,'speaker':3000,'headphone':1500},'Mouse',500)),
                ({'Keyboard':300,'speaker':3000,'headphone':1500},'headphone',1500),
                ({'Apple':300,'Banana':80,'Orange':150,'WaterMelon':100},'WaterMelon',100),
                ]
    pass_test_case=0
    fail_test_case=0
    for d,item,price in test_cases:
        if function(d,item)==price:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==3:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")

def test_character_frequency(function):
    test_cases=[('Neelesh',{'N': 1, 'e': 3, 'l': 1, 's': 1, 'h': 1}),
                ('Siliguri',{'S': 1, 'i': 3, 'l': 1, 'g': 1, 'u': 1, 'r': 1}),
                ('institute',{'i': 2, 'n': 1, 's': 1, 't': 3, 'u': 1, 'e': 1}),
                ('technology',{'t': 1, 'e': 1, 'c': 1, 'h': 1, 'n': 1, 'o': 2, 'l': 1, 'g': 1, 'y': 1}),
                ('frequencycounter',{'f': 1, 'r': 2, 'e': 3, 'q': 1, 'u': 2, 'n': 2, 'c': 2, 'y': 1, 'o': 1, 't': 1})
                
                ]
    pass_test_case=0
    fail_test_case=0
    for word,d in test_cases:
        if function(word)==d:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==5:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")


def test_oneD2twoD(function):
    test_cases=[([1,2,3,4,5,6,7,8], 3,[[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7], [6, 7, 8]]),
                ([1,2,3,4,5,6,7,8,9,10], 2, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]]),
                ([1,2,3,4,5,6,7,8], 4, [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]),
                ([1,2,3,4,5,6,7,8], 1, [[1], [2], [3], [4], [5], [6], [7], [8]])
                ]
    pass_test_case=0
    fail_test_case=0
    for oned,l,twod in test_cases:
        if function(oned,l)==twod:
            pass_test_case+=1
        else:
            fail_test_case+=1
    if pass_test_case==4:
        print("All test cases passed")
    else:
        print(f"{pass_test_case} test cases passed")
        print(f"{fail_test_case} test cases failed")



def filteringSignal(sig,fltr):
    """
This function will apply the filter fltr from left to right by
multiplying the corresponding values and then adding
"""
    lengthS=len(sig)
    lengthF=len(fltr)
    filteredS=list()
    for i in range(lengthS-lengthF+1):
        fltrd=0
        for ind in range(lengthF):
            fltrd+=sig[i+ind]*fltr[ind]
        filteredS.append(fltrd)
        print(filteredS)
