import { useEffect, useMemo, useState } from "react";
import { AlertCircle } from "lucide-react";
import StatsHeader from "@/components/StatsHeader";
import BucketChart from "@/components/BucketChart";
import BucketGrid from "@/components/BucketGrid";
import LoadingState from "@/components/LoadingState";
import Toolbar from "@/components/Toolbar";
import { useBuckets } from "@/hooks/useBuckets";
import { bucketsToCsv, downloadCsv } from "@/lib/csv";

function filterBucket(bucket, query) {
  if (!query) return bucket;
  const q = query.toLowerCase();
  const requests = bucket.requests.filter((r) => {
    return [
      r.hcp_response,
      r.first_name,
      r.last_name,
      r.npi,
      r.slack_channel,
      r.pulse,
    ]
      .filter(Boolean)
      .some((v) => v.toLowerCase().includes(q));
  });
  return { ...bucket, requests, count: requests.length };
}

export default function App() {
  const { data, loading, error, refresh, refreshedAt } = useBuckets();
  const [highlightId, setHighlightId] = useState(null);
  const [sort, setSort] = useState("count");
  const [query, setQuery] = useState("");

  useEffect(() => {
    document.documentElement.classList.add("dark");
  }, []);

  const buckets = data?.buckets ?? [];

  const filteredAndSorted = useMemo(() => {
    let result = buckets.map((b) => filterBucket(b, query));
    if (query) result = result.filter((b) => b.count > 0);
    if (sort === "count") {
      result.sort((a, b) => b.count - a.count);
    } else {
      result.sort((a, b) => a.bucket_name.localeCompare(b.bucket_name));
    }
    return result;
  }, [buckets, query, sort]);

  const visibleRequestCount = useMemo(
    () => filteredAndSorted.reduce((acc, b) => acc + b.count, 0),
    [filteredAndSorted]
  );

  const handleBucketClick = (id) => {
    setHighlightId(id);
    const el = document.getElementById(`bucket-${encodeURIComponent(id)}`);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    window.setTimeout(() => setHighlightId(null), 2000);
  };

  const handleExport = () => {
    const csv = bucketsToCsv(filteredAndSorted);
    const stamp = new Date().toISOString().replace(/[:.]/g, "-");
    downloadCsv(`hcp-unmet-needs-${stamp}.csv`, csv);
  };

  return (
    <div className="min-h-full">
      <div className="mx-auto w-full max-w-7xl px-4 py-6 sm:px-6 lg:px-8 lg:py-10">
        <StatsHeader
          totalRequests={data?.total_requests}
          totalBuckets={buckets.length}
          refreshedAt={refreshedAt}
          loading={loading}
          onRefresh={refresh}
        />

        {error && (
          <div className="mt-6 flex items-start gap-3 rounded-xl border border-red-200 bg-red-50 p-4 text-sm text-red-800 dark:border-red-900/50 dark:bg-red-950/40 dark:text-red-200">
            <AlertCircle className="mt-0.5 h-5 w-5 shrink-0" />
            <div>
              <p className="font-medium">Could not load buckets</p>
              <p className="mt-0.5 text-red-700/90 dark:text-red-300/90">
                {error}
              </p>
              <button
                type="button"
                onClick={refresh}
                className="mt-2 inline-flex items-center gap-1.5 rounded-md border border-red-300 bg-white px-2.5 py-1 text-xs font-medium text-red-700 hover:bg-red-50 dark:border-red-900 dark:bg-red-950 dark:text-red-200"
              >
                Try again
              </button>
            </div>
          </div>
        )}

        <div className="mt-6 space-y-6">
          {loading && !data ? (
            <LoadingState />
          ) : (
            <>
              {buckets.length > 0 && (
                <BucketChart
                  buckets={buckets}
                  highlightId={highlightId}
                  onBucketClick={handleBucketClick}
                />
              )}

              <Toolbar
                query={query}
                onQueryChange={setQuery}
                sort={sort}
                onSortChange={setSort}
                onExport={handleExport}
                totalShown={visibleRequestCount}
              />

              <BucketGrid
                buckets={filteredAndSorted}
                highlightId={highlightId}
                query={query}
              />
            </>
          )}
        </div>

        <footer className="mt-12 border-t border-slate-200 pt-6 text-center text-xs text-slate-500 dark:border-slate-800 dark:text-slate-400">
          Internal tool · Impiricus HCP Unmet Needs · powered by Claude
        </footer>
      </div>
    </div>
  );
}
