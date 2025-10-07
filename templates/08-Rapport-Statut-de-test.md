---
title: "08 — Rapport de Statut de Test (Test Status Report)"
version: "0.1.0"
statut: "draft"
projet: "<Nom du projet / périmètre>"
équipe: "<TRA / équipe de test>"
responsable: "<Nom, rôle>"
reviseurs_attendus:
  - Qualité
  - Test Lead
  - Métier / PO (si applicable)
source_normes:
  - ISO/IEC/IEEE 29119-3 — Test documentation (contenu du statut)
  - ISTQB® Glossary — Terminologie
  - ISO/IEC 25010 — Modèle de qualité (NFR)
licence: "CC BY 4.0"
---

# 08 — Rapport de Statut de Test (Test Status Report)

> **But du document** — Communiquer l’**état d’avancement** des tests sur la période : couverture, résultats, défauts, risques, disponibilité des environnements/données, écarts et décisions. Sert de base aux **arbitrages** et **plans d’action**.
>
> **À remplir** — Remplacer les `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Synthèse exécutive (RAG)

| Dimension                | Statut | Commentaire clé      | Décision / Reco       |
| ------------------------ | -----: | -------------------- | --------------------- |
| Portée / Couverture      | 🟢🟡🔴 | `<points marquants>` | `<décision proposée>` |
| Résultats (PASS/FAIL)    | 🟢🟡🔴 | `<…>`                | `<…>`                 |
| Défauts / Qualité        | 🟢🟡🔴 | `<…>`                | `<…>`                 |
| Environnements / Données | 🟢🟡🔴 | `<…>`                | `<…>`                 |
| Planning / Jalons        | 🟢🟡🔴 | `<…>`                | `<…>`                 |

**Faits saillants.**

* `+` `<succès ou avancement notable>`
* `–` `<blocage/risk>`

**Décisions à prendre.** `<liste courte avec options>`

---

## 2. Périmètre & références

**Périmètre testé.** `<modules, US, caractéristiques>`

**Hors périmètre.** `<exclusions de la période>`

**Références.**

* Stratégie (01) : `templates/01-Strategie-de-test.md`
* Plan de test (02) : `templates/02-Plan-de-test.md`
* Conception (03), Cas (04), Procédures (05) : `<liens>`
* Plan Données (06) / Exigences Environnement (07) : `<liens>`

---

## 3. Avancement global (exécution)

### 3.1 Résultats de la période

| Indicateur                                  |    Valeur | Δ (vs période -1) |
| ------------------------------------------- | --------: | ----------------: |
| Cas exécutés (nb)                           |     `<N>` |            `<±n>` |
| PASS (nb / %)                               | `<N / %>` |       `<±n / ±p>` |
| FAIL (nb / %)                               | `<N / %>` |       `<±n / ±p>` |
| BLOCKED/NA (nb / %)                         | `<N / %>` |       `<±n / ±p>` |
| Taux d’exécution (cas exécutés / planifiés) |     `<%>` |            `<±p>` |

### 3.2 Couverture fonctionnelle

| Indicateur                          | Valeur |    Cible |
| ----------------------------------- | -----: | -------: |
| % exigences critiques (H) couvertes |  `<%>` |   `100%` |
| % TCN priorité H avec ≥1 TCS        |  `<%>` |  `≥ 95%` |
| % parcours critiques automatisés    |  `<%>` | `≥ <x>%` |

### 3.3 Détail par niveau/type (option)

| Niveau      | Planifiés | Exécutés |  PASS |  FAIL | Blocages majeurs |
| ----------- | --------: | -------: | ----: | ----: | ---------------- |
| Composant   |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`            |
| Intégration |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`            |
| Système     |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`            |
| UAT         |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`            |

---

## 4. Défauts / Qualité

### 4.1 Vue d’ensemble

| Indicateur                                                 |      Valeur | Δ (vs période -1) |
| ---------------------------------------------------------- | ----------: | ----------------: |
| Défauts ouverts (total)                                    |       `<N>` |            `<±n>` |
| Ouverts par sévérité (Bloquants/Critiques/Majeurs/Mineurs) | `<n/n/n/n>` |       `<±/±/±/±>` |
| Défauts créés (période)                                    |       `<N>` |            `<±n>` |
| Défauts résolus (période)                                  |       `<N>` |            `<±n>` |
| Temps moyen de correction (MTTR)                           |     `<j/h>` |             `<±>` |
| Taux de réouverture                                        |       `<%>` |             `<±>` |

### 4.2 Répartition & tendances

| Catégorie         | % (top) | Commentaire      |
| ----------------- | ------: | ---------------- |
| `<fonction/zone>` |   `<%>` | `<observations>` |
| `<type défaut>`   |   `<%>` | `<observations>` |

**Défauts notables.** `<liste courte avec liens et impacts>`

---

## 5. Non-fonctionnel (NFR) — résultats vs cibles

| Domaine       | Indicateur                   |      Cible |     Résultat | Écart |
| ------------- | ---------------------------- | ---------: | -----------: | ----: |
| Performance   | p95 latence                  |   `≤ <ms>` |       `<ms>` | `<±>` |
| Disponibilité | uptime env REC               |  `≥ 99.x%` |        `<%>` | `<±>` |
| Sécurité      | Vulnérabilités haute gravité |        `0` |        `<n>` | `<±>` |
| Accessibilité | Conformité WCAG              | `<niveau>` | `<résultat>` | `<±>` |

**Tests menés.** `<k6/jmeter, ZAP/DAST, audits a11y, etc.>`

---

## 6. Environnements & données

| Indicateur                              | Valeur | Commentaire                 |
| --------------------------------------- | -----: | --------------------------- |
| Disponibilité env (REC/PRP)             |  `<%>` | `<incidents, maintenances>` |
| Incidents env (période)                 |  `<N>` | `<résumé>`                  |
| Données prêtes (% TCN couvertes par DT) |  `<%>` | `<jeux manquants>`          |
| Problèmes de données                    |  `<N>` | `<qualité, masquage, seed>` |

**Incidents majeurs & impacts.** `<liste courte>`

---

## 7. Risques & problèmes

| ID      | Description |   Prob. |  Impact |  Niveau | État          | Plan / Action  |
| ------- | ----------- | ------: | ------: | ------: | ------------- | -------------- |
| `RSK-…` | `<…>`       | `H/M/B` | `H/M/B` | `H/M/B` | `ouvert/clos` | `<mitigation>` |

**Nouveaux risques** : `<…>`

**Risques clôturés** : `<…>`

---

## 8. Écarts / décisions (normatifs & internes)

* **Écarts** aux modèles/standards : `DR-000x — <intitulé>` → `<raison, impact>`
* **Décisions prises** (comité qualité/métier) : `<liste datée>`
* **Décisions en attente** : `<liste + propriétaire>`

---

## 9. Actions & prochains pas

|      ID | Action | Propriétaire | Échéance       | Statut                 |
| ------: | ------ | ------------ | -------------- | ---------------------- |
| `A-001` | `<…>`  | `<Nom>`      | `<AAAA-MM-JJ>` | `ouvert/en cours/clos` |

**Prochaines activités** (période +1) : `<campagnes, UAT, non-fonctionnel, corrections>`

---

## 10. Détail par lot/campagne (option)

| Campagne / Lot | Étendue         | Exécutés |  PASS |  FAIL | Blocages | Commentaire |
| -------------- | --------------- | -------: | ----: | ----: | -------: | ----------- |
| `<Lot-1>`      | `<parcours/us>` |    `<…>` | `<…>` | `<…>` |    `<…>` | `<…>`       |

---

## 11. KPI de pilotage (récap)

* **Exécution** : taux d’exécution, PASS%, rythme quotidien
* **Couverture** : % REQ H couvertes ; % TCN H avec ≥1 TCS
* **Défauts** : ouverts / résolus / réouverture ; MTTR ; âges > *n* jours
* **NFR** : écart vs SLO (perf, dispo, sécu, a11y)
* **Envs/DT** : disponibilité, incidents, readiness

---

## 12. Annexes

* **Exports détaillés** : cas/procédures exécutés, journaux, métriques
* **Graphiques** (option) : courbe d’exécution, burn-up, histogramme défauts, tendance PASS/FAIL
* **Liens** : dashboards, runs CI, tickets majeurs

---

## 13. Liste de contrôle du rapport (DoD)

* [ ] Périmètre & période explicités (§2)
* [ ] Avancement chiffré & couverture fournis (§3)
* [ ] Défauts analysés (quantité, sévérité, tendances) (§4)
* [ ] NFR vs cibles documentés (§5)
* [ ] Environnements/données évalués (§6)
* [ ] Risques & actions à jour (§7–9)
* [ ] Décisions/écarts consignés (§8)

---

## 14. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |


* Conventions d'identifiants : `standards/conventions-identifiants.md`
