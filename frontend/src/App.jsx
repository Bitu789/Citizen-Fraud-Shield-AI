import { useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [count, setCount] = useState(0);

  const analyzeMessage = async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/check", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: message,
        }),
      });

      const data = await response.json();

      setResult(data);
      setCount((prev) => prev + 1);
    } catch (error) {
      console.error(error);
      alert("Backend not running!");
    }
  };

  return (
    <div
      style={{
        maxWidth: "900px",
        margin: "auto",
        padding: "30px",
        fontFamily: "Arial",
      }}
    >
      <h1 style={{ color: "#d32f2f" }}>🛡️ Citizen Fraud Shield AI</h1>

      <p>
        Detect banking scams, OTP frauds, digital arrest scams,
        lottery scams, investment scams, job scams and UPI scams.
      </p>

      <h3>Messages Analyzed: {count}</h3>

      <textarea
        rows="8"
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
        }}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Paste suspicious message here..."
      />

      <br />
      <br />

      <button
        onClick={analyzeMessage}
        style={{
          padding: "12px 25px",
          fontSize: "16px",
          backgroundColor: "#1976d2",
          color: "white",
          border: "none",
          borderRadius: "5px",
          cursor: "pointer",
        }}
      >
        Analyze Message
      </button>

      {result && (
        <div
          style={{
            marginTop: "30px",
            padding: "20px",
            border: "1px solid #ddd",
            borderRadius: "10px",
          }}
        >
          <h2>Analysis Result</h2>

          <p>
            <strong>Risk Score:</strong> {result.risk_score}
          </p>

          <p>
            <strong>Risk Level:</strong> {result.risk_level}
          </p>

          <p>
            <strong>Fraud Type:</strong> {result.fraud_type}
          </p>

          {result.warning && (
            <div
              style={{
                background: "#ffdddd",
                padding: "10px",
                marginTop: "10px",
                borderRadius: "5px",
              }}
            >
              <pre>{result.warning}</pre>
            </div>
          )}

          <h3>Reasons</h3>

          <ul>
            {result.reasons?.map((reason, index) => (
              <li key={index}>{reason}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;