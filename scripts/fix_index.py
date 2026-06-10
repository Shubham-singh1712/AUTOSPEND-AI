import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

bad_block = """            <div class="dash-actions">
              <button class="icon-button" style="border-radius: 50%;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg></button>
              <button class="primary-button" onclick="document.querySelector('[data-view=\\'intake\\']').click()" style="border-radius: 20px;">+ Add Expense</button>
              </div>
              <div>
                <strong id="dashTotalExpense" class="mono" style="font-size: 2rem;">$0</strong>"""

good_block = """            <div class="dash-actions">
              <button class="icon-button" style="border-radius: 50%;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path><path d="M13.73 21a2 2 0 0 1-3.46 0"></path></svg></button>
              <button class="primary-button" onclick="document.querySelector('[data-view=\\'intake\\']').click()" style="border-radius: 20px;">+ Add Expense</button>
            </div>
          </header>

          <div class="dash-header" style="display: flex; flex-direction: column; gap: 12px; margin-bottom: 20px;">
            <div>
              <p style="display: inline-flex; align-items: center; gap: 8px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.1); background: rgba(255,255,255,0.04); padding: 4px 12px; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.18em; color: var(--brand); margin-bottom: 8px; line-height: 1;">✦ Live backend</p>
              <h1 class="screen-title" style="margin-bottom: 4px;">Good morning, <span id="dashProfileName">User</span></h1>
              <p style="color: var(--text-muted); font-size: 0.875rem; line-height: 1.5; margin-top: 4px;">Financial overview • <span id="dashMonthLabel">May 2026</span></p>
            </div>
          </div>

          <section class="summary-grid dash-4-col" aria-label="Financial summary">
            <article class="metric glass-card">
              <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <span>Spent This Month</span>
                <div class="card-icon icon-cyan"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><line x1="2" y1="10" x2="22" y2="10"/></svg></div>
              </div>
              <div>
                <strong id="dashTotalExpense" class="mono" style="font-size: 2rem;">$0</strong>"""

if bad_block in html:
    html = html.replace(bad_block, good_block)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed index.html")
else:
    print("Bad block not found, check exactly.")
