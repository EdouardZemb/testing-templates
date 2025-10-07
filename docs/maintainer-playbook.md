# Maintainer Playbook

Ce guide décrit la routine attendue pour les mainteneurs de **testing-templates**. Il complète `CONTRIBUTING.md`, `GOVERNANCE.md`, `docs/release-lifecycle.md` et `SECURITY.md`.

## 1. Rythme de tri

- **Quotidien** :
  - Revue des issues nouvelles → vérifier DoR (#56) et priorité (#64, à venir).
  - Vérifier les PR ouvertes (`gh pr status`), s’assurer que la CI a tourné.
- **Hebdomadaire** :
  - Audit du board (#63) : colonnes Backlog → Done.
  - Revue des milestones (cf. `docs/release-lifecycle.md`).

## 2. Gestion des issues

1. Valider/compléter le DoR (commentaire standard).
2. Appliquer les labels (`type`, `prio`, `scope`) – voir issue #55.
3. Assigner un milestone si la cible est connue.
4. Déplacer l’issue dans la colonne adaptée (Ready / In progress...).

## 3. Gestion des PR

- Vérifier :
  - CI (`Docs CI`) = ✅.
  - Bloc “Référence normative” rempli le cas échéant.
  - Bloc “Sécurité” coché ou argumenté (PR template).
- Revue : au moins 1 review mainteneur (cf. `GOVERNANCE.md`). Ajout d’un second reviewer si besoin.
- Merge : squash par défaut, message conventionnel.
- Post-merge :
  - Supprimer la branche, `git pull --ff-only`.
  - Ajouter un commentaire sur l’issue liée (progrès/CI).

## 4. Cycle de release

- Suivre `docs/release-lifecycle.md` :
  - Vérifier l’avancement du milestone actif.
  - Préparer la checklist RC (tests complémentaires, freeze).
  - Générer notes de version et communication.
- Compléter les DR si décisions structurantes (#7/#30).

## 5. Escalade & sécurité

- Vulnérabilités : appliquer `SECURITY.md` (réponse sous 3 jours ouvrés, suivi privé).
- Bugs critiques :
  - Créer issue P1 + milestone courant.
  - Planifier hotfix si release en production.
  - Documenter dans un DR si décision impact majeure.

## 6. Outils

- `gh pr status`, `gh issue status` (via board quand il sera configuré #54).
- `scripts/validate_references.py` : vérifier lors de modifications (ex. `python3 scripts/validate_references.py`).
- Vale (`shopt -s globstar && vale ...`) pour l’orthographe française.

## 7. Contact & onboarding

- Nouveaux mainteneurs : mettre à jour `GOVERNANCE.md` (table des rôles) et CODEOWNERS si nécessaire.
- Communiquer via commentaires GitHub ou canal interne (à définir).

## 8. Références

- `GOVERNANCE.md`
- `CONTRIBUTING.md`
- `docs/release-lifecycle.md`
- `SECURITY.md`
- `standards/` (références, glossaire, cartographie NFR, conventions identifiants)
