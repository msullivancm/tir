import unittest
from CRIAUSUTESTCASE import CRIAUSU

suite = unittest.TestSuite()
suite.addTest(CRIAUSU('test_CRIAUSU_001'))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)