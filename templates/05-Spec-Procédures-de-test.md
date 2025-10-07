---
title: "05 — Spécification de Procédures de Test (Test Procedure Specification)"
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

# 05 — Spécification de Procédures de Test (Test Procedure Specification)

> **But du document** — Décrire les **procédures d'exécution** qui orchestrent un ou plusieurs **cas de test** (TCS) dans un **ordre contrôlé**, avec préparation d'environnement et de données, critères d'arrêt, collecte d'évidences et nettoyage.
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires HTML `<!-- … -->` si vous souhaitez garder l'aide à la rédaction.

---

## 1. Objet et périmètre

**Objet.** Spécifier les **procédures** à exécuter pour le périmètre : `<Périmètre / Release / Epic / Lot>`.

**Hors périmètre.** `<Ce qui n'est pas couvert par ces procédures.>`

**Hypothèses / Contraintes.** `<Hypothèses (ex.: anonymisation disponible), contraintes (outils, environnements, délais), conformité.>`

---

## 2. Références

* Spécification de **conception** (conditions) : `<lien vers 03-Spec-Conception-de-test>`
* Spécification de **cas de test** : `<lien vers 04-Spec-Cas-de-test>`
* Exigences / User Stories : `<lien(s) référentiel : JIRA/Squash/…>`
* Stratégie / Plan de test : `templates/01-Strategie-de-test.md`
* Normes et référentiels : `ISO 29119-3`, `ISTQB Glossary`, `ISO 25010`, autres : `<…>`

---

## 3. Règles de nommage et structure

* **Procédures** : `TPS-<périm>-<nnn>` (ex. `TPS-PAIEMENT-010`).
* **Étapes** : `1..n`, typées `Setup / Action / Vérif / Teardown`.
* **Jeux de données** : `DT-<périm>-<nnn>`.
* **Environnements** : `ENV-<code>`.
* **Scripts/Pipelines** : `SCR-<périm>-<nnn>` (si automatisation).
* **Traçabilité** : chaque `TPS-…` référence ≥1 **cas** `TCS-…`, **conditions** `TCN-…` et **exigences** `REQ-…`.

---

## 4. Registre des procédures (vue synthèse)

> *Vue d'ensemble pour planifier et contrôler l'exécution.*

| ID proc. | Titre        | Cas inclus     | Ordonnancement           | Priorité | Env     | Données (ID) | Durée estimée | Automatisation              |
| -------- | ------------ | -------------- | ------------------------ | -------: | ------- | ------------ | ------------- | --------------------------- |
| `TPS-…`  | `<intitulé>` | `TCS-…; TCS-…` | `Parallèle / Séquentiel` |  `H/M/B` | `ENV-…` | `DT-…`       | `<mm:ss>`     | `Manuelle / Auto / Hybride` |

---

## 5. Gabarit de **fiche de procédure** (à dupliquer par procédure)

> Copiez-collez ce bloc pour chaque `TPS-…` et remplacez les valeurs.

### 5.x `TPS-<périm>-<nnn>` — `<Titre de la procédure>`

**Objectif.** `<Ce que la procédure valide de bout en bout>`

**Liens & traçabilité.**

* Cas de test : `TCS-…` (liste & ordre)
* Conditions : `TCN-…`
* Exigences : `REQ-…`
* Risques : `RSK-…`

**Métadonnées.**

* Priorité : `H/M/B`
* Fréquence : `Build / Quotidien / Sprint / Release / Ad hoc`
* Mode : `Manuel / Automatisé / Hybride`
* Durée cible : `<mm:ss>` (temps opérateur / temps total)

**Préconditions (procédure).**

* Accès & rôles : `<comptes, profils, clés API>`
* État système : `<flags, caches, files d'attente, batchs>`
* Données initiales : `DT-…` — `<description>`
* Configuration : `ENV-…` — `<versions, variables>`

**Hypersensibilité / Sécurité / Sécurité opérationnelle.**

* Données sensibles manipulées ? `Oui/Non` — `<mesures (masquage, cloisonnement)>`
* Étapes destructives ? `Oui/Non` — `<gardes, sandbox, restauration>`

**Oracles globaux.** `<règles d'acceptation, SLIs/SLOs, logs/événements attendus>`

#### Étapes détaillées

|  # | Type     | Acteur   | Instruction / Commande | Attendu mesurable (oracle) | Données / Notes | Attente/Timeout | Évidence à collecter     |
| -: | -------- | -------- | ---------------------- | -------------------------- | --------------- | --------------- | ------------------------ |
|  1 | Setup    | `<Rôle>` | `<préparer …>`         | `<état prêt>`              | `DT-…`          | `≤10s`          | `capture: pre-ENV`       |
|  2 | Action   | `<Rôle>` | `<effectuer …>`        | `<résultat>`               | `<…>`           | `≤30s`          | `screenshot: … / log: …` |
|  3 | Vérif    | `<Rôle>` | `<contrôler …>`        | `<assertion>`              | `<…>`           | `≤5s`           | `export: rapport.csv`    |
|  n | Teardown | `<Rôle>` | `<nettoyer …>`         | `<état restauré>`          | `<…>`           | `≤15s`          | `evidence: cleanup-ok`   |

**Collecte & nommage des preuves.**

* Dossier : `evidence/<TPS>/<date>_<heure>/`
* Règle : `<TPS>-<étape>-<horodatage>.<ext>` (ex. `TPS-PAIEMENT-010-002-20250105_101233.png`)

**Journalisation & corrélation.**

* Niveau de logs : `<INFO/DEBUG>` — Correlation ID : `<GUID>`
* Points d'observation : `<APM, traces, métriques>`

**Teardown & remise en état.**

* Nettoyage fonctionnel : `<annulation, purge>`
* Nettoyage technique : `<reset cache, files>`
* Données : `<rollback, réinitialisation seed>`

**Gestion des incidents pendant exécution.**

* Critères d'arrêt : `<conditions>`
* Ouverture d'anomalie (DEFECT) : `Projet/Type/Template` — Titre : `TPS-… — <résumé>` — Preuves : `…`
* Reprise : `Re-run complet / Reprise à l'étape <n>` — Conditions : `<…>`

**Automatisation (si applicable).**

* Script : `SCR-…` — `<chemin ou référentiel>`
* Commande : `<ex.: mvn -Ptests -Dgroups="paiement">`
* Paramètres : `<ENV=REC DT=DT-… USERS=…>`
* Sorties : `rapport JUnit / Allure / artifact` — `chemin`
* Stabilité : `Stable / Flaky` — `<dernière observation>`

**Remarques.** `<dettes, TODO, améliorations>`

---

## 6. Procédures **composées** et parallélisme (option)

> Décrire la synchronisation entre procédures (workflows multi-composants, E2E).

| ID      | Type                   | Dépend de | Lance   | Synchronisation        | Points de contrôle      |
| ------- | ---------------------- | --------- | ------- | ---------------------- | ----------------------- |
| `CPS-…` | `Séquence / Parallèle` | `TPS-…`   | `TPS-…` | `<barrières, verrous>` | `<événements attendus>` |

---

## 7. Environnements & outillage

| ID env  | Description   | Versions            | Outils de test/mesure                | Journalisation / traces         | Remarques |
| ------- | ------------- | ------------------- | ------------------------------------ | ------------------------------- | --------- |
| `ENV-…` | `<REC/PRP/…>` | `<OS, DB, runtime>` | `<frameworks, injecteurs, scanners>` | `<niveau de logs, corrélation>` | `<…>`     |

**Accès & secrets** : `<gestion (vault), expiration>`

---

## 8. Données de test (rappel)

| ID jeu | Finalité           | Contenu clé              | Source / Méthode                          | Sensible ? | Localisation              |
| ------ | ------------------ | ------------------------ | ----------------------------------------- | ---------: | ------------------------- |
| `DT-…` | `<alimente TPS-…>` | `<champs, cardinalités>` | `synthétique / masqué / semi-synthétique` |  `Oui/Non` | `<repo / BDD / stockage>` |

**Consommation** : `<idempotence, réutilisation, seeds>`

---

## 9. Checklists d'exécutabilité

### 9.1 **Definition of Ready (Exec)**

* [ ] Environnement `ENV-…` **opérationnel** et versions vérifiées
* [ ] Accès & secrets valides (aucune expiration imminente)
* [ ] Jeux de données `DT-…` chargés et référencés
* [ ] Préconditions satisfaites (feature flags, batchs, queues vides)
* [ ] Capteurs d'observabilité disponibles (logs/metrics/traces)

### 9.2 **Definition of Done (Exec)**

* [ ] Toutes les étapes exécutées ou motif d'arrêt consigné
* [ ] Preuves collectées et nommées selon la convention
* [ ] Résultats enregistrés (`PASS/FAIL/BLOCKED/NA`) + horodatage
* [ ] Anomalies créées avec pièces jointes et références `TPS/TCS/TCN`
* [ ] Nettoyage/rollback effectué

---

## 10. Couverture & métriques d'exécution

* `Taux de réussite des procédures` (PASS rate)
* `Durée réelle vs cible` par `TPS`
* `Taux de flaky` pour les `TPS` automatisées
* `Incidents par 100 exécutions` et temps moyen de reprise

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

## Annexe A — Exemple de **script d'orchestration** (option)

```bash
#!/usr/bin/env bash
set -euo pipefail
# SCR-PAIEMENT-001 — Orchestration TPS-PAIEMENT-010
export ENV=REC DT=DT-PAIEMENT-005 USERS=users-rec.csv

log_dir="evidence/TPS-PAIEMENT-010/$(date +%Y%m%d_%H%M%S)"; mkdir -p "$log_dir"

step() { echo "[$(date +%T)] $1" | tee -a "$log_dir/steps.log"; }

step "Setup: reset cache"; curl -s -X POST "$API/reset-cache"
step "Action: submit order"; ./runner --case TCS-PAIEMENT-012 --env "$ENV" --data "$DT" | tee "$log_dir/tcs-012.log"
step "Vérif: check p95 latency"; ./metrics --assert p95<=300
step "Teardown: rollback"; ./db --rollback "$DT"
```

## Annexe B — Modèle de **template d'anomalie** lié à une procédure

```md
Titre: TPS-<périm>-<nnn> — <résumé>
Étapes: lien vers procédure + index des étapes
Résultat attendu: …
Résultat observé: …
Preuves: chemin evidence/, logs, exports
Traçabilité: TPS-…, TCS-…, TCN-…, REQ-…
Contexte: ENV-…, version build, hash commit
```

