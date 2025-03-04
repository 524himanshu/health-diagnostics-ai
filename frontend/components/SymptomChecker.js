import { useState } from "react";
import { motion } from "framer-motion";

export default function SymptomChecker() {
  const [symptoms, setSymptoms] = useState("");
  const [response, setResponse] = useState("");
  const [followUp, setFollowUp] = useState("");
  const [file, setFile] = useState(null);
  const [reportData, setReportData] = useState({});

  const handleSymptomSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("/api/symptoms", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ symptoms }),
    });
    const data = await res.json();
    setResponse(data.prediction);
    setFollowUp(data.follow_up);
  };

  const handleFileUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("/api/report", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setReportData(data);
  };

  return (
    <motion.div
      className="p-4 max-w-lg mx-auto bg-white rounded-2xl shadow-lg"
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <h2 className="text-2xl font-bold mb-4 text-center">
        🩺 AI Health Diagnostics
      </h2>

      <motion.form
        onSubmit={handleSymptomSubmit}
        className="mb-4"
        whileHover={{ scale: 1.02 }}
      >
        <input
          type="text"
          placeholder="Describe your symptoms..."
          value={symptoms}
          onChange={(e) => setSymptoms(e.target.value)}
          className="w-full p-3 border rounded-2xl mb-2 focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
        <motion.button
          type="submit"
          className="bg-blue-500 text-white w-full px-4 py-2 rounded-2xl"
          whileHover={{ scale: 1.05 }}
        >
          Check Symptoms
        </motion.button>
      </motion.form>

      {response && (
        <p className="mt-4 text-lg text-green-600">🩺 Prediction: {response}</p>
      )}
      {followUp && (
        <p className="mt-2 text-yellow-600">❓ Follow-up: {followUp}</p>
      )}

      <motion.form
        onSubmit={handleFileUpload}
        className="mt-6"
        whileHover={{ scale: 1.02 }}
      >
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="w-full p-3 border rounded-2xl mb-2"
        />
        <motion.button
          type="submit"
          className="bg-green-500 text-white w-full px-4 py-2 rounded-2xl"
          whileHover={{ scale: 1.05 }}
        >
          Upload Report
        </motion.button>
      </motion.form>

      {reportData.Recommendations && (
        <motion.div
          className="mt-6 bg-gray-100 p-4 rounded-2xl"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.5 }}
        >
          <h3 className="text-lg font-bold">📄 Report Analysis:</h3>
          {Object.entries(reportData).map(
            ([key, value]) =>
              key !== "Recommendations" && (
                <p key={key}>
                  {key}: {value}
                </p>
              )
          )}
          <h4 className="font-semibold mt-2">📝 Recommendations:</h4>
          {reportData.Recommendations.map((rec, index) => (
            <p key={index}>➡️ {rec}</p>
          ))}
        </motion.div>
      )}
    </motion.div>
  );
}
