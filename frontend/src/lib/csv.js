function escapeCell(value) {
  const str = value === null || value === undefined ? "" : String(value);
  if (/[",\n\r]/.test(str)) {
    return `"${str.replace(/"/g, '""')}"`;
  }
  return str;
}

export function bucketsToCsv(buckets) {
  const headers = [
    "bucket_name",
    "bucket_description",
    "first_name",
    "last_name",
    "npi",
    "date_time",
    "slack_channel",
    "slack_link",
    "pulse",
    "hcp_response",
  ];

  const rows = [headers.join(",")];
  for (const bucket of buckets) {
    for (const req of bucket.requests) {
      rows.push(
        [
          bucket.bucket_name,
          bucket.description,
          req.first_name,
          req.last_name,
          req.npi,
          req.date_time,
          req.slack_channel,
          req.slack_link,
          req.pulse,
          req.hcp_response,
        ]
          .map(escapeCell)
          .join(",")
      );
    }
  }
  return rows.join("\n");
}

export function downloadCsv(filename, csv) {
  const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
}
