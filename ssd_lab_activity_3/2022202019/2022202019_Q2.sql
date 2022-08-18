with tab as ( select count(Super_ssn) as cnt,Super_ssn from EMPLOYEE Group By Super_ssn) select concat(Fname,Minit,Lname) as Fullname,Ssn,Dno,cnt as No_of_emp from tab Inner join EMPLOYEE on tab.Super_ssn = EMPLOYEE.Ssn order by cnt ASC;

