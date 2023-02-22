grammar broCode;

// PARSER

program: start line* end;

start: START;

end: END;

line: statement | ifBlock | loopBlock;

statement: (assignment | printstmt ) SEMICOLON;

ifBlock: IF expression innerBlock (ELSEIF expression innerBlock)* (ELSE innerBlock)? ;

innerBlock: block | ifBlock | loopBlock;

loopBlock: LOOP expression innerBlock;

block: LSECONDPAREN line* RSECONDPAREN;

assignment: IDENTIFIER ASSIGN expression;

printstmt: PRINT term;

term: IDENTIFIER | INTEGER | STRING;

// functionCall: IDENTIFIER LFIRSTPAREN (expression (COMM expression)*)? RFIRSTPAREN;

expression
    : constant                          #constantExpression
    | IDENTIFIER                        #identifierExpression
    // | functionCall                      #functionCallExpression
    | LFIRSTPAREN expression RFIRSTPAREN #parenthesizedExpression
    | NOT expression                    #notExpression
    | expression MULTOP expression      #multiplicativeExpression
    | expression ADDOP expression       #additiveExpression
    | expression COMPAREOP expression   #comparisionExpression
    | expression BOOLOP expression      #booleanExpression
    ;


constant: INTEGER | FLOAT | STRING | BOOL | NULL;

// LEXER


WS: [ \n\t\r]+ -> skip; 

INTEGER: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: ('"' ~'"'* '"') | ('\'' ~'\''* '\'');
BOOL: 'true' | 'false';
NULL: 'null';

START: 'start bro\n';
END: 'stop bro' EOF;

// Keywords

LOOP: 'jotokhon bro';
IF: 'jodi bro';
ELSE: 'na hole bro';
ELSEIF: 'jodi na bro';
PRINT: 'bol bro';
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;


// Opperators

ASSIGN: '->';
NOT: '!';
MULTOP: '*' | '/' | '%';
ADDOP: '+' | '-';
COMPAREOP: '==' | '!=' | '>' | '<' | '>=' | '<=';
BOOLOP: 'and' | 'or' | 'xor';


SEMICOLON: ';';
LSECONDPAREN: '{';
RSECONDPAREN: '}';
LFIRSTPAREN: '(';
RFIRSTPAREN: ')';
COMM: ',';