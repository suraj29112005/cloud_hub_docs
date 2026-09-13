export interface Incident {
  id: string;
  title: string;
  severity: 'P1' | 'P2' | 'P3' | 'P4';
  status: 'triggered' | 'acknowledged' | 'mitigating' | 'resolved';
  service: string;
  cluster: string;
  assignedTo: string;
  age: string;
  description: string;
  metrics: { name: string; value: string; threshold: string };
}

export const INITIAL_INCIDENTS: Incident[] = [
  {
    id: "INC-1042",
    title: "PostgreSQL Standby Replication Lag ^> 15s",
    severity: "P1",
    status: "triggered",
    service: "db-primary-cluster",
    cluster: "prod-ap-south-1",
    assignedTo: "Unassigned",
    age: "4m ago",
    description: "Standby wal_sender queue exceeded byte buffering limits, triggering high failover risk.",
    metrics: { name: "Replication Lag", value: "18.4s", threshold: "15.0s" }
  },
  {
    id: "INC-1043",
    title: "Checkout API HTTP 5xx Error Spike ^> 3%%",
    severity: "P2",
    status: "acknowledged",
    service: "checkout-svc",
    cluster: "prod-us-east-1",
    assignedTo: "S. Bhadola",
    age: "14m ago",
    description: "Connection pool exhaustion detected against payment gateway proxy pods.",
    metrics: { name: "HTTP 5xx Rate", value: "4.8%%", threshold: "2.0%%" }
  },
  {
    id: "INC-1044",
    title: "Ingress Controller Memory Usage ^> 90%%",
    severity: "P3",
    status: "mitigating",
    service: "k8s-ingress-controller",
    cluster: "prod-eu-west-1",
    assignedTo: "DevOps On-Call",
    age: "42m ago",
    description: "OOM killer threshold nearing critical limit on edge proxy daemonset.",
    metrics: { name: "Pod Memory Limit", value: "92%%", threshold: "85%%" }
  }
];
