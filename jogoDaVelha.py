import os
import platform

class JogoVelha:
	def __init__(self):
		self.jogadas = 0
		self.jogadorDaVez = 2
		self.maxJogadas = 9
		self.vitoria = False
		self.velha = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]
    
	def tela(self):

		if(platform.system() == "Windows"):
			os.system("cls")
		else:
			os.system("clear")
		
		print("    0   1   2")
		print("0:  " + self.velha[0][0] + " | " + self.velha[0][1] + " | " + self.velha[0][2])
		print("   -----------")
		print("1:  " + self.velha[1][0] + " | " + self.velha[1][1] + " | " + self.velha[1][2])
		print("   -----------")
		print("2:  " + self.velha[2][0] + " | " + self.velha[2][1] + " | " + self.velha[2][2])
		print("\nJogadas: " + "\033[1;32m" + str(self.jogadas) + "\033[0;0m")
        
		return ""
    
	def vezJogador(self):
		if(self.jogadorDaVez == 2 and self.jogadas < self.maxJogadas):
			try:
				print("\n\033[1;32m" + "JOGADOR 1 (X)\n" + "\033[0;0m")
				linha = int(input("Linha: "))
				coluna = int(input("Coluna: "))
				while(self.velha[linha][coluna] != " "):
					tela()
					linha = int(input("Linha: "))
					coluna = int(input("Coluna: "))
            
				self.velha[linha][coluna] = "X"
				self.jogadorDaVez = 1
				self.jogadas+= 1
			except:
				print("linha e/ou coluna inválida!")
		return " "
    
	def vezJogador2(self):
		if(self.jogadorDaVez == 1 and self.jogadas < self.maxJogadas):
			try:
				print("\n\033[1;32m" + "JOGADOR 2 (O)\n" + "\033[0;0m")
				linha = int(input("Linha: "))
				coluna = int(input("Coluna: "))
				while(self.velha[linha][coluna] != " "):
					tela()
					linha = int(input("Linha: "))
					coluna = int(input("Coluna: "))
            
				self.velha[linha][coluna] = "O"
				self.jogadorDaVez = 2
				self.jogadas+= 1
			except:
				print("linha e/ou coluna inválida!")
		return " "
    
	def verificarVitoria(self):
   		simbolos = ['O', 'X']
   		
   		#VERIFICAR COLUNAS
   		for s in simbolos:
   			self.vitoria = False
   			il=ic=0
   			while ic < 3:
   				soma = 0
   				il = 0
   				while il < 3:
   					if (self.velha[il][ic] == s):
   						soma+=1
   					il+=1
   				
   				if (soma == 3):
   					self.vitoria = s
   					break
   				ic+=1
   			if (self.vitoria != False):
   				break
   		#VERIFICAR LINHAS
   			il=ic=0
   			while il < 3:
   				soma = 0
   				ic = 0
   				while ic < 3:
   					if (self.velha[il][ic] == s):
   						soma+=1
   					ic+=1
   				
   				if (soma == 3):
   					self.vitoria = s
   					break
   				il+=1
   			if (self.vitoria != False):
   				break
   		#VERIFICAR DIAGONAL1
   			soma = 0
   			idiag = 0
   			while (idiag < 3):
   				if (self.velha[idiag][idiag] == s):
   					soma+=1
   				idiag+=1
   				if (soma == 3):
   					self.vitoria = s
   					break
   			if (self.vitoria != False):
   				break
   		#VERIFICAR DIAGONAL2
   			soma = 0
   			idiagl = 0
   			idiagc = 2
   			while (idiagc >= 0):
   				if (self.velha[idiagl][idiagc] == s):
   					soma+=1
   				idiagl+=1
   				idiagc-=1
   				if (soma == 3):
   					self.vitoria = s
   					break
   			if (self.vitoria != False):
   				break

   		return self.vitoria
	
	def redefinir(self):
		self.jogarNovamente = 's'
		self.jogadas = 0
		self.jogadorDaVez = 2
		self.maxJogadas = 9
		self.vitoria = False
		self.velha = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]


jogo = JogoVelha()
jogarNovamente = 's'

while(jogarNovamente == 's'):
	while(True):
		jogo.tela()
		jogo.vezJogador()
		jogo.tela()

		vitoria = jogo.verificarVitoria()
    
		if (vitoria != False or jogo.jogadas >= jogo.maxJogadas):
			jogo.tela()
			break

		jogo.vezJogador2()

		vitoria = jogo.verificarVitoria()

		if (vitoria != False or jogo.jogadas >= jogo.maxJogadas):
			jogo.tela()
			break

	if vitoria == False:
		vitoria = "\n\033[1;32m" + "Velha!"
	elif vitoria == "X":
		vitoria = "\n\033[1;32m" + "Jogador 1 (X) venceu!"
	elif vitoria == "O":
		vitoria = "\n\033[1;32m" + "Jogador 2 (O) venceu!"
    	
		

	print(vitoria)
	jogarNovamente = input("\nJogar novamente? \ns - para jogar novamente\nou qualquer coisa para sair: " + "\033[0;0m")
	jogo.redefinir()