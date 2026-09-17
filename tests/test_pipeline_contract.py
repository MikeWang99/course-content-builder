import importlib.util, json, tempfile, unittest
from pathlib import Path

ROOT=Path(__file__).parents[1]
def load(name):
    spec=importlib.util.spec_from_file_location(name,ROOT/"scripts"/f"{name}.py"); mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
VS=load("validate_scope"); VR=load("validate_requirements"); VM=load("validate_learning_map"); VC=load("validate_coverage"); VRun=load("validate_run")

class PipelineTests(unittest.TestCase):
    def scope(self):
        return {"schema_version":"1.1","course":"Course","request":"Unit 1","status":"ready","matched_sections":[{"source_file":"s.pdf","locator":"Unit 1"}],"excluded_neighbors":[],"unresolved":[]}
    def requirements(self):
        return {"schema_version":"1.1","course":"Course","request":"Unit 1","requirements":[{"id":"REQ-001","category":"learning_objective","text":"State and explain X","source_file":"s.pdf","locator":"p1","scope_class":"required"},{"id":"REQ-002","category":"skill_or_practice","text":"Apply X to unfamiliar cases","source_file":"s.pdf","locator":"p1","scope_class":"required"}],"constraints":[{"id":"CON-001","category":"boundary_statement","text":"Do not require Z","source_file":"s.pdf","locator":"p1"}],"unresolved":[]}
    def learning_map(self):
        return {"schema_version":"1.3","status":"ready","items":[{"id":"KM-001","title":"Definition of X","requirement_ids":["REQ-001"],"primary_type":"A","secondary_types":["B"],"rationale":"Definition must be recalled and then explained.","recommended_learning_action":"Closed-book recall, then reconstruct the explanation."},{"id":"KM-002","title":"Apply X","requirement_ids":["REQ-002"],"primary_type":"C","secondary_types":[],"rationale":"Mastery requires transfer to unfamiliar contexts.","recommended_learning_action":"Varied application practice."}],"unresolved":[]}
    def coverage(self):
        return {"schema_version":"1.1","status":"ready","coverage":[{"requirement_id":"REQ-001","planned_section":"Section X","teaching_mode":["recall","model"],"status":"planned"},{"requirement_id":"REQ-002","planned_section":"Applications","teaching_mode":["application"],"status":"planned"}],"constraint_handling":[{"constraint_id":"CON-001","handling":"exclude-or-label-extension"}],"unresolved":[]}
    def test_learning_map_passes(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; m=Path(d)/"learning-map.json"; r.write_text(json.dumps(self.requirements())); m.write_text(json.dumps(self.learning_map())); self.assertEqual(VM.validate(r,m),[])
    def test_missing_required_requirement_fails_learning_map(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; m=Path(d)/"learning-map.json"; r.write_text(json.dumps(self.requirements())); data=self.learning_map(); data["items"]=data["items"][:1]; m.write_text(json.dumps(data)); self.assertTrue(any("REQ-002" in e for e in VM.validate(r,m)))
    def test_invalid_primary_type_fails(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; m=Path(d)/"learning-map.json"; r.write_text(json.dumps(self.requirements())); data=self.learning_map(); data["items"][0]["primary_type"]="D"; m.write_text(json.dumps(data)); self.assertTrue(any("primary_type" in e for e in VM.validate(r,m)))
    def test_secondary_cannot_repeat_primary(self):
        with tempfile.TemporaryDirectory() as d:
            r=Path(d)/"requirements.json"; m=Path(d)/"learning-map.json"; r.write_text(json.dumps(self.requirements())); data=self.learning_map(); data["items"][0]["secondary_types"]=["A"]; m.write_text(json.dumps(data)); self.assertTrue(any("repeat" in e for e in VM.validate(r,m)))
    def test_final_run_requires_learning_mode_section(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d); paths={name:d/name for name in ["scope.json","requirements.json","learning-map.json","coverage.json","run.json","out.md"]}
            paths["scope.json"].write_text(json.dumps(self.scope())); paths["requirements.json"].write_text(json.dumps(self.requirements())); paths["learning-map.json"].write_text(json.dumps(self.learning_map())); paths["coverage.json"].write_text(json.dumps(self.coverage())); paths["run.json"].write_text(json.dumps({"language_profile":"zh-en-teaching"}))
            paths["out.md"].write_text("这是中文结构说明。"*20 + " This section explains physical relationships, definitions, conditions, models, representations, calculations, graphs, reasoning, applications, and exam language. "*8)
            errors=VRun.validate(paths["scope.json"],paths["requirements.json"],paths["learning-map.json"],paths["coverage.json"],paths["out.md"],paths["run.json"])
            self.assertTrue(any("learning-mode" in e for e in errors))
    def test_final_run_with_learning_mode_section_passes(self):
        with tempfile.TemporaryDirectory() as d:
            d=Path(d); paths={name:d/name for name in ["scope.json","requirements.json","learning-map.json","coverage.json","run.json","out.md"]}
            paths["scope.json"].write_text(json.dumps(self.scope())); paths["requirements.json"].write_text(json.dumps(self.requirements())); paths["learning-map.json"].write_text(json.dumps(self.learning_map())); paths["coverage.json"].write_text(json.dumps(self.coverage())); paths["run.json"].write_text(json.dumps({"language_profile":"zh-en-teaching"}))
            paths["out.md"].write_text("## 本章学习模式地图 · Learning Mode Map\n" + "这是中文结构说明。"*20 + " This section explains physical relationships, definitions, conditions, models, representations, calculations, graphs, reasoning, applications, and exam language. "*8)
            self.assertEqual(VRun.validate(paths["scope.json"],paths["requirements.json"],paths["learning-map.json"],paths["coverage.json"],paths["out.md"],paths["run.json"]),[])

if __name__=="__main__": unittest.main()
