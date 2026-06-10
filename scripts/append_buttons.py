with open('styles.css', 'a', encoding='utf-8') as f:
    f.write('''

/* Primary & Secondary Buttons */
.primary-button { background: var(--brand); color: #04040f; border-color: var(--brand); }
.primary-button:hover:not(:disabled) { background: var(--brand-hover); border-color: var(--brand-hover); box-shadow: 0 0 16px var(--brand-glow); }

.secondary-button { background: rgba(255, 255, 255, 0.08); color: var(--text-primary); border-color: rgba(255, 255, 255, 0.12); }
.secondary-button:hover:not(:disabled) { background: rgba(255, 255, 255, 0.12); border-color: rgba(255, 255, 255, 0.18); }

.ghost-button { background: transparent; border-color: transparent; color: var(--text-muted); }
.ghost-button:hover:not(:disabled) { background: rgba(255, 255, 255, 0.05); color: var(--text-primary); border-color: transparent; }
''')
print("Appended button styles to styles.css")
