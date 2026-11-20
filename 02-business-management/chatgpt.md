# ChatGPT: GPT 6.2 Astra and Sol

**What you will be able to do:** A weekly owner review from a sales export.

> **Updated:** 20 November 2026. Interface, account access and available models can change.

![ChatGPT: GPT 6.2 Astra and Sol](../assets/illustrations/management-review.svg)

*Original instructional artwork. Diagram labels are conceptual, not screenshots of a vendor interface.*

## Core guidance from the expanded handbook

*General reasoning model and business workspace*

### Where this tool earns its place

Use ChatGPT for conversational work with approved files and projects. GPT 6.2 Astra and Sol were announced on 17 November 2026 for the API. The API release does not mean both names appear in every ChatGPT model menu. Sol suits fast operational tasks when available; choose the more demanding option for difficult multi source analysis only if your account exposes it. Check the current picker instead of assuming a particular tier.

### Before the first prompt

Create one project per business area such as Finance, Customer Experience or Promotions. Place the current business brief, price list, brand voice, approved policies and the date of each file in that project. Turn on an appropriate data analysis tool when using spreadsheets. Begin by asking for an inventory of facts that can be proven rather than a proposal.

### A complete business exercise

For a weekly business review, upload the sales export and state which columns mean sales, returns, dates, products and currency. Ask for data cleaning notes and missing records first. Next request a descriptive table. Ask for three possible explanations for unusual changes, expressly identified as hypotheses. Then request decisions that the owner can make, with the assumptions and risks beside each. Export the chart and keep the working dataset.

### Copy ready prompt for this tool

> You are reviewing the attached shop sales workbook for the owner. Reporting period: 1 to 31 October 2026. Currency: UGX. Identify duplicate invoice numbers, blank dates, reversals and inconsistent category labels before calculating anything. Report revenue, gross margin only if verified costs exist, five best selling items, low movement stock signals and unresolved data questions. Give each finding its supporting rows or column names. Separate observations from explanations. No forecast until the source data has been checked.

### When the result is weak

If the result states a profit without verified cost data, stop and request a correction. If it hides a small number of unusual orders behind averages, ask for a breakdown by week, product and source. If it invents a customer reason for a decline, insist on labelling that as a hypothesis and suggest evidence to test it.

### Human editorial finish

Make the recommendations sound like the owner speaking to staff: name the actual product, time period and operational next step. Avoid grand claims about transformation. A grounded update might read, “Charging cables moved slowly in the second half of October. Check their shelf position and price before placing the next order.”

### Approval boundary and common errors

Do not upload sensitive customer information without authority. Never treat fluent output as audited accounts. Confirm API, app, connector and model availability separately.

**Official reference:** [ChatGPT with GPT 6.2 Astra and Sol product guidance](https://openai.com/index/introducing-gpt-6-2-astra-sol/)

## First session: from a blank workspace to a reviewable result

1. Choose one reporting question such as whether stock is moving slower this month. Avoid asking for a complete business strategy before the records are clean.
2. Export approved transaction data with one row per invoice line. Include an explanation of returns, taxes, discounts and the currency.
3. Start a fresh project or working conversation and provide a short file inventory. Name the authoritative workbook and reporting dates.
4. Request a data quality report before calculations. Inspect duplicate identifiers and negative amounts in the original workbook.
5. Ask for descriptive findings, then distinguish possible explanations from observed facts.
6. Revise the final management note so it names actual decisions, responsible people and dates.

## Prompt ladder: simple, evidence based and advanced

The prompts below are teaching examples. Replace fictional context with approved records. A tool that does not support freeform prompting may require you to perform the equivalent steps through its own interface.

### First pass

```text
Read the supplied sales table only. Tell me the column names, date range, number of records, missing fields and duplicate invoice IDs. Do not interpret performance yet.
```

### Evidence based

```text
Calculate weekly sales and returns using the approved definitions. Show the formula and the row count behind each period. Label any uncertain treatment of taxes or refunds.
```

### Owner decision

```text
Draft a one page decision memo with three verified findings, two hypotheses to test and no more than two next actions. Each action needs an owner, a deadline placeholder and a measure of success.
```

## What an acceptable result looks like

**Illustrative output:** “Sales of blue notebooks fell from 38 to 21 units across the two periods in this sample. Check shelf placement and availability before attributing the change to customer preference.” The statement would be invalid without matching source rows.

## If the first version disappoints

If a chart silently excludes refunds, ask for a reconciliation table. If the assistant says “profit” when only revenue is available, require it to remove the claim. If the memo contains broad strategy advice, ask which exact record supports each suggested action.

## Human editorial finish

Have the person who handles the till explain unusual transactions. Rewrite recommendations using the names of real categories and the vocabulary staff use. Do not create fake customer feedback to make a conclusion sound convincing.

## Practice assignment

Using a fictional or appropriately protected version of the case, complete **a weekly owner review from a sales export**. Save an evidence inventory, the first draft, a precise correction request and the reviewed deliverable. Write a short comparison showing what the revision genuinely improved.

## Approval and success test

Can an owner recompute any stated number from the saved workbook? Can every action be approved without revealing private customer data?

## Related reading

[Prompt anatomy](../01-foundations/prompting-fundamentals.md) · [Context engineering](../01-foundations/context-engineering.md) · [Humanisation](../01-foundations/humanization.md) · [Reference index](../06-reference/sources-and-updates.md)

## Studio lesson: the owner's Monday decision meeting

The most valuable use is not asking for a prediction of next month's sales. It is reconstructing the week from trustworthy records and arriving at a short list of decisions. Imagine a retailer who sends a sales export, a stock file and a note from the shop manager. The sales file records completed transactions. The stock file gives quantities at a particular time. The manager's note contains observations, not measured facts. Those three sources do not deserve the same level of confidence.

**Prepare the material.** Rename files with a date and owner, for example `sales_october_2026.csv`, `stock_november_01_2026.csv` and `manager_observations.txt`. Put currency, date format, return conventions, tax treatment and column definitions in a separate note. Remove customer identifiers and payment credentials. If the reporting period does not match across files, say so before calculating.

**First pass.** Ask for a data inventory, not a report. The response should identify file names, record counts, key columns, blank cells, duplicates, possible returns and mismatched product identifiers. Resolve them before calculating totals. Then request a descriptive report with a calculation method beside every number. Save it. Only after this should you request possible actions.

```text
We are preparing the weekly owner meeting for a fictional retailer.
Files: sales transactions, inventory snapshot and a manager note.
Currency: UGX. Dates are day/month/year. A negative quantity denotes
an authorised return; do not remove it silently.

PHASE ONE ONLY: inspect the files and list the exact fields, data types,
missing values, duplicate candidates, and inconsistent definitions.
Build a table with issue, affected field, business consequence, and
what you need me to confirm. Do not calculate profit, invent product
costs, produce a forecast or recommend purchases yet.
```

Follow with a second prompt only after you have resolved the ambiguous fields:

```text
Using the confirmed definitions, calculate revenue and unit movement
by product and week. Show the formula or calculation logic for each
metric, and reconcile transaction totals to the aggregate table.
Separate what the data demonstrates from what we suspect. Give three
owner decisions, their supporting evidence, an alternative explanation,
and the next piece of evidence needed. Finish with a five-minute meeting
agenda. Never call revenue profit.
```

**Review the work.** Open three random source transactions and one return, then verify that each appears correctly in the totals. Check whether cancelled orders were excluded for a documented reason. If a chart is produced, inspect axes, units, dates and the underlying numbers. Compare calculations in a spreadsheet. For a decision with financial consequences, have a competent person review the figures.

**Humanise the final briefing.** A report that says *optimise operational efficiencies* does not tell the owner what to do. Replace it with a sentence such as: *Two popular chargers were unavailable on four selling days. Confirm delivery dates before spending on another advert.* Use that sentence only if the record actually supports it. Keep the business's real product names and the manager's actual language, while removing unverifiable assumptions.

### Advanced exercise: separate analysis from execution

Create two documents: a read-only recommendation memo and a proposed action list. Ask the model to label each action `research`, `draft`, `requires approval`, or `not authorised`. Never allow the drafting stage to quietly become supplier orders, refunds, messages to customers, or changes to finance records. Where connected applications are available, inspect their permissions and confirmation steps before enabling actions.

### Model and product accuracy

OpenAI's November 17, 2026 notes describe GPT 6.2 Astra and Sol in the API. A model available through the API is not necessarily a selectable button inside an individual ChatGPT account. Choose the best available model and tool for the task, rather than teaching owners to look for a menu item that their plan may not show.

**Further reading:** [OpenAI model directory](https://developers.openai.com/api/docs/models) and [release notes](https://help.openai.com/en/articles/9624314-model-release-notes).
