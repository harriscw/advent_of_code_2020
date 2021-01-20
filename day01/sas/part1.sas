proc import datafile="input.txt" out=input dbms=dlm replace;
 delimiter=' ';
   getnames=no;
run;

/*proc print data=input;run;*/

proc sql;
    create table want as select a.VAR1 as VAR1,b.VAR1 as VAR2
         from input(keep=VAR1) a,input(keep=VAR1) b;
quit;

data want;
set want;
if VAR1+VAR2=2020;
VAR3=VAR1*VAR2;
run;

proc print;run;