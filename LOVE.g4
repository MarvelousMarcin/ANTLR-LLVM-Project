grammar LOVE;

prog: block
    ;

block: ( (stat|function|struct|class)? NEWLINE )* 
;

function: FUNCTION fparam fblock ENDFUNCTION
;

class: 'class' ID classBody 'endclass'
    ;

struct: 'struct' ID structBody 'endstruct'
    ;

structBody: ( ID? NEWLINE )* 
    ;

classBody: ( (ID | function)? NEWLINE )* 
    ;

stat: SHOW ID '.' ID        #showStructMember
    | SHOW ID '->' ID        #showClassMember
    | SHOW ID               #show
    | ID 'HEART' ID         #assignStruct
    | ID 'CLASS' ID         #assignClass
    | GET ID                #get
    | GETS ID               #gets
 	| ID 'LOVE' expr0	    #assign
    | ID 'LOVE' array       #assignArray
    | ID '.' ID 'LOVE' expr0  #assignStructMember
    | ID '->' ID 'LOVECLASS' expr0  #assignClassMember
    | ID '[' INT ']'        #arrayAccess
    | REPEAT repetitions block ENDREPEAT		#repeat
    | IF equal THEN blockif ENDIF 	#if
   ;

blockif: block
;

equal: ID '==' INT
;

expr0:  expr1			    #single0
      | expr1 ADD expr0	    #add 
      | expr1 MINUS expr0	#substr 
;

expr1:  expr2			    #single1
      | expr2 MULT expr2	#mult 
      | expr2 DIV  expr2    #div
;

expr2:   INT			    #int
       | REAL			    #real
       | '(float)' REAL     #float
       | ID                 #id
       | STRING             #string
       | '(' expr0 ')'		#par
;

repetitions: expr2
;


array: '{' (INT (',' INT)*)? '}' #arr
    ;

fblock: ( stat? NEWLINE )* 
; 



fparam: ID
;

FUNCTION: 'fLOVE'
;

ENDFUNCTION:	'endfLOVE'
;

REPEAT: 'loop'
;

IF:	'if'
;

THEN:	'then'
;

ENDIF:	'endif'
;

ENDREPEAT: 'endloop'
;

GET:    'get'
   ;

SHOW:   'show'
   ;

GETS:   'gets'
   ;
   
ID:   ('a'..'z'|'A'..'Z')+
   ;

REAL: '0'..'9'+'.''0'..'9'+
    ;

INT:   '0'..'9'+
    ;

ADD: '+'
    ;

DIV: '/'
    ;

MINUS: '-'
    ;

MULT: '*'
    ;

STRING :  '"' ( ~('\\'|'"') )* '"'
    ;

NEWLINE:	'\r'? '\n'
    ;

WS:   (' '|'\t')+ -> skip
    ;