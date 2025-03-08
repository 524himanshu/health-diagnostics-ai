import { useState } from 'react';

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [reportData, setReportData] = useState({});

  const handleFileUpload = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('file', file);

    try {
      const res = await fetch('https://health-diagnostics-ai.onrender.com/api/report', {
        method: 'POST',
        body: formData,
      });

      const data = await res.json();
      setReportData(data);
    } catch (error) {
      console.error('Failed to upload report:', error);
    }
  };

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center">📊 Health Reports Dashboard</h2>

      <form onSubmit={handleFileUpload} className="mb-4">
        <input
          type="file"
          onChange={(e) => setFile(e.target.files[0])}
          className="w-full p-3 border rounded-2xl mb-2"
        />
        <button
          type="submit"
          className="bg-blue-500 text-white w-full px-4 py-2 rounded-2xl"
        >
          Upload Report
        </button>
      </form>

      {reportData.Recommendations && (
        <div className="mt-6 bg-white p-4 rounded-2xl shadow-lg">
          <h3 className="text-lg font-bold">📄 Report Analysis:</h3>
          {Object.entries(reportData).map(([key, value]) =>
            key !== 'Recommendations' ? <p key={key}>{key}: {value}</p> : null
          )}
          <h4 className="font-semibold mt-2">📝 Recommendations:</h4>
          {reportData.Recommendations.map((rec, idx) => (
            <p key={idx}>➡️ {rec}</p>
          ))}
        </div>
      )}
    </div>
  );
}
