---
title: "Conventions d'identifiants"
source: "Projet internalisé — aligné ISO/IEC/IEEE 29119 & ISTQB"
last_updated: "2025-10-06"
---

> Règles de nommage pour les artefacts de test et la gouvernance associée. Format général : `PREFIX-Contexte-NNN`, où `PREFIX` est imposé, `Contexte` est un code lisible (ex. domaine, lot, feature) et `NNN` un compteur numérique sur 3 chiffres (`001`, `002`, ...). Utiliser des majuscules et le trait d'union comme séparateur.

## Tableau des préfixes

| Préfixe | Artefact | Regex recommandée | Exemple |
| ------- | -------- | ----------------- | ------- |
| `TCN` | Condition de test | `^TCN-[A-Z0-9]+-\d{3}$` | `TCN-CART-005` |
| `TCS` | Cas de test | `^TCS-[A-Z0-9]+-\d{3}$` | `TCS-CHECKOUT-012` |
| `TPS` | Procédure de test | `^TPS-[A-Z0-9]+-\d{3}$` | `TPS-REGRESSION-001` |
| `DT`  | Jeu de données (Data Test) | `^DT-[A-Z0-9]+-\d{3}$` | `DT-PAIEMENT-003` |
| `ENV` | Environnement de test | `^ENV-[A-Z0-9]+-\d{2}$` | `ENV-STG-01` |
| `REQ` | Exigence fonctionnelle/NFR | `^REQ-[A-Z0-9]+-\d{3}$` | `REQ-SECURITY-010` |
| `RSK` | Risque produit/projet | `^RSK-[A-Z0-9]+-\d{3}$` | `RSK-PROD-002` |
| `DR`  | Decision Record (gouvernance) | `^DR-\d{4}-\d{2}$` | `DR-2025-01` |

### Précisions

- **Contexte** (`[A-Z0-9]+`) : privilégier un code court (2-10 caractères) reflétant le périmètre (ex. `AUTH`, `DATA`, `OPS`).
- **Compteur** : démarrer à `001` (ou `01` selon regex) et incrémenter séquentiellement pour chaque nouveau document.
- **DR** : format date + incrément pour s'aligner sur les pratiques de registre de decisions.

## Bonnes pratiques

1. Documenter les codes de contexte utilisés dans la stratégie ou le plan de test pour garantir la cohérence.
2. Mettre à jour les matrices de traçabilité (ex. `REQ` ↔ `TCS`) en conservant ces identifiants.
3. Vérifier les identifiants lors des revues PR et dans la CI (à compléter via issue #26 pour une validation regex automatique).

## Références

- `standards/references.yaml` — ISO/IEC/IEEE 29119 pour la structuration documentaire.
- `standards/glossaire-istqb.md` — Terminologie associée.
