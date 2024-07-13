# Two famous competing companies ChemForces and TopChemist decided to show their sets of recently discovered chemical elements on an exhibition. However they know that no element should be present in the sets of both companies.

# In order to avoid this representatives of both companies decided to make an agreement on the sets the companies should present. The sets should be chosen in the way that maximizes the total income of the companies.

# All elements are enumerated with integers. The ChemForces company has discovered n
#  distinct chemical elements with indices a1,a2,…,an
# , and will get an income of xi
#  Berland rubles if the i
# -th element from this list is in the set of this company.

# The TopChemist company discovered m
#  distinct chemical elements with indices b1,b2,…,bm
# , and it will get an income of yj
#  Berland rubles for including the j
# -th element from this list to its set.

# In other words, the first company can present any subset of elements from {a1,a2,…,an}
#  (possibly empty subset), the second company can present any subset of elements from {b1,b2,…,bm}
#  (possibly empty subset). There shouldn't be equal elements in the subsets.

# Help the representatives select the sets in such a way that no element is presented in both sets and the total income is the maximum possible.

# Input
# The first line contains a single integer n
#  (1≤n≤105
# )  — the number of elements discovered by ChemForces.

# The i
# -th of the next n
#  lines contains two integers ai
#  and xi
#  (1≤ai≤109
# , 1≤xi≤109
# )  — the index of the i
# -th element and the income of its usage on the exhibition. It is guaranteed that all ai
#  are distinct.

# The next line contains a single integer m
#  (1≤m≤105
# )  — the number of chemicals invented by TopChemist.

# The j
# -th of the next m
#  lines contains two integers bj
#  and yj
# , (1≤bj≤109
# , 1≤yj≤109
# )  — the index of the j
# -th element and the income of its usage on the exhibition. It is guaranteed that all bj
#  are distinct.

# Output
# Print the maximum total income you can obtain by choosing the sets for both companies in such a way that no element is presented in both sets.






def maximize_income(n, chem_elements, m, top_elements):
    chem_dict = {}
    top_dict = {}
    
    for elem, income in chem_elements:
        chem_dict[elem] = income
        
    for elem, income in top_elements:
        top_dict[elem] = income

    unique_elements = set(chem_dict.keys()).union(set(top_dict.keys()))
    total_income = 0
    
    for elem in unique_elements:
        chem_income = chem_dict.get(elem, 0)
        top_income = top_dict.get(elem, 0)
        total_income += max(chem_income, top_income)
    
    return total_income

n = int(input())
chem_elements = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
top_elements = [tuple(map(int, input().split())) for _ in range(m)]

print(maximize_income(n, chem_elements, m, top_elements))
