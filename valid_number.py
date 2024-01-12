def valid_number(number):
  try:
    as_number = int(number)
  except:
    print("\nDigite um número válido\n")
    return 400
  else:
    return as_number
