import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
# 1. Load your dataset
# Assume 'label' is 'spam' or 'ham' and 'message' is the text
df = pd.read_csv('spam.csv', encoding='latin-1')
df = df[['v1', 'v2']] # Keep only the label and message columns
df.columns = ['label', 'message']

# 2. Convert labels to numbers (Computer prefers 0 and 1)
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# 3. Split data: 80% for training, 20% for testing the AI
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2)

# 4. Vectorization: Turn words into a matrix of counts
cv = CountVectorizer()
X_train_counts = cv.fit_transform(X_train)

# 5. Training the Multinomial Naive Bayes model
model = MultinomialNB()
model.fit(X_train_counts, y_train)

# 6. Test the model
X_test_counts = cv.transform(X_test)
predictions = model.predict(X_test_counts)

print(f"Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")