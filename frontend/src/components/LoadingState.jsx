import { Loader2 } from "lucide-react";

export default function LoadingState() {
  return (
    <div className="space-y-8">
      <div className="card p-6">
        <div className="flex items-center gap-3 text-accent-600">
          <Loader2 className="h-5 w-5 animate-spin" />
          <span className="text-sm font-medium">
            Analyzing HCP feedback with Claude — this can take 10–30 seconds…
          </span>
        </div>
        <div className="mt-4 grid grid-cols-2 gap-4 sm:grid-cols-4">
          {Array.from({ length: 4 }).map((_, idx) => (
            <div key={idx} className="space-y-2">
              <div className="skeleton h-3 w-20" />
              <div className="skeleton h-7 w-16" />
            </div>
          ))}
        </div>
      </div>

      <div className="card p-6">
        <div className="skeleton mb-4 h-4 w-40" />
        <div className="space-y-3">
          {Array.from({ length: 6 }).map((_, idx) => (
            <div key={idx} className="flex items-center gap-3">
              <div className="skeleton h-4 w-32" />
              <div className="skeleton h-3 flex-1" />
            </div>
          ))}
        </div>
      </div>

      <div className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3">
        {Array.from({ length: 6 }).map((_, idx) => (
          <div key={idx} className="card p-5">
            <div className="skeleton mb-3 h-5 w-1/2" />
            <div className="skeleton mb-2 h-3 w-full" />
            <div className="skeleton mb-4 h-3 w-3/4" />
            <div className="skeleton h-9 w-24 rounded-full" />
          </div>
        ))}
      </div>
    </div>
  );
}
