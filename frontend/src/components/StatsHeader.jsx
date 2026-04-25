import { RefreshCw } from "lucide-react";
import { cn } from "@/lib/cn";

function formatTimestamp(date) {
  if (!date) return "—";
  const d = typeof date === "string" ? new Date(date) : date;
  if (Number.isNaN(d.getTime())) return "—";
  return d.toLocaleString(undefined, {
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

function Stat({ label, value, mono = true }) {
  return (
    <div className="flex flex-col">
      <span className="text-[10px] font-medium uppercase tracking-wider text-slate-500 dark:text-slate-400">
        {label}
      </span>
      <span
        className={cn(
          "text-lg font-semibold leading-tight text-slate-900 dark:text-slate-100",
          mono && "tabular-nums"
        )}
      >
        {value}
      </span>
    </div>
  );
}

export default function StatsHeader({
  totalRequests,
  totalBuckets,
  refreshedAt,
  loading,
  onRefresh,
}) {
  return (
    <div className="card flex flex-wrap items-center justify-between gap-4 px-5 py-3">
      <div className="flex flex-wrap items-center gap-x-8 gap-y-3">
        <h1 className="text-base font-semibold tracking-tight text-slate-900 dark:text-slate-50">
          HCP Unmet Needs
        </h1>
        <div className="flex flex-wrap items-center gap-x-8 gap-y-3">
          <Stat label="Total Requests" value={totalRequests ?? "—"} />
          <Stat label="Buckets" value={totalBuckets ?? "—"} />
          <Stat
            label="Refreshed"
            value={formatTimestamp(refreshedAt)}
            mono={false}
          />
        </div>
      </div>
      <button
        type="button"
        onClick={onRefresh}
        disabled={loading}
        className="inline-flex items-center gap-1.5 rounded-md bg-accent-600 px-3 py-1.5 text-xs font-semibold text-white shadow-sm transition hover:bg-accent-700 disabled:cursor-not-allowed disabled:opacity-60"
      >
        <RefreshCw
          className={cn("h-3.5 w-3.5", loading && "animate-spin")}
          aria-hidden
        />
        {loading ? "Refreshing…" : "Refresh"}
      </button>
    </div>
  );
}
