import sys

def simple_interest(principal, interest, time):
    return (principal * interest * time) / 100

if __name__ == "__main__":
    p = input(sys.argv[1])
    i = input(sys.argv[2])
    t = input(sys.argv[3])

    print("Simple interest is:", simple_interest(p, i, t))
