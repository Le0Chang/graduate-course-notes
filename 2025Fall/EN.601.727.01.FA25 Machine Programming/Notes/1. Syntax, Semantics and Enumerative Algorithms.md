# First Week

## Synthesis(综合)

### Dimensions in Program Synthesis

#### Behavioral Specification
What should the program do?（give orders）
  
* input/output examples
* logical formula
* natural language
* ...

#### Structural Specification
What is the space of the programs?（make rules）

* language syntax/grammar

#### Synthesis Strategy
How do we find such a program?

* bottom-up/top-down search

### Inductive Synthesis
Inductive reasoning from existing examples.

## Syntax(语法)
Ensure that the program structure is legal and specify "what can be written and how to write it".

### Regular Tree Grammars(RTGs)
Composition: non-terminals(非终结符)[N], terminals[$ \Sigma $], production rules[R] and starting nonterminal[S]

## Semantics(语义)
Explain the calculation logic of the program and clarify how the program converts inputs into outputs.

## Enumerative search(枚举)
Enumerate programs from the grammar one by one and test them on the examples.

### Bottom-up enumeration
Starting from bottle - from basic elements.

### Top-down enumeration
Calculating from top - from frame.

### Bottom-up vs top-down

#### Bottom-up
Program candidates are complete but might not be whole.
* Can always run on inputs.
* Cannot always relate to outputs.

#### Top-down
Program candidates are whole but might not be complete.
* Cannot always run on inputs
* Can always relate to outputs
