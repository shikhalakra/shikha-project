
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
       
def main():
 nterms = input()
 for i in range(nterms):
    print(fibo(i)),

main()