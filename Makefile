build:
	rm -rf ./lib
	java -jar antlr-4.11.1-complete.jar -o lib -Dlanguage=Python3 LOVE.g4 


string:
	python Driver.py string.love > string.ll
	lli string.ll

simplecalc:
	python Driver.py simplecalc.love > simplecalc.ll
	lli simplecalc.ll

realcalc:
	python Driver.py realcalc.love > realcalc.ll
	lli realcalc.ll

readwrite:
	python Driver.py readwrite.love > readwrite.ll
	lli readwrite.ll

array:
	python Driver.py array.love > array.ll
	lli array.ll

error:
	python Driver.py error.love > error.ll
	lli error.ll


function:
	python Driver.py function.love > function.ll
	lli function.ll



if:
	python Driver.py if.love > if.ll
	lli if.ll


clean:
	rm -f *.ll
	rm -f *.class