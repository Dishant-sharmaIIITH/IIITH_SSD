Delimiter $$
create procedure custdetails()
begin

select CUST_NAME ,GRADE from customer where OPENING_AMT+RECEIVE_AMT>10000;
end $$


call custdetails()$$
