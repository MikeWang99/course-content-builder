import importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/"scripts"/f"{name}.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
VS=load("validate_scope"); VR=load("validate_requirements"); VC=load("validate_coverage")

class PipelineTests(unittest.TestCase):
    def scope(self):
        return {"schema_version":"1.1","course":"Course","request":"Unit 1","status":"ready","matched_sections":[{"source_file":"s.pdf","locator":"Unit 1"}],"excluded_neighbors":[],"unresolved":[]}
    def requirements(self):
        return {"schema_version":"1.1","course":"Course","request":"Unit 1","requirements":[{"id":"REQ-001","category":"learning_objective","text":"Explain X","source_file":"s.pdf","locator":"p1","scope_class":"required"},{"id":"REQ-002","category":"topic","text":"Y","source_file":"s.pdf","locator":"p1","scope_class":"supporting"}],"constraints":[{"id":"CON-001","category":"boundary_statement","text":"Do not require Z","source_file":"s.pdf","locator":"p1"}],"unresolved":[]}
    def coverage(self):
        return {"schema_version":"1.1","status":"ready","coverage":[{"requirement_id":"REQ-001","planned_section":"Section X","teaching_mode":["intuition"],"status":"planned"}],"constraint_handling":[{"constraint_id":"CON-001","handling":"exclude-or-label-extension"}],"unresolved":[]}
    def test_ready_scope_passes(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"scope.json"; p.write_text(json.dumps(self.scope())); self.assertEqual(VS.validate(p),[])
    def test_scope_rejects_legacy_embedded_requirements(self):
        with tempfile.TemporaryDirectory() as d:
            data=self.scope(); data["official_requirements"]={}; p=Path(d)/"scope.json"; p.write_text(json.dumps(data)); self.assertTrue(any("requirements.json" in e for e in VS.validate(p)))
    def test_valid_requirements_pass(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/"requirements.json"; p.write_text(json.dumps(self.requirements())); self.assertEqual(VR.validate(p),[])
    def test_duplicate_requirement_id_fails(self):
        with tempfile.TemporaryDirectory() as d:
            data=self.requirements(); data["constraints"][0]["id"]="REQ-001"; p=Path(d)/"requirements.json"; p.write_text(json.dumps(data)); self.assertTrue(any("duplicate id" in e for e in VR.validate(p)))
    def test_complete_coverage_passes(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; c=Path(d)/"coverage.json"; r.write_text(json.dumps(self.requirements())); c.write_text(json.dumps(self.coverage())); self.assertEqual(VC.validate(r,c),[])
    def test_missing_required_coverage_fails(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; c=Path(d)/"coverage.json"; r.write_text(json.dumps(self.requirements())); data=self.coverage(); data["coverage"]=[]; c.write_text(json.dumps(data)); self.assertTrue(any("REQ-001" in e for e in VC.validate(r,c)))
    def test_missing_constraint_handling_fails(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; c=Path(d)/"coverage.json"; r.write_text(json.dumps(self.requirements())); data=self.coverage(); data["constraint_handling"]=[]; c.write_text(json.dumps(data)); self.assertTrue(any("CON-001" in e for e in VC.validate(r,c)))

if __name__=="__main__": unittest.main()
