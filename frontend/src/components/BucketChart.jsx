import {
  Bar,
  BarChart,
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";

export default function BucketChart({ buckets, onBucketClick, highlightId }) {
  const data = [...buckets]
    .map((bucket) => ({
      id: bucket.bucket_name,
      name: bucket.bucket_name,
      count: bucket.count,
    }))
    .sort((a, b) => b.count - a.count);

  if (!data.length) return null;

  const chartHeight = Math.max(220, data.length * 36 + 40);

  return (
    <div className="card p-6">
      <div className="mb-4 flex items-baseline justify-between gap-3">
        <h2 className="text-base font-semibold text-slate-900 dark:text-slate-50">
          Requests by bucket
        </h2>
        <span className="text-xs text-slate-500 dark:text-slate-400">
          Click a bar to jump to that bucket
        </span>
      </div>
      <div style={{ width: "100%", height: chartHeight }}>
        <ResponsiveContainer>
          <BarChart
            data={data}
            layout="vertical"
            margin={{ top: 4, right: 24, left: 8, bottom: 4 }}
            onClick={(state) => {
              const payload = state?.activePayload?.[0]?.payload;
              if (payload?.id) onBucketClick?.(payload.id);
            }}
          >
            <CartesianGrid
              horizontal={false}
              strokeDasharray="3 3"
              stroke="currentColor"
              className="text-slate-200 dark:text-slate-800"
            />
            <XAxis
              type="number"
              allowDecimals={false}
              stroke="currentColor"
              className="text-slate-500 dark:text-slate-400"
              fontSize={12}
            />
            <YAxis
              type="category"
              dataKey="name"
              width={170}
              stroke="currentColor"
              className="text-slate-600 dark:text-slate-300"
              fontSize={12}
              tickLine={false}
              axisLine={false}
            />
            <Tooltip
              cursor={{ fill: "rgba(20,184,166,0.08)" }}
              contentStyle={{
                borderRadius: 8,
                border: "1px solid rgb(226 232 240)",
                fontSize: 12,
              }}
              formatter={(value) => [`${value} requests`, "Count"]}
            />
            <Bar
              dataKey="count"
              radius={[0, 6, 6, 0]}
              cursor="pointer"
              onClick={(entry) => onBucketClick?.(entry?.id)}
            >
              {data.map((entry) => (
                <Cell
                  key={entry.id}
                  fill={entry.id === highlightId ? "#0d9488" : "#14b8a6"}
                  fillOpacity={
                    !highlightId || entry.id === highlightId ? 1 : 0.55
                  }
                />
              ))}
            </Bar>
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
