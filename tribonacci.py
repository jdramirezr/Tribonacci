
lista=[12, 8, 19]

n=5

def tribonacci(signature, n):
    
  
    signature=signature[:n]
   

    for p in range(n-3):
      m=p+3 
      signature.append(sum(signature[p:m]))
    return  signature




def tribonaccis(signature, n):
  res = signature[:n]

  for i in range(n - 3):
     res.append(sum(res[-3:]))
  return res

