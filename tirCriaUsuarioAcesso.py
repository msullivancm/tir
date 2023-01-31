#!/usr/bin/env python
# -*- coding: latin-1 -*-

from tir import Webapp
import unittest
from datetime import datetime

#------------------------------------------------------------------
#- Criação do usuário acesso                                      -
#- Autor: Marcus Sullivan Cordeiro da Motta                       -
#------------------------------------------------------------------
class CRIAUSU(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        atual = datetime.now()
        hoje = atual.strftime("%d/%m/%Y")
        inst.oHelper = Webapp()
        inst.oHelper.Setup('SIGACFG',hoje,'11','02')
        oHelper.SetLateralMenu("Usuários")

    def test_CRIAUSU01(self):
        '''usuarioModelo = '002351'
        usuarioDestino = 'acesso'
        senhaDestino = keyring.get_password("acessoprotheus", "acesso")
        self.oHelper.SetValue('input', usuarioModelo)
        self.oHelper.SetButton('Pesquisar')
        self.oHelper.SetButton('Cópia')
        self.oHelper.SetValue('COMP7681', usuarioDestino)
        self.oHelper.SetValue('COMP7683', senhaDestino)
        self.oHelper.SetValue('COMP7684', senhaDestino)
        self.oHelper.SetButton('Confirmar')'''
        self.oHelper.SetButton('Fechar')
        self.oHelper.AssertTrue()
        
    @classmethod
    def tearDownClass(inst):
        inst.oHelper.TearDown()

if __name__ == '__main__':
    unittest.main()