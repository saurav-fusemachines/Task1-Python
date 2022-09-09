def twice_as_old(dad_years_old, son_years_old):
    age_at_birth = dad_years_old - son_years_old
    twice_as_old = age_at_birth * 2
    return abs(dad_years_old - twice_as_old)

print(twice_as_old(36,7))
print(twice_as_old(55,30))
