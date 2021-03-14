'''
1) find the union from 3 sets
2) find the difference from 3 sets
'''

set1={'vaibhavi','Kirti','Seema','Jimi'}
set2={'vaibhavi','Kirti','Seema'}
set3={'Kirti','Seema','Jimi'}
print(f'union name set is {set1.union(set2.union(set3))}')
print(set2.difference(set1.difference(set3)))
print(f'difference name set is {set1.difference(set2.difference(set3))}')

set1={1,2,2,3,4,5,6,7,8,9,10}
set2={11,12,13,14,15}
set3={16,17,18,19,20}
print(F'union numeric set is {set3.union(set2.union(set1))}')
print(f'difference of 2 numeric set s1, s2 is : {set1.difference(set2)}')
print(f'difference of 2 numeric set s2, s3 is : {set2.difference(set3)}')
print(f'difference of 2 numeric set s3, s1 is : {set3.difference(set1)}')
print(f'difference numeric set is {set1.difference(set2.difference(set3))}')

