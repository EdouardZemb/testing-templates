# Politique de sécurité

Merci de contribuer à la sécurité de **testing-templates**. Nous prenons au sérieux toute vulnérabilité potentielle affectant les templates, guides ou automatisations du dépôt.

## 1. Comment signaler une vulnérabilité

- **Canal principal** : envoyez un e-mail à `security@testing-templates.org` (ou, à défaut, à l’auteur : `edouard.zemb@gmail.com`).
- **Alternative GitHub** : utilisez la fonctionnalité "Private vulnerability report" (onglet **Security** du dépôt).
- Évitez d’ouvrir une issue publique tant que la vulnérabilité n’est pas corrigée.

Merci de fournir :

1. Une description claire du problème et de son impact.
2. Les étapes de reproduction ou un POC.
3. Toute information additionnelle qui faciliterait l’analyse (logs, fichiers concernés).

## 2. Engagement de réponse

- Accusé de réception sous **3 jours ouvrés**.
- Évaluation de la sévérité et plan d’action communiqué sous **10 jours ouvrés**.
- Publication d’une correction et d’une note publique dès que la mesure est prête (coordinations possibles pour une divulgation conjointe).

## 3. Portée

Cette politique couvre :

- les templates Markdown fournis (`templates/`),
- les documents standards et guides (`standards/`, `docs/`),
- les workflows CI et scripts (`.github/`, `styles/`).

Les incidents affectant des systèmes de production externes ou des dépendances tierces doivent être signalés au fournisseur concerné.

## 4. Reconnaissance

Lorsque la vulnérabilité est confirmée et corrigée, nous pouvons mentionner le chercheur (avec accord) dans les notes de version ou un DR associé.

## 5. Contact complémentaire

Pour toute question non confidentielle, vous pouvez utiliser les issues GitHub en précisant le label `question`.
