s = input()

mix = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for comp in mix:
    s = s.replace(comp,'*')

print(len(s))

