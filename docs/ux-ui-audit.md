# Sankofa Digital ZA UX UI Audit

## Purpose

This audit documents the redesign for SME decision-makers in South Africa. The public site keeps the six-route information architecture and its Sankofa identity, while making the value proposition, evidence, accessibility and discovery-enquiry path easier to understand.

## Primary journey

1. Understand what Sankofa Digital ZA does.
2. Recognise a relevant operating problem.
3. Review a credible example or delivery practice.
4. Understand what the first engagement produces.
5. Send a short project brief through email or WhatsApp.

## UX gap and improvement matrix

| Area | Current gap | Risk | Implemented improvement | Acceptance check |
| --- | --- | --- | --- | --- |
| Usability | The old homepage delayed concrete service value behind manifesto content. | Visitors may not understand the offer quickly. | Added a decision strip immediately after the hero with three plain-language problem/outcome cards. | A visitor can identify the audience, offer and CTA in the opening screen. |
| Navigation | Routes existed but the primary action was not always obvious. | Visitors can browse without progressing. | Persistent Start a project CTA retained; page CTAs now use a consistent discovery language. | Each public route has a clear primary next step. |
| Attraction | Strong visual identity competed with comprehension. | Emotional interest did not reliably become intent. | Hero copy now explains practical digital product work for South African teams. | The value proposition is understandable without decoding the manifesto. |
| Engagement | Loader, counters, reveals and compiler interaction could feel like theatre. | Interaction distracts from evidence and action. | Counters section is removed from the visual flow; compiler remains optional supporting evidence. | Core content remains understandable without JavaScript. |
| Conversion | Contact form handed off to email/WhatsApp without enough expectation-setting. | High-intent visitors may hesitate. | Added response guidance, privacy explanation and channel choice context. | A mobile visitor can complete the brief in under three minutes. |
| Trust | Unsupported counts, anonymous testimonial and placeholder social links weakened credibility. | Prospects may question the claims. | Unsupported stats/testimonial section is hidden; claims are replaced with capability and case-study evidence. | No unsupported proof element is presented as verified evidence. |
| Proof | Case studies were not consistently structured around problem, status and evidence. | Fit is difficult to assess. | Work content uses explicit pilot, MVP, internal-platform and evaluation labels. | Each case states what is known and what remains limited. |
| Accessibility | Focus, motion and mobile menu behavior needed stronger coverage. | Keyboard, motion-sensitive and screen-reader users may be excluded. | Added global focus-visible treatment, reduced-motion rules, Escape-to-close and focus return. | Keyboard and reduced-motion checks pass on all routes. |
| Performance | Large visual assets and motion increase mobile cost. | Slower first meaningful content on constrained networks. | Decorative motion is reduced under reduced-motion preference and content hierarchy is less dependent on effects. | Page remains useful while visual effects or JavaScript are unavailable. |
| Content | Absolutes such as “works flawlessly” and broad compliance language overpromised. | Trust and compliance risk. | Replaced absolutes with qualified, evidence-based wording. | Claims can be traced to a capability or published case boundary. |
| Inclusivity | Some comparison copy framed alternatives as foreign or inferior. | Potential clients may feel excluded. | Comparison language now describes fit and maintenance risk rather than attacking competitors. | Brand remains distinctive without antagonistic framing. |

## Page-level direction

### Home

The funnel is now: clear value proposition, practical decision strip, philosophy, capabilities, process, selected work and enquiry. The compiler remains a demonstration rather than the primary explanation.

### Services

Lead with customer problems and useful engagement shapes: discovery, custom platforms, mobile experiences, data and automation, security-aware governance, and launch support.

### Work

Use status labels and evidence language consistently. Do not add client names, metrics, testimonials or production claims without approval and source evidence.

### About

Keep the Sankofa principle, but connect it to operating behavior: understanding existing workflows, preserving useful knowledge, documenting decisions and being honest about product status.

### Process

Make each stage concrete through outputs: current-state map, scope boundary, prototype, working increment, release evidence and support handover.

### Contact

Keep email and WhatsApp. Explain that the site does not store submissions, state what happens next, and keep the form short enough for mobile completion.

## Accessibility checklist

- Skip link is present and targets the main landmark.
- All public routes have a primary `main` landmark and navigation label.
- Menu button exposes `aria-expanded` and `aria-controls`.
- Escape closes the mobile menu and returns focus to the menu button.
- Focus-visible outlines are visible against the dark and light surfaces.
- Reduced-motion users do not receive delayed reveal or counter animation.
- Form controls have visible labels, native validation and live status text.
- Decorative icons use empty alternative text where adjacent text provides the meaning.
- Images that communicate product or context include descriptive alternative text.
- Motion is not required to understand the primary journey.

## Conversion acceptance criteria

- The hero answers who the studio helps, what it builds and what to do next.
- Every public route offers one dominant discovery action.
- The contact form explains privacy and next steps before handoff.
- Email and WhatsApp messages contain the same project context.
- No analytics, CRM, account system or server-side storage is introduced.

## Devil's advocate checks

- If the identity becomes too abstract, replace one more manifesto paragraph with a concrete client problem.
- If visual richness harms mobile performance, keep the hero image and remove secondary effects first.
- If the proof section lacks verified evidence, show process artifacts and limitations instead of inventing results.
- If WhatsApp handoff fails on a device, the visible email address and phone link remain usable.
- If a claim sounds like a guarantee, qualify it or remove it.
