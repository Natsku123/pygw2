# GW2 API Answer Template

Use this structure for endpoint questions.

## Endpoint Summary
- Endpoint: API:2/<endpoint>
- Purpose: One sentence on returned data.
- Auth: Required/Not required/Depends (+ key scope note if documented).

## Request Shape
- Method: Usually GET (state if docs indicate otherwise).
- Key params: ids, id, page, page_size, lang, v, access_token (only if relevant).
- Path params: mention any required path segments like :id.

## Response Notes
- Important fields: only fields documented on the endpoint page.
- Schema/version notes: include v parameter guidance only when relevant.
- Caveats: stubs, deprecations, or ambiguous docs.

## Sources
- API:Main link used for discovery.
- Exact endpoint page link(s) used.
- Optional: API:API_key or API:Changelog if those were consulted.

## Style Rules
- Be concise and practical.
- Avoid speculation.
- Prefer v2 guidance unless user explicitly requests v1.
