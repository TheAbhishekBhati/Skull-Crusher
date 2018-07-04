try:
    a=95989
    b=5+5

    c = 5/0
    f = open("abc.txt")

    for line in  f:
        print(line)
#except Exception as e:
 #   print(dir(e))

except FileNotFoundError as e:
   print(e.filename)
except Exception as e:
    print(e)
except ZeroDivisionError as e:
    print(e)