# A weekly owner report

> **Updated:** 20 November 2026. Interface, account access and available models can change.

![A weekly owner report](../assets/illustrations/management-review.svg)

*Original instructional artwork. Diagram labels are conceptual, not screenshots of a vendor interface.*

## Scenario and evidence

The fictional Riverside Retail shop sells notebooks, pens and folders. Its owner wants a Monday review with sales, returns and possible stock concerns. The files are `transactions.csv`, `stock_count.csv` and `approved_prices.csv`. Real businesses must use their own protected exports.

### Step 1. Inspect the source

Ask for a report of field names, time span, blank dates, duplicate invoice lines and records marked as returns. Check that quantities use a consistent sign convention. Keep tax treatment and currency explicit. Do not calculate profit without genuine cost information.

```text
Act as a careful reporting analyst. Inventory the three attached tables and list their row counts, date ranges, identifiers, missing values and any fields that require explanation. Do not infer the business result yet. Return a source quality report with examples of affected rows.
```

### Step 2. Calculate and reconcile

Use the accepted definition of net sales. For example, if a fictional week has sales receipts of UGX 1,800,000 and recorded returns of UGX 120,000, the net receipts are UGX 1,680,000 before any further accounting treatment. This is an arithmetic illustration, not the shop’s records.

### Step 3. Prepare a human decision memo

Separate findings, possible explanations and next actions. “Folder units were lower” is an observation. “They were hard to find on the shelf” is a hypothesis. “Photograph the shelf and test the display position” is a proposed action. Each needs a responsible person and review date.

### Step 4. Review with the team

The person who processes returns should check whether credit notes are complete. The stock controller should check units counted. Keep the chart and the underlying tables alongside the final report.

**Exit test:** Another person can recompute the totals and identify every assumption.

## What to retain for the next cycle

Save the dated sales export, the calculation definitions, the exception list, the owner-approved memo and its next review date. Never mix the working draft with the approved account of performance.

[Return to the index](../README.md) · [Case studies](../05-real-world-examples/complete-campaign.md)

## From raw numbers to an owner-ready decision brief

A weekly report needs a source, a calculation, an interpretation and a decision. Suppose a shop reports 126 completed invoices and 12 returns. If returns are represented as separate negative transactions, the correct order count and net sales depend on the record definition. The owner should not accept a report that uses the word *sales* ambiguously.

**Source check:** identify the reporting period, currency, transaction grain and cancellation policy. Reconcile the computed total to the source system's own report. Keep an exception table rather than silently dropping unusual rows. **Interpretation:** distinguish an observed trend from an explanation. For example, a fall in a product's sales may be due to lower demand, missing stock, a price change or incomplete data. **Decision:** propose an action that the owner can approve and evaluate.

```text
Create a one-page Monday management briefing from the attached sales
export. Start with the data quality check and exact time range.
Define every financial and customer metric, list exceptions and
show the calculations. Next describe up to three actual changes with
source evidence. Then propose two low-risk checks for the owner.
Do not infer profit from revenue. Do not invent reasons for change.
```

**Final memo structure:** a five-line overview, three evidence-backed observations, unresolved data issues, actions for named roles to approve and the date of the next review. Use plain English. A sentence such as *Tuesday sales were lower than the previous three Tuesdays* is more useful than *sales performance requires strategic optimisation*, but only after the comparison is verified.

## Audit sample

Pick one top-selling item and check its transactions manually. Verify one discount, one cancelled transaction and one return. The arithmetic should lead back to exact source rows or reproducible formulas. Keep the original file untouched.
