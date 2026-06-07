# GW2 API Navigation Guide

Use this guide to quickly locate the right documentation pages from API:Main.

## v2-First Section Map
- Achievements: achievement metadata and daily objectives.
- Authenticated: account-bound endpoints requiring API keys.
- Daily Rewards: dailycrafting, mapchests, worldbosses.
- Game Mechanics: professions, skills, traits, mounts, masteries, etc.
- Guild and Guild Authenticated: guild metadata and owner-key-gated guild state.
- Home Instance and Homestead: unlock collections and categories.
- Items: items, materials, recipes, skins, finishers, gliders, mail carriers.
- Map information: continents and maps.
- Miscellaneous: build, colors, currencies, files, raids, titles, worlds, etc.
- Story: backstory, stories, quests.
- Structured PvP: pvp seasons, ranks, heroes, leaderboards.
- Trading post: commerce exchange, listings, prices, transactions.
- Wizard's Vault: season, listings, objectives.
- World vs. World: abilities, guilds, matches, objectives, timers, upgrades.

## Lookup Heuristics
1. Start from API:Main and find the category that best matches the user intent.
2. Follow the exact API:2/<endpoint> wiki page for details.
3. If endpoint has path params like :id, verify parameter semantics on that endpoint page.
4. If endpoint seems account or guild sensitive, verify auth/scopes via API:API_key and endpoint notes.
5. If user asks "what changed" or "new endpoint", consult API:Changelog after API:Main.

## Authentication Cues
- Account, characters, tokeninfo, many commerce/pvp endpoints can require API keys.
- Prefer explicit statements from endpoint pages over assumptions.
- If uncertain, say docs are unclear and provide the link used.

## Version Handling
- Prefer API:2 for all normal guidance.
- Mention API:1 only if explicitly requested or for migration/deprecation context.
