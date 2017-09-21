def factors(n):
    result = []

    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)

    return result


z = 10 

print factors(z)
print factors(z+1)
print factors(z+2)