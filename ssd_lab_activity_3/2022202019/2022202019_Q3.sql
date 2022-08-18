with dept as ( select p.Dnum from PROJECT as p INNER JOIN PROJECT as q ON p.Dnum = q.Dnum and p.Pname = 'ProductY') select Mgr_ssn,count(Dnum) as Num_of_project from dept INNER JOIN DEPARTMENT on
dept.Dnum=DEPARTMENT.Dnumber;

