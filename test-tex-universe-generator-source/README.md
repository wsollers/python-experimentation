# Test TeX Universe Generator

A stateful, coverage-guided generator of syntactically intended-valid mathematical TeX. It creates a synthetic universe containing objects such as `TestType01`, `TestAmbient01`, `TestStructure01`, `TestPredicate01`, `TestRelation01`, `TestFunction01`, and `TestNumberSystem01`, then combines them into formulas and mathematical discourse.

The generator is not a fixed regression corpus. It persists its universe, generated hashes, counters, and coverage statistics, then continues producing new cases on later runs.

## Meaning of valid

Here, valid means syntactically intended-valid and internally typed. Generated statements are not asserted to be logically true in a real mathematical model.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

On Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e .
```

## Basic use

```bash
test-tex-gen \
  --config config/default.yaml \
  --state work/generator-state.json \
  --output work/generated-tests.yaml \
  --coverage-report work/coverage-report.json
```

Continue an existing campaign:

```bash
test-tex-gen \
  --state work/generator-state.json \
  --output work/generated-tests.yaml \
  --count 500 \
  --append
```

## Important flags

```text
--count 500
--seed 42
--strategy least-covered
--max-formula-depth 6
--max-quantifier-depth 5
--predicate-arities 0,1,2,3,4
--function-arities 0,1,2,3
--connectives not,and,or,implies,iff
--quantifiers forall,exists,exists_unique
--discourse-forms formula,let-suppose-then,let-assume-therefore,given-it-follows
--renderers house,fully-parenthesized,text-connectives,expanded-quantifiers
```

## Generated case structure

Each YAML record includes:

- generated TeX;
- a canonical formula tree;
- a canonical hash;
- a rendering hash;
- root kind;
- quantifier depth;
- predicate arities;
- rendering and discourse features;
- `syntactically_intended_valid: true`.

The canonical formula tree is the independent oracle against which parser output should be compared.

## Synthetic universe

The universe currently generates:

- types;
- ambients;
- number systems;
- structures;
- elements;
- sets;
- constants;
- predicates of arity 0 through 4;
- relations of arity 2 through 4;
- functions of arity 0 through 3;
- operations of arity 1 through 3.

Predicate and function argument types may be homogeneous or heterogeneous.

## Logical forms

The generator composes:

- atomic predicate and relation applications;
- membership;
- equality;
- subset relations;
- negation;
- conjunction;
- disjunction;
- implication;
- biconditional;
- universal quantification;
- existential quantification;
- unique existential quantification.

It also generates discourse such as:

- `Let ...`;
- `Suppose that ... Then ...`;
- `Assume that ... Therefore ...`;
- `Given ... It follows that ...`.

## Adding predicates and relations

Extend `Universe.create_predicate` and `Universe.create_relation` in `src/test_tex_generator/universe.py`.

For a future registry-driven design, add a YAML registry with fields such as:

```yaml
predicates:
  - id: TestPredicateCustom01
    tex: C_1
    arity: 3
    argument_types: [element, ambient, structure]
    category: predicate
```

## Adding notation

Notation should remain independent of canonical formula identity. Add renderer alternatives for connectives, quantifiers, parentheses, function application, infix relations, and spacing while preserving the same canonical tree.

Suggested registry shape:

```yaml
notation:
  conjunction:
    symbolic: "\\land"
    alternatives: ["\\wedge", "\\mathbin{\\wedge}"]
    text: "\\quad\\text{and}\\quad"
```

## Adding structures

Extend structure symbols with carriers and signatures:

```yaml
structures:
  - id: TestStructureCustom01
    tex: "\\mathcal{S}_1"
    carrier: TestAmbient01
    components:
      constants: [TestConstant01]
      functions: [TestFunction01]
      relations: [TestRelation01]
      operations: [TestOperation01]
```

This enables declarations such as:

```latex
Let \(\mathcal{S}_1=(A_1,c_1,f_1,R_1,\star_1)\) be a test structure.
```

## Adding type categories

Extend `TYPE_POOL` and `symbol_for_type` for categories such as sequence, topology, metric, measure, field, vector space, index set, family, operator, language, formula, or model.

Each new type needs:

1. an ID prefix;
2. a TeX representation;
3. a generation method;
4. allowed predicate/function argument positions;
5. coverage accounting.

## Adding formula constructions

Extend `UniverseTestGenerator.formula` and `render_formula` for new canonical node kinds. Every node kind requires:

1. construction logic;
2. typing constraints;
3. TeX rendering;
4. structural metadata extraction;
5. coverage tracking.

Potential additions include set-builder notation, indexed families, function definitions, lambda notation, relation properties, induction schemes, and second-order quantification.

## Parser/validator loop

A productive Codex loop is:

```text
load state
select least-covered feature combinations
generate a batch
run parsers and validators
compare parser output with canonical_formula
cluster failures by construction and renderer
patch parser or validator
rerun the failed cluster
update state and coverage
generate another batch
```

Do not treat a parse as successful merely because a parser returns an object. Compare connective structure, binder scope, quantifier order and depth, predicate/function arity, argument order, and free/bound symbols.

## Tests

```bash
pip install pytest
pytest
```

The smoke test verifies that generated cases are unique and marked syntactically intended-valid.
