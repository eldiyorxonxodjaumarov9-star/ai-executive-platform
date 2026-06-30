# Claude.ai Connector Setup — AI Executive Platform

This guide explains how to connect **Claude.ai** to your deployed **AI Executive Platform** so users can ask questions like:

> CEO, bugungi Bitrix24 holatini tahlil qil

Claude will call your platform tools and return live Bitrix24-based executive answers.

---

## Important requirements

### 1. Public URL is required

Claude.ai runs in Anthropic's cloud. It **cannot** call `localhost` or private networks.

You must deploy the FastAPI app to a public HTTPS URL, for example:

```
https://YOUR-APP.onrender.com
```

### 2. Local development

- Dashboard: `http://127.0.0.1:8000/`
- Connector health: `http://127.0.0.1:8000/claude/health`
- Connector manifest: `http://127.0.0.1:8000/claude/manifest`

These work locally for testing the API, but **Claude.ai cannot use them** until deployed publicly.

### 3. After Render deploy

Set your production base URL in Render environment variables:

```
PUBLIC_BASE_URL=https://YOUR-APP.onrender.com
```

Then verify:

```bash
curl https://YOUR-APP.onrender.com/claude/health
curl https://YOUR-APP.onrender.com/claude/manifest
curl https://YOUR-APP.onrender.com/claude/instructions
```

---

## Available connector tools

| Tool | Method | Endpoint |
|------|--------|----------|
| `get_bitrix_summary` | GET | `/tools/bitrix/summary` |
| `run_ceo_agent` | POST | `/tools/agent/ceo` |
| `run_finance_agent` | POST | `/tools/agent/finance` |
| `run_sales_agent` | POST | `/tools/agent/sales` |
| `run_hr_agent` | POST | `/tools/agent/hr` |
| `run_marketing_agent` | POST | `/tools/agent/marketing` |
| `run_customer_success_agent` | POST | `/tools/agent/customer_success` |

Agent tools accept JSON body:

```json
{
  "question": "CEO, bugungi Bitrix24 holatini tahlil qil"
}
```

---

## Connector endpoints

| Endpoint | Purpose |
|----------|---------|
| `GET /claude/health` | Connector health (no secret required) |
| `GET /claude/manifest` | Tool manifest for Claude connector |
| `GET /claude/instructions` | Instructions Claude should follow |
| `GET /public/claude-tools.json` | Static manifest file (replace YOUR-APP URL) |

---

## Optional API protection

Set in Render (recommended for production):

```
CONNECTOR_SECRET=your-long-random-secret
```

When set, Claude (or any client) must send:

```
X-Connector-Secret: your-long-random-secret
```

Protected routes:

- `/tools/*`
- `/claude/*` except `/claude/health`

If `CONNECTOR_SECRET` is empty, local development works without the header.

**Never commit** `CONNECTOR_SECRET` to GitHub.

---

## Deploy on Render (summary)

1. Push code to GitHub (ensure `.env` is not committed).
2. Create Render Web Service from repo (`render.yaml` supported).
3. Set environment variables:
   - `BITRIX24_WEBHOOK_URL`
   - `ANTHROPIC_API_KEY`
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`
   - `PUBLIC_BASE_URL=https://YOUR-APP.onrender.com`
   - `CONNECTOR_SECRET` (recommended)
4. Deploy and open `https://YOUR-APP.onrender.com/health`.

---

## Connect Claude.ai

### Step 1 — Verify connector

```bash
curl https://YOUR-APP.onrender.com/claude/health
```

Expected:

```json
{
  "success": true,
  "service": "AI Executive Platform Claude Connector",
  "tools_available": ["get_bitrix_summary", "run_ceo_agent", "..."]
}
```

### Step 2 — Get manifest URL

```
https://YOUR-APP.onrender.com/claude/manifest
```

Or static file (update placeholder first):

```
https://YOUR-APP.onrender.com/public/claude-tools.json
```

### Step 3 — Add connector in Claude.ai

In Claude.ai (Connectors / Integrations):

1. Add a custom connector or HTTP tool integration.
2. Use manifest URL: `https://YOUR-APP.onrender.com/claude/manifest`
3. If using `CONNECTOR_SECRET`, configure header:
   - `X-Connector-Secret: <your-secret>`
4. Save and enable the connector.

### Step 4 — Test in Claude chat

Example prompts:

- `CEO, bugungi Bitrix24 holatini tahlil qil`
- `Finance, pipeline moliyaviy xulosasini ber`
- `Sales, lidlar va bitimlar bo'yicha qisqa tahlil`

Claude should call `run_ceo_agent` (or the matching agent) with your question.

---

## Manual API test (without Claude.ai)

```bash
# Health
curl https://YOUR-APP.onrender.com/claude/health

# Manifest
curl https://YOUR-APP.onrender.com/claude/manifest

# Bitrix summary (with secret if configured)
curl -H "X-Connector-Secret: YOUR_SECRET" \
  https://YOUR-APP.onrender.com/tools/bitrix/summary

# CEO agent (uses Claude API on server — costs credits)
curl -X POST https://YOUR-APP.onrender.com/tools/agent/ceo \
  -H "Content-Type: application/json" \
  -H "X-Connector-Secret: YOUR_SECRET" \
  -d "{\"question\":\"CEO, bugungi Bitrix24 holatini tahlil qil\"}"
```

---

## Security checklist

- [ ] `.env` is gitignored
- [ ] `ANTHROPIC_API_KEY` only in Render env vars
- [ ] `BITRIX24_WEBHOOK_URL` only in Render env vars
- [ ] `CONNECTOR_SECRET` set in production
- [ ] `PUBLIC_BASE_URL` points to Render HTTPS URL
- [ ] No secrets in `README.md`, logs, or `public/claude-tools.json`

---

## Architecture

```
Claude.ai chat
      │
      ▼
GET /claude/manifest  (discover tools)
      │
      ▼
POST /tools/agent/ceo  {"question": "..."}
      │
      ▼
AI Executive Platform
  ├── Bitrix24 CRM (live data)
  ├── Agent Brain + Knowledge
  └── Claude API (server-side analysis)
      │
      ▼
Executive answer returned to Claude → user
```
