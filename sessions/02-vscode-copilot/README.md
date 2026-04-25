# Session 2 - VS Code + GitHub Copilot

**Speaker:** Imoh Etuk | **Duration:** 20-25 minutes

## Learning Objectives

By completing this session, you will:
- ✅ Use Copilot Chat directly in VS Code for focused code generation
- ✅ Leverage inline suggestions for rapid, iterative coding
- ✅ Apply Copilot to UI/UX improvements and accessibility
- ✅ Use keyboard shortcuts and context attachment for efficiency
- ✅ Explore agent mode for multi-step design changes

---

## What You'll Build

A redesigned **Task Management Web Application** featuring:
- Modern, responsive UI with visual hierarchy
- Accessible semantic HTML and keyboard navigation
- Smooth CSS animations and transitions
- Mobile-first design (375px to 1440px+)
- Professional styling with design tokens (CSS variables)

---

## Quick Start

### Local Preview

```bash
cd sessions/02-vscode-copilot/starter/web
python -m http.server 8080
```

Open **http://127.0.0.1:8080** in your browser.

**Note:** For VS Code live preview, you can also use the Live Server extension (search "Live Server" in Extensions marketplace).

### GitHub Pages Deploy

1. Push this repository to GitHub
2. In repository settings → Pages
3. Select "Deploy from a branch" → main branch → root folder
4. Your site will be live at `https://username.github.io/repo-name/sessions/02-vscode-copilot/starter/web/`

### Static Host Deploy (Netlify, Vercel, Azure Static Web Apps)

Upload the contents of `starter/web/` to your preferred static host.

---

## Demo Flow (Live Demonstration)

Follow this step-by-step flow to demonstrate Copilot's power in VS Code:

### Step 1: Plan Visual Direction
- **Show:** Current web page on screen
- **Do:** Open Copilot Chat and ask for design direction
- **Explain:** How Copilot understands UX principles and suggests modern patterns
- **Result:** Clear CSS design system (colors, typography, spacing)

### Step 2: Implement Design System
- **Show:** The styles.css file
- **Do:** Ask Copilot to create CSS custom properties for design tokens
- **Accept:** Inline suggestions for color values, spacing scales
- **Explain:** Design tokens ensure consistency and maintainability
- **Result:** Complete design system with documented variables

### Step 3: Improve Layout & Hierarchy
- **Show:** HTML structure
- **Do:** Use Copilot Chat to enhance layout with modern CSS
- **Explain:** Flexbox and CSS Grid for responsive, professional layouts
- **Result:** Improved visual hierarchy and spacing

### Step 4: Enhance Accessibility
- **Show:** HTML source code
- **Do:** Ask Copilot for semantic HTML and ARIA improvements
- **Explain:** Accessibility benefits all users and improves SEO
- **Result:** Keyboard-navigable, semantic, accessible design

### Step 5: Add Animations
- **Show:** The styled page
- **Do:** Ask Copilot to add CSS animations
- **Accept:** Inline suggestions for smooth transitions
- **Explain:** Subtle animations improve user experience without distraction
- **Result:** Polished, professional feel

### Step 6: Refactor & Optimize
- **Show:** App.js or CSS that could be improved
- **Do:** Ask Copilot to refactor for readability and performance
- **Explain:** Better code is easier to maintain and debug
- **Result:** Clean, maintainable codebase

---

## Hands-On Challenge

**File:** `challenges/01-challenge.md`

Work through the 7-task challenge to redesign and improve the web app:

1. **Plan visual direction** with Copilot
2. **Implement a design system** (CSS custom properties)
3. **Improve layout & hierarchy** with modern CSS
4. **Enhance accessibility** (semantic HTML, focus states, ARIA)
5. **Add CSS animations** (smooth, performant)
6. **Refactor JavaScript** for readability
7. **Fix responsive issues** on all screen sizes

**Expected time:** 20-25 minutes

---

## VS Code Copilot Features

### Inline Suggestions
- Start typing code and let Copilot suggest the next line
- Press Tab to accept, Escape to dismiss
- Great for repetitive patterns and boilerplate

### Copilot Chat
- Open with `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)
- Ask multi-step questions and get contextual responses
- Paste code blocks for analysis, refactoring, or explanation

### Context Attachment
- Click `@` in Chat to attach specific files or workspace context
- Say `@workspace` to reference your entire project
- Ask Copilot to consider multiple files for consistency

### Agent Mode (Plan)
- Open Chat, select "Plan" mode from the dropdown
- Ask Copilot to propose multi-step changes before implementation
- Review the plan, then ask Copilot to implement it

### Slash Commands
- `/explain` - Explain the selected code
- `/fix` - Suggest fixes for errors
- `/refactor` - Improve code quality
- `/test` - Generate test cases
- `/doc` - Create documentation

---

## Key Prompts Used in This Session

### Visual Direction
```
Propose a bold visual direction and CSS improvements for a task management app.
Consider visual hierarchy, colors, spacing, typography, modern CSS patterns,
accessibility standards, and mobile-first responsive design.
```

### Design System
```
Create a comprehensive CSS design system with:
- Color palette (primary, secondary, accent, semantic colors)
- Typography scale (font sizes, weights, line heights)
- Spacing scale (multiples of 8px or 4px base unit)
- Shadow system (subtle, medium, prominent)
- Border radius system
Use CSS custom properties for all values.
```

### Layout Improvements
```
Improve the visual hierarchy and layout without changing data structure.
Strengthen the header, use CSS Grid/Flexbox for main content, add clear section
separation, improve spacing and alignment. Ensure mobile (320px+) and desktop 
(1200px+) responsiveness.
```

### Accessibility
```
Improve accessibility for this web app. Add semantic HTML (header, nav, main,
section, footer), focus states for keyboard navigation, color contrast (WCAG AA),
keyboard-navigable elements, and ARIA labels where needed.
```

### Animations
```
Add lightweight CSS animations to enhance UX:
- Smooth entrance animation for list items (fade + slide)
- Hover effects on interactive elements
- Loading state animation (optional)
- Smooth transitions for state changes
Keep animations subtle (200-300ms) and performant.
```

---

## Project Structure

```
starter/web/
├── index.html       # Semantic HTML with task list structure
├── styles.css       # Design system + layout + animations
├── app.js           # JavaScript for interactivity (optional)
└── assets/          # Images, icons (if any)
```

---

## File Descriptions

| File | Purpose |
|------|---------|
| `index.html` | Semantic HTML with task management structure |
| `styles.css` | Design tokens (colors, typography, spacing), layout, animations |
| `app.js` | Event handling for task creation, deletion, filtering |

---

## Accessibility Checklist

- [ ] HTML uses semantic elements (header, nav, main, section, footer)
- [ ] All interactive elements have focus states (keyboard visible outlines)
- [ ] Color contrast is WCAG AA (4.5:1 for normal text)
- [ ] All buttons have descriptive labels
- [ ] Page is fully navigable using only keyboard (Tab, Enter, Arrow keys)
- [ ] Images have descriptive alt text (if any)
- [ ] Form inputs have associated labels
- [ ] ARIA attributes used only where semantic HTML is insufficient

---

## Responsive Design Checklist

- [ ] Layout works on 375px (mobile)
- [ ] Layout works on 768px (tablet)
- [ ] Layout works on 1440px (desktop)
- [ ] Touch targets are at least 44px × 44px
- [ ] No horizontal scrolling on any screen size
- [ ] Text is readable at all sizes (minimum 16px for body)
- [ ] Images scale proportionally

---

## Troubleshooting

### "Port 8080 already in use"
**Solution:** Use a different port:
```bash
python -m http.server 8081
```

### Styles not updating after changes
**Solution:** Hard refresh your browser:
- Windows/Linux: Ctrl+Shift+R
- Mac: Cmd+Shift+R

### Copilot suggestions not appearing
**Solution:** 
1. Ensure GitHub Copilot extension is installed and enabled
2. Sign in with your GitHub account
3. Restart VS Code

---

## What's Next?

After this session, explore:
- **Agentic Workflows** for multi-step, autonomous changes (Session 3)
- **Copilot CLI** for terminal-driven development (Session 4)
- **Code Review Workflows** for team collaboration (Session 1)
- **GitHub Copilot Extensions** for domain-specific tasks

---

## Resources & References

- **GitHub Copilot Docs:** https://github.com/features/copilot
- **VS Code Keyboard Shortcuts:** https://code.visualstudio.com/docs/getstarted/keybindings
- **MDN HTML Reference:** https://developer.mozilla.org/en-US/docs/Web/HTML
- **MDN CSS Reference:** https://developer.mozilla.org/en-US/docs/Web/CSS
- **CSS Tricks:** https://css-tricks.com/
- **WCAG Accessibility Guidelines:** https://www.w3.org/WAI/WCAG21/quickref/
- **WebAIM Color Contrast Checker:** https://webaim.org/resources/contrastchecker/

---

## Learning Reflection

At the end of the session, consider:
- 💡 Which Copilot feature was most helpful?
- 🎨 How did the design system improve your workflow?
- ♿ Why is accessibility important for your users?
- 🚀 How could you apply this to your own projects?
