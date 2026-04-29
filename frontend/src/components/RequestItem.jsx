import { useState } from "react";
import {
  AlertTriangle,
  ChevronDown,
  ChevronUp,
  ExternalLink,
  Map,
} from "lucide-react";
import { cn } from "@/lib/cn";

const TRUNCATE_AT = 220;

function formatDate(value) {
  if (!value) return null;
  const d = new Date(value);
  if (Number.isNaN(d.getTime())) return value;
  return d.toLocaleString(undefined, {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
  });
}

export default function RequestItem({ request, query }) {
  const [expanded, setExpanded] = useState(false);
  const text = request.hcp_response || "";
  const isLong = text.length > TRUNCATE_AT;
  const visible = expanded || !isLong ? text : `${text.slice(0, TRUNCATE_AT)}…`;

  const fullName =
    [request.first_name, request.last_name].filter(Boolean).join(" ") ||
    "Unknown HCP";
  const date = formatDate(request.date_time);

  const highlight = (chunk) => {
    if (!query) return chunk;
    const lower = chunk.toLowerCase();
    const q = query.toLowerCase();
    const idx = lower.indexOf(q);
    if (idx === -1) return chunk;
    return (
      <>
        {chunk.slice(0, idx)}
        <mark className="rounded bg-yellow-200/70 px-0.5 dark:bg-yellow-500/30 dark:text-yellow-100">
          {chunk.slice(idx, idx + query.length)}
        </mark>
        {chunk.slice(idx + query.length)}
      </>
    );
  };

  return (
    <li className="rounded-lg border border-slate-200 bg-slate-50/60 p-3 transition hover:bg-slate-50 dark:border-slate-800 dark:bg-slate-900/60 dark:hover:bg-slate-900">
      <div className="flex flex-wrap items-baseline justify-between gap-x-3 gap-y-1">
        <div className="text-sm font-medium text-slate-900 dark:text-slate-100">
          {highlight(fullName)}
          {request.npi && (
            <span className="ml-2 text-xs font-normal text-slate-500 dark:text-slate-400">
              NPI ••{request.npi.slice(-4)}
            </span>
          )}
        </div>
        <div className="flex items-center gap-3 text-xs text-slate-500 dark:text-slate-400">
          {request.slack_channel && <span>{request.slack_channel}</span>}
          {date && <span>{date}</span>}
        </div>
      </div>

      <p
        className={cn(
          "mt-2 whitespace-pre-wrap text-sm leading-relaxed text-slate-700 dark:text-slate-200",
          "max-w-prose"
        )}
      >
        {highlight(visible)}
      </p>

      <div className="mt-2 flex items-center gap-3 text-xs">
        {isLong && (
          <button
            type="button"
            onClick={() => setExpanded((v) => !v)}
            className="inline-flex items-center gap-1 font-medium text-accent-700 hover:text-accent-800 dark:text-accent-300 dark:hover:text-accent-200"
          >
            {expanded ? (
              <>
                <ChevronUp className="h-3.5 w-3.5" />
                Show less
              </>
            ) : (
              <>
                <ChevronDown className="h-3.5 w-3.5" />
                Show more
              </>
            )}
          </button>
        )}
        {request.slack_link && (
          <a
            href={request.slack_link}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-1 font-medium text-accent-700 hover:text-accent-800 dark:text-accent-300 dark:hover:text-accent-200"
          >
            <ExternalLink className="h-3.5 w-3.5" />
            Open Slack post
          </a>
        )}
        {request.pulse && (
          <span className="rounded-full bg-slate-200/70 px-2 py-0.5 text-[11px] font-medium text-slate-700 dark:bg-slate-800 dark:text-slate-300">
            {request.pulse}
          </span>
        )}
      </div>

      <RoadmapAlignment request={request} />
    </li>
  );
}

const CLASSIFICATION_STYLES = {
  covered: {
    label: "Covered",
    container:
      "border-emerald-300/60 bg-emerald-50/70 text-emerald-900 dark:border-emerald-900/50 dark:bg-emerald-950/30 dark:text-emerald-100",
    pill:
      "bg-emerald-200/80 text-emerald-900 dark:bg-emerald-900/60 dark:text-emerald-100",
  },
  partial: {
    label: "Partial",
    container:
      "border-amber-300/60 bg-amber-50/70 text-amber-900 dark:border-amber-900/50 dark:bg-amber-950/30 dark:text-amber-100",
    pill:
      "bg-amber-200/80 text-amber-900 dark:bg-amber-900/60 dark:text-amber-100",
  },
  gap: {
    label: "Gap",
    container:
      "border-rose-300/60 bg-rose-50/70 text-rose-900 dark:border-rose-900/50 dark:bg-rose-950/30 dark:text-rose-100",
    pill:
      "bg-rose-200/80 text-rose-900 dark:bg-rose-900/60 dark:text-rose-100",
  },
};

const CONFIDENCE_STYLES = {
  high: "bg-slate-700/90 text-white dark:bg-slate-300 dark:text-slate-900",
  medium: "bg-slate-400/90 text-white dark:bg-slate-500 dark:text-slate-100",
  low: "bg-slate-300/90 text-slate-800 dark:bg-slate-700 dark:text-slate-200",
};

function RoadmapAlignment({ request }) {
  const alignments = request.roadmap_alignments || [];
  const classification = (request.roadmap_classification || "").toLowerCase();
  const confidence = (request.confidence || "").toLowerCase();
  const gapCategory = request.gap_category || "";
  const reasoning = request.roadmap_reasoning || "";

  // Nothing to show if no classification was produced AND no fallback flag.
  if (!classification && !alignments.length && !request.unaligned) return null;

  const style =
    CLASSIFICATION_STYLES[classification] || CLASSIFICATION_STYLES.gap;
  const isGap = classification === "gap" || (!classification && request.unaligned);

  return (
    <div
      className={`mt-2 space-y-1.5 rounded-md border px-2 py-1.5 text-xs ${style.container}`}
    >
      <div className="flex flex-wrap items-center gap-x-2 gap-y-1">
        {isGap ? (
          <AlertTriangle className="h-3.5 w-3.5" />
        ) : (
          <Map className="h-3.5 w-3.5" />
        )}
        <span
          className={`rounded-full px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide ${style.pill}`}
        >
          {style.label}
        </span>
        {confidence && (
          <span
            className={`rounded-full px-1.5 py-0.5 text-[10px] font-semibold uppercase tracking-wide ${
              CONFIDENCE_STYLES[confidence] || CONFIDENCE_STYLES.low
            }`}
          >
            {confidence} confidence
          </span>
        )}
        {gapCategory && (
          <span className="rounded-full bg-slate-200/70 px-1.5 py-0.5 text-[10px] font-medium uppercase tracking-wide text-slate-700 dark:bg-slate-800 dark:text-slate-300">
            {gapCategory}
          </span>
        )}
      </div>

      {reasoning && (
        <p className="text-[12px] leading-relaxed text-slate-700 dark:text-slate-300">
          {reasoning}
        </p>
      )}

      {alignments.length > 0 && (
        <ul className="space-y-1">
          {alignments.map((item) => (
            <li
              key={item.key}
              className="flex flex-wrap items-baseline gap-x-2 gap-y-0.5 rounded-md border border-slate-200 bg-white/70 px-2 py-1 text-xs dark:border-slate-700 dark:bg-slate-900/50"
            >
              <a
                href={item.url}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-flex items-center gap-1 font-mono font-medium text-accent-700 hover:underline dark:text-accent-300"
              >
                {item.key}
                <ExternalLink className="h-3 w-3" />
              </a>
              <span className="font-medium text-slate-800 dark:text-slate-100">
                {item.title}
              </span>
              {item.initiative && (
                <span className="rounded-full bg-slate-200/70 px-1.5 py-0.5 text-[10px] uppercase tracking-wide text-slate-700 dark:bg-slate-800 dark:text-slate-300">
                  {item.initiative}
                </span>
              )}
              {item.status && (
                <span className="text-[10px] uppercase tracking-wide text-slate-500 dark:text-slate-400">
                  {item.status}
                </span>
              )}
            </li>
          ))}
        </ul>
      )}

      {isGap && !reasoning && (
        <p className="text-[12px] text-slate-700 dark:text-slate-300">
          No roadmap item addresses this need.
        </p>
      )}
    </div>
  );
}
