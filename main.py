import sys
import logo
import os

class megador:
	def __init__(self):
		self.iniciar_sistema = True
	def datebaser(self, cmd):
		if 'clear' in cmd:
			os.system('clear')
		elif 'exit' in cmd:
			os.system('clear')
			sys.exit(1)
		elif 'start server' in cmd:
			logo.value = 'Server'
		else:
			print(f'Comando {cmd} não encontrado.')
		
	def Carregar_Logo(self):
		print(logo.logo01)
		
	def Principal(self):
		#self.Carregar_Logo()
		while self.iniciar_sistema:
			comandos = logo.Entrada()
			self.datebaser(comandos)
	
	def atualizar(self):
			self.Principal()
			
			
if __name__=='__main__':
		mg = megador()
		mg.atualizar()
		