---
title: World Cup 2026 ML Predictor
summary: A live forecast of the 2026 World Cup, built on Elo ratings, a Poisson model and a million simulated tournaments.
order: 1
kind: Solo project
period: June to July 2026
stack: [Python, pandas, NumPy, SciPy, GitHub Actions, Supabase]
highlight:
  value: 71/104
  label: results called by the blind model
links:
  - label: Live site
    href: https://worldcup2026ml.pt
  - label: Code on GitHub
    href: https://github.com/manuelcralves/WORLD-CUP-2026
---

## The problem

The 2026 World Cup was the first with 48 teams and 104 matches. I wanted a forecast for every match and every team's chance of winning the title, one that stayed current during the tournament without manual work and that I could check honestly once it was over.

## What I built

- Elo ratings computed over 49,520 international matches since 1872, feeding a Dixon-Coles Poisson model of the goals each team scores.
- A Monte Carlo simulation that plays the tournament a million times, with FIFA tiebreakers, the official bracket and a penalty model fitted on 677 shootouts.
- Two versions of the forecast: a live one that updates with real results, and a blind one trained and tuned only on matches played before 11 June 2026.
- A GitHub Actions job that pulled new results every 2 hours during the tournament, re-ran the model and redeployed the site.
- "Beat the Machine", a prediction game with Google sign-in and Supabase, where people played against the model.

## One hard decision

> **TODO(Manuel):** write this paragraph in your own words (3 to 5 sentences). The decision: judge the forecast on the blind version, not the live one. Cover the alternative (the live version, which kept learning from real results and so always looked better), why you chose the blind one, and what it cost (when the blind model picked Argentina and Spain won, the site said so instead of claiming it had called the champion).

## Result

- The blind version called the result of 71 of the 104 matches (68%), with a ranked probability score of 0.153 against 0.229 for a naive baseline.
- Its four favourites were exactly the four semi-finalists. Spain, the champion, was its second pick at 18.3%, just behind Argentina at 18.5%.
- On 4,567 held-out matches from 2022 to June 2026, a model using only Elo scored the same RPS as the full model (0.17 against 0.23 for the baseline), and XGBoost only tied it.
- What did not work: the blind model was underconfident about favourites. When it gave a result between 50 and 60%, that result happened 75% of the time, across 28 calls. The tuning grid was also too narrow, with three of the four best parameters at its edge.
