def frequency_analysis(msg):
    fa = {}
    for c in msg:
        if c in fa:
            fa[c] += 1
        else:
            fa[c] = 1

#    print(Sorted(fa.items(), key = lambda x: x[1], reverse = True))
    print(fa.items())

if __name__ == '__main__':
    msg = '53%%#.......'
    frequency_analysis(msg)
