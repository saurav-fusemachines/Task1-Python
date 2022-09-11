def get_decimal(n):
    n_parts = str(n).split('.')
    if len(n_parts) == 1:
        return 0
    return float('0.' + n_parts[1])


#  def zero_test_case():
    #     test.assert_approx_equals(get_decimal(10), 0)
        
    # @test.it("returns decimal part from -1.2 as 0.2")
    # def negative_test_case():
    #     test.assert_approx_equals(get_decimal(-1.2), 0.2)

    #BEST PRAACTICE
# def get_decimal(n): 
#     return abs(n) % 1