# Bank_Loan_Analysis
##1.Data Collection
-->Imported the given data set and analysed it.
-->id columns or other columns that have unique values are useless for model training, so it was dropped.
-->banks usually don't approve loans on how many members are dependent on you, so no_of_dependents was dropped.
-->education has no effect on approval of loan, so it was dropped.
-->bank usually only care about your annual income and don't care of your employment_type for loan approval, so both self_employment and employment are dropped.
