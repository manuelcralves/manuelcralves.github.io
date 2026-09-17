---
title: liga-record-mcp
summary: An MCP server I built to learn the protocol, with fantasy football rules as tested code, judgement left to Claude and a read-only design.
order: 3
kind: Solo project
period: August to September 2026
stack: [Python, MCP, pytest, GitHub Actions]
links:
  - label: Code on GitHub
    href: https://github.com/manuelcralves/liga-record-mcp
---

## The problem

I wanted to learn how the Model Context Protocol works, so I built a server for a problem I actually have: managing my team in Liga Record, the fantasy football game of the Portuguese sports newspaper Record. Its rules are strict arithmetic (a budget, legal formations, automatic substitutions), while choosing who to start or sell is a judgement call.

## What I built

- A Python MCP server with 27 tools, 3 prompts for the weekly routine, and the regulation as a resource generated from the same constants the code enforces.
- The rulebook as pure functions with no network, files or clock, so it can be tested without touching the site.
- A read-only client for the public market and calendar. The site's buy and sell endpoints are known and deliberately not implemented, and a test keeps it that way.
- An `as_of` timestamp on every read, so Claude can tell stored data from live data.
- A points model, with a scheduled GitHub Action that records its predictions before every round and scores them afterwards.

## One hard decision

> **TODO(Manuel):** write this paragraph in your own words (3 to 5 sentences). The decision: deterministic rules live in code and judgement stays with Claude. Cover the alternative (putting the rulebook in the prompt and letting the model do the arithmetic), why you did not, and the related line you drew: the server reads but never buys or sells.

## Result

- The rulebook is tested without the network.
- A measured negative result: across two seasons, the hand-written estimator (correlation 0.5386 and 0.5505) beat a trained ridge regression (about 0.5355 and 0.5344), so the simpler model stayed.
- It is too early to say whether following the model pays off. The predictions recorded before each round will answer that over the season.
