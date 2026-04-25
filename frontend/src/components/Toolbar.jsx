import { Download, Search, ArrowDownWideNarrow, ArrowDownAZ } from "lucide-react";
import { cn } from "@/lib/cn";

export default function Toolbar({
  query,
  onQueryChange,
  sort,
  onSortChange,
  onExport,
  totalShown,
}) {
  return (
    <div className="card flex flex-col gap-3 p-4 sm:flex-row sm:items-center sm:justify-between">
      <div className="relative flex-1 sm:max-w-sm">
        <Search className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400" />
        <input
          type="search"
          value={query}
          onChange={(e) => onQueryChange(e.target.value)}
          placeholder="Search requests, names, NPIs…"
          className="w-full rounded-lg border border-slate-200 bg-white py-2 pl-9 pr-3 text-sm text-slate-900 shadow-sm placeholder:text-slate-400 focus:border-accent-500 focus:outline-none focus:ring-2 focus:ring-accent-500/30 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-100"
        />
      </div>
      <div className="flex flex-wrap items-center gap-2">
        <span className="hidden text-xs text-slate-500 sm:inline dark:text-slate-400">
          {totalShown} shown
        </span>
        <div className="flex overflow-hidden rounded-lg border border-slate-200 dark:border-slate-700">
          <button
            type="button"
            onClick={() => onSortChange("count")}
            className={cn(
              "inline-flex items-center gap-1.5 px-3 py-2 text-xs font-medium transition",
              sort === "count"
                ? "bg-accent-600 text-white"
                : "bg-white text-slate-700 hover:bg-slate-50 dark:bg-slate-900 dark:text-slate-200 dark:hover:bg-slate-800"
            )}
          >
            <ArrowDownWideNarrow className="h-3.5 w-3.5" />
            Count
          </button>
          <button
            type="button"
            onClick={() => onSortChange("alpha")}
            className={cn(
              "inline-flex items-center gap-1.5 px-3 py-2 text-xs font-medium transition",
              sort === "alpha"
                ? "bg-accent-600 text-white"
                : "bg-white text-slate-700 hover:bg-slate-50 dark:bg-slate-900 dark:text-slate-200 dark:hover:bg-slate-800"
            )}
          >
            <ArrowDownAZ className="h-3.5 w-3.5" />
            A–Z
          </button>
        </div>
        <button
          type="button"
          onClick={onExport}
          className="inline-flex items-center gap-1.5 rounded-lg border border-slate-200 bg-white px-3 py-2 text-xs font-medium text-slate-700 shadow-sm transition hover:bg-slate-50 dark:border-slate-700 dark:bg-slate-900 dark:text-slate-200 dark:hover:bg-slate-800"
        >
          <Download className="h-3.5 w-3.5" />
          Export CSV
        </button>
      </div>
    </div>
  );
}
