# AutoSpend AI: Zero-Friction, Local-First Financial Intelligence

AutoSpend AI is a privacy-first, automated financial intelligence console designed to eliminate the friction of manual expense tracking.

---

## 💡 The Core Value Proposition

### ❌ The Problem: Manual Tracking Burnout
Most traditional expense tracking apps fail because **they demand manual inputs**. Opening an app, typing in the merchant, selecting a category, entering the amount, and specifying the payment method for every daily transaction is a chore. Within weeks, users experience burnout and abandon tracking, leaving them with incomplete financial ledgers.

### ⚠️ The Failure of Standard Trackers
"Smart" trackers often still require you to log into separate bank accounts (compromising API keys and passwords) or upload sensitive files to centralized cloud servers. If they don't support bank links, they fallback to manual forms—which still fails due to input exhaustion.

###  The AutoSpend AI Solution
AutoSpend AI implements a **zero-click background sync pipeline** with **local-first storage** and **secure local AI**:
1. **Google Drive Sync**: Simply take a screenshot of a receipt or invoice and upload it to a dedicated Google Drive folder (e.g., from your phone).
2. **Auto-Polling & Queueing**: AutoSpend AI’s lightweight server monitors your Drive folder in the background.
3. **AI Core Parsing**: Using Gemini 2.5 Flash or OpenAI, it parses receipt images, instantly extracting the merchant, category, amount, payment method, and date with structured JSON output.
4. **1-Click Review Inbox**: Extracted details sit in your dashboard's Review Inbox. Tap approve, edit, or reject to commit transactions straight to your database. No typing required!

---

## 🛠 Features

- **Google Drive Ingest Pipeline**: Background scanner fetches receipt screenshots, parses them with OCR + AI, and places them into an action queue.
- **Review Inbox**: Smart duplicate checking and easy 1-click approvals for extracted receipt logs.
- **Natural Language Ledger**: Turn raw notes like *"spent 450 on Uber ride home via GPAY"* into fully structured, clean ledger items.
- **Interactive Visualizations**: High-end, dependency-free monthly spending trends and category doughnut charts built with pure HTML5 Canvas. Includes responsive trigonometric hover states and floating glassmorphism tooltips.
- **Budget Progress Gauge**: Dynamic SVG radial progress ring that calculates remaining budget and alerts when you exceed boundaries.
- **Local-First Architecture**: Your financial data never leaves your machine. Saves transactions locally in `autospend.db` (SQLite).
- **AI Finance Assistant**: An inline chatbot that answers detailed queries (e.g., *"What is my top category this month?"* or *"Did I spend more on travel than last month?"*) using your local ledger.

---

## 📐 System Architecture

AutoSpend AI runs locally as a single-origin server, ensuring privacy and resolving Google OAuth redirect limitations.

```mermaid
graph TD
    subgraph Client Browser (Local View)
        GUI[Glassmorphic HTML5/CSS3 Dashboard]
        LS[localStorage Client Cache]
        Canvas[Trigonometric Canvas Visualizations]
    end

    subgraph Local Host Machine (Backend)
        Srv[Python ThreadingHTTPServer - Unified Port 8787]
        DB[(SQLite - autospend.db)]
        AI[AI Parser Client]
    end

    subgraph External Secure Integrations
        GDrive[Google Drive API - Receipts Folder]
        LLM[LLM API - OpenRouter/Gemini or OpenAI]
    end

    GUI <-->|API Calls / REST JSON| Srv
    LS <-->|Auto Sync| DB
    Srv <-->|OAuth/Fetch Screenshots| GDrive
    Srv <-->|Secure Extraction Prompt| LLM
```

---

## 🚀 Running AutoSpend AI

### 1. Prerequisites
Ensure you have **Python 3.8+** installed on your machine.

### 2. Fast Launch (Recommended)
On Windows, double-click or run:
```powershell
.\start-autospend.ps1
```
This script will:
- Automatically initialize a local `.env` configuration if one is missing.
- Launch the Python backend server in a background window.
- Launch your default browser and navigate directly to `http://127.0.0.1:8787/`.

*Note: Accessing the app via `http://127.0.0.1:8787/` (instead of double-clicking `index.html` as a `file://` link) is required to prevent CORS restrictions and make Google OAuth login popups function correctly.*

---

## ⚙️ AI & Google Drive Setup

### AI Configuration
1. Open the `.env` file generated in the project root directory.
2. **To use Gemini 2.5 Flash / OpenRouter (Recommended)**:
   ```env
   OPENROUTER_API_KEY=sk-or-v1-YOUR_OPENROUTER_KEY_HERE
   OPENROUTER_MODEL=google/gemini-2.5-flash
   ```
3. **To use OpenAI**:
   ```env
   OPENAI_API_KEY=sk-proj-YOUR_OPENAI_KEY_HERE
   AUTOSPEND_LLM_PROVIDER=openai
   ```
4. Restart your backend server. Go to the dashboard **Settings** tab, verify the Backend URL is set to `http://127.0.0.1:8787`, and click **Check AI** to test connection.

### Google Drive Integration (OCR Sync)
1. Register a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the **Google Drive API** and **Google Identity / OAuth 2.0**.
3. Set your Redirect URI in the Google Cloud Console to:
   ```text
   http://127.0.0.1:8787/oauth2callback
   ```
4. Populate your `.env` file with client details:
   ```env
   GOOGLE_CLIENT_ID=your-google-client-id
   GOOGLE_CLIENT_SECRET=your-google-client-secret
   GOOGLE_REDIRECT_URI=http://127.0.0.1:8787/oauth2callback
   ```
5. Restart the server. Click **Sign in with Google** on the settings tab to link your account. Navigate to the **Drive Sync** module on your dashboard to select your receipt uploads folder.

---

## 🗃 Production Deployment

Because AutoSpend AI uses a local-first SQLite database (`autospend.db`), deploying to ephemeral cloud platforms (such as Render or Railway's free tiers) requires mounting a persistent disk volume to prevent data loss.

**Render Mounting Guideline**:
- **Mount Path**: `/data`
- **Environment Variable**: Configure your python server to write the SQLite database inside `/data/autospend.db` (e.g. `AUTOSPEND_DB_PATH=/data/autospend.db`).
- This guarantees your database file survives daily container recycles and automatic updates.
