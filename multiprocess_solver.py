from multiprocessing import Pool

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret

#======================== BOF  =============================#

def solver(data_container):
    pass # return result as string


class DataContainer:
    def __init__(self):
        pass # read data

#======================== EOF  =============================#

if __name__ == '__main__':
    NUM_THREAD = 2
    pool = Pool(NUM_THREAD)
    T = input()
    input_queue = [DataContainer() for _ in xrange(T)]
    result = pool.map(solver, input_queue)

    for i in range(0, T):
        print 'Case #%d: %s' % (i+1, result[i])
