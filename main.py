'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  # codul vostru aici
  pass
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  # codul vostru aici
  pass
  
  
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

# Return an int list generated from a string
def str_to_list(str_lst):
  map_obj = (int, str_list.split())
  
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
      print(is_prime(num))

  if option == 2:
      str_list = input("Enter the numbers separated by spaces")
      print(get_product(str_to_list(str_list)))

  if option == 3 or option == 4:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      if option == 3:
          print(get_cmmd_v1(num1, num2))
      else:
          print(get_cmmd_v2(num1, num2))



if __name__ == '__main__':
  main()
