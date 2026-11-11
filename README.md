# Comcast telecom complaints analysis

This R coursework explores ticket volume over time, open complaints by state, complaint themes, and resolution by intake channel. The [original analysis](Telecom.R), charts in [Photos](Photos/), and course report are preserved.

## Metrics and run steps

- Ticket volume counts rows by complaint date. The archived script aggregates dates by calendar month number.
- Resolved combines Closed and Solved. Open combines Open and Pending.
- Channel resolution rate divides resolved tickets in that channel by all tickets received through that channel.
- The original text rules assign a single category through sequential keyword matching. Later matching assignments can overwrite earlier ones. Treat the categories as a heuristic and check overlap and fallback behaviour before relying on theme counts.

Run `Rscript resolution_by_channel.R` from the repository root for the corrected channel aggregation. It uses base R. The table below was independently recomputed from the committed CSV. The R script itself was not run in the audit environment.

| Channel | Resolved | Total | Resolution rate |
|---|---:|---:|---:|
| Customer Care Call | 864 | 1119 | 77.21% |
| Internet | 843 | 1105 | 76.29% |

The original R analysis is an interactive legacy workflow. To explore it, open the script in RStudio and choose the committed Comcast CSV when prompted. The corrected aggregation keeps the original report available for historical reference.

The repository also contains a separate [dress recommendation exercise](DRESS_EVALUATION.md).
