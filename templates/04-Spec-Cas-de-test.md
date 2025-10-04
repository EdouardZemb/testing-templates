---
title: "04 — Spécification de Cas de Test (Test Case Specification)"
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
  - ISO/IEC/IEEE 29119-3 — Test documentation (référence principale)
  - ISO/IEC/IEEE 29119-2 — Test processes (contexte processus)
  - ISTQB® Glossary — Terminologie de test
  - ISO/IEC 25010 — Modèle de qualité (exigences non fonctionnelles)
licence: "CC BY 4.0"
---

# 04 — Spécification de Cas de Test (Test Case Specification)

> **But du document** — Définir les **cas de test** détaillés dérivés des **conditions de test** (cf. `03-Spec-Conception-de-test`), avec leurs **étapes**, **données**, **oracles/attendus**, **pré-/post-conditions**, et métadonnées utiles (priorité, environnement, automatisation, traçabilité).
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires HTML `<!-- … -->` si vous souhaitez garder l'aide à la rédaction dans le fichier.

---

## 1. Objet et périmètre

**Objet.** Spécifier les cas de test couvrant le périmètre : `<Périmètre / Release / Epic / Lot>`.

**Hors périmètre.** `<Ce qui n'est pas couvert dans ce lot de cas de test.>`

**Hypothèses / Contraintes.** `<Hypothèses (ex.: anonymisation disponible), contraintes (outils, environnements, délais), conformité.>`

---

## 2. Références

* Spécification de **conception** (conditions) : `<lien vers 03-Spec-Conception-de-test>`
* Exigences / User Stories : `<lien(s) référentiel : JIRA/Squash/…>`
* Stratégie / Plan de test : `<lien>`
* Normes et référentiels : `ISO 29119-3`, `ISTQB Glossary`, `ISO 25010`, autres : `<…>`

---

## 3. Règles de nommage et structure

* **Cas de test** : `TCS-<périm>-<nnn>` (par ex. `TCS-PAIEMENT-012`).
* **Étapes** : numérotation séquentielle `1..n`.
* **Jeux de données** : `DT-<périm>-<nnn>`.
* **Environnements** : `ENV-<code>` (cf. référentiel d'envs du projet).
* **Traçabilité** : chaque cas **doit** référencer ≥1 **condition de test** `TCN-…` et, si possible, les **exigences** `REQ-…`.

---

## 4. Registre des cas de test (vue synthèse)

> *Vue d'ensemble pour prioriser et planifier. La fiche détaillée de chaque cas est définie au §5.*

| ID cas  | Titre        | Condition(s) couverte(s) | Exigences | Niveau                          | Type                      | Priorité | Risque couvert | Env     | Données (ID) | Automatisation      |
| ------- | ------------ | ------------------------ | --------- | ------------------------------- | ------------------------- | -------: | -------------: | ------- | ------------ | ------------------- |
| `TCS-…` | `<intitulé>` | `TCN-…`                  | `REQ-…`   | `Composant/Int/Système/E2E/UAT` | `Fonctionnel/Perf/Sécu/…` |  `H/M/B` |        `H/M/B` | `ENV-…` | `DT-…`       | `Oui/Non/À évaluer` |

---

## 5. Gabarit de **fiche de cas de test** (à dupliquer par cas)

> Copiez-collez ce bloc pour chaque `TCS-…` et remplacez les valeurs.

### 5.x `TCS-<périm>-<nnn>` — `<Titre du cas>`

**Résumé.** `<Brève description de l'objectif du cas (idée de test)>`

**Liens & traçabilité.**

* Condition(s) : `TCN-…`
* Exigence(s) : `REQ-…`
* Risque(s) : `RSK-…`

**Métadonnées.**

* Niveau : `Composant / Intégration / Système / E2E / UAT`
* Type : `Fonctionnel / Performance / Sécurité / Accessibilité / Compatibilité / Robustesse / …`
* Priorité : `H/M/B`
* Critères de couverture visés : `<ex.: chemins critiques, partitions d'équivalence, limites, paires, etc.>`
* Ordonnancement : `Isolé / Séquence avec TCS-…`
* Fréquence d'exécution : `À chaque build / Quotidien / Sprint / Release / Ad hoc`

**Préconditions.** `<état du système, prérequis fonctionnels/techniques, comptes, droits, configuration>`

**Postconditions.** `<état attendu après exécution, y compris nettoyage/rollback>`

**Environnement.** `ENV-…` — `<version appli, DB, navigateur/OS, flags>`

**Jeux de données.** `DT-…` — `<lien/référence>`

**Oracles / Attendus globaux.** `<règles d'acceptation, assertions non-fonctionnelles, logs/traces à vérifier>`

#### Étapes détaillées

|  # | Action / Entrée | Résultat attendu (oracle) | Données / Notes  |
| -: | --------------- | ------------------------- | ---------------- |
|  1 | `<étape>`       | `<attendu mesurable>`     | `<DT-… champ …>` |
|  2 | `<étape>`       | `<attendu mesurable>`     | `<…>`            |
|  … | …               | …                         | …                |

**Critères d'arrêt** (du cas) : `<conditions qui rendent la suite non pertinente>`

**Critères de réussite** (du cas) : `<conditions pour déclarer PASS>`

**Spécificités non-fonctionnelles** (si applicable) :

* **Performance** : `<latence max p95, débit, erreurs %>`
* **Sécurité** : `<contrôle d'accès, input validation, comportements anormaux refusés>`
* **Accessibilité** : `<règles WCAG ciblées, lecture d'écran, contraste>`

**Automatisation.**

* État : `Non / Envisagée / En cours / Automatisée`
* Cadre : `<framework/outillage>`
* Script/ID pipeline : `<référence>`
* Données paramétrables : `<variables exposées>`
* Stabilité : `Stable / Flaky` — `<dernière observation>`

**Pièces jointes.** `<captures, logs, HAR, traces, liens monitoring>`

**Remarques.** `<dettes, TODO, améliorations>`

---

## 6. Cas **paramétrés** (option)

> Pour limiter la maintenance, privilégier un **cas générique** avec un tableau de **paramètres** (ex.: partitions d'équivalence, bornes, combinaisons pairwise).

### 6.1 Modèle de tableau de paramètres

| Variante | Jeux de données | Paramètres   | Attendus spécifiques   |
| -------: | --------------- | ------------ | ---------------------- |
|        1 | `DT-…`          | `P1=…; P2=…` | `<oracle additionnel>` |
|        2 | `DT-…`          | `…`          | `…`                    |

### 6.2 Recommandations

* Garder le **même ID** de cas (`TCS-…`) et numéroter les variantes `TCS-…-V01`.
* Isoler les **oracles** qui varient afin d'éviter la duplication des étapes.
* Pour l'automatisation, exposer les **paramètres** via **data providers** ou CSV.

---

## 7. Données de test (rappel)

| ID jeu | Finalité            | Contenu clé              | Source / Méthode                          | Sensible ? | Localisation              |
| ------ | ------------------- | ------------------------ | ----------------------------------------- | ---------: | ------------------------- |
| `DT-…` | `<alimenter TCS-…>` | `<champs, cardinalités>` | `synthétique / masqué / semi-synthétique` |  `Oui/Non` | `<repo / BDD / stockage>` |

**Règles de nettoyage** : `<purge, rollback, réinitialisation>`

---

## 8. Environnements & observabilité

| ID env  | Description   | Versions            | Outils de test/mesure                | Journalisation / traces         | Remarques |
| ------- | ------------- | ------------------- | ------------------------------------ | ------------------------------- | --------- |
| `ENV-…` | `<REC/PRP/…>` | `<OS, DB, runtime>` | `<frameworks, injecteurs, scanners>` | `<niveau de logs, corrélation>` | `<…>`     |

**Observabilité** : métriques, logs, traces, *dashboards* nécessaires pour valider les oracles.

---

## 9. Couverture & métriques

* `% de conditions (TCN) couvertes par ≥1 cas (TCS)`
* `% d'exigences critiques (REQ priorité H) couvertes`
* `Distribution H/M/B des priorités de cas`
* `Taux de stabilité des cas automatisés (flaky rate)`

> *Visualisations possibles : heatmap REQ↔TCN↔TCS, répartition des techniques par risque.*

---

## 10. Plan de revue

* **Relectures requises** : Qualité + Test Lead (obligatoires), Métier (si impact UX/processus).
* **Liste de contrôle (extrait)** :

  * [ ] Chaque `TCS-…` référence au moins une `TCN-…` (traçabilité amont).
  * [ ] Les **oracles** sont **mesurables** et sans ambiguïté.
  * [ ] Les **pré/post-conditions** sont complètes (données, droits, état système).
  * [ ] Les **données** et **environnements** référencés existent et sont accessibles.
  * [ ] Les cas non-fonctionnels définissent des **seuils quantitatifs**.
  * [ ] Les **écarts** aux normes sont documentés via DR.
  * [ ] Les cas destinés à l'automatisation identifient **paramètres** et **stabilité**.

---

## 11. Conformité & écarts (normatifs)

* **Alignements** : `Terminologie ISTQB`, `Structure ISO 29119-3`, `NFR via ISO 25010`.
* **Écarts / décisions internes** :

  * `DR-000x — <intitulé>` : `<description courte, raison, impact>`

---

## 12. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

---

## Annexe A — Gabarit **CSV** pour cas paramétrés (option)

```csv
variant,id_tcs,id_tcn,id_req,id_dt,env,param_P1,param_P2,expected_notes
1,TCS-PAIEMENT-012,TCN-PAIEMENT-003,REQ-PAI-021,DT-PAIEMENT-005,ENV-REC,100,EUR,"p95<=300ms"
```

## Annexe B — Gabarit **Gherkin** (option)

```gherkin
Feature: <Fonctionnalité>
  # Lier la feature aux exigences / conditions de test
  # REQ: REQ-… | TCN: TCN-…

  Scenario: <Titre du cas>
    Given <préconditions>
    And <données/état nécessaires>
    When <action>
    Then <résultat attendu mesurable>
    And <oracle additionnel>
```

