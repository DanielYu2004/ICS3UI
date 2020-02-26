from time import time

mem = {
    1 : 1,
    2 : 1
    }

fibos = []
counter = 0
def fibo(n):
    global counter
    counter +=1
    if n in mem:
        return(mem[n])
    else:
        mem[n] = fibo(n-1) + fibo(n-2)
        return(mem[n])
start = time()
print(fibo(30))
end = time() - start
print(end)
print(counter)

counter = 0
def fiboBad(n):
    global counter
    counter +=1
    if n == 1 or n == 2:
        return(1)
    else:
        
        return(fiboBad(n-1) + fiboBad(n-2))

start = time()

print(fiboBad(30))

end = time() - start
print(end)
print(counter)