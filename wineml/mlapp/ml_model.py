import joblib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    wine = load_wine()
    X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    joblib.dump(model, 'mlapp/wine_model.pkl')

def predict(input_data):
    model = joblib.load('mlapp/wine_model.pkl')
    prediction = model.predict([input_data])
    return prediction


if __name__ == "__main__":
    train_model()
