# content of test_sample.py
import unittest
import os,subprocess
from CkdPrompt import CkdPrompt

class TestCkdScaleway(unittest.TestCase):

    def test_dummy_pre(self):
        assert 1 == 1

    def test_script_help(self):
        try: 
            c = subprocess.call(['python','ckd-scaleway.py','-h'])
        except:
            c = 100
        assert c == 0

    def test_interactive_loading(self):
        """Test loading and quit"""
        prompt = CkdPrompt()
        with self.assertRaises(SystemExit):
            prompt.do_quit('')

    def test_dummy_post(self):
        assert 1 == 1


if __name__ == '__main__':
    unittest.main()
