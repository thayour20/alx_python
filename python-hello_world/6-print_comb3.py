for i in range(10):
    for j in range(i+1, 10):
        print("{:02}".format(i * 10 + j), end="\n" if i == 8 and j == 9 else ", ")