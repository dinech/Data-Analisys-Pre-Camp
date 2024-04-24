for i in [1, 2, 3, 4]:
    print(i)
for i in [1, 2, 3, 4]:
    print(i*20)
l3 = [i[0] for i in ['Ele', 'Tim', 'Matt']]
l4 = [i for i in [1, 2, 3, 4, 5, 6] if i%2 == 0]
l5 = [i for i in [1, 2, 3, 4] if i in [3, 4, 5, 6]]
l6 = [i[::-1].lower() for i in ['Ele', 'Tim', 'Matt']]
l7 = [i for i in 'first' if i in 'third']
l8 = [i for i in range(1, 100) if i%12 == 0]
l9 = [i for i in 'amazing' if not i in 'euoaiy']
l10 = [[j for j in range(3)] for i in range(3)]
l11 = [[j for j in range(10)] for i in range(10)]
