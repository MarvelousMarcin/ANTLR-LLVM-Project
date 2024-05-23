build:
	rm -rf ./lib
	java -jar antlr-4.11.1-complete.jar -o lib -Dlanguage=Python3 LOVE.g4 

compile:
	python Driver.py input.love > text.ll
