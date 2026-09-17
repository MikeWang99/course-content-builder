import importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
spec=importlib.util.spec_from_file_location("validate_language",ROOT/"scripts"/"validate_language.py")
VL=importlib.util.module_from_spec(spec); spec.loader.exec_module(VL)

class LanguagePolicyTests(unittest.TestCase):
    def validate_text(self,profile,text):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); run=root/"run.json"; out=root/"out.md"
            run.write_text(json.dumps({"language_profile":profile}),encoding="utf-8")
            out.write_text(text,encoding="utf-8")
            return VL.validate(run,out)

    def test_mixed_profile_accepts_functional_bilingual_content(self):
        zh="这一部分先解释为什么需要这个模型，并帮助学生降低阅读负担。"*8
        en=("Velocity describes the rate of change of position. The slope of a position-time graph represents velocity. "
            "Check the sign convention, model conditions, and physical meaning before solving. ")*12
        self.assertEqual(self.validate_text("zh-en-teaching",zh+"\n"+en),[])

    def test_mixed_profile_rejects_chinese_only_output(self):
        text="这一部分全部使用中文解释运动学、速度、加速度、图像和模型条件。"*30
        self.assertTrue(any("English" in e for e in self.validate_text("zh-en-teaching",text)))

    def test_mixed_profile_rejects_english_only_output(self):
        text=("This chapter explains velocity acceleration graphs models conditions and problem solving reasoning. ")*40
        self.assertTrue(any("Chinese" in e for e in self.validate_text("zh-en-teaching",text)))

if __name__=="__main__": unittest.main()
