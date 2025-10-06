---
title: "03 — Spécification de Conception de Test (Test Design Specification)"
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

# 03 — Spécification de Conception de Test (Test Design Specification)

> **But du document** — Définir *comment* nous dérivons les **conditions de test** et l'**approche de conception** à partir des exigences et risques, en vue de produire des **cas** et **procédures** cohérents, traçables et mesurables.
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires HTML `<!-- … -->` si vous souhaitez garder l'aide à la rédaction dans le fichier.

---

## 1. Objet et périmètre

**Objet.** Décrire le résultat de l'activité de *conception de test* pour le périmètre : `<Périmètre / Release / Epic / Lot>`.

**Hors périmètre.** `<Ce qui n'est pas couvert par cette spécification de conception.>`

**Hypothèses.** `<Hypothèses qui ont guidé la conception (ex.: disponibilité d'un jeu de données anonymisé, API stabilisées, etc.)>`

**Contraintes.** `<Délais, outils imposés, environnements, conformité, etc.>`

---

## 2. Références

* Exigences / User Stories : `<lien(s) référentiel : JIRA/Squash/…>`
* Risques et criticités : `<lien(s) AMDEC / registre des risques>`
* Stratégie / Plan de test : `<lien>`
* Normes et référentiels : `ISO 29119-3`, `ISTQB Glossary`, `ISO 25010`, autres : `<…>`
* Glossaire ISTQB : `standards/glossaire-istqb.md`

<!-- Saisir ici, si connu, les clauses/sections normatives précises qui motivent un choix de conception. -->

---

## 3. Glossaire et acronymes

| Terme     | Définition     | Source                    |
| --------- | -------------- | ------------------------- |
| `<terme>` | `<définition>` | `ISTQB / interne / autre` |

---

## 4. Éléments testés (Test Items) et contexte

| Élément / Composant | Version | Référence       | Interface(s)     | Remarques |
| ------------------- | ------: | --------------- | ---------------- | --------- |
| `<module/service>`  |   `<v>` | `<spec/API/CI>` | `<UI/API/Batch>` | `<…>`     |

**Dépendances & stubs/mocks prévus.** `<Liste + justification>`

---

## 5. Caractéristiques / exigences couvertes

> *Objectif :* lister ce que **cette conception** vise à couvrir. La granularité habituelle est la **caractéristique** (feature) ou l'**exigence** regroupée.

| ID exigence | Intitulé / Caractéristique | Type (F/NF)             | Priorité |  Risque | Remarques |
| ----------- | -------------------------- | ----------------------- | -------: | ------: | --------- |
| `REQ-…`     | `<…>`                      | `F / Perf / Sécu / ...` |  `H/M/B` | `H/M/B` | `<…>`     |

**Caractéristiques exclues / non testées ici.** `<Liste + raison (p.ex. hors release, traité ailleurs, risque faible)>`

---

## 6. Approche de conception et techniques

> *Décrire les **techniques de test** retenues et la **logique** de dérivation des conditions à partir des exigences et risques.*

* **Niveau(x) de test** : `Composant / Intégration / Système / E2E / UAT`.
* **Type(s) de test** : `Fonctionnel, Exploratoire, Performance, Sécurité, Compatibilité, Accessibilité, Robustesse,…`.
* **Techniques** (exemples) :

  * **Boîte noire** : partitions d'équivalence, analyse des valeurs limites, tables de décision, transitions d'état, pairwise, use case testing.
  * **Non-fonctionnel** : profil de charge, scénarios de performance (TPS/latence), abus/malveillance, disponibilité, fiabilité.
  * **Exploratoire** : chartes d'exploration (voir §10).
* **Règles de priorisation** : `<critères : risque, usage, criticité métier, historique incidents, complexité>`
* **Critères de couverture ciblés** : `<p.ex. 100% conditions critiques, 80% combinaisons pairwise, 100% parcours majeurs>`

---

## 7. Conditions de test dérivées (Test Conditions)

> *Les **conditions de test** expriment **quoi** vérifier (idée/objectif de test), sans détailler le **comment** (qui appartiendra aux cas/procédures).* Utiliser des identifiants stables : `TCN-<périmètre>-<n>`.

### 7.1 Registre des conditions

| ID condition | Source (REQ/Risque) | Objectif / Idée de test | Préconditions | Données nécessaires (référence) | Environnement | Priorité | Couverture visée | Rationale (justif. normative ou DR) |
| ------------ | ------------------- | ----------------------- | ------------- | ------------------------------- | ------------- | -------: | ---------------: | ----------------------------------- |
| `TCN-…`      | `REQ-… / RSK-…`     | `<…>`                   | `<…>`         | `<Jeu: DT-…>`                   | `<ENV-…>`     |  `H/M/B` |   `<% ou règle>` | `<ISO 29119-3 §… / DR-…>`           |

### 7.2 Exemples orientés techniques

* **Valeurs limites** : `min, min+1, max-1, max, hors-bornes` pour `<champ/métrique>`.
* **Tables de décision** : `<règles et actions>` → conditions couvrant chaque règle significative.
* **États/transitions** : `<diagramme/référence>` → conditions pour *chemins critiques* et *transitions invalides*.
* **Pairwise** : paramètres `<P1, P2, P3>` → conditions couvrant toutes paires.

---

## 8. Données de test (vue conception)

> *Définir ici **ce qu'il faut** comme données et **comment** on les obtient (synthèse/anonymisation), sans entrer dans le détail des fichiers*. Les artefacts concrets seront référencés.

* **Jeux de données** :

| ID jeu | Finalité            | Méthode d'obtention                       | Localisation / Référence | Sensible ? | Remarques                            |
| ------ | ------------------- | ----------------------------------------- | ------------------------ | ---------: | ------------------------------------ |
| `DT-…` | `<alimenter TCN-…>` | `synthétique / masqué / semi-synthétique` | `<repo / S3 / BDD>`      |  `Oui/Non` | `<conformité RGPD, réutilisabilité>` |

* **Génération / anonymisation** : `<outils/ scripts / contraintes>`
* **Règles de variation** (p.ex. valeurs frontières, formats, locales) : `<…>`

---

## 9. Environnement, outillage et observabilité

| ID env  | Description         | Versions clés       | Outils de test/mesure                | Journalisation / traces         | Remarques |
| ------- | ------------------- | ------------------- | ------------------------------------ | ------------------------------- | --------- |
| `ENV-…` | `<DEV/INT/REC/PRP>` | `<OS, DB, runtime>` | `<frameworks, injecteurs, scanners>` | `<niveau de logs, corrélation>` | `<…>`     |

**Stubs/Mocks/Simulateurs** : `<liste + usage>`

**Observabilité** : métriques, logs, traces, *dashboards* nécessaires pour valider les oracles de test.

---

## 10. Charte(s) d'exploration (si applicable)

> *Pour les sessions de test exploratoire, définir des chartes ciblées.*

| ID charte | Mission                                     | Heuristiques               | Contraintes      | Oracles/Orienteurs             | Durée      |
| --------- | ------------------------------------------- | -------------------------- | ---------------- | ------------------------------ | ---------- |
| `EXP-…`   | `<p.ex. parcours paiement en mode offline>` | `<SFDPOT, CRUSSPIC, etc.>` | `<données, env>` | `<qu'attend-on comme signaux>` | `<90 min>` |

---

## 11. Critères de complétude de la conception

* **Entrée (prêt à concevoir)** : exigences stables, risques qualifiés, env & données *au moins* spécifiés, *Definition of Ready* respectée.
* **Sortie (conception terminée)** :

  * Registre des **conditions** complété et priorisé.
  * Liens de **traçabilité** vers exigences/risques établis.
  * Besoins **données** et **environnements** définis.
  * Critères de **couverture** atteignables et mesurables.

**Mesures** : `% exigences critiques avec ≥1 condition`, `% conditions liées à un risque H couvertes`, etc.

---

## 12. Traçabilité (aperçu)

> *La matrice détaillée peut être maintenue dans l'outil (Squash/JIRA). Conserver ici un extrait ou un lien exportable.*

| Exigence | Risque  | Condition(s) de test | Cas de test (à produire) | Procédures | Incidents |
| -------- | ------- | -------------------- | ------------------------ | ---------- | --------- |
| `REQ-…`  | `RSK-…` | `TCN-…`              | `TCS-…`                  | `TPS-…`    | `DEF-…`   |

---

## 13. Conformité & écarts (normatifs)

* **Alignements** : `Terminologie ISTQB`, `Structure ISO 29119-3`, `NFR via ISO 25010`.
* **Écarts / décisions internes** :

  * `DR-000x — <intitulé>` : `<description courte, raison, impact>`

---

## 14. Risques, contraintes, dépendances spécifiques à la conception

| ID      | Description |   Prob. |  Impact | Stratégie (évitement/mitigation/acceptation) |
| ------- | ----------- | ------: | ------: | -------------------------------------------- |
| `RSK-…` | `<…>`       | `H/M/B` | `H/M/B` | `<…>`                                        |

---

## 15. Règles de nommage & préparation des artefacts suivants

* **Conditions** : `TCN-<périm>-<nnn>`
* **Cas de test** : `TCS-<périm>-<nnn>` (1..n par condition selon la technique)
* **Procédures** : `TPS-<périm>-<nnn>`
* **Jeux de données** : `DT-<périm>-<nnn>`

**Guides de dérivation** :

* 1 condition **→** ≥1 cas couvrant les valeurs/chemins/états définis.
* Paramétrisation privilégiée pour limiter la maintenance.

---

## 16. Plan de revue

* **Relectures requises** : Qualité + Test Lead (obligatoires), Métier (si impact UX/processus).
* **Liste de contrôle (extrait)** :

  * [ ] Toutes les exigences prioritaires ont ≥1 condition liée.
  * [ ] Les techniques choisies sont justifiées vs. risques & objectifs de qualité.
  * [ ] Les besoins en données & environnements sont définis et réalistes.
  * [ ] Les critères de couverture sont mesurables.
  * [ ] Les écarts normatifs sont consignés via DR.

---

## 17. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

