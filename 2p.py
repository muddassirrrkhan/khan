# Fibonacci series using a loop

def fibonacci_series(n):
    a, b = 0, 1
    series = []

    for _ in range(n):
        series.append(a)
        a, b = b, a + b

    return series

# Example usage
terms = int(input("Enter the number of terms: "))
print("Fibonacci series:")
print(fibonacci_series(terms))
