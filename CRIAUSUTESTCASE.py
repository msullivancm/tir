from tir import Webapp
import unittest

class CRIAUSU(unittest.TestCase):


	@classmethod
	def setUpClass(inst):
		inst.oHelper = Webapp()
		inst.oHelper.Setup("sigacfg","31/01/2023","11","01","FRP_P12133_TESTE")
		
	def test_CRIAUSU_001(self):
		self.oHelper.SetButton("OK")
		self.oHelper.SetValue("cGetUser","admin")
		self.oHelper.SetValue("cGetPsw","●●●●●●●●●●●●●")
		self.oHelper.SetButton("Entrar")
		self.oHelper.SetValue("cFil","02")
		self.oHelper.SetButton("Entrar")
		self.oHelper.SetLateralMenu("Usuário > Senhas > Usuários")
		self.oHelper.SearchBrowse("filipe.santana")
		self.oHelper.SetButton("Outras Ações")
		self.oHelper.SetValue("USR_CODIGO","acesso")
		self.oHelper.SetValue("USR_NOME","Acesso")
		self.oHelper.SetValue("USR_PSW","●●●●●●●●")
		self.oHelper.SetValue("USR_PSWCMP","●●●●●●●●")
		self.oHelper.SetButton("Confirmar")
		self.oHelper.SetButton("Fechar")
		self.oHelper.SetButton('x')
	@classmethod
	def tearDownClass(inst):
		inst.oHelper.TearDown()

if __name__ == '__main__':
	unittest.main()