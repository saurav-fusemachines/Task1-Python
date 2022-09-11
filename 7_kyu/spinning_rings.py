def spinning_rings(inner_max, outer_max):
    inner_count = 0
    outer_count = 0
    increments = 0
    while True:
        inner_count -= 1
        outer_count += 1
        increments += 1
        inner_count = inner_count if inner_count >= 0 else inner_max
        outer_count = outer_count if outer_count <= outer_max else 0
        if inner_count == outer_count:
            return increments

# test.assert_equals(spinning_rings(2, 3), 5)
# test.assert_equals(spinning_rings(3, 2), 2)
# test.assert_equals(spinning_rings(1, 1), 1)
# test.assert_equals(spinning_rings(2, 2), 3)
# test.assert_equals(spinning_rings(3, 3), 2)