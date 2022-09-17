from sort import sort_array

input = [2, 3, 1]
expected_output = [1, 2, 3]

output = sort_array(input)

print("expected output: {}".format(expected_output))
print("program output: {}".format(output))

if expected_output == output:
    print("Test successfully passed!")
