import BucketCard from "./BucketCard";

export default function BucketGrid({ buckets, highlightId, query }) {
  if (!buckets.length) {
    return (
      <div className="card p-10 text-center">
        <p className="text-sm font-medium text-slate-700 dark:text-slate-200">
          No buckets to display.
        </p>
        <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">
          Try clearing your filter or refreshing the data.
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
      {buckets.map((bucket) => (
        <BucketCard
          key={bucket.bucket_name}
          bucket={bucket}
          highlighted={highlightId === bucket.bucket_name}
          query={query}
        />
      ))}
    </div>
  );
}
