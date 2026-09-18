---
title: Agents and Multi-Agent Systems
summary: Two team projects, with waste-collection agents that coordinate over XMPP and A2C, DQN and PPO agents compared on LunarLander.
order: 4
kind: Team of 3, FEUP course
period: February to June 2025
stack: [Python, SPADE, XMPP, Flask, Stable-Baselines3]
team: [Diogo Santos, Manuel Alves, Rodrigo Esteves]
highlight:
  value: '271'
  label: best mean reward on LunarLander
links:
  - label: Code on GitHub
    href: https://github.com/manuelcralves/FEUP-ASMA
---

Two team projects for the Agents and Multi-Agent Systems course at FEUP, University of Porto.

## Waste collection with agents

Bins fill at unpredictable rates, and a central dispatcher reacts slowly. We simulated 16 bins and a depot in Porto, where bins and trucks are SPADE agents that coordinate only through XMPP messages. A full bin asks every truck for a pickup, and a truck claims the nearest bin it still has room for and tells the other trucks to skip it. In our tests, going from 2 to 32 trucks raised the waste collected in 120 seconds from 160 to 1,580 units, but the average time a bin stayed full only fell from 98 to 68.5 seconds.

## Reinforcement learning on LunarLander

We trained A2C, DQN and PPO with Stable-Baselines3 for one million steps each, then two variants of each with changed hyperparameters. PPO with a higher learning rate and shorter rollouts scored a mean reward of 271 over 20 evaluation episodes, against 208 with the defaults (200 counts as solved), while four of the six variants ended with negative scores.

## What we would do differently

In the waste collection simulation, we would replace the greedy rule, where each truck goes to the nearest bin it has room for, with real route planning across all trucks, and we would have bins ask for a pickup before they are full, for example at 80%. On LunarLander, we would change one hyperparameter at a time and train each setup with several seeds, so we could tell what caused each difference and rule out luck.
