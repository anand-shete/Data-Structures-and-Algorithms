try:
    num = int(input("Enter a number:"))
    result = 10/num
except Exception as e:
    print('error:', e)
finally:
    print('print regardless')
print()


# raise...from is used for exception chain
try:
    if num < 0:
        raise ValueError("wrong value")
except Exception as e:
    raise Exception('throw exception:',e) from None

# TODO - what is python GIL?