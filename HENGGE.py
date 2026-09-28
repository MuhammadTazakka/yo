def main():
  N = int(input())
  for i in range(N):
    total = 0
    X = int(input())
    Yn = input().trim()
    Yn = Yn.split(' ')
    for j in Yn:
      if int(j) < 0:
        total += int(j)**4
    print(total)
        
      
if __name__ == "__main__":
  main()
