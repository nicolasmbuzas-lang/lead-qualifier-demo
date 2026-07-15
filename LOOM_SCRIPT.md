# Loom Demo Script — AI Lead Qualification Agent

Target length: **90 seconds**. Tight and punchy — the first 5 seconds decide
whether the viewer keeps watching, so lead with the problem, not a greeting.
Practice reading it out loud once or twice before recording so the pacing feels
natural, not rushed.

Recording checklist before you hit record:
- [ ] Terminal font size increased (readable on a small Loom window)
- [ ] Close unrelated tabs/apps, clean desktop
- [ ] `leads.csv` open in a code editor tab, ready to show
- [ ] Terminal ready in the project folder, `qualified_leads.csv` deleted or renamed so the run visibly regenerates it live
- [ ] GitHub repo page open in a browser tab for the end

---

## ENGLISH VERSION (Upwork)

**[0:00–0:10] Hook + problem (screen: `leads.csv` open)**

> "Hi, I'm Nicolas. Here's a messy inbound leads file — hot opportunities,
> curious browsers, even spam, all mixed together. Sorting this by hand wastes
> your sales team's time every day."

**[0:10–0:40] Live run (screen: terminal, run `python lead_qualifier.py`)**

> "This script sends each lead to Claude, scores it 1 to 10, tags it Hot, Warm,
> or Cold, and suggests the next action. Let's run it live."
>
> *(let the terminal output print, narrate over it)*
>
> "In a few seconds, all seven leads are processed — no manual reading needed."

**[0:40–0:55] The result (screen: open `qualified_leads.csv`, scroll)**

> "Here's the output, sorted hottest first. Sarah's lead scored a 9 — clear
> budget, tight timeline — call her within 24 hours. This crypto spam got
> flagged Cold automatically, zero manual rules."

**[0:55–1:15] Why this matters (extensibility)**

> "This is a simplified demo. In a real setup, this connects straight to your
> contact form or CRM, pushing hot leads into Slack or HubSpot automatically —
> no CSV needed."

**[1:15–1:30] Call to action (screen: GitHub repo page)**

> "Full code's on my GitHub, link below. If your team is manually triaging
> leads or tickets, this is exactly what I build — message me and let's talk."

---

## VERSION FRANÇAISE (Malt)

**[0:00–0:10] Accroche + problème (écran : `leads.csv` ouvert)**

> « Bonjour, je suis Nicolas. Voici un fichier de leads entrants en vrac —
> opportunités chaudes, curieux, et même du spam, tout mélangé. Trier ça à la
> main fait perdre du temps à votre équipe commerciale chaque jour. »

**[0:10–0:40] Exécution en direct (écran : terminal, lancer `python lead_qualifier.py`)**

> « Ce script envoie chaque lead à Claude, lui donne un score de 1 à 10, le
> catégorise Chaud, Tiède ou Froid, et propose la prochaine action. On le
> lance en direct. »
>
> *(laisser défiler la sortie terminal, commenter par-dessus)*
>
> « En quelques secondes, les sept leads sont traités — sans lecture manuelle. »

**[0:40–0:55] Le résultat (écran : ouvrir `qualified_leads.csv`, défiler)**

> « Voici le résultat, trié du plus chaud au plus froid. Le lead de Sarah
> obtient un 9 — budget clair, délai serré — à appeler sous 24 heures. Ce
> spam crypto est classé Froid automatiquement, sans aucune règle manuelle. »

**[0:55–1:15] Pourquoi c'est utile (extensibilité)**

> « C'est une démo simplifiée. Chez un client, ce système se connecterait
> directement à votre formulaire ou votre CRM, et pousserait les leads chauds
> vers Slack ou HubSpot automatiquement — sans passer par un fichier CSV. »

**[1:15–1:30] Appel à l'action (écran : page GitHub du dépôt)**

> « Le code complet est sur mon GitHub, lien en description. Si votre équipe
> trie encore ses leads ou tickets à la main, c'est exactement ce que je
> conçois — contactez-moi pour en discuter. »
