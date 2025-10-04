---
title: "01 — Stratégie de Test (Test Strategy)"
version: "0.1.0"
statut: "draft"
projet: "<Nom du projet / périmètre>"
équipe: "<TRA / équipe de test>"
responsable: "<Nom, rôle>"
reviseurs_attendus:
  - Qualité
  - Test Lead
  - Métier / PO (si applicable)
  - Sécurité / Performance (si applicable)
source_normes:
  - ISO/IEC/IEEE 29119-3 — Test documentation (structure des livrables)
  - ISO/IEC/IEEE 29119-2 — Test processes (cadre processus)
  - ISTQB® Glossary — Terminologie
  - ISO/IEC 25010 — Modèle de qualité (NFR)
  - IEEE 1012 — V&V (notions de traçabilité / intégrité)
licence: "CC BY 4.0"
---

# 01 — Stratégie de Test (Test Strategy)

> **But du document** — Définir l’**approche globale de test** au niveau produit/projet/périmètre, afin d’aligner objectifs, responsabilités, niveaux & types de test, critères d’entrée/sortie, priorisation par le risque, besoins en données et environnements, couverture non-fonctionnelle et modalités de reporting.
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Contexte, objectifs et périmètre

**Contexte.** `<Contexte métier et technique, enjeux, contraintes règlementaires, dépendances majeures>`

**Objectifs qualité (haut niveau).** `<Fiabilité, sécurité, performance, compatibilité, UX, conformité…>`

**Périmètre couvert par la stratégie.** `<Produits/Modules/Épics/Releases>`

**Hors périmètre.** `<Ce qui n’est pas couvert et la justification>`

---

## 2. Références & documents reliés

* **Exigences / Backlog** : `<lien(s) JIRA/Squash/outil>`
* **Politiques / normes internes** : `<sécurité, RGPD, accessibilité, qualité données…>`
* **Plan de test** (02) : `<lien>`
* **Conception de test** (03) : `<lien>`
* **Cas de test** (04) : `<lien>`
* **Procédures** (05) : `<lien>`
* **Autres** : `<charte de dev, DoD, architecture>`

---

## 3. Terminologie et acronymes

| Terme     | Définition     | Source                    |
| --------- | -------------- | ------------------------- |
| `<terme>` | `<définition>` | `ISTQB / interne / autre` |

---

## 4. Modèle de qualité & cibles non-fonctionnelles (ISO 25010)

> *Lister les caractéristiques **NFR** pertinentes, leurs cibles et mesures.*

| Caractéristique | Sous-caractéristique | Indicateur / SLI | Cible / SLO       | Méthode de mesure   | Notes |
| --------------- | -------------------- | ---------------- | ----------------- | ------------------- | ----- |
| Performance     | Efficience temps     | p95 latence      | `≤ <ms>`          | `<injecteur/trace>` | `<…>` |
| Sécurité        | Contrôle d’accès     | violations       | `0` haute gravité | `<scan / test>`     | `<…>` |
| Fiabilité       | Disponibilité        | uptime           | `≥ <99.x>%`       | `<APM>`             | `<…>` |
| Maintenabilité  | Testabilité          | dette test       | `≤ <seuil>`       | `<sonar/metrics>`   | `<…>` |

---

## 5. Niveaux et types de test

**Niveaux.** `Composant, Intégration, Système, End-to-End, UAT, Non-régression`.

**Types (exemples).** `Fonctionnel, Exploratoire, Performance/Charge, Sécurité, Accessibilité, Compatibilité, Robustesse, Observabilité, Résilience (chaos), Portabilité`.

**Couverture par niveau/type.**

| Niveau      | Types cibles        | Objectifs principaux      | Evidence attendue         |
| ----------- | ------------------- | ------------------------- | ------------------------- |
| Composant   | Unit-like, Contrats | Détection précoce         | Rapports unit/integration |
| Intégration | API, messages, jobs | Contrats inter-composants | Logs corrélés, traces     |
| Système     | Parcours clés       | Oracles métier & NFR      | Cas/procédures PASS, KPIs |
| E2E/UAT     | Scénarios métier    | Acceptation               | PV d’acceptation          |

---

## 6. Organisation, responsabilités et RACI

| Rôle         | Responsabilités                        | Titulaire(s) | RACI |
| ------------ | -------------------------------------- | ------------ | ---- |
| Test Lead    | Stratégie, priorisation, consolidation | `<Nom>`      | R    |
| Qualité      | Processus, conformité, audits          | `<Nom>`      | A    |
| Testeurs     | Conception/exécution, evidence         | `<Noms>`     | C    |
| Développeurs | Correction, tests de composant         | `<Noms>`     | C    |
| Métier/PO    | Acceptation, critères métier           | `<Nom>`      | A/I  |

**Canaux & cadences.** `<cérémonies de test, rituels qualité, points de synchronisation>`

---

## 7. Gestion des risques et priorisation

**Méthode.** `Analyse de risque produit > conception par le risque > priorisation des conditions/cas.`

| ID risque | Description |   Prob. |  Impact |  Niveau | Atténuation par test       |
| --------- | ----------- | ------: | ------: | ------: | -------------------------- |
| `RSK-…`   | `<…>`       | `H/M/B` | `H/M/B` | `H/M/B` | `<technique/type de test>` |

**Règles de priorisation.** `<p. ex. priorité = max(risque, criticité métier, usage, dette historique)>`

---

## 8. Approche de test & techniques

**Technique(s) boîte noire.** `Partitions d’équivalence, valeurs limites, tables de décision, transitions d’état, use cases, pairwise`.

**Technique(s) non-fonctionnel.** `Profil de charge, stress/soak, sécurité (OWASP), résilience (chaos), a11y (WCAG)`.

**Exploratoire.** `Sessions timeboxed avec chartes (mission, heuristiques, oracles)`.

**Automatisation (principes).**

* Cible : `régression, parcours stables, contrats, checks non régressifs NFR`.
* Stabilité : `objectif flaky < x% ; quarantaines & triage hebdo`.
* Pipeline : `exécution CI par niveau, rapport JUnit/Allure, badges`.

---

## 9. Critères d’entrée (Entry) et de sortie (Exit)

**Entry (par niveau).**

* Exigences stables / acceptées (DoR).
* Build déployable en `ENV-…` ; dépendances disponibles.
* Données de test prêtes (`DT-…`).

**Exit (par niveau).**

* Couverture atteinte (cf. §10).
* Défauts bloquants : `0` ; majeurs sous contrôle.
* Rapports & evidence collectés ; risques résiduels documentés.

---

## 10. Objectifs de couverture et métriques clés

| Domaine          | Indicateur                            | Cible        |
| ---------------- | ------------------------------------- | ------------ |
| Fonctionnel      | `% exigences critiques (H) couvertes` | `100%`       |
| Conditions (TCN) | `% TCN H couvertes par ≥1 TCS`        | `≥ 95%`      |
| Régression       | `% parcours critiques automatisés`    | `≥ <x>%`     |
| Défauts          | `Taux de fuite (post-prod)`           | `≤ <x/1000>` |
| Perf             | `p95 latence / erreur %`              | `≤ / ≤`      |

**Reporting.** `hebdo/sprint` via tableau de bord ; tendance NRJ (new/resolved/justified).

---

## 11. Environnements, outillage & observabilité

| ID env  | Usage             | Versions clés       | Particularités          | Accès         |
| ------- | ----------------- | ------------------- | ----------------------- | ------------- |
| `ENV-…` | `DEV/INT/REC/PRP` | `<OS, DB, runtime>` | `<flags, données seed>` | `<vault/SSO>` |

**Stubs/Mocks/Simulateurs.** `<liste + justificatif>`

**Observabilité.** `logs, traces, métriques` nécessaires pour les oracles ; corrélation (Trace/Span ID).

---

## 12. Données de test & conformité (RGPD / sécurité)

| ID jeu | Finalité              | Méthode                                   | Sensible ? | Localisation | Nettoyage          |
| ------ | --------------------- | ----------------------------------------- | ---------: | ------------ | ------------------ |
| `DT-…` | `<alimenter TCN/TCS>` | `synthétique / masqué / semi-synthétique` |  `Oui/Non` | `<repo/BDD>` | `<rollback/purge>` |

**Règles.** `minimisation, anonymisation/masquage, traçabilité des extractions, délai de rétention`.

---

## 13. Gestion des défauts & SLA

**Workflow.** `Nouveau → Tri → En cours → En revue → Résolu → Vérifié → Clos`.

**Severities/Priorities.** `<tableau de définition (Blocker/Critique/Majeur/Mineur/Trivial)>`

**SLA.** `prise en charge, correction, re-test` par sévérité et niveau de risque.

---

## 14. Planification & jalons

| Jalons | Date cible     | Description                     | Dépendances |
| ------ | -------------- | ------------------------------- | ----------- |
| `M#`   | `<AAAA-MM-JJ>` | `<ex.: fin conception TCN/TCS>` | `<…>`       |

**Cadence.** `sprint/hebdo` — points de synchronisation QA/DEV/OPS.

---

## 15. Gouvernance des revues & conformité

* **Revues obligatoires :** Qualité + Test Lead, Métier si impact UX/processus.
* **Audits / traçabilité :** exigences ↔ TCN ↔ TCS ↔ TPS ↔ rapports.
* **Écarts normatifs :** consignés via `DR-000x` (contexte, décision, impacts).

---

## 16. Risques, hypothèses, contraintes transverses

| ID      | Description |   Prob. |  Impact | Plan                                 |
| ------- | ----------- | ------: | ------: | ------------------------------------ |
| `RSK-…` | `<…>`       | `H/M/B` | `H/M/B` | `<évitement/mitigation/acceptation>` |

---

## 17. Liste de contrôle (extrait)

* [ ] Périmètre & hors périmètre explicités.
* [ ] Niveaux/types/normes référencés ; responsabilités claires.
* [ ] Critères Entry/Exit mesurables par niveau.
* [ ] Objectifs de couverture fixés (fonctionnels & NFR).
* [ ] Besoins **ENV**/**DT** définis et sécurisés (RGPD/a11y/sécu).
* [ ] Gouvernance des revues & gestion des défauts détaillées.

---

## 18. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

