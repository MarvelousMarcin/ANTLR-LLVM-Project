### Packages

- llvm
- antlr4-python3-runtime
- miniconda
- makefile

`conda create -n love`

`conda activate love`

`conda install antlr4-python3-runtime`

### Running

`make build` -> creates classes in lib folder

`make compile` -> creates file .ll

`lli text.ll` -> runs program
