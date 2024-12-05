select *
from SALESLT.Customer

select FirstName , MiddleName , LastName ,Suffix
from SALESLT.Customer

select SalesPesron,CONCAT(FirstName,' ' , MiddleName,' ' , LastName ) as CustomerName
from SALESLT.Customer



select CustomerID , CompanyName 
from SALESLT.Customer

select RevisionNumber 
from SalesLT.salesorederheader 