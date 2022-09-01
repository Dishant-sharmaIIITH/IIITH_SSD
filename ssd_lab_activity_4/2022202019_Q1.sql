Delimiter $$
create procedure Addtwonum(in num1 int ,in num2 int,out result int )
begin
set result=(num1+num2);
end $$




call Addtwonum(3,2,@sum);
select @sum;

