PREDICTING MILES PER GALLON (FUEL EFFICIENCY)
A MULTI LINEAR REGRESSION ANALYSIS OF WEIGHT, ACCELERATION, CYLINDER AGAINST MILES PER GALLON
This data science project is a personal effort aimed at building a multi linear regression model that accurately forecast miles per gallon using these key factors; weight, acceleration and cylinder of the car.
This data was obtained from geeksforseeks.com, the data set contains information for various car brands, the weight, the horse power, the displacement, cylinder, acceleration and the model year
PROBLEM STATEMENT
We will examine the relationship between weight acceleration cylinder and miles per gallon of different car brand, for the average citizen, getting a car of low fuel consumption is of great necessity and one of the major factors to look out for when choosing a car of choice.
DATA DESCRIPTION
This data set contains the following columns:
Miles per gallon; This column contains the miles per gallon of different car brand.
Cylinders; In this column contains the amount of cylinders or plugs in each car, a car cylinder is a chamber in a car engine that burns fuel to create power that moves the vehicle.
Displacement; This column shows us the maximum displacement of the car, it is the way to measure the engine size and power.
Horse Power; This column gives us the horse power of the car, the horse power of the car tells us how much power a car engine produces it is a key factor in determining a car performance such as its top speed and ability to accelerate.
Weight; This column shows us the weight of each car, the weight of each car actually plays a major role in determining the acceleration of the car.
Acceleration; This column shows us the acceleration of each car, a car’s accelerator, also known as the gas pedal or throttle, controls the speed of the vehicle by controlling the amount of fuel that goes into the engine.
Model Year; This column tells us the year the car is manufactured.
Car Name; This column tells us the different car brands that is present in this data set i.e; ford torino, Chevrolet monte carlo, Plymouth duster, BMW 2002, dodge d200
METHODOLOGY
1.	Data Loading and cleaning:  The dataset was loaded using Pandas, and initial data exploration was conducted to understand its structure and identify any missing values or inconsistencies. It was found that the dataset was complete, with no missing values, consisting of 399 rows and 9 columns as there were no irregularities, no rows needed to be dropped or refilled.
2.	Exploratory Data Analysis: Descriptive statistics and visualizations were used to gain insights into the data distribution, relationships between variables, and potential outliers. Boxplots helped us view the distribution of data and identify any outliers in the dataset.
3.	Data Preprocessing: Outliers were identified and handled using the flooring technique.
4.	Feature Selection: Relevant features for the model were selected based on their correlation with the target variable (miles per gallon (MPG)). Weight acceleration and cylinder showed a good linear relationship with the target variable.
5.	Model Building: A multi linear regression model was trained using the selected features and the target variable. A baseline model was also created for comparison.
6.	Training and Testing the Model: The dataset was split into training and testing sets (using an 80/20 split). The multi linear regression model was trained on the training set and then tested on the testing set to evaluate its predictive performance. The model was assessed based on how well it predicted miles per gallon (MPG) using the testing data.
7.	Model Evaluation: The model’s performance was evaluated using the Mean Absolute Error (MAE) metric. 
RESULTS
The multi linear regression model demonstrated a good fit to the data and achieved a satisfactory level of accuracy in predicting miles per gallon based on the weight, acceleration and cylinder of the car. This model performance was compared to the baseline model, and it was found to be significantly better.
CONCLUSION
This project successfully developed a multi linear regression model to predict the miles per gallon of a car using the weight, acceleration and cylinder. This model can be used by individual to make and informed decisions regarding picking a good fuel efficient car, further testing can be done to improve its 
