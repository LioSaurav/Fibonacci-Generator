import time

# Function to generate Fibonacci sequence using iteration
def fiboIter(n):
    fib_sequence = []
    prevNum = 0 
    currentNum = 1
    for i in range(n):
        fib_sequence.append(prevNum)
        prevNum, currentNum = currentNum, prevNum + currentNum
    return fib_sequence

# Function to generate Fibonacci sequence 
def fiborecur(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        fib_sequence = fiborecur(n-1)
        fib_sequence.append(fib_sequence[-1] + (fib_sequence[-2] if len(fib_sequence) > 1 else 1))
        return fib_sequence

if __name__ == "__main__":
    num = int(input("Enter the number of terms: "))
    
    start_time = time.time()
    print(f"Using iteration, Fibonacci sequence of {num} terms: {fiboIter(num)}")
    print(f"Time taken (iteration): {time.time() - start_time} seconds) ")
    start_time = time.time()
    print(f"Using recursion, Fibonacci sequence of {num} terms: {fiborecur(num)}")
    print(f"Time taken (recursion): {time.time() - start_time} seconds")
    print("you done your task")