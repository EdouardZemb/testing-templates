# Release lifecycle & milestones

Ce guide formalise la gestion d'une release pour **testing-templates** : planification via milestones, stabilisation (release candidate) et publication (notes de version, tags).

## 1. Cycle général

1. **Planification**
   - Créer/mettre à jour un milestone (`vX.Y.Z`) avec la date cible.
   - Ajouter les issues priorisées (cf. `governance: define backlog prioritization strategy` #64) en vérifiant leur DoR (#56).
2. **Développement**
   - Issues en colonne "In Progress" du board (#63) et PR associées.
   - CI (`Docs CI`) doit rester verte; Vale/markdownlint obligatoires.
3. **Stabilisation (RC)**
   - Geler le scope du milestone.
   - Exécuter la checklist de release (voir ci-dessous) incluant tests complémentaires/manuels si nécessaire.
   - Créer une branche `release/vX.Y.Z-rc` optionnelle pour les retouches.
4. **Publication**
   - Merging des PR restantes après review (au moins 1 review mainteneur, se synchronise avec `GOVERNANCE.md`).
   - Créer le tag `vX.Y.Z` sur `main`.
   - Générer les notes de version (CHANGELOG ou GitHub Release) et communiquer.
5. **Post-release**
   - Déplacer le milestone en "Closed".
   - Créer le milestone suivant.

## 2. Checklist release

Avant de tagger `vX.Y.Z`, cocher :

- [ ] Toutes les issues du milestone sont `Done` ou déplacées vers un autre milestone.
- [ ] `CONTRIBUTING.md`, `GOVERNANCE.md` et `standards/*` reflètent les nouveautés.
- [ ] Licence/nores normatives inchangées ou mises à jour (#47/#48 le cas échéant).
- [ ] Dépendances critiques vérifiées (#61).
- [ ] Templates lintés (`vale`, `markdownlint`) localement.
- [ ] Notes de version préparées (voir modèle ci-dessous).

## 3. Milestones GitHub

- Utiliser les milestones comme jalon principal (ex. `v0.1.0 — Initialisation`).
- À l'ouverture d'une issue, définir son milestone si elle vise la release en cours.
- En revue hebdomadaire, vérifier l'avancement du milestone (#63/board).

## 4. Release notes

Modèle Github Release / CHANGELOG :

```
## vX.Y.Z – yyyy-mm-dd

### Nouveautés
- …

### Gouvernance
- …

### Normes
- …

### Remarques
- …
```

Ajouter une section "Crédits" si contribution externe.

## 5. Communication

- Publier les notes de version sur GitHub.
- Diffuser (mail/Slack interne) un court résumé avec lien vers la release et issues.
- Mettre en évidence les changements de gouvernance (ex. nouveaux DR, politiques).

## 6. Références

- Issue #62 – cadre unifié (ce document).
- Issue #27 – workflow & changelog (remplacé).
- Issue #52 – milestones (intégré).
- Issue #53 – stabilisation & publication (intégré).
- `LICENSE`, `GOVERNANCE.md`, `CONTRIBUTING.md`.
