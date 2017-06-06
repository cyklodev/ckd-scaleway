# content of test_sample.py
import os,subprocess

def test_dummy_pre():
   assert 1 == 1

def test_script_help():
    try: 
        c = subprocess.call(['python','ckd-scaleway.py','-h'])
    except:
        c = 100
    assert c == 0

def test_dummy_post():
   assert 1 == 1
