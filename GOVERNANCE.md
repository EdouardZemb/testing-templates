# Gouvernance du dépôt

Cette page décrit les rôles, responsabilités et processus de décision pour le dépôt **testing-templates**. Elle complète `CONTRIBUTING.md`, `CODEOWNERS` et les artefacts de standards.

## Rôles

| Rôle | Responsabilités | Personne(s) actuelle(s) |
| ---- | ---------------- | ----------------------- |
| Mainteneur principal | Direction technique du dépôt, validation finale des PR, publication des releases | @EdouardZemb |
| Référent Qualité | Veille à l’alignement avec les normes ISO/ISTQB, supervise les évolutions de templates | @EdouardZemb (provisoirement) |
| Test Lead / Contributeurs | Proposent des améliorations, créent issues/PR, appliquent la check-list CONTRIBUTING | Communauté / contributeurs externes |

> _Lorsque de nouveaux mainteneurs seront nommés, ce tableau sera mis à jour pour refléter la répartition officielle._

## Processus de revue

1. **CODEOWNERS** définit les répertoires sensibles (`templates/`, `standards/`, `docs/`, `.github/`). Toute PR qui touche ces zones notifie automatiquement le mainteneur.
2. **Nombre de reviews** :
   - Actuellement, **1 review approuvée** (mainteneur) suffit pour fusionner.
   - Objectif à moyen terme : **2 reviews minimum**, dont un mainteneur et un référent qualité / domaine (sera formalisé lorsque plusieurs mainteneurs seront actifs).
3. Les checks CI (Docs CI + lint) doivent être verts avant merge.
4. Les commits doivent suivre la convention (anglais, type `feat`, `docs`, `ci`, etc.).

## Decision Records (DR)

- Les décisions structurantes sont consignées dans le dossier `decisions/` via des DR (`DR-YYYY-NN`).
- Chaque DR doit utiliser le préfixe `DR` défini dans `standards/conventions-identifiants.md`.
- Lorsqu’une PR introduit ou modifie un DR :
  1. Créer un fichier `decisions/DR-YYYY-NN-titre.md` documentant le contexte, les décisions et alternatives.
  2. Référencer le DR dans la PR (`Closes` ou `Refs` selon le cas).
  3. Mettre à jour la section concernée de `README.md` ou des standards si nécessaire.

## Maintien des documents de gouvernance

- `CONTRIBUTING.md` : flux amont → merge, check-lists.
- `GOVERNANCE.md` (ce document) : rôles, revues, DR.
- `standards/references.yaml` : sources normatives autorisées.
- `standards/glossaire-istqb.md` & `standards/cartographie-nfr-iso25010.md` : ressources de référence.
- `standards/conventions-identifiants.md` : préfixes d’artefacts.
- `docs/release-lifecycle.md` : cycle release, milestones, checklist.
- `docs/maintainer-playbook.md` : routine mainteneurs, escalades.

Toute évolution du processus doit être discutée via issue + PR associées. Lorsque des rôles supplémentaires sont nommés ou que les règles de revue évoluent, ce document constitue la référence officielle.
