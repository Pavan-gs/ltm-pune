function App() {

  const callApi = async () => {

    const response = await fetch(
      "http://127.0.0.1:8000/predict",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          age: 45,
          salary: 75000
        })
      }
    );

    const data = await response.json();

    console.log(data);
  };

  return (
    <div>
      <button onClick={callApi}>
        Predict
      </button>
    </div>
  );
}

export default App;

# npx create-react-app react-demo
# npm start

'''Click Button
↓
React calls FastAPI
↓
FastAPI returns prediction
↓
Prediction printed in browser console'''

'''React Frontend
      ↓
.NET Backend API
      ↓
FastAPI ML Service'''

'''| Ecosystem | Library       |
| --------- | ------------- |
| Python    | requests      |
| .NET      | HttpClient    |
| React     | fetch / axios |
'''