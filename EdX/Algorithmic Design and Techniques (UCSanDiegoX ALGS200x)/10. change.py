# Uses python3
import sys

def get_change(m):
    # Initialize the number of coins
    num_coins = 0
    
    # Use the largest denomination first
    num_coins += m // 10
    m %= 10
    
    # Use the next largest denomination
    num_coins += m // 5
    m %= 5
    
    # Use the smallest denomination
    num_coins += m // 1
    
    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
    

