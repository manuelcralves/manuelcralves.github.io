---
title: CERN planning tool
summary: A planning tool for CERN's programmed stops, where an interactive Gantt editor and a CP-SAT optimiser work on the same reusable templates.
order: 2
kind: MSc thesis at CERN
period: September 2025 to July 2026
stack: [React, TypeScript, Material UI, Spring Boot, Oracle, Python, Flask, OR-Tools]
highlight:
  value: 74%
  label: of a real stop rebuilt from six templates
---

## The problem

CERN stops its accelerators every year to maintain and upgrade them. Planning one of these stops means sequencing several hundred interdependent tasks under tight time and resource limits, and every extra day of stoppage is expensive. The planning was still done largely by hand in Microsoft Project, which records a schedule but does not help you see how its constraints interact.

## What I built

This was my MSc thesis, built as an extension of CERN's Scheduling Tools platform. The tool is internal, so this page describes it without screenshots or code.

- A reusable template that captures the recurring structure of an intervention once and turns it into concrete plans with one action.
- An interactive Gantt chart in React and TypeScript, with a visual notation for tasks, their dependencies and their constraints.
- A Python service that models the plan for Google OR-Tools CP-SAT and minimises the length of the stop, putting working time and calendar time on the same scale.
- A review step that shows every change the optimiser proposes, so the coordinator can inspect, correct and commit it before exporting the plan back to Microsoft Project.

## One hard decision

I used the same template for both halves of the tool: it is what the coordinator edits and also the input the optimiser works on. Existing tools usually handle either the visual side or the optimisation, rarely both on the same model, and with two separate representations what the coordinator sees can drift from what the optimiser uses. The hard part was making one template serve both: simple enough for a coordinator to edit, yet complete enough for CP-SAT, with dependencies, calendars, holidays, and working time and calendar time on the same scale. The payoff is that the structure of a stop is captured once and reused across plans.

## Result

- Both the front-end and the optimisation service were merged into the platform the EN-ACE team uses, and the thesis was graded 19/20.
- In a usability study with 20 CERN members the tool scored 81.5 on the System Usability Scale, and planning coordinators judged the workflow an improvement over their current practice.
- The optimiser returned proven-optimal schedules at the size and dependency structure of a real stop.
- On a real Proton Synchrotron year-end stop, six templates covered 74% of the plan and the optimiser reproduced its duration exactly, in seconds. The order of the remaining tasks still depends on the coordinators' experience.
