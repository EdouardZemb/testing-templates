---
title: "Cartographie NFR ↔ ISO 25010"
source: "ISO/IEC 25010"
link: "https://www.iso.org/standard/35733.html"
last_updated: "2025-10-06"
---

> Synthèse des caractéristiques et sous-caractéristiques ISO/IEC 25010, avec exemples de mappage vers des exigences non fonctionnelles de projet.

## Tableau ISO 25010

| Caractéristique | Sous-caractéristique | Description synthétique | Exemple d’exigence projet |
| --------------- | -------------------- | ----------------------- | ------------------------- |
| Fonctionnalité  | Adéquation fonctionnelle | Capacité du produit à fournir les fonctions spécifiées. | "L’API expose toutes les opérations CRUD planifiées." |
| Fonctionnalité  | Exactitude fonctionnelle | Niveau d’exactitude des résultats. | "Les calculs de TVA respectent les barèmes officiels." |
| Fonctionnalité  | Interopérabilité | Capacité à interagir avec d’autres systèmes. | "Supporte SSO SAML avec l’IdP d’entreprise." |
| Fonctionnalité  | Sécurité fonctionnelle | Prévention des effets négatifs en cas de défaillance. | "Les transactions critiques disposent d’un mécanisme d’annulation." |
| Fonctionnalité  | Traçabilité | Possibilité d’identifier les origines des actions. | "Historique complet des commandes accessible 12 mois." |
| Fiabilité       | Maturité | Probabilité de fonctionnement sans défaillance. | "MTBF ≥ 500 h en production." |
| Fiabilité       | Disponibilité | Aptitude à être opérationnel quand requis. | "Disponibilité ≥ 99,5 % (heures ouvrées)." |
| Fiabilité       | Tolérance aux fautes | Capacité à fonctionner malgré des fautes. | "Failover automatique sur région secondaire ≤ 5 min." |
| Fiabilité       | Récupérabilité | Capacité à se rétablir après incident. | "Restauration de données ≤ 1 h avec perte ≤ 15 min." |
| Performance/efficience | Comportement temporel | Temps de réponse, latence. | "Page produit s’affiche ≤ 3 s pour 95 % des requêtes." |
| Performance/efficience | Utilisation des ressources | Consommation CPU, mémoire, bande passante. | "Charge CPU < 70 % sur 4 vCPU lors des pics." |
| Performance/efficience | Capacité | Capacité à traiter un volume donné. | "Supporte 10 000 sessions concurrentes." |
| Compatibilité   | Coexistence | Partage de ressources avec d’autres produits. | "Installation possible sur serveur mutualisé sans conflit." |
| Compatibilité   | Interopérabilité | Interaction avec systèmes externes. | "Expose un connecteur REST aligné sur XConnect v2." |
| Sécurité        | Confidentialité | Protection des données contre l’accès non autorisé. | "Les données sensibles en transit chiffrées (TLS 1.3)." |
| Sécurité        | Intégrité | Prévention des modifications non autorisées. | "Signatures numériques pour les documents PDF." |
| Sécurité        | Non-répudiation | Preuve des actions effectuées. | "Journal signé pour chaque opération financière." |
| Sécurité        | Traçabilité | Capacité à suivre l’activité. | "Logs audit horodatés, conservés 1 an." |
| Sécurité        | Authenticité | Vérification de l’identité. | "Authentification MFA pour les comptes admin." |
| Sécurité        | Responsabilité | Attribution des actions aux acteurs. | "Flux métier associé à un identifiant utilisateur." |
| Maintenabilité  | Modulabilité | Facilité à être modifié sans impact. | "Architecture modulaire (microservices)." |
| Maintenabilité  | Réutilisabilité | Capacité à réutiliser des composants. | "Bibliothèque UI partagée sur 3 projets." |
| Maintenabilité  | Analysabilité | Capacité à diagnostiquer les défauts. | "Logs applicatifs enrichis (correlation IDs)." |
| Maintenabilité  | Modifiabilité | Facilité de changement. | "Un changement de règle métier se fait via configuration." |
| Maintenabilité  | Testabilité | Facilité à tester. | "Couverture automatisée > 80 % sur modules critiques." |
| Portabilité     | Adaptabilité | Capacité à être adapté à différents environnements. | "Application compatible Desktop & mobile responsive." |
| Portabilité     | Installabilité | Facilité d’installation. | "Déploiement automatisé en moins de 15 minutes." |
| Portabilité     | Remplaçabilité | Capacité à être remplacé par un autre produit. | "APIs documentées pour migration future." |

## Utilisation

1. Choisir les sous-caractéristiques pertinentes pour le projet.
2. Traduire les exemples en exigences mesurables (SLO, métriques).
3. Associer les exigences aux sections NFR de la stratégie / plan / cas de test.

## Références

- `standards/references.yaml` — ISO/IEC 25010.
- `standards/glossaire-istqb.md` — Terminologie ISTQB.
