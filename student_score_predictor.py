# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

# Step 2: Load Data
url = "https://raw.githubusercontent.com/AdiPersonalWorks/Random/master/student_scores%20-%20student_scores.csv"
df = pd.read_csv(url)

# Step 3: Visualize the Data
plt.scatter(df['Hours'], df['Scores'], color='blue')
plt.title('Hours vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.grid(True)
plt.show()

# Step 4: Split the Data
X = df[['Hours']]   # Features
y = df['Scores']    # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train the Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Predict on Test Data
y_pred = model.predict(X_test)

# Step 7: Compare Actual vs Predicted
results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(results)

# Step 8: Visualize Regression Line
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')  # regression line
plt.title('Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.show()

# Step 9: Check Model Accuracy
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))

# Step 10: Predict Custom Input
hours = [[9.25]]
predicted_score = model.predict(hours)
print(f"Predicted score if a student studies for 9.25 hours = {predicted_score[0]:.2f}")
