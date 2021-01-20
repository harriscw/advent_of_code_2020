proc import datafile="input.txt" out=input dbms=dlm replace;
 delimiter=' ';
   getnames=no;
run;

/*proc print data=input;run;*/

proc sql;
    create table want as select a.VAR1 as VAR1,b.VAR1 as VAR2,c.VAR1 as VAR3
         from input(keep=VAR1) a,input(keep=VAR1) b,input(keep=VAR1) c;
quit;

data want;
set want;
if VAR1+VAR2+VAR3=2020;
VAR4=VAR1*VAR2*VAR3;
run;

proc print;run;