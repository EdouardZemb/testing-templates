# Guide de contribution

Ce guide décrit le flux complet pour proposer, cadrer, développer et fusionner une évolution dans `testing-templates`. Il formalise la Definition of Ready (DoR), la création de branches, l’usage des PR et les exigences de CI.

## 1. Idéation & qualification

1. **Créer une issue** depuis le backlog :
   - Choisir le formulaire adapté (`User Story`, `Exigence`, `Bug`, `Proposition d'évolution`).
   - Renseigner *contexte*, *valeur*, *critères d’acceptation*, *références normatives*, *impacts*.
2. **Étiqueter** l’issue : type (`type:US`, `type:Exigence`, `type:Bug`…), priorité (`prio:P1..P3`), périmètre (`scope:templates`, `scope:docs`, etc.).
3. **Assigner** un responsable et relier :
   - Projet GitHub (backlog / sprint / roadmap).
   - Milestone si pertinent.
4. **Definition of Ready (DoR)** : l’issue passe en colonne *Ready* lorsque :
   - Les critères d’acceptation sont clairs.
   - Les impacts (templates, docs, CI) sont identifiés.
   - Les dépendances sont connues.
   - Une estimation a été fournie.

## 2. Préparation de la branche

1. **Synchroniser `main`** :

   ```bash
   git switch main
   git pull --ff-only
   ```

2. **Créer la branche** (une issue = une branche) :

   - Convention : `feat/<issue-123>-slug`, `fix/<issue-456>-slug`, `docs/<issue-789>-slug`.
   - Exemple : `docs/issue-36-contributing-workflow`.
3. **Ouvrir immédiatement une PR brouillon** :
   - Base `main`, head = branche créée.
   - Lier l’issue via un mot-clé (`Closes #36`).
   - Remplir le template PR (objet, justification, bloc `Référence normative`).
   - La Draft PR assure la visibilité et déclenche la CI.

## 3. Développement

1. **Commits** : respecter Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`…).
2. **Lint local** :

   ```bash
   shopt -s globstar && vale README.md templates/**/*.md .github/**/*.md CONTRIBUTING.md
   npx markdownlint-cli2 README.md CONTRIBUTING.md
   ```

3. **Rebase régulier** :

   ```bash
   git fetch origin
   git rebase origin/main
   ```

4. **Push** à cadence régulière pour alimenter la PR.

## 4. Validation CI & revue

1. **Docs CI** doit être verte :
   - `markdownlint`.
   - `Vale` (style `Fr`, dictionnaire hunspell).
   - Script `Référence normative` (seulement si la PR modifie `templates/` ou `standards/`; citer au moins une entrée de `standards/references.yaml`, sinon indiquer `N/A`).
2. **Branch protection** :
   - Historique linéaire.
   - Conversations résolues.
   - Pas de merge si la CI échoue.
3. **Revue CODEOWNERS** :
   - Les propriétaires sont ajoutés automatiquement.
   - Exiger ≥1 approbation lorsqu’il y a plusieurs mainteneurs.

## 5. Merge & post-merge

1. **Passer la PR en Ready for Review** lorsque :
   - DoR respecté → travail effectué.
   - Toilettage (rebases, lint) fait.
2. **Squash & merge** (par défaut) :
   - Le message de merge doit rester en anglais, résumer le changement.
   - L’issue est fermée automatiquement via les mots-clés (`Closes #...`).
3. **Nettoyage** : supprimer la branche distante (`Delete branch`), archiver la branche locale.
4. **Release** (si applicable) :
   - Ajouter un tag sémantique.
   - Mettre à jour le changelog / notes de release (cf. `docs/release-lifecycle.md`).
   - Les liens Issue ↔ PR ↔ commit assurent la traçabilité.

## 6. Automatisations & templates

- **Issue Forms** : fichiers YAML sous `.github/ISSUE_TEMPLATE/` imposent les champs DoR.
- **Security** : pour signaler un problème, suivre `SECURITY.md`.
- **PR Template** : `.github/PULL_REQUEST_TEMPLATE.md` avec bloc `Référence normative`.
- **CI** : `.github/workflows/docs-ci.yml` (markdownlint + Vale + contrôle PR).
- **Validation références** : `scripts/validate_references.py` (via Docs CI).
- **Vale** : `.vale.ini`, style `styles/Fr/`, dictionnaire `styles/Fr/dictionaries/fr.dic`.
- **Branch naming** et **Draft PR** : requis pour tous les contributeurs.

## 7. Rappels

- Normes supportées : ISO/IEC/IEEE 29119-2/-3, ISO/IEC 25010, ISTQB Glossary, IEEE 1012.
- Les documents doivent citer les sources dans leur front matter ou dans la PR (voir `standards/references.yaml` et `standards/glossaire-istqb.md`).
- Respecter les conventions d'identifiants décrites dans `standards/conventions-identifiants.md`.
- Toute décision structurante est documentée via un Decision Record (`decisions/`).

En suivant ce flux, chaque contribution reste traçable, normée et mergeable sans surprise.
