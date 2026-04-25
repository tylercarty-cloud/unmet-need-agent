import { useEffect, useRef, useState } from "react";
import { ChevronDown } from "lucide-react";
import { cn } from "@/lib/cn";
import RequestItem from "./RequestItem";

export default function BucketCard({ bucket, highlighted, query }) {
  const [open, setOpen] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    if (highlighted && ref.current) {
      ref.current.scrollIntoView({ behavior: "smooth", block: "start" });
      setOpen(true);
    }
  }, [highlighted]);

  return (
    <article
      ref={ref}
      id={`bucket-${encodeURIComponent(bucket.bucket_name)}`}
      className={cn(
        "card card-hover flex flex-col p-5 transition",
        highlighted &&
          "ring-2 ring-accent-500 ring-offset-2 ring-offset-slate-50 dark:ring-offset-slate-950"
      )}
    >
      <header className="flex items-start justify-between gap-3">
        <h3 className="text-base font-semibold leading-snug text-slate-900 dark:text-slate-50">
          {bucket.bucket_name}
        </h3>
        <span className="inline-flex shrink-0 items-center rounded-full bg-accent-50 px-2.5 py-1 text-xs font-semibold text-accent-700 ring-1 ring-inset ring-accent-200 dark:bg-accent-900/40 dark:text-accent-200 dark:ring-accent-800">
          {bucket.count} {bucket.count === 1 ? "request" : "requests"}
        </span>
      </header>

      {bucket.description && (
        <p className="mt-2 text-sm leading-relaxed text-slate-600 dark:text-slate-400">
          {bucket.description}
        </p>
      )}

      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="mt-4 inline-flex items-center justify-between gap-2 rounded-lg border border-slate-200 px-3 py-2 text-sm font-medium text-slate-700 transition hover:bg-slate-50 dark:border-slate-800 dark:text-slate-200 dark:hover:bg-slate-800/60"
        aria-expanded={open}
      >
        <span>{open ? "Hide requests" : "View requests"}</span>
        <ChevronDown
          className={cn(
            "h-4 w-4 transition-transform",
            open && "rotate-180"
          )}
        />
      </button>

      {open && (
        <ul className="mt-3 flex flex-col gap-2">
          {bucket.requests.map((request, idx) => (
            <RequestItem
              key={`${request.npi || "anon"}-${idx}`}
              request={request}
              query={query}
            />
          ))}
        </ul>
      )}
    </article>
  );
}
