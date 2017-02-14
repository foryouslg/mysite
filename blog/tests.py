def two_dimension(h=0,w=0):
    while h > 0:                    #因为电脑是一行一行输出的，所以需要把列循环行放在外层循环中，即把第一行中的每一列先循环完，再第二行
        for j in range(w):
            print('%10s+' % str(h),end='')
        print()
        h -= 1
    print("-" * 10 * (w + 1))

    for i in range(w):
        print("%10s" % i,end='')



if __name__ == '__main__':
    h = 5
    w = 3
    two_dimension(h,w)