---
title: "06 — Plan de Données de Test (Test Data Plan)"
version: "0.1.0"
statut: "draft"
projet: "<Nom du projet / périmètre>"
équipe: "<TRA / équipe de test>"
responsable: "<Nom, rôle>"
reviseurs_attendus:
  - Qualité
  - Test Lead
  - Data Steward / Référent données
  - Sécurité / DPO (si applicable)
source_normes:
  - ISO/IEC/IEEE 29119-3 — Test documentation (référentiel de livrables)
  - ISO/IEC 25010 — Modèle de qualité (pertinent pour les tests non fonctionnels)
  - ISTQB® Glossary — Terminologie
  - Règlement (UE) 2016/679 — RGPD (conformité données personnelles)
licence: "CC BY 4.0"
---

# 06 — Plan de Données de Test (Test Data Plan)

> **But du document** — Définir **quelles données** sont nécessaires aux tests, **comment** elles sont obtenues (extraction, anonymisation, synthèse), **où** elles résident (environnements), **quand** et **par qui** elles sont mises à disposition, ainsi que les **règles de conformité, sécurité, qualité, rafraîchissement et nettoyage**.
>
> **À remplir** — Remplacer tout texte entre `<…>` et compléter les tableaux. Conserver les commentaires `<!-- … -->` si vous souhaitez garder l’aide à la rédaction.

---

## 1. Objet et périmètre

**Objet.** `<Décrire le périmètre fonctionnel et technique couvert par ce plan de données>`

**Hors périmètre.** `<Ce qui n’est pas couvert et pourquoi (ex. périmètres gérés par un autre projet)>`

**Hypothèses & contraintes.** `<Accès aux systèmes sources, fenêtres d’extraction, capacités d’anonymisation, volumétrie, délais>`

---

## 2. Références

* **Conception de test** (03) : `<lien>`
* **Cas de test** (04) : `<lien>`
* **Procédures** (05) : `<lien>`
* **Politiques internes** : `<sécurité, RGPD, confidentialité, archivage>`
* **Contrats / DPA / clauses** : `<si des données personnelles ou sous-traitants sont impliqués>`

---

## 3. Gouvernance & responsabilités

| Rôle              | Responsabilités                                    | Titulaire(s) | RACI |
| ----------------- | -------------------------------------------------- | ------------ | ---- |
| Test Data Manager | Pilotage des données de test, arbitrages, planning | `<Nom>`      | R    |
| Data Steward      | Qualité/gestion des dictionnaires et règles        | `<Nom>`      | A    |
| Équipe Test       | Spécifie les besoins, valide la qualité            | `<Noms>`     | C    |
| Sécurité / DPO    | Conformité (RGPD, sécurité, conservation)          | `<Nom>`      | A    |
| Ops / DBA         | Provisionnement, sauvegarde, restauration          | `<Nom>`      | R    |

**Canaux & cadences.** `<rituels, approbations, fenêtres de provisioning>`

---

## 4. Classification & sensibilité des données

> *Catégoriser les données (ex. Public / Interne / Confidentiel / Sensible — Données personnelles / santé / finance).*

| Classe       | Description                            | Exemples                     | Mesures minimales                                                       |
| ------------ | -------------------------------------- | ---------------------------- | ----------------------------------------------------------------------- |
| Public       | Diffusable sans risque                 | Catalogue, notices           | Accès ouvert, logs de base                                              |
| Interne      | Usage interne                          | Paramétrages                 | ACL projet                                                              |
| Confidentiel | Risque si fuite                        | Clients pseudonymisés        | Chiffrement au repos/transit, contrôle d’accès                          |
| Sensible     | Données personnelles / santé / finance | NIR, IBAN, données médicales | Anonymisation/masquage fort, journalisation renforcée, rétention courte |

**Décision de licéité (si PII)** : `<bases légales, minimisation, DPIA si nécessaire>`

---

## 5. Inventaire des **sources** et éléments de données

| Système source  | Type               | Propriétaire | Schéma/Collection | Volumétrie (attendue) | Fenêtre d’extraction | Sensible ? | Remarques |
| --------------- | ------------------ | ------------ | ----------------- | --------------------: | -------------------- | ---------: | --------- |
| `<CRM/ERP/...>` | `DB/Table/CSV/API` | `<owner>`    | `<schema.table>`  |                 `<N>` | `<J-? à H:MM>`       |  `Oui/Non` | `<…>`     |

**Dictionnaire de données** (extrait) :

| Champ           | Description | Type     | Contraintes | Exemple | Sensible | Règle de masquage            |
| --------------- | ----------- | -------- | ----------- | ------- | -------: | ---------------------------- |
| `<customer_id>` | `<…>`       | `UUID`   | `unique`    | `…`     |      Non | `—`                          |
| `<iban>`        | `<…>`       | `string` | `regex`     | `…`     |      Oui | `Masquage format-preserving` |

---

## 6. Besoins **par conditions de test** (traçabilité)

> *Associer les jeux de données requis aux **conditions de test (TCN)** et cas (TCS).*

| Condition (TCN) | Cas (TCS) | Données requises              | Cardinalité | Variations         | Sensible ? | Jeu (ID) |
| --------------- | --------- | ----------------------------- | ----------: | ------------------ | ---------: | -------- |
| `TCN-…`         | `TCS-…`   | `<clients actifs sans email>` |      `≥ 50` | `<fr/en, limites>` |  `Oui/Non` | `DT-…`   |

---

## 7. Stratégies d’obtention des données

**Options et critères de choix.**

* **Extraction prod + anonymisation/masquage** : réalisme élevé ; contrainte RGPD & délais.
* **Synthétique** : contrôle total, pas de PII ; risque d’écart avec prod.
* **Semi-synthétique** : structure réelle + valeurs synthétiques ; bon compromis.
* **Jeux “seed” paramétrés** : reproductibles, pour automatisation.

**Arbre de décision (indicatif).**

1. Données personnelles nécessaires ? → **Synthétique** par défaut ; si impossible, **anonymisation forte**.
2. Besoin de distributions réalistes ? → **Semi-synthétique** ou **échantillons anonymisés**.
3. Tests de charge/perf ? → **Génération à grande échelle** + **profil de charge** (cf. §11).

---

## 8. Règles d’anonymisation / masquage

| Champ   | Technique                  | Détail                     | Réidentification possible ? | Remarques         |
| ------- | -------------------------- | -------------------------- | --------------------------: | ----------------- |
| `nom`   | Pseudonymisation           | dictionnaire noms factices |                    `Faible` | `—`               |
| `email` | Masquage format-preserving | `user+hash@example.test`   |                    `Faible` | domaine `.test`   |
| `iban`  | Tokenisation               | jeton irrécupérable        |                     `Nulle` | conforme PCI-like |

**Contraintes** : préserver **unicité**, **formats**, **clés étrangères**, **cohérences métiers**.

---

## 9. Génération de données **synthétiques**

**Approche.** `<générateurs, librairies, scripts, data factory>`

**Schémas et paramètres.**

| Jeu (ID) | Finalité                       | Générateur       | Paramètres clés | Oracles associés |
| -------- | ------------------------------ | ---------------- | --------------- | ---------------- |
| `DT-…`   | `pairwise`, `limites`, `états` | `<outil/script>` | `<P1..Pn>`      | `<attendus>`     |

**Exemples de variations** : bornes (`min, min+1, max-1, max`), locales (`fr-FR/en-GB`), formats (`UTF-8`, accents), valeurs invalides contrôlées.

---

## 10. Qualité des données de test (validation)

**Règles de validation.**

* **Intégrité référentielle** (clés étrangères, cardinalités).
* **Complétude** (champs requis non nuls).
* **Conformité de format** (regex, domaines de valeurs, IBAN, emails).
* **Cohérence métier** (règles si/alors, tables de décision).

| Règle   | Portée    | Méthode      | Seuil       | Action si KO         |
| ------- | --------- | ------------ | ----------- | -------------------- |
| `R-001` | `clients` | `SQL/Script` | `0% erreur` | `rejeter & corriger` |

---

## 11. Données de **performance/charge**

**Profil de charge** : `<utilisateurs virtuels, TPS, ramp-up, durée>`

**Volumétrie** : `<N enregistrements par entité>`

**Données temporelles** : `<distributions inter-arrivées, pics>`

**Masse de données** : `<taille BDD, index, archives simulées>`

---

## 12. Environnements & provisioning

| ID env    | Emplacement    | Mécanisme de provisioning | Fenêtre      | Restauration            | Observabilité   |
| --------- | -------------- | ------------------------- | ------------ | ----------------------- | --------------- |
| `ENV-REC` | `<cluster/db>` | `<scripts IaC/DBA>`       | `<J-? H:MM>` | `<sauvegarde/rollback>` | `<logs/traces>` |

**Secrets & accès** : stockés dans `<vault/secret manager>`, rotation `<périodicité>`.

---

## 13. Plan de rafraîchissement

| Jeu (ID) | Fréquence              | Méthode                         | Dépendances | Responsable |
| -------- | ---------------------- | ------------------------------- | ----------- | ----------- |
| `DT-…`   | `Hebdo/Mensuel/Ad hoc` | `ré-extraction + anonymisation` | `<sources>` | `<Nom>`     |

**Déclencheurs** : nouvelle release, évolution schéma, défauts liés aux données.

---

## 14. Nettoyage / rollback / idempotence

**Principes.**

* Tests **idempotents** ; sinon, **teardown** clair.
* **Rollbacks** disponibles (transactions, snapshots, scripts de purge).

| Contexte | Action de nettoyage   | Script     | Preuve           |
| -------- | --------------------- | ---------- | ---------------- |
| `TPS-…`  | `purge lignes créées` | `<script>` | `log nettoyages` |

---

## 15. Sécurité, confidentialité & conformité

* **Accès par rôle (RBAC)** : principle of least privilege.
* **Journalisation** : accès et extractions tracés ; conservation `<x>` jours.
* **Chiffrement** : **au repos** et **en transit**.
* **Rétention** : `<durée>` puis **purge/archivage**.
* **Registre des traitements** : `<référence>` ; **DPIA** si nécessaire.

---

## 16. Risques & plans de mitigation

| ID          | Risque               | Prob. | Impact | Mitigation                                 | Propriétaire |
| ----------- | -------------------- | ----: | -----: | ------------------------------------------ | ------------ |
| `RSK-DT-01` | Fuite de PII         |     H |      H | Masquage fort + coffre-fort + logs d’accès | `<Nom>`      |
| `RSK-DT-02` | Données incohérentes |     M |      H | Règles de validation + jeu seed            | `<Nom>`      |

---

## 17. KPIs & suivi

| KPI                      | Définition                               | Cible    |
| ------------------------ | ---------------------------------------- | -------- |
| Data Readiness           | `% TCN avec jeux de données disponibles` | `≥ 95%`  |
| Défauts liés aux données | `% défauts imputables aux jeux`          | `≤ <x>%` |
| Temps de provisioning    | `durée moyenne d’un rafraîchissement`    | `≤ <h>`  |

**Reporting.** `hebdo/sprint` — tableau de bord dédié.

---

## 18. Liste de contrôle (prête à l’emploi)

* [ ] Classification & DPIA (si PII) validées
* [ ] Inventaire sources complété et propriétaires identifiés
* [ ] Règles d’anonymisation/masquage documentées et testées
* [ ] Jeux `DT-…` définis et traçables vers `TCN/TCS`
* [ ] Validation qualité (intégrité/completude/format) outillée
* [ ] Provisioning & rafraîchissement planifiés
* [ ] Sécurité/accès/secrets conformes aux politiques
* [ ] Procédures de nettoyage/rollback éprouvées

---

## 19. Historique des modifications

| Version | Date           | Auteur  | Changements         |
| ------: | -------------- | ------- | ------------------- |
| `0.1.0` | `<AAAA-MM-JJ>` | `<Nom>` | Création du modèle. |

---

## Annexes

### A — Exemple de règles de masquage (CSV)

```csv
field,technique,detail,notes
first_name,pseudonymization,from_dict:noms_fr.csv,preserve_gender
email,mask_fpe,user+hash@example.test,unique
iban,tokenization,random_token(length=27),format_preserving
```

### B — Schéma de génération synthétique (JSON)

```json
{
  "dataset": "clients",
  "count": 5000,
  "fields": {
    "id": { "type": "uuid" },
    "age": { "type": "int", "min": 18, "max": 95, "edge": [18,19,94,95] },
    "locale": { "type": "enum", "values": ["fr-FR", "en-GB"] },
    "email": { "type": "email", "domain": "example.test" }
  }
}
```

