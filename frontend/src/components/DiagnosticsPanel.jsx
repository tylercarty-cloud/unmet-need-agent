import { useCallback, useEffect, useState } from "react";
import { AlertTriangle, CheckCircle2, ChevronDown, RefreshCw, XCircle } from "lucide-react";
import { api } from "@/lib/api";

function StatusPill({ ok, configured }) {
  if (!configured) {
    return (
      <span className="inline-flex items-center gap-1 rounded-full bg-slate-200 px-2 py-0.5 text-xs font-medium text-slate-700 dark:bg-slate-800 dark:text-slate-300">
        <AlertTriangle className="h-3 w-3" /> Not configured
      </span>
    );
  }
  if (ok) {
    return (
      <span className="inline-flex items-center gap-1 rounded-full bg-emerald-100 px-2 py-0.5 text-xs font-medium text-emerald-800 dark:bg-emerald-950 dark:text-emerald-200">
        <CheckCircle2 className="h-3 w-3" /> OK
      </span>
    );
  }
  return (
    <span className="inline-flex items-center gap-1 rounded-full bg-red-100 px-2 py-0.5 text-xs font-medium text-red-800 dark:bg-red-950 dark:text-red-200">
      <XCircle className="h-3 w-3" /> Error
    </span>
  );
}

function Row({ label, value }) {
  if (value === undefined || value === null || value === "") return null;
  return (
    <div className="flex justify-between gap-4 py-0.5 text-xs">
      <span className="text-slate-500 dark:text-slate-400">{label}</span>
      <span className="break-all text-right font-mono text-slate-700 dark:text-slate-300">
        {String(value)}
      </span>
    </div>
  );
}

function Section({ title, info, children }) {
  const ok = !!info?.ok;
  const configured = info?.configured ?? false;
  return (
    <div className="rounded-lg border border-slate-200 bg-white p-3 dark:border-slate-800 dark:bg-slate-950">
      <div className="flex items-center justify-between">
        <h3 className="text-sm font-semibold text-slate-800 dark:text-slate-100">
          {title}
        </h3>
        <StatusPill ok={ok} configured={configured} />
      </div>
      {info?.error && (
        <p className="mt-2 rounded-md bg-red-50 px-2 py-1.5 text-xs text-red-800 dark:bg-red-950/50 dark:text-red-200">
          {info.error}
        </p>
      )}
      <div className="mt-2 space-y-0">{children}</div>
    </div>
  );
}

export default function DiagnosticsPanel() {
  const [open, setOpen] = useState(false);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchDiagnostics = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await api.getDiagnostics();
      setData(result);
    } catch (err) {
      setError(err.message || "Failed to fetch diagnostics");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchDiagnostics();
  }, [fetchDiagnostics]);

  const anyBroken =
    data &&
    [data.anthropic, data.sheets, data.slack, data.roadmap].some(
      (s) => s && s.configured && !s.ok
    );
  const anyUnconfigured =
    data && data.slack && !data.slack.configured;

  const headerColor = anyBroken
    ? "border-red-300 bg-red-50 text-red-900 dark:border-red-900 dark:bg-red-950/40 dark:text-red-100"
    : anyUnconfigured
    ? "border-amber-300 bg-amber-50 text-amber-900 dark:border-amber-900 dark:bg-amber-950/40 dark:text-amber-100"
    : "border-slate-200 bg-white text-slate-700 dark:border-slate-800 dark:bg-slate-950 dark:text-slate-200";

  const summary = !data
    ? loading
      ? "Checking integrations…"
      : error || "Diagnostics unavailable"
    : anyBroken
    ? "One or more integrations are broken"
    : anyUnconfigured
    ? "Slack integration is not configured"
    : "All integrations healthy";

  return (
    <div className={`mt-4 rounded-xl border ${headerColor}`}>
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="flex w-full items-center justify-between gap-3 px-4 py-2.5 text-left text-sm font-medium"
      >
        <span className="flex items-center gap-2">
          {anyBroken ? (
            <XCircle className="h-4 w-4" />
          ) : anyUnconfigured ? (
            <AlertTriangle className="h-4 w-4" />
          ) : (
            <CheckCircle2 className="h-4 w-4" />
          )}
          Diagnostics — {summary}
        </span>
        <span className="flex items-center gap-2">
          <button
            type="button"
            onClick={(e) => {
              e.stopPropagation();
              fetchDiagnostics();
            }}
            className="inline-flex items-center gap-1 rounded-md border border-slate-300 bg-white px-2 py-0.5 text-xs font-medium text-slate-700 hover:bg-slate-50 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200"
          >
            <RefreshCw className={`h-3 w-3 ${loading ? "animate-spin" : ""}`} />
            Recheck
          </button>
          <ChevronDown
            className={`h-4 w-4 transition-transform ${open ? "rotate-180" : ""}`}
          />
        </span>
      </button>

      {open && (
        <div className="space-y-3 border-t border-slate-200 px-4 py-3 dark:border-slate-800">
          {error && (
            <p className="rounded-md bg-red-50 px-2 py-1.5 text-xs text-red-800 dark:bg-red-950/50 dark:text-red-200">
              {error}
            </p>
          )}
          {data && (
            <>
              <Section title="Anthropic (Claude)" info={data.anthropic}>
                <Row label="Model" value={data.anthropic?.model} />
                <Row label="API key" value={data.anthropic?.key_preview} />
              </Section>

              <Section title="Google Sheets" info={data.sheets}>
                <Row
                  label="Spreadsheet ID"
                  value={data.sheets?.spreadsheet_id_preview}
                />
                <Row label="Range" value={data.sheets?.range} />
                <Row
                  label="Credentials path"
                  value={data.sheets?.credentials_path}
                />
                <Row
                  label="Credentials present"
                  value={data.sheets?.credentials_present ? "yes" : "no"}
                />
              </Section>

              <Section title="Roadmap (alignment)" info={data.roadmap}>
                <Row label="Path" value={data.roadmap?.path} />
                <Row label="Items parsed" value={data.roadmap?.items} />
                <Row label="Initiatives" value={data.roadmap?.initiatives} />
              </Section>

              <Section title="Slack" info={data.slack}>
                <Row label="Channel ID" value={data.slack?.channel_id} />
                <Row label="Channel name" value={data.slack?.channel_name} />
                <Row label="Bot user ID" value={data.slack?.bot_user_id} />
                <Row label="Team" value={data.slack?.team} />
                <Row label="Token preview" value={data.slack?.token_preview} />
                <Row
                  label="Token format OK"
                  value={data.slack?.token_format_ok ? "yes" : "no"}
                />
                <Row
                  label="Publishing"
                  value={data.slack?.publish_enabled ? "enabled" : "disabled"}
                />
              </Section>

              <p className="text-[10px] text-slate-500 dark:text-slate-500">
                Last checked: {data.checked_at}
              </p>
            </>
          )}
        </div>
      )}
    </div>
  );
}
