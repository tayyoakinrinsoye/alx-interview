#!/usr/bin/python3
'''The minimum operations challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.
    '''
    if not isinstance(n, int):
        return 0
    count = 0
    board = 0
    done = 1
    # print('H', end='')
    while done < n:
        if board == 0:
            # init (the first copy all and paste)
            board = done
            done += board
            count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif n - done > 0 and (n - done) % done == 0:
            # copy all and paste
            board = done
            done += board
            count += 2
            # print('-(11)->{}'.format('H' * done), end='')
        elif board > 0:
            # paste
            done += board
            count += 1
            # print('-(01)->{}'.format('H' * done), end='')
    # print('')
    return count
