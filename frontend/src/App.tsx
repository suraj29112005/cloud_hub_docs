import React, { useState, useEffect } from "react";

export default function App() {
  const [view, setView] = useState<"landing" | "dashboard" | "detail">("dashboard");
  const [backendStatus, setBackendStatus] = useState<string>("Connecting...");

  useEffect(() => {
    const checkBackend = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/");
        if (!res.ok) throw new Error("HTTP status " + res.status);
        setBackendStatus("Connected (200 OK)");
      } catch (err) {
        console.warn("Backend not reachable yet:", err);
        setBackendStatus("Offline / Reconnecting");
      }
    };
    checkBackend();
  }, []);

  return (
    <div style={{ fontFamily: "system-ui, sans-serif", minHeight: "100vh", background: "#0b0f19", color: "#f1f5f9", padding: "24px" }}>
      <header style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid #1e293b", paddingBottom: "16px" }}>
        <div>
          <h1 style={{ margin: 0, fontSize: "20px", color: "#38bdf8" }}>CloudTrace Incident Hub</h1>
          <p style={{ margin: "4px 0 0", fontSize: "13px", color: "#94a3b8" }}>Full-Stack Incident & Telemetry Tracker</p>
        </div>
        <span style={{ fontSize: "12px", padding: "6px 12px", borderRadius: "20px", fontWeight: 600, background: backendStatus.includes("Connected") ? "#065f46" : "#7f1d1d", color: backendStatus.includes("Connected") ? "#34d399" : "#f87171" }}>
          API: {backendStatus}
        </span>
      </header>
      <nav style={{ display: "flex", gap: "8px", margin: "20px 0" }}>
        {( ["landing", "dashboard", "detail"] as const).map(tab => (
          <button key={tab} onClick={() => setView(tab)} style={{ padding: "8px 16px", borderRadius: "6px", border: "1px solid #334155", cursor: "pointer", textTransform: "capitalize", background: view === tab ? "#0284c7" : "#1e293b", color: "#ffffff", fontWeight: view === tab ? 600 : 400 }}>
            {tab}
          </button>
        ))}
      </nav>
      <main style={{ background: "#111827", border: "1px solid #1f2937", borderRadius: "8px", padding: "20px" }}>
        {view === "landing" && <div><h2 style={{ marginTop: 0 }}>System Overview</h2><p>Welcome to CloudTrace. Operational telemetry and alerts dashboard.</p></div>}
        {view === "dashboard" && <div><h2 style={{ marginTop: 0 }}>Active Incident Dashboard</h2><p>Real-time database latency and service status logs.</p></div>}
        {view === "detail" && <div><h2 style={{ marginTop: 0 }}>Incident Detail View</h2><p>Root-cause diagnostics and remediation history.</p></div>}
      </main>
    </div>
  );
}
