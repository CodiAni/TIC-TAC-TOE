import os
global state
state=[[1,1,1],[1,1,1],[1,1,1]]
def win(chk):
  for i in chk:
    if i>6 and len(chk[:chk.index(i)+1])%2==0:
        state[2][i-7]="O"
    elif i>3 and len(chk[:chk.index(i)+1])%2==0:
        state[1][i-4]="O"
    elif i>6 and len(chk[:chk.index(i)+1])%2!=0:
        state[2][i-7]="X"
    elif i>3 and len(chk[:chk.index(i)+1])%2!=0:
        state[1][i-4]="X"
    elif i<=3 and len(chk[:chk.index(i)+1])%2==0:
        state[0][i-1]="O"
    elif i<=3 and len(chk[:chk.index(i)+1])%2!=0:
        state[0][i-1]="X"
  win_state = [
      [state[0][0], state[0][1], state[0][2]],
      [state[1][0], state[1][1], state[1][2]],
      [state[2][0], state[2][1], state[2][2]],
      [state[0][0], state[1][0], state[2][0]],
      [state[0][1], state[1][1], state[2][1]],
      [state[0][2], state[1][2], state[2][2]],
      [state[0][0], state[1][1], state[2][2]],
      [state[2][0], state[1][1], state[0][2]],
  ]
  if ["X", "X", "X"] in win_state:
    return 0
  elif ["O","O","O"] in win_state:
    return 1
  else:
    return 2
def tictac(chk=[10]):
  k = 1
  for i in range(3):
    for j in range(3):
      if chk == [10]:
        print("", k, end="")
        k += 1
      else:
        for l in chk:
          if k == l:
            if len(chk[:chk.index(k)+1])%2==0:
              print("","O", end="")
            else:
              print("","X", end="")
            k += 1
            break
        else:
          print("", k, end="")
          k += 1
      if j < 2:
        print(" |", end="")
    if i < 2:
      print("\n---|---|--")
chk = []
l=[1,2,3,4,5,6,7,8,9]
x=2
while x==2:
  os.system('cls' if os.name == 'nt' else 'clear')
  tictac(chk)
  box=int(input("\nWhich box do you want to enter:"))
  if box not in l:
    continue
  chk+=[box]
  l.remove(box)
  x=win(chk)
  if x==1:
    os.system('cls' if os.name == 'nt' else 'clear')
    tictac(chk)
    print("\nUser 2 won")
    break
  elif x==0:
    os.system('cls' if os.name == 'nt' else 'clear')
    tictac(chk)
    print("\nUser 1 won")
    break
  if len(chk)==9:
    break
if len(chk)==9 and x==2:
  os.system('cls' if os.name == 'nt' else 'clear')
  tictac(chk)
  print("\nmatch is a draw")
