---
name: gw2-api-doc-reader
description: 'Read Guild Wars 2 API documentation from the GW2 wiki. Use for GW2 API endpoint questions, authentication and API key scope questions, schema version behavior, endpoint discovery, and changelog-aware answers from API:Main and linked API:2 docs.'
argument-hint: 'Question about a GW2 API endpoint or API behavior'
user-invocable: true
---

# GW2 API Doc Reader

Use this skill to answer Guild Wars 2 API documentation questions by reading the live wiki docs.

## When to Use
- User asks what endpoint to use for GW2 data.
- User asks if an endpoint requires authentication or specific permissions.
- User asks about query parameters, schema version behavior, or endpoint structure.
- User asks for recent/new API additions.
- User asks for v1 vs v2 behavior.

## Source of Truth
- Primary index: https://wiki.guildwars2.com/wiki/API:Main
- Endpoint pages: https://wiki.guildwars2.com/wiki/API:2/<endpoint>
- Auth reference: https://wiki.guildwars2.com/wiki/API:API_key
- Changelog: https://wiki.guildwars2.com/wiki/API:Changelog

## Required Workflow
1. Open API:Main first to locate the endpoint family and canonical wiki links.
2. Open the exact endpoint page(s) needed to answer the question.
3. For authentication questions, verify with API:API_key and the endpoint page.
4. For schema/version questions, verify with API:2#Schemas and endpoint notes.
5. For "latest" or "new" questions, also check API:Changelog.
6. Provide a concise answer with links to the exact page(s) used.

## Answer Rules
- Default to v2 endpoints and terminology.
- Mention v1 only when the user explicitly asks, or when v1 context is necessary (deprecated/history).
- If wiki content appears stubbed, incomplete, or ambiguous, state that clearly.
- Do not invent endpoint behavior or fields not supported by docs.
- Prefer short, directly actionable answers.

Use [GW2 API Navigation Guide](./references/gw2-api-navigation.md) for endpoint lookup strategy.
Use [GW2 API Answer Template](./references/answer-template.md) for response structure.
