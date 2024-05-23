grammar LOVE;

prog: ( stat? NEWLINE )* 
    ;

stat: SHOW ID               #show
    | GET ID                #get
 	| ID 'LOVE' expr0	    #assign
    | ID 'LOVE' array       #assignArray
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


GET:    'get'
   ;

SHOW:   'show'
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
