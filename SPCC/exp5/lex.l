%{
int keywords = 0;
int arithmetic = 0;
int logic = 0;
int relational = 0;
int identifiers = 0;
%}

%%

"int"|"float"|"char"|"double"|"while"|"for"|"do"|"if"|"break"|"continue"|"void"|"switch"|"case"|"long"|"struct"|"const"|"typedef"|"return"|"else" {keywords++; printf("\n keywords : %s", yytext);}

[a-zA-Z_][a-zA-Z0-9_]* {identifiers++; printf("\n identifier : %s", yytext);} 

"+"|"-"|"*"|"/"|"%" {arithmetic++; printf("\n  arithmetic operator : %s", yytext);}

">"|">="|"<"|"<="|"=="|"!=" {relational++; printf("\n relational operator : %s", yytext);} 

"&&"|"||"|"!" {logic++;printf("\n logic operator : %s", yytext);}
%%
int main(int argc, char **argv)
{
FILE *file;
file=fopen("lex.c","r");
if(!file)
{
printf("could not open the file");
exit(0);
}
yyin=file;
yylex();
printf("\n");
printf("\n Total no. of keywords = %d\n", keywords);
printf("\n Total no. of arithmetic operators = %d\n", arithmetic);
printf("\n Total no. of logic operators = %d\n", logic);
printf("\n Total no. of relational operators = %d\n", relational);
printf("\n Total no. of identifiers = %d\n", identifiers);
return(0);
}
int yywrap()
{
return(1);
}
