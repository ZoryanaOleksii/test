def Foo(read_a, read_b, read_c, a_or_b, a_or_c, b_or_c, abc, pupils):

    read_a_and_b = read_a + read_b - a_or_b
    print(read_a_and_b)
    read_a_and_c = read_a + read_c - a_or_c
    print(read_a_and_c)
    read_b_and_c = read_b + read_c - b_or_c
    print(read_b_and_c)
    read_at_least_one = read_a + read_b + read_c - read_a_and_b - read_b_and_c - read_a_and_c + abc
    print(read_at_least_one)
    read_no_one = pupils - read_at_least_one

    print(read_no_one)
Foo(25, 22, 22, 33, 32, 31, 10, 40)
