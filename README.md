# Bank_Loan_Analysis

## 1.Data Collection

-->Imported the given data set and analysed it.<br>
-->Id columns or other columns that have unique values are useless for model training, so it was dropped.<br>
-->Banks usually don't approve loans on how many members are dependent on you, so no_of_dependents was dropped.<br>
-->Education has no effect on approval of loan, so it was dropped.<br>
-->Bank usually only care about your annual income and don't care of your employment_type for loan approval, so both self_employment and employment are dropped.<br>
-->Annual income,loan amount,loan term are important variables since annual income shows whether or not the person will be able to repay his loan in the given duration which is the loan term.<br>
-->Cibil score is the measure that says whether a person has payed his previous loans in time, the lower the measure the more time the particular individual has delayed to ppay his loan, so it is required.<br>
-->All commercial,residental,luxury,bank asset are all assets that bank considers while giving loan, so all these columns are combined into one column "total_assets".<br>
-->Loan status is our output column, so naturally it is considered.<br>

## 2.Data Preprosessing

-->Checking for null values
-->Checking for duplicate records.

## 3.Exploratory Data Analysis (EDA)

-->Checking if the data is skewed by plotting PDA
-->Checking for outliers in the skewed columns

## 4. Data Preparation

-->Applying train_test_split on the data set.
-->Applying Label Encoder on output column.
-->Applying standardization on all the input columns since all input columns are numeric.

## 5. Model Selection And Evaluation

-->Selected algorithms for model training are Logistic Regression, Decision Trees, Random Forest,Gradient Boosting,SVM,Naive Bayers.
-->All these 6 algorithms are trained on the data sets and accracy are obtained after apllying cross validation as well.
-->The selected algorithm for hyper parameter tuning is Random Forest since it gave a higher accuracy.

## 6. Hyperparameter Tuning Of Random Forest

-->Used GridSearchcv to find the correct measure of the hyper parameters such that a highest accracy is obtained.
-->










