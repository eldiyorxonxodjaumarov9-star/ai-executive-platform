# Enterprise Knowledge Base

This directory contains **company knowledge files** for all AI agents. These files are **not** system prompts — they hold business information that the client updates over time.

System prompts live in `prompts/`. Knowledge lives here.

---

## Directory structure

```
knowledge/
  README.md                 ← This file
  ceo/
    knowledge.md            ← Company & domain facts
    kpi.md                  ← KPI definitions and targets
    rules.md                ← Policies and operating rules
    faq.md                  ← Frequently asked questions
    examples.md             ← Example reports and decisions
  sales/
  finance/
  hr/
  marketing/
  customer_success/
```

Each agent has its **own folder**. Files are loaded automatically before every AI report.

---

## What each file does

| File | Purpose |
|------|---------|
| `knowledge.md` | Core company and department knowledge: structure, processes, strategy, terminology |
| `kpi.md` | KPI names, formulas, targets, thresholds, reporting frequency |
| `rules.md` | Policies, escalation paths, decision rules, compliance requirements |
| `faq.md` | Common questions and approved answers for the department |
| `examples.md` | Sample reports, good/bad examples, reference decisions |

---

## How AI uses these files

Before every report, the **Agent Runner** automatically:

1. Loads the **system prompt** from `prompts/{agent}.md`
2. Loads **all knowledge files** from `knowledge/{agent}/`
3. Fetches live **Bitrix24 CRM data**
4. Optionally includes a **user question** (Claude tools API)

Context order sent to Claude:

```
1. System Prompt        → Claude `system` parameter
2. Company Knowledge    → Claude user message (section 1)
3. Bitrix24 CRM Data    → Claude user message (section 2)
4. User Question        → Claude user message (section 3, if provided)
```

You do **not** need to change code when updating knowledge — only edit the markdown files.

---

## How to update knowledge

### Incremental import from `Ai agentlar/` (recommended)

When new company documents are added to the `Ai agentlar/` folder:

```bash
python scripts/incremental_knowledge_update.py
```

This processes **only new or modified files**, preserves existing knowledge, detects duplicates, supersedes outdated revisions, and validates all agents. Report: `scripts/incremental_knowledge_report.json`.

### Adding new information manually

1. Open the relevant agent folder (e.g. `knowledge/ceo/`)
2. Open the appropriate file (`knowledge.md`, `rules.md`, etc.)
3. **Append** new content at the bottom with a date header:

```markdown
## 2026-06-29 — Yangi strategiya

Client will provide this information.
```

4. Save the file. The next report will include the new content automatically.

### Supported source formats (manual workflow)

The client may send:

- PDF
- DOCX
- TXT
- Markdown
- Policies and business documents
- KPI spreadsheets

**Workflow:** Extract text from the document and paste/append into the correct knowledge file. No code changes required.

### Best practices

- **One topic per section** — use `##` headings with dates for audit trail
- **Facts only** — do not ask AI to invent; write what the company confirms
- **Keep KPIs measurable** — include name, formula, target, owner
- **Update rules when policy changes** — old rules can stay with a "Superseded" note
- **Use Uzbek or bilingual** as preferred by the company; AI reads both
- **Never put secrets in knowledge** — API keys stay in `.env` only
- **Agent-specific content** — CEO knowledge in `ceo/`, sales in `sales/`, etc.

---

## Agents covered

| Folder | Agent |
|--------|-------|
| `ceo/` | CEO Agent |
| `sales/` | Sales Agent |
| `finance/` | Finance Agent |
| `hr/` | HR Agent |
| `marketing/` | Marketing Agent |
| `customer_success/` | Customer Success Agent |

---

## Technical reference

- Loader: `app/knowledge/loader.py`
- Integration: `app/agents/runner.py` → `build_user_context()`
- Knowledge path: `knowledge/{agent_name}/`

To verify knowledge is loaded, check server logs for:

```
Loading knowledge base | agent=ceo | dir=...
Knowledge base loaded | agent=ceo | files=5 | chars=...
```

---

## Continuous expansion

This architecture is designed so the client can grow the knowledge base indefinitely by editing markdown files only — no redeployment or code changes required for new company documents.
