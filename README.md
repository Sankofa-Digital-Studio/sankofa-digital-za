# Sankofa Digital ZA Website

Multi-page static business website for Sankofa Digital ZA.

## Structure

- `dist/index.html` is the home page.
- `dist/services.html` describes the studio offer.
- `dist/work.html` presents five public-safe product summaries.
- `dist/about.html`, `dist/process.html` and `dist/contact.html` explain the studio and conversion path.
- `dist/privacy.html` and `dist/terms.html` provide launch-ready legal information for the current static implementation.
- `dist/assets/css/styles.css` contains the responsive design system.
- `dist/assets/js/main.js` controls navigation, reveal behaviour and prepared email or WhatsApp enquiries.

## Contact behaviour

The website does not store enquiry data. The contact form opens the visitor's email application or WhatsApp with a prepared message. If a server-side form or CRM is added later, update the privacy notice before launch.

## Product claim policy

Portfolio copy distinguishes controlled pilots, internal systems, MVPs and evaluation products. Do not add delivery counts, customer counts, testimonials or production claims without supporting evidence and publication approval.

## Hosting

The Sites project identity and static directory are declared in `.openai/hosting.json`. Publish the `dist` directory through the Sites workflow after checks and source synchronization.

## Local preview

Serve the project root and open `/dist/`, or serve the `dist` directory directly with a local static server. Do not open the HTML files directly when checking navigation and form behaviour.
Run python server: `python -m http.server`
