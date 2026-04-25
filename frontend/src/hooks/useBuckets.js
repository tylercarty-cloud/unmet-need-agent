import { useCallback, useEffect, useState } from "react";
import { api } from "@/lib/api";

export function useBuckets() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [refreshedAt, setRefreshedAt] = useState(null);

  const refresh = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await api.getBuckets();
      setData(response);
      setRefreshedAt(new Date());
    } catch (err) {
      setError(err.message || "Failed to load buckets");
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    refresh();
  }, [refresh]);

  return { data, loading, error, refresh, refreshedAt };
}
