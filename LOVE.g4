grammar LOVE;

prog: ( (stat|function)? NEWLINE )* 
    ;

function: FUNCTION fparam fblock ENDFUNCTION
;

stat: SHOW ID               #show
    | GET ID                #get
    | GETS  ID              #gets
 	| ID 'LOVE' expr0	    #assign
    | ID 'LOVE' array       #assignArray
    | ID '[' INT ']'        #arrayAccess
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
       | ID                 #id
       | STRING             #string
       | '(' expr0 ')'		#par
;

array: '{' (INT (',' INT)*)? '}' #arr
    ;

fblock: ( stat? NEWLINE )* 
; 

fparam: ID
;

FUNCTION: 'function'
;

ENDFUNCTION:	'endfunction'
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