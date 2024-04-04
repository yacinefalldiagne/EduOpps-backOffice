create Databases Tests;
use Tests;
create table utilisateurs(
   login varchar(30),
   password varchar(30)
);
insert into utilisateurs(login,password) values('yacine','passer');
