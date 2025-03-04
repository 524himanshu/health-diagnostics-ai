import { useState, useEffect } from 'react';

export default function Dashboard() {
  const [reports, setReports] = useState([]);

  useEffect(() => {
    const fetchReports = async () => {
      const res = await fetch('/api/reports?email=user@example.com');
      const data = await res.json();
      setReports(data);
    };
    fetchReports();
  }, []);

  return (
    <div className="p-4 max-w-2xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center">📊 Health Reports Dashboard</h2>
      {reports.length === 0 ? (
        <p>No reports available.</p>
      ) : (
        reports.map((report, index) => (
          <div key={index} className="bg-white p-4 rounded-2xl shadow-lg mb-4">
            <h3 className="text-lg font-bold">📝 Report {index + 1}</h3>
            {Object.entries(report.report).map(([key, value]) => (
              key !== 'Recommendations' && <p key={key}>{key}: {value}</p>
            ))}
            <h4 className="font-semibold mt-2">📝 Recommendations:</h4>
            {report.report.Recommendations.map((rec, idx) => (
              <p key={idx}>➡️ {rec}</p>
            ))}
          </div>
        ))
      )}
    </div>
  );
}
