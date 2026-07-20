There is an Apache-style access log at `/app/access.log`.

Parse every line and write a JSON object to `/app/report.json` containing exactly these three fields:

- `total_requests` — integer: total number of log lines
- `unique_ips` — integer: number of distinct client IP addresses
- `top_path` — string: the URL path that appears in the most requests

Example shape (values are illustrative):
```json
{"total_requests": 42, "unique_ips": 7, "top_path": "/index.html"}
```
