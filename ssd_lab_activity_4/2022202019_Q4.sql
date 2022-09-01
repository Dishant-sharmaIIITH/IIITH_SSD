Delimiter $$
create procedure callcur()
begin
DECLARE exit INT DEFAULT 0;

DECLARE name VARCHAR(50);
DECLARE  dist VARCHAR(20);
DECLARE  country VARCHAR(20);
DECLARE  grad decimal(10,0);
DECLARE pointer CURSOR FOR select CUST_NAME,WORKING_AREA,CUST_COUNTRY,GRADE from customer WHERE AGENT_CODE LIKE "A00%";
DECLARE CONTINOU HANDLER FOR NOT FOUND SET exit=1;
OPEN pointer;
label: Loop
FETCH POINTER INTO name,dist,country,grad;
INSERT INTO data VALUES(name,dist,country,grad);
IF exit=1 THEN LEAVE label;
END IF;
END LOOP;
CLOSE CUR;
END $$


