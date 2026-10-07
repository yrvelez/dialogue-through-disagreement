# Analysis plan (reconstructed post hoc — NOT pre-registered)

No pre-registration for this study was found. This plan was written on 2026-10-05, after data collection,
from the original analysis behind the published results (`replication_script.R`), so the pipeline can run.
Every analysis below is post hoc; "registered" tags in the report only mean "matches this reconstructed plan".

## Design

Online survey experiment on the CloudResearch panel, November 2023 (Columbia IRB AAAU8308). Respondents
first said whether the federal government should spend more or less on transportation and infrastructure
(`group`: `pro` = more, `anti` = less). They were then randomly assigned (`treatment`):

- `1` (Op-ed + chatbot): read an op-ed arguing against their position, then talked with a GPT-3.5-turbo
  chatbot prompted to elicit arguments for and against more spending. Pro-spending respondents read an
  anti-spending op-ed (Coppock, Ekins & Kirby 2018, on the 2015 Amtrak crash); anti-spending respondents
  read a pro-spending op-ed written with GPT for this study.
- `0` (Placebo + chatbot): read an unrelated placebo article, then talked with the same chatbot.

The order of the chatbot and the outcome questions was randomized; the order is not in the data.

## Sample and exclusions

- Keep respondents with a recorded assignment: `treatment` in 0, 1. Three respondents have no recorded
  assignment and are excluded.
- Complete cases on each outcome.

## Outcomes

- `toward_counterarg`: support for more spending (1–7) recoded so higher = closer to the op-ed's position
  (pro-spending respondents: 8 − strength; anti-spending respondents: strength).
- `certainty`: certainty in one's position (0–100).
- `counterarg_keyword`: 1 if the respondent's recall of arguments on the op-ed's side uses at least one
  keyword from the op-ed they were assigned (fixed keyword lists per op-ed).
- `supportive_keyword`: 1 if the respondent's recall of arguments for their own side uses an op-ed keyword.

## Hypotheses

- H1: Op-ed + chatbot changes `toward_counterarg` relative to placebo + chatbot (expected: higher).
- H2: Op-ed + chatbot changes `certainty` (expected: lower).
- H3: Op-ed + chatbot changes `counterarg_keyword` (expected: higher).
- H4: Op-ed + chatbot changes `supportive_keyword`.

## Heterogeneity

- S1: the H1 effect by prior position (`group`: pro-spending vs anti-spending), estimated within each group.

## Estimation

OLS of each outcome on the treatment indicator, HC2 robust standard errors, two-sided tests at α = 0.05, no
covariates, no multiple-testing correction.
