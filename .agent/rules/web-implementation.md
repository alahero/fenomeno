---
globs: ["**/*.html", "**/*.css", "**/*.js"]
---

# Web Implementation Rule

Implement Fenomeno pages with predictable sections, tokenized styles, and concise copy blocks.

## Apply Structure
- Create semantic sections in this order: hero, concept, highlights, practical info, social proof, footer.
- Keep section IDs stable and readable.
- Keep one clear purpose per section.

## Apply Styling
- Define design tokens in `:root` and consume them everywhere.
- Prefer fluid spacing and type scales with `clamp(...)`.
- Reuse utility classes for recurring layout patterns.

Preferred CSS pattern:

```css
:root {
  --color-bg: #0f0f12;
  --color-text: #f5f5f2;
  --color-accent: #c9a66b;
  --space-2: 0.5rem;
  --space-4: 1rem;
  --space-8: 2rem;
}

.section {
  padding-block: clamp(2rem, 6vw, 5rem);
}

.container {
  width: min(1100px, 92vw);
  margin-inline: auto;
}
```

## Apply Markup
- Use accessible landmarks and heading hierarchy.
- Keep CTAs explicit and action-oriented.
- Keep copy short, high-impact, and consistent with nightlife tone.

Preferred HTML pattern:

```html
<section id="hero" class="section">
  <div class="container">
    <h1>Fenomeno</h1>
    <p>Nights, sound, and atmosphere in Madrid.</p>
    <a href="#visit">Plan your night</a>
  </div>
</section>
```

## Apply JavaScript
- Keep JavaScript progressively enhanced and optional.
- Guard DOM queries before attaching listeners.
- Avoid framework-style abstractions in baseline static mode.

Preferred JS pattern:

```js
const cta = document.querySelector('[data-scroll-cta]');
if (cta) {
  cta.addEventListener('click', () => {
    document.querySelector('#visit')?.scrollIntoView({ behavior: 'smooth' });
  });
}
```

## Enforce Content Discipline
- Derive all brand claims from validated sources.
- Reject invented facts about hours, prices, events, or services.
- Flag missing source data before publishing copy.
