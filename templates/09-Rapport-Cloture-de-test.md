---
title: "09 — Rapport de Clôture de Test (Test Completion Report)"
version: "0.1.0"
statut: "draft"
projet: "<Nom du projet / périmètre>"
équipe: "<TRA / équipe de test>"
responsable: "<Nom, rôle>"
reviseurs_attendus:
  - Qualité
  - Test Lead
  - Métier / PO
  - Sécurité / Performance (si applicable)
source_normes:
  - ISO/IEC/IEEE 29119-3 — Test documentation (contenu du rapport de clôture)
  - ISTQB® Glossary — Terminologie
  - ISO/IEC 25010 — Modèle de qualité (NFR)
licence: "CC BY 4.0"
---

# 09 — Rapport de Clôture de Test (Test Completion Report)

> **But du document** — Synthétiser les **résultats finaux** de la campagne : portée réellement testée, couverture, résultats, défauts restants, **atteinte des critères Exit**, **risques résiduels**, **leçons apprises** et **recommandations**. Sert à **statuer** sur l’acceptation de la release et à **capitaliser** pour les cycles suivants.
>
> **À remplir** — Remplacer les `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Synthèse exécutive (décision)

| Dimension      | Statut final | Commentaire clé                         | Décision                          |
| -------------- | -----------: | --------------------------------------- | --------------------------------- |
| Critères Exit  |       🟢🟡🔴 | `<atteints/partiellement/KO>`           | `<Go / Go avec réserves / No-Go>` |
| Couverture     |       🟢🟡🔴 | `<% TCN H, % REQ H, % régression auto>` | `<…>`                             |
| Défauts        |       🟢🟡🔴 | `<ouverts par sévérité>`                | `<…>`                             |
| NFR            |       🟢🟡🔴 | `<perf/sécu/a11y vs SLO>`               | `<…>`                             |
| Envs & Données |       🟢🟡🔴 | `<disponibilité, incidents>`            | `<…>`                             |

**Décision proposée par QA/Test Lead :** `<Go / Go avec réserves / No-Go>` — **Motifs principaux :** `<…>`

---

## 2. Périmètre final & références

**Périmètre testé vs prévu.**

| Élément       | Prévu | Réalisé |  Écart | Commentaire |
| ------------- | ----- | ------- | -----: | ----------- |
| Modules/US    | `<…>` | `<…>`   | `<±…>` | `<…>`       |
| Niveaux/types | `<…>` | `<…>`   | `<±…>` | `<…>`       |

**Références.** Stratégie (01) · Plan (02) · Conception (03) · Cas (04) · Procédures (05) · Données (06) · Environnements (07) · Rapports de statut (08).

---

## 3. Résultats d’exécution (final)

| Indicateur                                  |    Valeur |
| ------------------------------------------- | --------: |
| Cas exécutés (total)                        |     `<N>` |
| PASS (nb / %)                               | `<N / %>` |
| FAIL (nb / %)                               | `<N / %>` |
| BLOCKED/NA (nb / %)                         | `<N / %>` |
| Taux d’exécution (cas exécutés / planifiés) |     `<%>` |

**Détail par niveau/type (option).**

| Niveau      | Planifiés | Exécutés |  PASS |  FAIL | Principaux blocages |
| ----------- | --------: | -------: | ----: | ----: | ------------------- |
| Composant   |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`               |
| Intégration |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`               |
| Système     |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`               |
| UAT         |     `<…>` |    `<…>` | `<…>` | `<…>` | `<…>`               |

---

## 4. Couverture & traçabilité

| Domaine                 | Indicateur             | Résultat |    Cible |
| ----------------------- | ---------------------- | -------: | -------: |
| Exigences critiques (H) | `% REQ(H) couvertes`   |    `<%>` |   `100%` |
| Conditions (TCN)        | `% TCN(H) avec ≥1 TCS` |    `<%>` |  `≥ 95%` |
| Parcours critiques (NR) | `% automatisés`        |    `<%>` | `≥ <x>%` |

**Matrice (extrait).**

| REQ     | RSK     | TCN     | TCS     | TPS     | Résultat    |
| ------- | ------- | ------- | ------- | ------- | ----------- |
| `REQ-…` | `RSK-…` | `TCN-…` | `TCS-…` | `TPS-…` | `PASS/FAIL` |

---

## 5. Défauts restants & dette

### 5.1 Défauts ouverts à la clôture

| Sévérité         | Ouverts | Acceptés en release ? | Condition de suivi                      |
| ---------------- | ------: | --------------------: | --------------------------------------- |
| Bloquants        |   `<n>` |                 `Non` | `—`                                     |
| Critiques        |   `<n>` |             `Oui/Non` | `<patch X / release Y / contournement>` |
| Majeurs          |   `<n>` |             `Oui/Non` | `<…>`                                   |
| Mineurs/Trivials |   `<n>` |             `Oui/Non` | `<…>`                                   |

**Analyse des causes principales** (Pareto) : `<types, zones, patterns>`

### 5.2 Dette de test

| Domaine        | Dette            | Impact     | Recommandation               | Priorité |
| -------------- | ---------------- | ---------- | ---------------------------- | -------- |
| Automatisation | `<lacune NR>`    | `<risque>` | `<couverture cible + outil>` | `H/M/B`  |
| Données        | `<jeu manquant>` | `<risque>` | `<génération/masquage>`      | `H/M/B`  |
| Environnements | `<instabilité>`  | `<risque>` | `<observabilité/ressources>` | `H/M/B`  |

---

## 6. NFR : résultats vs SLO

| Domaine       | Indicateur                   |        SLO |     Résultat | Écart | Commentaire |
| ------------- | ---------------------------- | ---------: | -----------: | ----: | ----------- |
| Performance   | p95 latence                  |   `≤ <ms>` |       `<ms>` | `<±>` | `<…>`       |
| Disponibilité | uptime env PRP/REC           |  `≥ 99.x%` |        `<%>` | `<±>` | `<…>`       |
| Sécurité      | Vulnérabilités haute gravité |        `0` |        `<n>` | `<±>` | `<…>`       |
| Accessibilité | Conformité WCAG              | `<niveau>` | `<résultat>` | `<±>` | `<…>`       |

---

## 7. Critères de **sortie (Exit)** — évaluation

| Critère           | Cible                      |    État | Preuve                |
| ----------------- | -------------------------- | ------: | --------------------- |
| Couverture Reqs H | `100%`                     | `OK/KO` | `Matrice traçabilité` |
| Défauts blocants  | `0`                        | `OK/KO` | `Exports défauts`     |
| NFR clés          | `Toutes dans les SLO`      | `OK/KO` | `Rapports perf/sécu`  |
| Documentation     | `Livrables 03/04/05/08/09` | `OK/KO` | `Liens`               |

---

## 8. Risques résiduels & acceptation

| ID      | Risque résiduel |   Prob. |  Impact | Justification d’acceptation       | Propriétaire | Suivi               |
| ------- | --------------- | ------: | ------: | --------------------------------- | ------------ | ------------------- |
| `RSK-…` | `<…>`           | `H/M/B` | `H/M/B` | `<raison + mitigations en place>` | `<Nom>`      | `<ticket/échéance>` |

**Réserves** (si Go avec réserves) : `<conditions, délais, critères de levée>`

---

## 9. Leçons apprises

| Thème          | Observation | Impact | Action d’amélioration |
| -------------- | ----------- | ------ | --------------------- |
| Organisation   | `<…>`       | `<…>`  | `<…>`                 |
| Processus      | `<…>`       | `<…>`  | `<…>`                 |
| Outils/CI      | `<…>`       | `<…>`  | `<…>`                 |
| Données/ENV    | `<…>`       | `<…>`  | `<…>`                 |
| Automatisation | `<…>`       | `<…>`  | `<…>`                 |

**Retours des parties prenantes** : `<extraits ou liens>`

---

## 10. Recommandations & plan d’actions

|      ID | Recommandation | Bénéfice attendu | Propriétaire | Échéance       | Statut   |
| ------: | -------------- | ---------------- | ------------ | -------------- | -------- |
| `R-001` | `<…>`          | `<…>`            | `<Nom>`      | `<AAAA-MM-JJ>` | `ouvert` |

**Améliorations prioritaires** (Top 3) : `<liste courte>`

---

## 11. Indicateurs globaux & ROI (option)

| Indicateur                        |     Valeur | Commentaire    |
| --------------------------------- | ---------: | -------------- |
| Taux de fuite (post-prod) attendu | `<x/1000>` | `<estimation>` |
| Temps moyen de détection          |      `<h>` | `<…>`          |
| Taux d’automatisation NR          |      `<%>` | `<…>`          |

---

## 12. Signatures / approbations

| Rôle      | Nom     | Décision                    | Date           | Commentaire |
| --------- | ------- | --------------------------- | -------------- | ----------- |
| Test Lead | `<Nom>` | `Go/Go avec réserves/No-Go` | `<AAAA-MM-JJ>` | `<…>`       |
| Qualité   | `<Nom>` | `Approuve / Réserve`        | `<…>`          | `<…>`       |
| Métier/PO | `<Nom>` | `Accepte / Refuse`          | `<…>`          | `<…>`       |

---

## 13. Annexes

* **Exports détaillés** : exécution, défauts, logs, métriques
* **Rapports NFR** : performance, sécurité, a11y
* **Matrice de traçabilité complète**
* **Décisions/DR liés**

---

## 14. Liste de contrôle de clôture (DoD)

* [ ] Tous les livrables sont archivés et référencés (03/04/05/08/09)
* [ ] Critères **Exit** évalués et statutés (§7)
* [ ] Risques **résiduels** documentés avec propriétaires (§8)
* [ ] Défauts restants et réserves **acceptés** (signature)
* [ ] **Leçons apprises** et **recommandations** formalisées (§9–10)
* [ ] **Décision** d’acceptation consignée (§1 & §12)

---

## 15. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

