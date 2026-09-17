# Language policy · v1.2

Course Builder supports explicit output language profiles. The default profile is `zh-en-teaching`.

## `zh-en-teaching` (default)

The goal is not line-by-line translation. Use each language where it reduces teaching friction.

### English-first content
Use English as the primary language for content the teacher or student may need to recognize, say, write, or reason with in an English-language exam or classroom:

- official course terminology and named concepts;
- definitions worth learning in exam-ready wording;
- physical relationships and directional/spatial relationships;
- mathematical reasoning and derivation steps when they carry physics meaning;
- graph descriptions, representation language, vector/component language, sign conventions, conditions, assumptions, and boundary statements;
- problem-recognition cues and common exam wording;
- worked-example physics reasoning and short justifications that could be spoken directly in class;
- claim/evidence/reasoning or other assessment-style sentences when relevant.

For first introduction of an important term, prefer `English term（中文释义）`. After that, keep the canonical English term unless Chinese is genuinely clearer for a transition.

### Chinese-first content
Use Chinese primarily for navigation and cognitive-load reduction:

- section titles and structural headings unless an official English title is especially useful;
- transitions between ideas;
- short teacher-facing notes about why the next section matters;
- misconception diagnosis/explanation around the core English term;
- summary labels such as 核心误区、自查清单、关系式总表、知识地图、题型识别;
- meta-instructions, pacing notes, and brief pedagogical commentary.

### Bilingual when useful
Use concise bilingual presentation when both recognition and fast reading matter:

- first occurrence of high-value terminology;
- official Learning Objective / Essential Knowledge wording followed by a short Chinese explanation;
- table column labels when the table is likely to be reused for teaching;
- short exam-ready sentence patterns followed by a Chinese note explaining when to use them.

Avoid duplicate paragraphs that say the same thing fully in both languages.

## `en-full`
Use English for essentially all student-facing content. Chinese may appear only in user-requested teacher notes.

## `zh-full`
Use Chinese prose, but preserve official English terminology on first use and never translate symbols/equation notation into nonstandard forms.

## Priority rule
If the user explicitly specifies a language format for a run, that run-level request overrides the default profile. Otherwise use `zh-en-teaching`.
