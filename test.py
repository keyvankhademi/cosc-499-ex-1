from sort import sort_array

input = [2, 3, 1]
expected_output = [1, 2, 3]

output = sort_array(input)

print("expected output: {}".format(expected_output))
print("program output: {}".format(output))

if expected_output == output:
    print("Test successfully passed!")

input2 = ['b', 'c', 'a']
expected_output2 = ['a', 'b', 'c']

output2 = sort_array(input2)

if expected_output2 == output2:
    print("Test 2 successfully passed!")
