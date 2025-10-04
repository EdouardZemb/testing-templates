---
title: "07 — Exigences d’Environnement de Test (Test Environment Requirements)"
version: "0.1.0"
statut: "draft"
projet: "<Nom du projet / périmètre>"
équipe: "<TRA / équipe de test>"
responsable: "<Nom, rôle>"
reviseurs_attendus:
  - Test Lead
  - OPS / SRE
  - Sécurité / SecOps
  - DBA / Data Engineer (si BDD)
  - Performance / APM (si non-fonctionnel)
source_normes:
  - ISO/IEC/IEEE 29119-3 — Test documentation (référentiel de livrables)
  - ISO/IEC/IEEE 29119-2 — Test processes (contexte processus)
  - ISTQB® Glossary — Terminologie
  - ISO/IEC 25010 — Modèle de qualité (NFR)
licence: "CC BY 4.0"
---

# 07 — Exigences d’Environnement de Test (Test Environment Requirements)

> **But du document** — Définir **ce dont les tests ont besoin** côté environnements (matériel/virtuel, réseau, logiciels, données, observabilité, sécurité, outillage), **comment** préparer et opérer ces environnements (provisioning, configuration, accès, secrets), et **comment** vérifier leur **prêt à tester** (DoR) et leur **conformité** tout au long de la campagne.
>
> **À remplir** — Remplacer les `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Objet et périmètre

**Objet.** `<Périmètre fonctionnel/technique ciblé par ces exigences d’environnement>`

**Hors périmètre.** `<Ce qui n’est pas couvert (p.ex. perf à très grande échelle traitée ailleurs)>`

**Hypothèses & contraintes.** `<Fenêtres de maintenance, budgets de ressource, cloud/on-prem, contraintes réglementaires, dépendances externes>`

---

## 2. Références

* **Stratégie (01)** : `<lien>`
* **Plan de test (02)** : `<lien>`
* **Conception (03)** : `<lien>`
* **Cas (04) / Procédures (05)** : `<lien>`
* **Plan de données (06)** : `<lien>`
* **Politiques internes** : `<sécurité, backups, observabilité, RGPD, a11y>`

---

## 3. Cartographie des environnements

> *Lister les environnements cibles, leur usage et leurs spécifications minimales.*

| ID env    | Usage               | Capacités minimales (CPU/RAM/Stockage) | Versions clés (OS/Runtime/DB) | Particularités              | Statut       |
| --------- | ------------------- | -------------------------------------- | ----------------------------- | --------------------------- | ------------ |
| `ENV-DEV` | Dev / tests rapides | `≥ <vCPU>, ≥ <Go>, ≥ <Go>`             | `<OS x>, <JDK/Node>, <DB>`    | `<feature flags, mocks>`    | `disponible` |
| `ENV-INT` | Intégration         | `≥ …`                                  | `…`                           | `<contrats, messaging>`     | `…`          |
| `ENV-REC` | Recette système     | `≥ …`                                  | `…`                           | `<proche prod>`             | `…`          |
| `ENV-PRP` | Pré-prod / UAT      | `≈ prod`                               | `…`                           | `<données/volume>`, `<WAF>` | `…`          |

**Inventaire des composants par env** :

| Composant     | Version | Mode                    | Endpoints/Ports | Dépendances         | Observabilité           |
| ------------- | ------- | ----------------------- | --------------- | ------------------- | ----------------------- |
| `<service-X>` | `<v>`   | `container / VM / bare` | `:443, :8080`   | `<DB, MQ, API-Ext>` | `logs, traces, metrics` |

---

## 4. Capacité & dimensionnement

| Domaine  | Indicateur     |  Minimum |    Cible | Note             |
| -------- | -------------- | -------: | -------: | ---------------- |
| CPU      | vCPU totaux    |    `<n>` |   `<n+>` | burst accepté ?  |
| Mémoire  | RAM            |   `<Go>` |   `<Go>` | swap interdit ?  |
| Stockage | SSD            |   `<Go>` |   `<Go>` | IOPS `≥ <x>`     |
| Réseau   | Bande passante | `<Gbps>` | `<Gbps>` | latence `≤ <ms>` |

**Élasticité/Autoscaling** : `<règles de scale, limites hautes/basses>`

---

## 5. Topologie & réseau

| Zone  | Sous-réseau   | Accès entrants   | Accès sortants    | Pare-feu / WAF | Notes |
| ----- | ------------- | ---------------- | ----------------- | -------------- | ----- |
| `REC` | `10.x.x.x/24` | `443 depuis VPN` | `HTTPS → API-Ext` | `WAF activé`   | `<…>` |

**DNS & certificats** : `<noms, wildcard, ACME/PKI, renouvellement>`

**Latence cible par parcours** : `<p95 ≤ … ms>`

---

## 6. Accès & identités (RBAC)

| Rôle           | Accès applicatif        | Accès infra  | Justification           | Durée   |
| -------------- | ----------------------- | ------------ | ----------------------- | ------- |
| Testeur        | UI/API lecture/écriture | lecture logs | exécution cas/procédure | sprint  |
| Automatisation | API techniques          | runners CI   | exécutions quotidiennes | continu |

**Comptes techniques & audit** : `<création, rotation, journalisation des accès>`

---

## 7. Secrets & clés

| Secret        | Usage         | Stockage                 | Rotation | Portée    |
| ------------- | ------------- | ------------------------ | -------- | --------- |
| `DB_PASSWORD` | Connexion BDD | `<vault/secret manager>` | `90 j`   | `REC/PRP` |

**Politique** : jamais en clair dans les repos ; injectés via variables d’env / providers sécurisés.

---

## 8. Configuration & **feature flags**

| Catégorie | Paramètre           | Valeur par env                         | Source                 | Remarques       |
| --------- | ------------------- | -------------------------------------- | ---------------------- | --------------- |
| Flags     | `FEATURE_X_ENABLED` | `DEV: on, INT: on, REC: off, PRP: off` | `<config server/.env>` | `<…>`           |
| Limites   | `MAX_ITEMS`         | `DEV:100 INT:100 REC:100 PRP:100`      | `…`                    | `tests limites` |

**Traçabilité config** : commits/IaC + version de config exposée par `/actuator/info` ou équivalent.

---

## 9. Données & **seeding** (rappel)

* Jeux `DT-…` requis par env ; scripts de **seed** reproductibles.
* Idempotence : ré-exécuter le seed ne doit pas corrompre l’état.

| Env   | Jeu (DT) | Méthode      | Fenêtre      | Restauration          |
| ----- | -------- | ------------ | ------------ | --------------------- |
| `REC` | `DT-…`   | `script/ETL` | `<J-? H:MM>` | `snapshot + rollback` |

---

## 10. Observabilité : logs / traces / métriques

| Signal    | Besoin                           | Exposition           | Rétention   | Seuils              |
| --------- | -------------------------------- | -------------------- | ----------- | ------------------- |
| Logs      | niveau `INFO/DEBUG` paramétrable | `ELK/CloudWatch/…`   | `<x> jours` | erreurs fatales = 0 |
| Traces    | Corrélation requise              | `OTLP/Jaeger/Zipkin` | `<x> jours` | p95 durée par span  |
| Métriques | KPIs métier & techniques         | `Prometheus/APM`     | `<x> jours` | SLOs (cf. §11)      |

**Convention d’ID corrélés** : `X-Correlation-Id` propagé de bout en bout.

**Dashboards requis** : `<liste + URLs internes>`

---

## 11. Disponibilité, SLO & maintenance

| SLI                     | SLO cible  | Méthode de mesure  | Fenêtre |
| ----------------------- | ---------- | ------------------ | ------- |
| Disponibilité env REC   | `≥ 99.x%`  | `APM / synthetics` | `mois`  |
| Erreur `%` API critique | `≤ <0.x%>` | `metrics/http_*`   | `jour`  |

**Fenêtres de maintenance** : `<jours/horaires>` (communication D-?).

**Freeze** : `<périodes sans changement>` avant jalon critique.

---

## 12. Virtualisation, stubs & simulateurs

| Dépendance   | Type | Solution       | Couverture            | Limites               |
| ------------ | ---- | -------------- | --------------------- | --------------------- |
| `API-Banque` | Mock | `<WireMock/…>` | cas heureux + erreurs | pas de latence réelle |

**Contrats** : vérifier schémas et exemples (OpenAPI/Avro/…)

---

## 13. Outillage de test requis

| Catégorie      | Outil                            | Usage        | Intégration   |
| -------------- | -------------------------------- | ------------ | ------------- |
| Automatisation | `<Playwright/Cypress/K6/JMeter>` | e2e/perf     | CI, reporting |
| Sécurité       | `<ZAP/DAST/SAST>`                | scans ciblés | pipeline      |
| Accessibilité  | `<axe-core/…>`                   | audits       | CI / manuel   |

---

## 14. Provisioning & IaC

**Méthode** : `<Terraform/Ansible/Helm/Kustomize>` ; **revue de code** obligatoire.

| Ressource | Définie dans | Validation         | Sortie        |
| --------- | ------------ | ------------------ | ------------- |
| `DB REC`  | `iac/db.tf`  | plan + approbation | état back-end |

**Livrables** : plan d’exécution, journal des déploiements, versionning des manifests.

---

## 15. Contrôles qualité **pré-exécution** (Smoke/Health)

| Contrôle     | Endpoint / Script  | Attendu      | Évidence |
| ------------ | ------------------ | ------------ | -------- |
| Health app   | `/health`          | `UP`         | capture  |
| Contrat API  | `openapi validate` | `OK`         | log      |
| Données seed | `sql check`        | `> N lignes` | export   |

**DoR (ENV)** : voir §19.

---

## 16. Gestion des changements & versions

* **Change management** : demande, évaluation, approbation, fenêtre, rollback.
* **Versioning** : env expose versions **appli/config/schema** (`/info`).
* **Compatibilité** : règles de migration BDD (version + scripts rollback).

---

## 17. Sécurité & conformité

* **Durcissement** (CIS/benchmarks internes), `TLS 1.2+`, chiffrement en transit/au repos.
* **Scans** (dépendances, conteneurs, images).
* **RBAC/Least Privilege** sur tous les composants.
* **Journaux d’accès** et **alertes** (tentatives ratées, élévation de privilèges).

---

## 18. Sauvegarde, restauration & **rollback**

| Ressource | Stratégie         | RPO   |   RTO | Test de restauration |
| --------- | ----------------- | ----- | ----: | -------------------: |
| `DB REC`  | snapshot nocturne | `<h>` | `<h>` |            `Mensuel` |

**Procédures** : documentées et testées (exercices réguliers).

---

## 19. Checklists

### 19.1 **Definition of Ready (ENV)**

* [ ] Environnement **disponible** et **inventorié** (§3)
* [ ] **Accès** & **secrets** fournis et testés (§6–7)
* [ ] **Config** & **flags** appliqués (§8)
* [ ] **Données** seed chargées (§9)
* [ ] **Observabilité** active : logs/traces/metrics visibles (§10)
* [ ] **Smoke checks** PASS (§15)

### 19.2 **Definition of Done (ENV)**

* [ ] Exécution terminée, **preuves** collectées
* [ ] **Nettoyages**/rollback exécutés (§18)
* [ ] **Anomalies env** créées/résolues
* [ ] **État** & **versions** consignés

---

## 20. Risques & plans de mitigation

| ID           | Risque          | Prob. | Impact | Mitigation                | Propriétaire |
| ------------ | --------------- | ----: | -----: | ------------------------- | ------------ |
| `RSK-ENV-01` | indispo REC     |     M |      H | redémarrage auto, alertes | `<Nom>`      |
| `RSK-ENV-02` | secrets exposés |     B |      H | vault + revue secrets     | `<Nom>`      |

---

## 21. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

---

## Annexes

### A — Matrice `.env` (exemple)

```ini
# DEV
FEATURE_X_ENABLED=true
API_URL=https://api.dev.example.test

# REC
FEATURE_X_ENABLED=false
API_URL=https://api.rec.example.test
```

### B — Inventaire d’endpoints (extrait)

| Service | Endpoint       | Méthode | Auth               | Note |
| ------- | -------------- | ------- | ------------------ | ---- |
| auth    | `/oauth/token` | POST    | client_credentials | `…`  |
| order   | `/orders/{id}` | GET     | bearer             | `…`  |

### C — Niveaux de logs recommandés

| Logger   | DEV   | INT  | REC  | PRP  |
| -------- | ----- | ---- | ---- | ---- |
| app.root | DEBUG | INFO | INFO | WARN |
| http     | DEBUG | INFO | INFO | INFO |

