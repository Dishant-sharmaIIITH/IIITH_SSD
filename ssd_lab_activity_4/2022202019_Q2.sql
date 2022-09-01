
Delimiter $$
create procedure custname(in city varchar(50))
begin

select CUST_NAME from customer where WORKING_AREA=city;
end $$


call custname("Bangalore")$$
