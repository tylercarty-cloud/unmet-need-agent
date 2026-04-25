import { useState } from "react";
import { ExternalLink, ChevronDown, ChevronUp } from "lucide-react";
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
    </li>
  );
}
