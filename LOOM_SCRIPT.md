# Loom Demo Script — AI Lead Qualification Agent

Target length: **2-3 minutes**. Read naturally, don't rush. Pause briefly after each
section break (marked with `---`) so you can cut/edit later if needed.

Recording checklist before you hit record:
- [ ] Terminal font size increased (readable on a small Loom window)
- [ ] Close unrelated tabs/apps, clean desktop
- [ ] `leads.csv` and `qualified_leads.csv` open in a code editor tab, ready to show
- [ ] `lead_qualifier.py` open in another tab, ready to show
- [ ] Terminal ready in the project folder, `qualified_leads.csv` deleted or renamed so the run visibly regenerates it live
- [ ] GitHub repo page open in a browser tab for the end

---

## ENGLISH VERSION (Upwork)

**[0:00–0:15] Hook — show yourself or just start on screen recording**

> "Hi, I'm Nicolas — I build AI automation tools for businesses. Let me show you
> a quick example: an agent that reads inbound sales leads and tells your team
> exactly who to call first."

**[0:15–0:35] The problem (screen: show `leads.csv` open in editor)**

> "Here's a typical inbound leads file — messy, unstructured text messages from
> a contact form. Some are hot opportunities, some are just curious, one is
> spam. Reading through these one by one and prioritizing them by hand wastes
> your sales team's time every single day."

**[0:35–0:55] The code (screen: show `lead_qualifier.py`, scroll briefly)**

> "This script sends each lead to Claude, Anthropic's AI model, with a simple
> instruction: score it from 1 to 10, categorize it as Hot, Warm, or Cold, and
> suggest the next action. It's about 90 lines of Python — small, but this is
> the same logic I'd plug into a real CRM or Slack workflow for a client."

**[0:55–1:25] Live run (screen: terminal, run `python lead_qualifier.py`)**

> "Let's run it live."
>
> *(let the terminal output print, narrate over it)*
>
> "You can see it's going through each lead one at a time, calling the AI, and
> in a few seconds it's processed all seven — no manual reading required."

**[1:25–2:00] The result (screen: open `qualified_leads.csv`, scroll through)**

> "And here's the output, sorted hottest lead first. Sarah from Nairobi
> FreshFoods scored a 9 — she has a clear problem, a budget, and a two-week
> timeline, so the recommended action is to call her within 24 hours. Down at
> the bottom, this crypto spam message got flagged as Cold with zero manual
> filtering rules — the AI just understood it wasn't a real lead."

**[2:00–2:20] Why this matters / extensibility**

> "This is a simplified standalone demo. In a real client setup, this would
> plug directly into your contact form or CRM webhook, and push hot leads
> straight into Slack or HubSpot automatically — no CSV required."

**[2:20–2:40] Call to action (screen: GitHub repo page)**

> "Full source code is on my GitHub, link in the description. If your team is
> manually triaging leads, forms, or support tickets, this is exactly the kind
> of automation I build — message me and let's talk about your workflow."

---

## VERSION FRANÇAISE (Malt)

**[0:00–0:15] Accroche**

> « Bonjour, je suis Nicolas — je conçois des outils d'automatisation basés sur
> l'IA pour les entreprises. Je vais vous montrer un exemple concret : un
> agent qui lit les leads entrants et indique à votre équipe commerciale qui
> appeler en priorité. »

**[0:15–0:35] Le problème (écran : `leads.csv` ouvert dans l'éditeur)**

> « Voici un fichier de leads entrants typique — des messages non structurés
> venant d'un formulaire de contact. Certains sont des opportunités chaudes,
> d'autres juste curieux, un est du spam. Les lire un par un et les prioriser
> à la main fait perdre du temps à votre équipe commerciale, chaque jour. »

**[0:35–0:55] Le code (écran : `lead_qualifier.py`, défilement rapide)**

> « Ce script envoie chaque lead à Claude, le modèle d'IA d'Anthropic, avec une
> consigne simple : lui donner un score de 1 à 10, le catégoriser en Chaud,
> Tiède ou Froid, et suggérer la prochaine action. Une centaine de lignes de
> Python — court, mais c'est exactement la logique que j'intègre ensuite dans
> un vrai CRM ou un workflow Slack pour un client. »

**[0:55–1:25] Exécution en direct (écran : terminal, lancer `python lead_qualifier.py`)**

> « On le lance en direct. »
>
> *(laisser défiler la sortie terminal, commenter par-dessus)*
>
> « Vous voyez qu'il traite chaque lead un par un, interroge l'IA, et en
> quelques secondes les sept leads sont traités — sans lecture manuelle. »

**[1:25–2:00] Le résultat (écran : ouvrir `qualified_leads.csv`, défiler)**

> « Et voici le résultat, trié du lead le plus chaud au plus froid. Sarah, de
> Nairobi FreshFoods, obtient un score de 9 — elle a un problème clair, un
> budget, et un délai de deux semaines, donc l'action recommandée est de
> l'appeler sous 24 heures. En bas, ce message de spam crypto est classé Froid
> sans aucune règle de filtrage manuelle — l'IA a simplement compris que ce
> n'était pas un vrai lead. »

**[2:00–2:20] Pourquoi c'est utile / extensibilité**

> « C'est une démo simplifiée. Chez un client, ce système se connecterait
> directement à votre formulaire de contact ou votre CRM, et pousserait les
> leads chauds automatiquement vers Slack ou HubSpot — sans passer par un
> fichier CSV. »

**[2:20–2:40] Appel à l'action (écran : page GitHub du dépôt)**

> « Le code source complet est sur mon GitHub, lien en description. Si votre
> équipe trie encore ses leads, formulaires ou tickets à la main, c'est
> exactement le type d'automatisation que je conçois — contactez-moi pour
> qu'on discute de votre besoin. »
