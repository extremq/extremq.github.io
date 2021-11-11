from math import gcd

def phi(n):
    amount = 0        
    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1
    return amount

if __name__ == '__main__':
    print("This program computes a ^ b % c in two ways and checks if both ways of computing are equal.")
    
    a = int(input("a = "))
    c = int(input("c = "))
   
    b_start = int(input("b start = "))
    b_finish = int(input("b finish = "))
   
    correct = 0
    wrong = 0

    for b in range(b_start, b_finish):
        brute = a ** b % c
        #print(f"a ^ b % c = {brute}")

        optimized = a ** (b % phi(c)) % c
        #print(f"a ^ (b % phi(c)) % c = {optimized}")

        if brute == optimized:
            correct += 1
        else:
            wrong += 1
        
    print(f"Correct answers: {correct}")
    print(f"Wrong answers: {wrong}")