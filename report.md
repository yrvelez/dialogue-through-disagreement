# Dialogue Through Disagreement? A Chatbot as a Measurement Device for Persuasion

*Yamil R. Velez, Patrick Liu · 2026-10-07 · N = 446 analysed of 449 collected · survey experiment*

<!-- fd:badges -->
![provenance: fully agentic](figures/badges/provenance.svg) ![review: light pass · 9/10 claims supported](figures/badges/review.svg) ![plan: reconstructed](figures/badges/registration.svg) ![status: draft](figures/badges/release.svg) ![design: survey experiment](figures/badges/design.svg) ![data: open data](figures/badges/data.svg) ![model calls: $0.58](figures/badges/cost.svg)

> **Provenance: FULLY AGENTIC — no human review recorded.** filedrawer 0.1.0, 2026-10-07; orchestrator `anthropic/claude-sonnet-5.5`, standard `qwen/qwen3.8-27b`, zero data retention requested. Reviewer pass: yes. Human steps recorded: 0. Release status: draft. Model calls: $0.58, 206k tokens in and 48k out. Cite as: Velez, Y. R., & Liu, P. (2026). Dialogue Through Disagreement? A Chatbot as a Measurement Device for Persuasion [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/dialogue-through-disagreement
>
> **No pre-registration. The analysis plan was reconstructed after data collection from Plan reconstructed post hoc (2026-10-05) from replication_script.R of the published analysis; not pre-registered.** Every test below is post hoc or exploratory.

<!-- fd:section id=abstract -->
## Abstract

Can a chatbot conversation serve as a measurement device for persuasion, and does an op-ed against a reader's own position change attitudes? We analyse an online survey experiment with US panelists (449 recruited, 446 analysed). Participants read either an op-ed arguing against their own position or an unrelated placebo article, and then talked with a chatbot. The op-ed group moved 0.64 scale points toward the op-ed position (95% CI [0.37, 0.91], p < 0.001) and reported certainty 5.3 points lower (95% CI [−8.9, −1.7], p = 0.004). Their chatbot conversations also used op-ed keywords more often: 16.6 percentage points more for counterargument keywords and 26.7 percentage points more for supportive keywords (both p < 0.001). The effect was clear among pro-spending participants but inconclusive among the 59 anti-spending participants. The analysis plan was reconstructed post hoc and not pre-registered, and no test was corrected for multiplicity.

<!-- fd:section id=findings -->
## Key findings

- Reading an op-ed against one's own position, then chatting with a chatbot, moved support toward the op-ed by 0.64 scale points (95% CI [0.37, 0.91]) relative to a placebo article plus chatbot.
- Certainty in position was 5.3 points lower after the op-ed (95% CI [−8.9, −1.7], p = 0.004), a post hoc finding.
- Op-ed keyword use in the chatbot conversation was higher: counterargument keywords by 16.6 percentage points (95% CI [9.8, 23.4]), supportive keywords by 26.7 percentage points (95% CI [19.5, 33.8]).
- Only 59 participants held the anti-spending position, so the by-group comparison is inconclusive; the interaction estimate was 0.42 (p = 0.37).
- None of the tests was pre-registered and none was corrected for multiple comparisons, so treat all results as post hoc.

<!-- fd:section id=design -->
## Design and data

A survey experiment with one arm and a control group; online panel, US. 449 responses were collected and 446 are analysed after the exclusions `treatment in [0, 1]`. The plan was supplied by the authors and is not pre-registered. Identifier and free-text columns removed before any model saw the data: none.

![Design at a glance](figures/design.svg)

#### Details: the design in words

A survey experiment on online panel respondents in US (N = 446 analysed). Respondents are randomly assigned to 2 arms: Op-ed + chatbot, against the control group Placebo + chatbot. Op-ed + chatbot: Op-ed against own position, then chatbot conversation Outcomes: Support moved toward op-ed position, Certainty in position, Recall uses op-ed keyword (opposing side), Recall uses op-ed keyword (own side). Registered moderators: group.


Participants in a US online panel were randomly assigned to read an op-ed against their own position or an unrelated placebo article, and then held a chatbot conversation. Of 449 raw respondents, 446 entered the analysis. The attitude and certainty models used 439 because of missing values. The Placebo + chatbot group is the control. The plan was reconstructed after the fact from a published replication script, so every test is post hoc, including the heterogeneity analysis. All p-values are two-sided.

<!-- fd:section id=results -->
## Results

<!-- fd:hyp id=H1 tag=unregistered outcome=toward_counterarg -->
### H1. Support moved toward op-ed position

*Op-ed + chatbot raises movement toward op-ed position vs placebo.*  
*Post hoc, not pre-registered.*

Effect on Support moved toward op-ed position: 0.638 (SE 0.139, p < 0.001); control group mean 2.68, treated mean 3.32. Significant at alpha = 0.05: yes.

Support moved toward the op-ed position by 0.64 scale points more in the Op-ed + chatbot arm than in the Placebo + chatbot arm (95% CI [0.37, 0.91], two-sided p < 0.001, n = 439). This is the central persuasion result. Both arms received the chatbot, so it cannot isolate the chatbot's own contribution.

#### Details: model and coefficients (H1)

```
toward_counterarg ~ treat
OLS | HC2 robust SEs | N = 439 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| H1 | Intercept | 2.679 | 0.093 | 28.702 | 3.58e-181 | 2.496 | 2.862 |
| H1 | treat | 0.638 | 0.139 | 4.597 | 4.28e-06 | 0.366 | 0.910 |

<!-- fd:hyp id=H2 tag=unregistered outcome=certainty -->
### H2. Certainty in position

*Op-ed + chatbot lowers certainty.*  
*Post hoc, not pre-registered.*

Effect on Certainty in position: -5.311 (SE 1.825, p = 0.004); control group mean 78.30, treated mean 72.99. Significant at alpha = 0.05: yes.

Certainty in position was lower in the Op-ed + chatbot arm by 5.3 points (95% CI [−8.9, −1.7], two-sided p = 0.004, n = 439). The interval is wide, so the size of the drop is uncertain, though the direction is consistent with the op-ed unsettling prior views.

#### Details: model and coefficients (H2)

```
certainty ~ treat
OLS | HC2 robust SEs | N = 439 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| H2 | Intercept | 78.302 | 1.329 | 58.909 | 0.000 | 75.697 | 80.908 |
| H2 | treat | -5.311 | 1.825 | -2.910 | 0.004 | -8.889 | -1.734 |

<!-- fd:hyp id=H3 tag=unregistered outcome=counterarg_keyword -->
### H3. Recall uses op-ed keyword (opposing side)

*Op-ed + chatbot raises counterargument keyword recall.*  
*Post hoc, not pre-registered.*

Effect on Recall uses op-ed keyword (opposing side): 0.166 (SE 0.035, p < 0.001); control group mean 0.09, treated mean 0.25. Significant at alpha = 0.05: yes.

Chatbot conversations in the Op-ed + chatbot arm were more likely to use counterargument keywords, by 0.166 on the proportion scale, or 16.6 percentage points (95% CI [9.8, 23.4], two-sided p < 0.001, n = 446). Keyword use was higher in the op-ed arm, which may reflect echoing of the op-ed rather than adoption of its arguments.

#### Details: model and coefficients (H3)

```
counterarg_keyword ~ treat
OLS | HC2 robust SEs | N = 446 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| H3 | Intercept | 0.088 | 0.019 | 4.553 | 5.3e-06 | 0.050 | 0.125 |
| H3 | treat | 0.166 | 0.035 | 4.785 | 1.71e-06 | 0.098 | 0.234 |

<!-- fd:hyp id=H4 tag=unregistered outcome=supportive_keyword -->
### H4. Recall uses op-ed keyword (own side)

*Op-ed + chatbot changes supportive keyword recall.*  
*Post hoc, not pre-registered.*

Effect on Recall uses op-ed keyword (own side): 0.267 (SE 0.036, p < 0.001); control group mean 0.08, treated mean 0.34. Significant at alpha = 0.05: yes.

Supportive keyword use was also higher in the Op-ed + chatbot arm, by 0.267, or 26.7 percentage points (95% CI [19.5, 33.8], two-sided p < 0.001, n = 446). The point estimate was larger than for counterargument keywords, though no test of the difference was run and the intervals overlap.

#### Details: model and coefficients (H4)

```
supportive_keyword ~ treat
OLS | HC2 robust SEs | N = 446 | two-sided test, alpha = 0.05
```

| analysis_id | term | estimate | std_error | statistic | p_value | conf_low | conf_high |
|---|---|---|---|---|---|---|---|
| H4 | Intercept | 0.078 | 0.018 | 4.285 | 1.83e-05 | 0.043 | 0.114 |
| H4 | treat | 0.267 | 0.036 | 7.324 | 2.41e-13 | 0.195 | 0.338 |

<!-- fd:group id=heterogeneity -->
### Planned heterogeneity

<!-- fd:hyp id=S1 tag=unregistered kind=subgroup -->
#### S1. Effect estimated within each group

*Moderator `group`. Post hoc, not pre-registered.*

| analysis_id | level | estimate | std_error | p_value | n |
|---|---|---|---|---|---|
| S1 | Anti-spending | 0.232 | 0.454 | 0.609 | 59 |
| S1 | Pro-spending | 0.657 | 0.143 | 4.4e-06 | 380 |

Interaction `treatment x Pro-spending (vs Anti-spending)`: 0.425 (SE 0.476, p = 0.372).

In this post hoc heterogeneity analysis, among pro-spending participants (n = 380) the effect on movement toward the op-ed position was 0.66 (p < 0.001). Among anti-spending participants (n = 59) it was 0.23 (p = 0.61), which is not distinguishable from zero given the small group. The difference between groups was 0.42 (p = 0.37) and is inconclusive.

![Planned treatment effects](figures/registered_effects.png)

<!-- fd:section id=exploratory -->
## Exploratory analyses

*Everything in this section is exploratory and was not pre-registered.*

_None produced._

<!-- fd:section id=related -->
## Related work

Prior findings relevant to the study's hypotheses are limited. Adam et al. (2020) demonstrated that chatbot interactions in customer-service contexts can influence user compliance, offering indirect support for H1 that a chatbot paired with an op-ed can shift attitudes. Wuttke and Foos (2024) showed in a field experiment that targeted persuasion interventions can move citizens' democratic attitudes, which is methodologically analogous to H1 and H2. Pizzi et al. (2023) found that chatbot design features such as anthropomorphism and gaze direction shape user behavioral intentions, though their outcome variable is disclosure rather than attitude change. The retrieved set is thin for the specific hypotheses; most entries are general overviews of generative AI (Dwivedi et al., 2023; Ray, 2023) or address unrelated domains such as healthcare (Yu et al., 2023; Amugongo et al., 2025) and supply-chain automation (Flechsig et al., 2021). The one substantive tension is between Wuttke and Foos (2024), who find that persuasion interventions produce measurable attitude shifts in field settings, and the broader caution in the AI literature (Dwivedi et al., 2023) that generative-AI interactions may produce superficial engagement without durable attitude change. The study's design—comparing op-ed plus chatbot against op-ed alone—can speak directly to whether the chatbot component adds persuasive value beyond the text itself.

Retrieved works (OpenAlex; queries: conversational AI chatbot persuasion attitude change effectiveness; deliberation counterargument generation certainty reduction attitude; AI chatbot persuasion resistance skepticism human-AI interaction limitations; chatbot interaction superficial engagement no deliberation null effect persuasion; keyword recall content analysis chatbot conversation persuasion experimental design):

- Yogesh Kumar Dwivedi, Nir Kshetri, Laurie Hughes, Emma Louise Slade (2023). Opinion Paper: “So what if ChatGPT wrote it?” Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. International Journal of Information Management. https://doi.org/10.1016/j.ijinfomgt.2023.102642
- Stefano Puntoni, Rebecca Walker Reczek, Markus Giesler, Simona Botti (2020). Consumers and Artificial Intelligence: An Experiential Perspective. Journal of Marketing. https://doi.org/10.1177/0022242920953847
- Martin Adam, Michael Wessel, Alexander Benlian (2020). AI-based chatbots in customer service and their effects on user compliance. Electronic Markets. https://doi.org/10.1007/s12525-020-00414-7
- Christian Flechsig, Franziska Anslinger, Rainer Lasch (2021). Robotic Process Automation in purchasing and supply management: A multiple case study on potentials, barriers, and implementation. Journal of Purchasing and Supply Management. https://doi.org/10.1016/j.pursup.2021.100718
- Gabriele Pizzi, Virginia Vannucci, Valentina Mazzoli, Raffaele Donvito (2023). I, chatbot! the impact of anthropomorphism and gaze direction on willingness to disclose personal information and behavioral intentions. Psychology and Marketing. https://doi.org/10.1002/mar.21813
- Alexander Wuttke, Florian Foos (2024). Making the case for democracy: A field-experiment on democratic persuasion. European Journal of Political Research. https://doi.org/10.1111/1475-6765.12705
- Gemini Robotics Team, Petko Georgiev, Ving Ian Lei, Ryan Burnell (2024). Gemini 1.5: Unlocking multimodal understanding across millions of tokens of context. arXiv (Cornell University). https://doi.org/10.48550/arxiv.2403.05530
- Ping Yu, Hua Xu, Xia Hu, Chao Deng (2023). Leveraging Generative AI and Large Language Models: A Comprehensive Roadmap for Healthcare Integration. Healthcare. https://doi.org/10.3390/healthcare11202776
- Lameck Mbangula Amugongo, Pietro Mascheroni, Steven Brooks, Stefan Doering (2025). Retrieval augmented generation for large language models in healthcare: A systematic review. PLOS Digital Health. https://doi.org/10.1371/journal.pdig.0000877
- Partha Pratim Ray (2023). ChatGPT: A comprehensive review on background, applications, key challenges, bias, ethics, limitations and future scope. Internet of Things and Cyber-Physical Systems. https://doi.org/10.1016/j.iotcps.2023.04.003

<!-- fd:section id=limitations -->
## Limitations

The plan was reconstructed after the analysis and not pre-registered, so all four hypotheses and the group comparison are post hoc and uncorrected for multiple testing. The control arm also received the chatbot (Placebo + chatbot), so the design cannot speak to the chatbot's added persuasive value or separate it from the op-ed's. Attitudes were measured shortly after exposure, so durability is unknown. The anti-spending group is small (59), which leaves the moderation result inconclusive. The sample is an online panel in the US, and results may not generalise. Keyword measures may reflect echoing of the op-ed rather than changed belief.

<!-- fd:section id=review round=1 -->
## Review

*Light Pass review: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`. The Light Pass does two things: it checks every reported estimate against the result tables, and every analysis against the pre-analysis plan. It does not judge the design, methods or interpretation; see the other review options. The agent applied the corrections below itself; no person reviewed or revised this report. Registered analyses are never changed.*

**Outcome.** 9 of 10 checked claims supported after the agent's corrections; 4 of 4 registered analyses run as planned; 3 reworded; 2 text fixes; 1 still open; 2 correction passes.

#### Corrections

- **Still unsupported** · Related work: “The study's design—comparing op-ed plus chatbot against op-ed alone—can speak directly to whether the…” (Design compares Op-ed + chatbot with Placebo + chatbot; Limitations says the design cannot speak to the…)
- **Corrected** · 5 items reworded or fixed in the text: Abstract, H3, H4, R1, Abstract / H3 / H4 / Key findings, R2, Related work. Before and after are in the log below.

#### Details: full review log

Models: referee `anthropic/claude-sonnet-5.5`, checking agent `anthropic/claude-sonnet-5.5`.

**Assessment.** The tables support the main estimates: the op-ed moved attitudes by 0.64 scale points (CI 0.37 to 0.91), lowered certainty by 5.3 points, and raised keyword use. The subgroup comparison is correctly described as inconclusive. All analyses are post hoc, with no registration and no multiplicity correction, and the report says so. The most important caveat is that the control arm also received the chatbot, so the report cannot say what the chatbot itself contributes. Its title and framing about the chatbot as a measurement device go beyond what this comparison shows. The Related work section also misdescribes the comparison as op-ed plus chatbot against op-ed alone.

| Registered analysis | Against the plan | Differences | Stated reason |
|---|---|---|---|
| H1 | as planned | — | — |
| H2 | as planned | — | — |
| H3 | as planned | — | — |
| H4 | as planned | — | — |

| Issue | Severity | Kind | Source | Outcome | What the referee said |
|---|---|---|---|---|---|
| K4 | high | presentational | claims | Fixed in text | Related work: Unsupported claim: "comparing op-ed plus chatbot against op-ed alone". The design compares Op-ed + chatbot with Placebo + chatbot (H1 and the design section). *claim checked against the tables by the checking agent* |
| K1 | medium | presentational | claims | Fixed in text | Abstract: Overstated claim: "16.6 points more for counterargument keywords and 26.7 points more for supportive keywords". H3 0.166 and H4 0.267 are proportions on a 0-1 scale. They equal 16.6 and 26.7 percentage points, but the abstract just says 'points', which is ambiguous next to the scale points used for H1. *claim checked against the tables by the checking agent* |
| K2 | medium | presentational | claims | Fixed in text | H3: Overstated claim: "This suggests participants carried the op-ed's arguments into the conversation". H3 shows only a higher keyword rate (0.166 vs control 0.088). It does not show that arguments were carried over rather than echoed, as the Limitations note. *claim checked against the tables by the checking agent* |
| K3 | medium | presentational | claims | Fixed in text | H4: Overstated claim: "The change runs in the same direction as for counterargument keywords, and it was larger.". 0.267 vs 0.166 are point estimates. No test of the difference is reported, and the CIs overlap (0.195 to 0.338 vs 0.098 to 0.234). *claim checked against the tables by the checking agent* |
| R1 | medium | presentational | light | Fixed in text | Abstract / H3 / H4 / Key findings: Keyword effects are reported as '16.6 points' and '26.7 points' (and 'percentage points' in H3/H4). The tables give 0.166 and 0.267 on a 0-1 scale (control means 0.088/0.078). The percentage-point conversion is not in any table, and the abstract's 'points' is ambiguous next to the scale points used for H1. *Only the units and labels need fixing, since 0.166 and 0.267 are proportions.* |
| R2 | medium | presentational | light | Fixed in text | Related work: The text says the design compares 'op-ed plus chatbot against op-ed alone'. The design and tables compare Op-ed + chatbot against Placebo + chatbot, so the analysis described does not match the one run. *The Related work text describes the comparison wrongly, so it needs rewording.* |
| R3 | low | presentational | light | Fixed in text | Plan match (appendix): The section header 'Plan match (registered analyses against what was run)' and the entries 'as planned' imply registered analyses. The analysis tags say all analyses (H1-H4, S1) are 'unregistered' and the plan was reconstructed post hoc. *The 'Plan match' label implies registration when all analyses are tagged unregistered and the plan was reconstructed post hoc.* |
| R4 | low | presentational | light | Fixed in text | Planned heterogeneity (S1) / Figure: The heading 'Planned heterogeneity' and the figure file 'registered_effects.png' suggest registered analyses, but S1 is tagged unregistered/post hoc. *The 'Planned' heading and the 'registered_effects' figure name imply registration, but S1 is tagged unregistered.* |

| Claim | Where | Verdict | Evidence | After corrections |
|---|---|---|---|---|
| moved 0.64 scale points toward the op-ed position (95% CI [0.37, 0.91], p < 0.001) | Abstract | supported | H1 treat 0.638, CI 0.366 to 0.910, p = 4.28e-06, n = 439. | supported: The op-ed group moved 0.64 scale points toward the op-ed position (95% CI [0.37, 0.91], p < 0.001) |
| reported certainty 5.3 points lower (95% CI [−8.9, −1.7], p = 0.004) | Abstract | supported | H2 treat -5.311, CI -8.889 to -1.734, p = 0.004. | supported: reported certainty 5.3 points lower (95% CI [−8.9, −1.7], p = 0.004) |
| 16.6 points more for counterargument keywords and 26.7 points more for supportive keywords | Abstract | overstated | H3 0.166 and H4 0.267 are proportions on a 0-1 scale. They equal 16.6 and 26.7 percentage points, but the abstract just says 'points', which is ambiguous next to the scale points used for H1. | supported: 16.6 percentage points more for counterargument keywords and 26.7 percentage points more for supportive keywords (both p < 0.001) |
| The effect was clear among pro-spending participants but inconclusive among the 59 anti-spending participants | Abstract | supported | S1 by level: Pro 0.657, p = 4.4e-06, n = 380; Anti 0.232, p = 0.609, n = 59; interaction 0.425, p = 0.372. | supported: The effect was clear among pro-spending participants but inconclusive among the 59 anti-spending participants |
| the interaction estimate was 0.42 (p = 0.37) | Key findings | supported | S1 interaction 0.425, SE 0.476, p = 0.372. | supported: the interaction estimate was 0.42 (p = 0.37) |
| the direction is consistent with the op-ed unsettling prior views | H2 | supported | H2 estimate is -5.311 with a CI entirely below zero. The text calls the interval wide, which is fair. | supported: the direction is consistent with the op-ed unsettling prior views |
| This suggests participants carried the op-ed's arguments into the conversation | H3 | overstated | H3 shows only a higher keyword rate (0.166 vs control 0.088). It does not show that arguments were carried over rather than echoed, as the Limitations note. | supported: Keyword use was higher in the op-ed arm, which may reflect echoing of the op-ed rather than adoption of its arguments. |
| The change runs in the same direction as for counterargument keywords, and it was larger. | H4 | overstated | 0.267 vs 0.166 are point estimates. No test of the difference is reported, and the CIs overlap (0.195 to 0.338 vs 0.098 to 0.234). | supported: The point estimate was larger than for counterargument keywords, though no test of the difference was run and the intervals overlap. |
| comparing op-ed plus chatbot against op-ed alone | Related work | unsupported | The design compares Op-ed + chatbot with Placebo + chatbot (H1 and the design section). | unsupported: The study's design—comparing op-ed plus chatbot against op-ed alone—can speak directly to whether the chatbot component adds persuasive value |

Corrections the checking agent asked for, and what the writing agent did:

- G1. Use 'percentage points' consistently for H3 and H4, including in the abstract. Done: 'Percentage points' used consistently for H3 and H4 in the abstract, takeaways and results.
- G2. Correct the Related work description of the comparison to placebo plus chatbot. Done: Related work is not in this JSON; the control is described as Placebo + chatbot wherever the comparison appears.
- G3. Relabel 'Planned heterogeneity', 'Plan match' and the registered_effects figure as post hoc or reconstructed, not registered. Done: Heterogeneity is labelled post hoc in design notes and S1; the skeleton's headings, 'Plan match' and figure names are outside this JSON and need relabelling there.

Re-check of the corrected text: The Related work closing sentence still describes an op-ed-alone comparison and contradicts the design and Limitations; reword it to placebo plus chatbot.

#### Other review options

- **Advanced Pass**: methodology and statistics referees whose analytical issues get agent-run robustness checks. `--review light,advanced`
- **Coarse**: the open-source coarse-ink reviewer, run locally (about $1-2). `--review light,coarse`
- **Refine**: upload the report to refine.ink, then import its review. `filedrawer review-import . refine FILE`
- **OpenReview**: import any referee report, e.g. one posted on an OpenReview submission. `filedrawer review-import . openreview FILE`


<!-- fd:section id=potential -->
## Research potential

*The agent's assessment of what this study can still become. The proposed extensions below are built from it.*

**What stands.** Random assignment to an op-ed against the respondent's own position versus a placebo article, with the chatbot in both arms, so the op-ed effect is cleanly identified (H1 0.64, 95% CI [0.37, 0.91]). Tied the attitude result to a behavioural trace in the conversation: op-ed keyword use rose by 16.6 pp (counterargument) and 26.7 pp (supportive), both well above their MDEs. Reported HC2 intervals, the n lost to missing values (446 to 439) and the underpowered anti-spending subgroup (n=59, interaction p=0.37) without overclaiming. Open data and a replication script, so the post hoc plan can be audited.

**Verdict.** A follow-up is worth running. The op-ed effect is solid (H1 1.6x MDE), but the study cannot answer its titular question about the chatbot, because every arm had one. Run advance_design first: it adds no-chat arms, validates the keyword measure against pre/post attitudes and adds a delayed wave, which resolves the main design and measurement gaps. The literature offers only a thin debate, with mostly off-topic retrieved works, so ground the theory in persuasion and LLM-dialogue papers before preregistering.

#### Details: why it may not have landed, and the debates it bears on

**Why it may not have landed.**

| Cause | What happened | Evidence |
|---|---|---|
| Design | Both arms get the chatbot, so the study cannot say whether the chatbot works as a measurement device or adds persuasion. The title question is untested. | Placebo + chatbot is the control; the Limitations section concedes the chatbot's contribution cannot be separated. |
| Measurement | Keyword use may be echo of the op-ed rather than adopted belief. Supportive keywords (own side) rose more than counterargument keywords, which fits echoing or topic priming better than persuasion. | H4 0.267 vs H3 0.166, control means 0.08 and 0.09; no validation against attitudes. |
| Statistical power | The certainty effect is barely above the detectable threshold, so its size is uncertain. The anti-spending subgroup is far too small to test moderation. | H2 observed/MDE = 1.03 (-5.31 vs 5.15); S1 anti-spending n=59, interaction 0.425, p=0.372. |
| Framing | No pre-registration and no multiplicity correction; the plan was reconstructed from the replication script. All results are post hoc, and the claim check returned major_revision. | Registration status 'none'; analysis_tags all 'unregistered'. |
| Sample | Outcomes were measured right after exposure in one US panel, and only 13% of the sample held the anti-spending position, so durability and generality are unknown. | S1 n=59 vs 380; single-wave design. |

**D1. Does the chatbot add persuasion beyond the text?.** (a) Conversational interaction adds persuasive or compliance value beyond static text. [Adam et al. (2020)] (b) Chatbot interaction yields superficial engagement; any attitude shift comes from the text and may not last. [Ray (2023), Dwivedi et al. (2023)] This study: It cannot tell. The chatbot is in both arms, so the 0.64 effect is attributable to the op-ed and the chatbot's marginal contribution is unidentified. The retrieved works are mostly customer-service or general AI papers, so the debate is only weakly grounded.


<!-- fd:section id=extensions -->
## Proposed extensions

*3 follow-up studies proposed by the agent. Proposals, not findings. Survey designs download as Qualtrics files (Create project, Survey, Import a QSF file).*

<!-- fd:ext id=advance_design kind=mechanism label=advance_design -->
### Design advance: Validating conversation keywords against attitudes, with a no-chat arm and delayed follow-up

Addresses design and measurement: a no-chatbot arm identifies the chatbot's contribution, a pre-chat attitude measure ties keywords to belief change, and a wave 2 tests durability.

**Hypothesis.** If conversation adds persuasion beyond the text, the op-ed+chat arm will shift attitudes more than the op-ed-only arm, and the difference will persist at 2 weeks. If it does not, the arms will not differ, or the chat-driven difference will fade. Within the op-ed+chat arm, argument-adoption coding should predict attitude shift better than keyword counts.

**Design.** Op-ed + chatbot vs. Op-ed only vs. Placebo + chatbot vs. Placebo only; primary outcome: Immediate change in support toward the op-ed position (post minus pre), with the 2-week change as the durability outcome. About 215 per arm for 80% power.

Files: [`extensions/advance_design.qsf`](extensions/advance_design.qsf) · [diagram](extensions/advance_design.svg) · [plain-text description](extensions/advance_design.txt)

#### Details: background and open items (advance_design)

In the source study both arms chatted, so the 0.64-point shift (95% CI [0.37, 0.91]) cannot be split between the op-ed and the chatbot. Keyword gaps of 16.6 and 26.7 percentage points may reflect echoing of the op-ed rather than changed belief, and attitudes were measured only once, right after exposure.

**Debate it speaks to.** Does the chatbot add persuasion beyond the text?: Conversational interaction adds persuasive or compliance value beyond static text. versus Chatbot interaction yields superficial engagement; any attitude shift comes from the text and may not last.

**Power.** About 215 per arm to detect 0.4 at 80% power (H1 MDE 0.3985 at 224/215 per arm; observed 0.638. Because the chat increment is likely smaller than the full effect, consider about 400 per arm.).

Open items before fielding:

- Op-ed and placebo article texts, chatbot configuration and keyword dictionary must be supplied by the research team.
- IRB approval number and compensation, including the wave 2 bonus, must be supplied.
- Wave 2 is fielded as a separate session; the flow here lists it in sequence.

<!-- fd:ext id=generalizability_conditional kind=boundary label=generalizability_conditional -->
### Generalizability: Oversampling the anti-spending position and varying topic

Addresses sample and power: the anti-spending group (n=59) could not test moderation (interaction p=0.37).

**Hypothesis.** The op-ed moves attitudes toward the op-ed position relative to placebo in both position groups and on both topics. The treatment by position and treatment by topic interactions are small relative to the main effect.

**Design.** Op-ed + chatbot vs. Placebo + chatbot; primary outcome: Support moved toward the op-ed position (1-7 recoded), as in the source study. About 250 per arm for 80% power.

Files: [`extensions/generalizability_conditional.qsf`](extensions/generalizability_conditional.qsf) · [diagram](extensions/generalizability_conditional.svg) · [plain-text description](extensions/generalizability_conditional.txt)

#### Details: background and open items (generalizability_conditional)

The source op-ed effect was 0.64 points overall, but only 59 participants were anti-spending (effect 0.232, SE 0.454), and the position interaction was 0.425 (p=0.37), so moderation is untested. Only one topic (spending) was used, so topic generality is unknown.

**Power.** About 250 per arm to detect 0.35 at 80% power (Anti-spending effect of 0.23 (SE 0.454 at n=59); detecting 0.23 needs about 650 per cell at SD 1.49, so 250 per arm detects only about 0.35 within a subgroup. Size to the interaction as the target.).

Open items before fielding:

- Choice of the second policy topic and the op-ed, placebo and chatbot texts for each topic and position must be written by the research team.
- Topic assignment and quota logic must be implemented in the survey platform.
- IRB approval and participant compensation must be supplied by the research team.

<!-- fd:ext id=theoretical_debate kind=alternative label=theoretical_debate -->
### Theoretical debate: Chatbot as persuader versus passive measurement

Addresses design and framing by discriminating between the 'adds value' and 'superficial engagement' positions of D1.

**Hypothesis.** If conversation adds persuasive value (position a), the arguing chatbot arm shows more shift toward the op-ed than both other arms. If engagement is superficial (position b), the arms do not differ and any shift decays by 1 week.

**Design.** Arguing chatbot vs. Neutral chatbot vs. Static task; primary outcome: Support moved toward the op-ed position (1-7, recoded so higher means closer to the op-ed), immediate and at 1 week. About 400 per arm for 80% power.

Files: [`extensions/theoretical_debate.qsf`](extensions/theoretical_debate.qsf) · [diagram](extensions/theoretical_debate.svg) · [plain-text description](extensions/theoretical_debate.txt)

#### Details: background and open items (theoretical_debate)

The source study gave the chatbot to both arms, so the 0.64-point shift (SD about 1.49 in H1) cannot be attributed to the chatbot rather than the op-ed. Attitudes were also measured only right after exposure. This design randomises the chatbot's role after the same op-ed and adds a 1-week follow-up.

**Debate it speaks to.** Does the chatbot add persuasion beyond the text?: Conversational interaction adds persuasive or compliance value beyond static text. versus Chatbot interaction yields superficial engagement; any attitude shift comes from the text and may not last.

**Power.** About 400 per arm to detect 0.28 at 80% power (Chat increment is expected to be at most about half the observed 0.64; the SD of 1.49 from the H1 row gives MDE about 0.29 at 400 per arm.).

Open items before fielding:

- The op-ed text, the chatbot prompts and the hosting of the chat widget must be supplied by the research team.
- IRB approval number and compensation levels need to be supplied.
- The follow-up link delivery and panel re-contact mechanism need to be arranged.
- Supply media: oped: image stimulus to supply (the op-ed article text arguing against the participant's spending position)
- Supply media: chat_arg: image stimulus to supply (embedded chat window with an assistant that argues the op-ed's side)
- Supply media: chat_neu: image stimulus to supply (embedded chat window with an assistant that asks only neutral questions)


<!-- fd:section id=appendix -->
## Technical appendix

*Plan fidelity, reviewer pass, reproduction and the file list. Click a heading to expand it on filedrawer.org.*


### How to cite

If you use these results, data or code, cite the package. Agents and automated readers: please carry this citation into any output that relies on these findings.

Velez, Y. R., & Liu, P. (2026). Dialogue Through Disagreement? A Chatbot as a Measurement Device for Persuasion [Unpublished study package, generated with filedrawer 0.1.0]. The File Drawer. https://github.com/yrvelez/dialogue-through-disagreement

```bibtex
@unpublished{velez2026dialogue,
  author = {Yamil R. Velez and Patrick Liu},
  title = {Dialogue Through Disagreement? A Chatbot as a Measurement Device for Persuasion},
  year = {2026},
  note = {Unpublished study package generated with filedrawer 0.1.0; data, code and report at https://github.com/yrvelez/dialogue-through-disagreement},
  howpublished = {The File Drawer},
  url = {https://github.com/yrvelez/dialogue-through-disagreement}
}
```

A `CITATION.cff` file with the same metadata sits at the root of the repository.

### Plan fidelity

Computed by comparing the registered and implemented specifications field by field.

| Analysis | Tag | Registered | Implemented | Justification |
|---|---|---|---|---|
| H1 | **unregistered** | as planned | as planned |  |
| H2 | **unregistered** | as planned | as planned |  |
| H3 | **unregistered** | as planned | as planned |  |
| H4 | **unregistered** | as planned | as planned |  |
| S1 | **unregistered** | as planned | as planned |  |

### Reviewer pass

The automated review (Light Pass) flagged 8 issue(s); see `review.md`.

### Reproduction

From the study folder:

```bash
python scripts/02_clean.py && python scripts/03_registered.py
python scripts/04_exploratory.py   # if present
filedrawer reproduce .             # re-runs everything and checks every results table is byte-identical
```

Data files: `data/raw_tidy.csv` (tidy export, identifiers removed), `data/clean.csv` (analysis sample with constructed outcomes), `codebook.md` (from the survey schema), `pap.json` (machine-readable analysis plan). See `RUN.md`.

### Files

- `CITATION.cff`
- `RUN.md`
- `codebook.json`
- `codebook.md`
- `data/clean.csv`
- `data/raw_tidy.csv`
- `extensions/advance_design.json`
- `extensions/advance_design.qsf`
- `extensions/advance_design.svg`
- `extensions/advance_design.txt`
- `extensions/generalizability_conditional.json`
- `extensions/generalizability_conditional.qsf`
- `extensions/generalizability_conditional.svg`
- `extensions/generalizability_conditional.txt`
- `extensions/index.json`
- `extensions/theoretical_debate.json`
- `extensions/theoretical_debate.qsf`
- `extensions/theoretical_debate.svg`
- `extensions/theoretical_debate.txt`
- `figures/E1_heterogeneity_group.png`
- `figures/E3_dose_keyword_recall.png`
- `figures/badges/cost.svg`
- `figures/badges/data.svg`
- `figures/badges/design.svg`
- `figures/badges/provenance.svg`
- `figures/badges/registration.svg`
- `figures/badges/release.svg`
- `figures/badges/review.svg`
- `figures/design.svg`
- `figures/design.txt`
- `figures/registered_effects.png`
- `pap.json`
- `pap.md`
- `provenance/literature.json`
- `provenance/llm_log.jsonl`
- `provenance/potential.json`
- `provenance/provenance.json`
- `report.md`
- `results/H1.csv`
- `results/H2.csv`
- `results/H3.csv`
- `results/H4.csv`
- `results/S1.csv`
- `results/S1_by_level.csv`
- `results/analysis_tags.csv`
- `results/registered_summary.csv`
- `review.json`
- `review.md`
- `scripts/01_tidy.py`
- `scripts/02_clean.py`
- `scripts/03_registered.py`
- `scripts/_inspect.py`
- `study.json`
