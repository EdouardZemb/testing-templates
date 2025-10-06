# Testing Templates (docs-as-code)

Ce dépôt fournit des modèles de documentation de test alignés ISO/IEC/IEEE 29119, maintenus en mode docs-as-code avec linting automatisé.

## Vue d'ensemble

- **Objectif.** Capitaliser des gabarits prêts à l'emploi pour plans, stratégies, rapports et annexes QA.
- **Public cible.** Test leads, QA engineers, équipes projet et contributeurs gouvernance.
- **État actuel.** Ensemble de gabarits 01-09 disponibles, règle Vale francisée, workflow Docs CI opérationnel.

## Structure du dépôt

- `templates/` — gabarits principaux :
  - `01-Strategie-de-test.md` – stratégie globale.
  - `02-Plan-de-test.md` – plan de test release / itération.
  - `03-Spec-Conception-de-test.md` – conception et conditions de test.
  - `04-Spec-Cas-de-test.md` – cas de test détaillés.
  - `05-Spec-Procedures-de-test.md` – procédures d'exécution.
  - `06-Plan-Donnees-de-test.md` – stratégie & gestion des données.
  - `07-Exigences-Environnement-de-test.md` – environnements, accès, monitoring.
  - `08-Rapport-Statut-de-test.md` – suivi d'avancement.
  - `09-Rapport-Cloture-de-test.md` – bilan et critères de sortie.
- `styles/` — configuration Vale (dictionnaire français, règles `Fr.Spelling`).
- `standards/` — références normatives (`references.yaml`) et glossaires (`glossaire-istqb.md`).
- `docs/` — guides d'adoption et usage (#29).
- `decisions/` — journal des Decision Records (DR) futur (#7, #30).

## Outillage & CI

- **Vale 3.12.0** avec style `Fr` : vérifie orthographe / terminologie française. Commandes utiles :
  - `vale README.md`
  - `shopt -s globstar && vale README.md templates/**/*.md`
- **markdownlint-cli2** : exécuté via GitHub Actions `Docs CI` (action `DavidAnson/markdownlint-cli2-action`).
- **Workflow `Docs CI`.** Étapes : checkout → markdownlint → Vale → script qui exige un bloc `Référence normative` dans le corps de PR.
- **Protection `main`.** Historique linéaire, résolution des conversations obligatoire, pas de reviews obligatoires tant que l'équipe est solo.

## Méthode de contribution

1. Créer une branche (`feature/...`, `docs/...` ou `chore/...`).
2. Installer/réutiliser Vale via `~/.local/bin/vale` (voir `styles/` pour config).
3. Modifier les gabarits / docs en respectant le front matter YAML et la terminologie.
4. Lancer localement :
   - `vale README.md templates/**/*.md`
   - `npx markdownlint-cli2 README.md` (ou via container/outillage local).
5. Ouvrir une PR avec un paragraphe `Référence normative` listant les sources (ISO, ISTQB, etc.).
6. Vérifier le workflow `Docs CI`, répondre aux alertes, fusionner via squash/rebase.

Conventions : commits en anglais (`conventional commits`), décisions structurées via DR (#7) lorsque nécessaire.

## Références normatives

- ISO/IEC/IEEE 29119-2 & 29119-3 (processus et livrables test).
- ISO/IEC 25010 (modèle de qualité / NFR).
- ISTQB® Glossary 4.0 (cf. `standards/glossaire-istqb.md`).
- IEEE 1012 (V&V) — en préparation.
- Fichier `standards/references.yaml` pour centraliser les identifiants utilisés dans les PR et documents.

## Feuille de route

- [ ] #2 Rédiger ce README (en cours).
- [ ] #3 CONTRIBUTING.md (règles de contribution détaillées).
- [ ] #4 GOVERNANCE.md (processus de décision, rôles).
- [ ] #5 CODEOWNERS (revues obligatoires par périmètre).
- [ ] #6 Conventions d’identifiants (nomenclatures templates/tests).
- [ ] #7 Modèle de Decision Record et guide DR (#30).
- [ ] #22 Annexes techniques & chartes exploratoires.
- [ ] #27 Workflow de release + changelog.

Consulter les issues pour priorités à jour.

## Licence

Publication sous licence Creative Commons BY 4.0 (issue #1). Toute contribution implique l’acceptation de cette licence et le respect des sources normatives citées.
