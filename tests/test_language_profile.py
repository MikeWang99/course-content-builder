import importlib.util, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]

def load():
    spec=importlib.util.spec_from_file_location("init_workspace",ROOT/"scripts"/"init_workspace.py")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod

IW=load()

class LanguageProfileTests(unittest.TestCase):
    def test_profiles_are_explicit(self):
        self.assertEqual(IW.PROFILES,("zh-en-teaching","en-full","zh-full"))

if __name__=="__main__": unittest.main()
