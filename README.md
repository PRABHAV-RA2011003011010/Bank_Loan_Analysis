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
-->Final accuracies of all alogorithms are:
      Logistic Regression Accuracy: 0.6458131301470023
      Decision Tree Accuracy: 0.9857120867280184
      Random Forest Accuracy: 0.9859462787654891
      Gradient Boosting Accuracy: 0.9852442523996439
      SVM Accuracy: 0.622159734362459
      Naive Bayes Accuracy: 0.622159734362459
-->The selected algorithms for hyper parameter tuning are Random Forest and Decision Tree since both gave a close and higher accuracy.

## 6. Hyperparameter Tuning

-->Used GridSearchcv to find the correct measure of the hyper parameters such that a highest accracy is obtained.
-->After hyper parameter tuning of both random forest and decision tree accuracies obtained are:
      Decision Tree Accuracy: 0.9871156661786238
      Random Forest Accuracy: 0.9885797950219619  
-->Random Forest gave a higher accracy than Decision Tree, so created a new model of Random Forest with the parameters provided by Grid Search and trained it.
-->After training and cross validation of the new model the accuracy obtained is 0.9889918747457422 (98.89%)

## 7. Model Testing 
-->Created an inference code that accepts inputs from the user and predicts whether his loan approval request will be 'Approved' or 'Rejected'.













