import random
def numberguess():
	l=True
	while(l):
		print("Guess the number")
		beg=int(input("Enter lower limit:"))
		end=int(input("Enter upper limit:"))
		print("You have 5 guesses")
		p=random.randint(beg,end)
		c=0
		loop=True
		while(loop):
			k=int(input("Guess the number:"))
			c+=1
			if c==5:
				if(k==p):
					print("Correct guess")
				else:
					print("Wrong answer")
					print("The number is:",p)
				break
			if(k<p):
				print("Try a larger number")
			elif(k>p):
				print("Try a smaller number")
			else:
				print("Correct guess")
				break
			print("You have ",5-c," more guesses")
			if(k!=p and c<5):
				loop=True
			else:
				loop=False
		a=input("Do you want to play again?(Y/N):")
		if a=='Y' or a=='y':
			print("\n")
			l=True
		else:
			l=False

def rockpaperscissors():
	l=True
	while(l):
		print("Rock Paper Scissors")
		print("Rules of the game:")
		print("1.Rock beats scissors")
		print("2.Paper beats rock")
		print("3.Scissors beats paper")
		print("\n")
		d={1:'Rock',2:'Paper',3:'Scissors'}
		k=int(input("Enter 1(Rock), 2(Paper) or 3(Scissors):"))
		p=random.randint(1,3)
		if (k==1 and p==3) or (k==2 and p==1) or (k==3 and p==2):
			print("You:",d[k])
			print("CPU:",d[p])
			print("You won!")
		else:
			print("You:",d[k])
			print("CPU:",d[p])
			print("Try again")
		a=input("Do you want to play again?(Y/N):")
		if a=='Y' or a=='y':
			print("\n")
			l=True
		else:
			l=False	

def hangman():
	l=True
	while(l):
		print("Hangman")
		inp=open("./names.txt","r")
		data=[]
		for line in inp:
			data.append(line.split())
		ans=data[random.randint(0,len(data))]
		word=list(ans[0])
		print("Number of characters:",len(word))
		print("You have 5 guesses")
		lst=[]
		for i in range(len(word)):
			lst.append('_')
		c=0
		while(c<5):
			k=input("Guess the character:")
			flag=0
			for i in range(len(word)):
				if word[i]==k:
					lst.pop(i)
					lst.insert(i,k)
					flag=1
			if flag==0:
				c+=1
				print("Wrong guess")
				print("You have ",5-c," more guesses")
				if c==5:
					print("Sorry! Try again")
					print("The word is:",ans[0])
			else:
				print("Correct guess")
				if lst==word:
					print("Congratulations! You have guessed the word correctly")
					c=5
				else:
					print("You have ",5-c," more tries")
			print(lst)
		a=input("Do you want to play again?(Y/N):")
		if a=='Y' or a=='y':
			print("\n")
			l=True
		else:
			l=False

def horizontal(mat,num):
	for i in range(len(mat)):
		c=0
		for j in range(len(mat)):
			if mat[i][j]==num:
				c+=1
		if c==3:
			return 1	
	return 0

def vertical(mat,num):
	for i in range(len(mat)):
		c=0
		for j in range(len(mat)):
			if mat[j][i]==num:
				c+=1
		if c==3:
			return 1	
	return 0

def diagonal(mat,num):
	c=0
	d=0
	for i in range(len(mat)):
		if mat[i][i]==num:
			c+=1
	if c==3:
		return 1
	for i in range(len(mat)):
		for j in range(len(mat)):
			if i+j==2:
				if mat[i][j]==num:
					d+=1
	if d==3:
		return 1	
	return 0

def result(mat,num):
	if horizontal(mat,num)==1 or vertical(mat,num)==1 or diagonal(mat,num)==1:
		return 1
	else:
		return 0

def tictactoe():
	l=True
	while(l):
		print("Tic-Tac-Toe")
		c=0
		mat=[[0,0,0],[0,0,0],[0,0,0]]
		loop=True
		while(loop):
			flag=0
			print("Player",(c%2)+1)
			row=int(input("Enter row:"))
			col=int(input("Enter column:"))
			if mat[row-1][col-1]==0:
				mat[row-1][col-1]=(c%2)+1
			else:
				flag=1
			if flag==1:
				continue
			if result(mat,(c%2)+1)==1:
				print("Player",(c%2)+1,"won")
				loop=False
			else:
				c+=1
				if c==9:
					print("It's a tie")	
					loop=False
				else:
					loop=True
			for i in mat:
				print(i)
		a=input("Do you want to play again?(Y/N):")
		if a=='Y' or a=='y':
			print("\n")
			l=True
		else:
			l=False
		

def main():
	loop=True
	while(loop):
		print("Games:")
		print("1.Guess the number")
		print("2.Rock Paper Scissors")
		print("3.Hangman")
		print("4.Tic-Tac-Toe")
		i=int(input("Enter your choice:"))
		print("\n")
		if i==1:
			numberguess()
		elif i==2:
			rockpaperscissors()
		elif i==3:
			hangman()
		else:
			tictactoe()
		a=input("Do you want to play a different game?(Y/N):")
		if a=='Y' or a=='y':
			print("\n")
			loop=True
		else:
			loop=False

main() 	