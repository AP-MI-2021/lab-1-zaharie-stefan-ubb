'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  if n > 1:
      for i in range(2, int(n / 2) + 1):
          if (n % i) == 0:
              return False
  else:
    return False
  return True

  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  ans = 1
  for i in lst:
      ans *= i
  return ans
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  # codul vostru aici
  pass
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  # codul vostru aici
  pass

def main():
  # interfata de tip consola aici
  print("""
Menu:
1. Verify if a number is prime
2. Get product of a list of numbers
3. Get GCD v1
4. Get GCD v2
  """)
  option = int(input("Enter an option: "))

  if option == 1:
      num = int(input("Enter a number: "))
      if is_prime(num):
          print("The number is prime!")
      else:
          print("The number is not prime!")

  elif option == 2:
      str_list = input("Enter the numbers separated by spaces: ")
      map_obj = map(int, str_list.split())
      lst = list(map_obj)
      print(get_product(lst))

  elif option == 3 or option == 4:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      if option == 3:
          print(get_cmmd_v1(num1, num2))
      else:
          print(get_cmmd_v2(num1, num2))
  else:
      print("Incorrect option!")



if __name__ == '__main__':
  main()
