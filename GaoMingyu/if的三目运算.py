def main():
   a="apple"
   b="apple"
   c="banana"
   print(a if a==b else b)
   print(c if a!=c else a)
   a=10
   b=20
   print(a if a>b else b)
   print(b if a>b else a)


if __name__ =='__main__':
    main()