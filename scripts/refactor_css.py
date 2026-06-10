import re

with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update CSS Variables for cleaner glass cards
css = css.replace('--glass-bg: rgba(8, 8, 22, 0.82);', '--glass-bg: rgba(8, 8, 22, 0.5);')
css = css.replace('--glass-border: rgba(255, 255, 255, 0.08);', '--glass-border: rgba(255, 255, 255, 0.04);')
css = css.replace('--shadow-card: 0 24px 80px rgba(0, 0, 0, 0.28);', '--shadow-card: 0 12px 32px rgba(0, 0, 0, 0.15);')
css = css.replace('--radius-card: 1.5rem;', '--radius-card: 1rem;')

# 2. Update .tab-button styling
tab_button_old = '''
.tab-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 12px;
  min-height: 44px;
  padding: 0 12px;
  border-radius: var(--radius-btn);
  color: var(--text-muted);
  font-weight: 650;
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
}
'''
tab_button_new = '''
.tab-button {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 10px;
  min-height: 36px;
  padding: 0 10px;
  border-radius: 8px;
  color: var(--text-muted);
  font-weight: 600;
  text-align: left;
  white-space: nowrap;
  overflow: hidden;
  transition: all 0.15s ease;
  border: 1px solid transparent;
}
'''
if '.tab-button {' in css:
    css = re.sub(r'\.tab-button\s*\{[^}]*\}', tab_button_new.strip(), css, count=1)

tab_hover_old = '''
.tab-button:hover,
.tab-button.active {
  background: rgba(255, 255, 255, 0.07);
  border-color: rgba(255, 255, 255, 0.12);
  color: var(--text-primary);
}

.tab-button.active {
  color: var(--brand);
}
'''
tab_hover_new = '''
.tab-button:hover {
  background: rgba(255, 255, 255, 0.03);
  color: var(--text-primary);
}

.tab-button.active {
  background: rgba(255, 255, 255, 0.06);
  color: var(--text-primary);
  font-weight: 700;
}
'''
if '.tab-button:hover,' in css:
    css = css.replace(tab_hover_old.strip(), tab_hover_new.strip())

# 3. Add Nav Group styles
nav_group_styles = '''
.nav-group {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-section-title {
  padding: 0 10px;
  margin-top: 8px;
  margin-bottom: 4px;
  font-size: 0.68rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--text-muted);
  opacity: 0.6;
}

body.sidebar-collapsed .nav-section-title {
  display: none;
}
'''
if '.nav-group' not in css:
    css = css.replace('.tabs {', nav_group_styles + '\n.tabs {')

# Fix `.tabs` gap if exists
css = css.replace('flex-direction: column;\n  gap: 8px;', 'flex-direction: column;\n  gap: 16px;')

with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated styles.css")
