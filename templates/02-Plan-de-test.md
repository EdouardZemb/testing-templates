---
title: "02 — Plan de Test (Test Plan)"
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
  - ISO/IEC/IEEE 29119-3 — Test documentation (structure de plan)
  - ISO/IEC/IEEE 29119-2 — Test processes
  - ISTQB® Glossary — Terminologie
  - ISO/IEC 25010 — Modèle de qualité (NFR)
licence: "CC BY 4.0"
---

# 02 — Plan de Test (Test Plan)

> **But du document** — Décrire **quoi** sera testé, **quand**, **par qui** et **comment**, pour une **release / itération / lot** donné. Précise le périmètre, l’organisation, le calendrier, les ressources, les risques, les critères d’entrée/sortie et les livrables.
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Contexte et périmètre

**Contexte.** `<Synthèse métier/technique : objectifs de la release, contraintes (règlementaires, sécurité), dépendances majeures.>`

**Périmètre testé.** `<Produits/Modules/Épics/US inclus>`

**Hors périmètre.** `<Exclusions + justification>`

**Hypothèses.** `<Stabilité des exigences, disponibilité des environnements et données, jalons externes, SLA d’équipes tierces…>`

---

## 2. Références & artefacts liés

* **Stratégie de test** (01) : `<lien>`
* **Spécification de conception** (03) : `<lien>`
* **Spécification des cas** (04) : `<lien>`
* **Spécification des procédures** (05) : `<lien>`
* **Exigences / backlog** : `<lien(s) JIRA/Squash>`
* **Politiques internes / conformité** : `<sécurité, RGPD, a11y, etc.>`

---

## 3. Éléments testés (Test Items) et interfaces

| Élément / composant | Version / Build | Référence (spec / API) | Interfaces           | Remarques |
| ------------------- | --------------- | ---------------------- | -------------------- | --------- |
| `<module/service>`  | `<v>`           | `<spec/API/CI>`        | `<UI/API/Batch/Msg>` | `<…>`     |

**Dépendances externes.** `<Systèmes tiers, contrats, stubs/mocks prévus>`

---

## 4. Organisation, rôles et responsabilités (RACI)

| Rôle         | Responsabilités                       | Titulaire(s) | RACI |
| ------------ | ------------------------------------- | ------------ | ---- |
| Test Lead    | Planification, pilotage, reporting    | `<Nom>`      | R    |
| Qualité      | Processus, audits, conformité         | `<Nom>`      | A    |
| Testeurs     | Conception/exécution, evidence        | `<Noms>`     | R    |
| Développeurs | Corrections, tests de composant       | `<Noms>`     | C    |
| Métier/PO    | Acceptation, critères métier          | `<Nom>`      | A/I  |
| OPS/SEC/PERF | Environnements, sécurité, performance | `<Noms>`     | C    |

**Canaux & rituels.** `<points quotidiens, revues, comités qualité, synchronisations DEV/OPS>`

---

## 5. Niveaux, types et portée des tests

**Niveaux ciblés.** `Composant, Intégration, Système, E2E/UAT, Non-régression`.

**Types.** `Fonctionnel, Exploratoire, Performance/Charge, Sécurité, Accessibilité, Compatibilité, Résilience, Observabilité`.

**Portée par niveau/type.**

| Niveau      | Types cibles            | Objectifs            | Sorties attendues        |
| ----------- | ----------------------- | -------------------- | ------------------------ |
| Composant   | Unit-like, Contrats     | Détection précoce    | Rapports CI, logs        |
| Intégration | API/Msg/Batch           | Contrats & flux      | Cas/procéd. PASS, traces |
| Système     | Parcours clés           | Oracles métier & NFR | Evidence, métriques      |
| UAT         | Scénarios d’acceptation | Validation métier    | PV d’acceptation         |

---

## 6. Planification (jalons, itérations, exécutions)

> *Adapter à votre cadence (sprint/release). Les charges sont des estimations initiales.*

### 6.1 Jalons

| Jalon | Date cible     | Description                   | Dépendances |
| ----- | -------------- | ----------------------------- | ----------- |
| `M1`  | `<AAAA-MM-JJ>` | Fin de conception (TCN)       | `<…>`       |
| `M2`  | `<AAAA-MM-JJ>` | Cas de test prêts (TCS)       | `<…>`       |
| `M3`  | `<AAAA-MM-JJ>` | Procédures prêtes (TPS)       | `<…>`       |
| `M4`  | `<AAAA-MM-JJ>` | Fin exécution / critères Exit | `<…>`       |
| `M5`  | `<AAAA-MM-JJ>` | Rapport de clôture            | `<…>`       |

### 6.2 Itérations / Vagues d’exécution

| Vague | Période           | Cible                      | Envs    | Jeux de données | Charge (j.h) |
| ----- | ----------------- | -------------------------- | ------- | --------------- | -----------: |
| `V1`  | `<JJ/MM → JJ/MM>` | Smoke + Parcours critiques | `ENV-…` | `DT-…`          |        `<…>` |
| `V2`  | `<…>`             | Régression élargie         | `ENV-…` | `DT-…`          |        `<…>` |
| `V3`  | `<…>`             | UAT & Non-fonctionnel      | `ENV-…` | `DT-…`          |        `<…>` |

### 6.3 Fenêtres quotidiennes (exécution)

| Jour    | Matin            | Après-midi       | Soir / Nuit    |
| ------- | ---------------- | ---------------- | -------------- |
| Lun–Ven | `<campagne/lot>` | `<campagne/lot>` | `<batch/perf>` |

---

## 7. Ressources, charges et compétences

| Rôle           | Nom   | Capacité (j.h) | Compétences clés   | Remarques |
| -------------- | ----- | -------------: | ------------------ | --------- |
| Testeur        | `<…>` |          `<…>` | `<domaine, outil>` | `<…>`     |
| Automatisation | `<…>` |          `<…>` | `<framework>`      | `<…>`     |
| Performance    | `<…>` |          `<…>` | `<injecteur, APM>` | `<…>`     |

**Besoins en formation / onboarding.** `<outils, normes, sécurité, données>`

---

## 8. Environnements & données de test

### 8.1 Environnements

| ID env  | Usage             | Versions clés       | Particularités          | Accès         |
| ------- | ----------------- | ------------------- | ----------------------- | ------------- |
| `ENV-…` | `DEV/INT/REC/PRP` | `<OS, DB, runtime>` | `<flags, données seed>` | `<vault/SSO>` |

**Stubs/mocks/simulateurs** : `<liste + justification>`

### 8.2 Données

| ID jeu | Finalité              | Méthode                                   | Sensible ? | Localisation | Nettoyage          |
| ------ | --------------------- | ----------------------------------------- | ---------: | ------------ | ------------------ |
| `DT-…` | `<alimenter TCN/TCS>` | `synthétique / masqué / semi-synthétique` |  `Oui/Non` | `<repo/BDD>` | `<rollback/purge>` |

**Règles RGPD / sécurité** : `minimisation, anonymisation/masquage, rétention, traçabilité`.

---

## 9. Critères d’entrée (Entry) et de sortie (Exit)

### 9.1 Entry par niveau

| Niveau      | Pré-requis                                               |
| ----------- | -------------------------------------------------------- |
| Composant   | Build OK, tests unitaires ≥ `<seuil>`, artefacts publiés |
| Intégration | Endpoints contractés, stubs prêts, ENV dispo             |
| Système     | Exigences stables, données prêtes, jeux de rôles créés   |
| UAT         | Critères métier définis, jeu de scénario accepté         |

### 9.2 Exit par niveau

| Niveau      | Critères Exit                                           |
| ----------- | ------------------------------------------------------- |
| Composant   | Taux succès `≥ <x>%`, défauts blocants `= 0`            |
| Intégration | Contrats PASS, défauts majeurs `≤ <n>`                  |
| Système     | Couverture TCN/TCS atteinte, risques résiduels acceptés |
| UAT         | PV signé, écarts documentés                             |

---

## 10. Métriques & objectifs de couverture

| Domaine          | Indicateur                            | Cible        |
| ---------------- | ------------------------------------- | ------------ |
| Fonctionnel      | `% exigences critiques (H) couvertes` | `100%`       |
| Conditions (TCN) | `% TCN H couvertes par ≥1 TCS`        | `≥ 95%`      |
| Régression       | `% parcours critiques automatisés`    | `≥ <x>%`     |
| Défauts          | `Taux de fuite (post-prod)`           | `≤ <x/1000>` |
| Perf             | `p95 latence / erreur %`              | `≤ / ≤`      |

**Reporting.** `hebdo/sprint` via tableau de bord ; tendance NRJ (new/resolved/justified).

---

## 11. Gestion des anomalies & non-conformités

**Workflow.** `Nouveau → Tri → En cours → En revue → Résolu → Vérifié → Clos`.

**Severities/Priorities.** `<tableau de définitions>`

**SLA.** `prise en charge, correction, re-test` par sévérité.

**Templates d’anomalie.** `<liens vers modèles/PRÉ-REMPLIS>`

---

## 12. Traçabilité & livrables

**Matrice (aperçu).**

| Exigence (REQ) | Risque (RSK) | Condition (TCN) | Cas (TCS) | Procédure (TPS) | Rapport          |
| -------------- | ------------ | --------------- | --------- | --------------- | ---------------- |
| `REQ-…`        | `RSK-…`      | `TCN-…`         | `TCS-…`   | `TPS-…`         | `Statut/Clôture` |

**Livrables.** `03/04/05 complétés`, `Rapport Statut (08)`, `Rapport Clôture (09)`.

---

## 13. Risques projet & plans de contingence

| ID      | Description |   Prob. |  Impact | Réponse (éviter/mitiger/accepter) | Propriétaire |
| ------- | ----------- | ------: | ------: | --------------------------------- | ------------ |
| `RSK-…` | `<…>`       | `H/M/B` | `H/M/B` | `<plan>`                          | `<nom>`      |

---

## 14. Plan de communication

| Audience          | Message                  | Fréquence   | Canal       | Propriétaire |
| ----------------- | ------------------------ | ----------- | ----------- | ------------ |
| Équipe test       | Avancement, risques      | `Quotidien` | `<standup>` | `<TL>`       |
| Parties prenantes | KPI, décisions           | `Hebdo`     | `<revue>`   | `<Qualité>`  |
| Direction/Client  | Bilan, risques résiduels | `Par jalon` | `<comité>`  | `<PO/TL>`    |

---

## 15. Conformité & écarts normatifs

* **Alignements** : `Terminologie ISTQB`, `Structure ISO 29119-3`, `NFR via ISO 25010`.
* **Écarts / décisions internes** : consignés via `DR-000x` (contexte, décision, impacts).

---

## 16. Liste de contrôle (prête à l’emploi)

* [ ] Périmètre/hors périmètre explicites
* [ ] Rôles/RACI explicités ; canaux/rituels définis
* [ ] Planification jalons & vagues validée
* [ ] Environnements `ENV-…` et jeux `DT-…` disponibles
* [ ] Critères Entry/Exit définis par niveau
* [ ] Objectifs de couverture & métriques définis
* [ ] Risques projet analysés et propriétaires nommés
* [ ] Plan de communication convenu

---

## 17. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

