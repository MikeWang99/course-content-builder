import importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
def load(name, path):
    spec=importlib.util.spec_from_file_location(name, ROOT/path); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
VS=load("validate_scope", "scripts/validate_scope.py")

class ScopeTests(unittest.TestCase):
    def test_ready_scope_passes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"scope.json"
            p.write_text(json.dumps({
                "schema_version":"1.0","course":"Course","request":"Unit 1","status":"ready",
                "matched_sections":[{"source_file":"s.pdf","locator":"Unit 1","title":"Unit 1","evidence":"x"}],
                "official_requirements":{k:[] for k in VS.REQUIRED_REQ_KEYS},"unresolved":[]
            }))
            self.assertEqual(VS.validate(p), [])
    def test_review_scope_blocks_generation(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"scope.json"
            p.write_text(json.dumps({"schema_version":"1.0","request":"Kinematics","status":"review","matched_sections":[],"official_requirements":{k:[] for k in VS.REQUIRED_REQ_KEYS},"unresolved":["ambiguous"]}))
            self.assertTrue(VS.validate(p))

if __name__=="__main__": unittest.main()
