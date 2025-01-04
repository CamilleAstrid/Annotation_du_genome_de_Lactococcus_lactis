# Annotation génomique de *Lactococcus lactis*

Ce dépôt contient le code, les données et les résultats associés à l'annotation bioinformatique d'un fragment du génome de *Lactococcus lactis*. Ce projet a été réalisé dans le cadre du Master 1 Bioinformatique et Biologie des Systèmes, année universitaire 2024-2025.

## Description du projet

*Lactococcus lactis* est une bactérie gram-positive utilisée dans les fermentations laitières et la production de levains. Cette étude vise à réannoter une région de son génome pour identifier les régions codantes (CDS) et leurs produits protéiques à l'aide d'outils bioinformatiques.

Les étapes principales incluent :
- Identification des cadres de lecture ouverts (ORF).
- Détection des codons start/stop, des sites de fixation du ribosome (RBS), et des promoteurs sigma.
- Caractérisation fonctionnelle et localisation subcellulaire des protéines codées.

## Contenu

### Dossiers et fichiers

- **scripts/** : Contient les scripts Python pour l'analyse et la conversion des fichiers.
  - `convert_to_GFF.py` : Script Python pour convertir les sorties des outils au format GFF.
  - `man.py`: Manuel utilisation du programme Python.
  - `search_motif` : Module Python pour la création d'en-tête du fichier de sortie.
  - `search_data` : Module Python pour la conversion des informations au format GFF.
  - **pseudocode/** : Scripts précédents écrits en pseudocode.
- **data/** : Données utilisées pour l'analyse.
  - `seq_L_lactis_lactis.fasta` : Séquence génomique d'intérêt.
- **results/** : Résultats générés par les outils d'analyse.
  - **GeneMark/** : Résultats de l'outil GeneMark.
  - **GeneMarkHMM/** : Résultats de l'outil GeneMarkHMM.
  - **ScanForMatches/** : Résultats de l'outil ScanForMatches.
    - **RBS/** : Matrice utilisée et résultats obtenus suite à la recherche de RBS.
    - **sigma_factor/** : Matrice utilisée et résultats obtenus suite à la recherche du facteur sigma.
    - **terminator_rho/** : Pattern utilisé et résultats obtenus suite à la recherche de terminateur rho-dépendant.
  - **ExtractSeq/** : Séquences génomiques de protéines hypothétiques extraites.
  - **TranSeq/** : Séquences protéiques traduites des séquences génomiques des ORF extraits.
  - **BLASTP/** : Alignements obtenus avec un Blast sur les séquences protéiques et analyse de la fonction par homologie de séquences.
  - **SignalIP/** : Résultats obtenus à la suite de l'analyse de la présence de signaux d'adressage de la protéine à la membrane avec l'outil SignalIP
  - **DeepTMHMM/** : Résultats obtenus avec DeepTMHMM sur la localisation subcellulaire des protéines et sur leur structure tridimensionnelle.
- **test_files/** : Dossier permettant de tester le programme de conversion au format GFF.
  - `test_convert_*.txt` : Fichiers correspondants aux fichiers de sortie des outils
  - `expected_GenMHMM_GFF-format.txt` : Fichier correspondant la sortie de l'outil GeneMarkHMM au format GFF directement, correspond au format attendu.
  - **output_files/** : Fichiers de sortie obtenus après conversion avec le programme convert_to_GFF.py
  
## Outils utilisés

1. **ORFfinder** : Identification des ORF.
2. **GeneMark** et **GeneMarkHMM** : Détection des régions codantes et des gènes.
3. **ScanForMatches** : Recherche des motifs RBS, sigma, et terminateurs rho-dépendants.
4. **BlastP** : Annotation fonctionnelle basée sur l’homologie de séquences.
5. **SignalIP** : Prédiction des peptides signaux.
6. **DeepTMHMM** : Analyse des protéines transmembranaires et localisation subcellulaire.
7. **Python/Perl** : Scripts pour automatiser l'analyse et convertir les données au format standard.

## Résultats principaux

- Identification de 7 protéines hypothétiques, dont 2 transmembranaires.
- Analyse fonctionnelle et localisation subcellulaire des protéines prédictives.
- Points d'amélioration : Entraînement spécifique des algorithmes pour *L. lactis* et exploration des terminateurs alternatifs.

## Installation et utilisation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/<votre-dépôt>.git
   cd <votre-dépôt>
   ```
2. Assurez-vous d'avoir Python et les dépendances nécessaires installés.
3. Exécutez les scripts pour reproduire les analyses :
   
   Utilisation avec un fichier GeneMarkHMM.LST :
   ```bash
   python scripts/convert_to_GFF.py GENMH <input_file> <output_file.GFF>
   ```
   Utilisation avec un fichier GeneMark :
   ```bash
   python scripts/convert_to_GFF.py GENM <input_file> <output_file.GFF>
   ```
   Utilisation avec un fichier ScanForMatches contenant les informations sur les RBS :
   ```bash
   python scripts/convert_to_GFF.py SFM <input_file> RBS <output_file.GFF>
   ```
   Utilisation avec un fichier ScanForMatches contenant les informations sur les promoteurs :
   ```bash
   python scripts/convert_to_GFF.py SFM <input_file> PROM <output_file.GFF>
   ```
   Utilisation avec un fichier ScanForMatches contenant les informations sur les terminateurs :
   ```bash
   python scripts/convert_to_GFF.py SFM <input_file> TERM <output_file.GFF>
   ```

## Licence

Ce projet et donc l'ensemble des éléments de ce répertoire est sous licence [MIT](LICENSE) (sauf cas précisé).

## Références

- Mémoire de Magistère : Isolement et sélection des souches de bactéries lactiques productrices des métabolites antibactériennes, par BELARBI Fatima (2010-2011) doi:10.13140/RG.2.2.13373.82405
- Wheeler, D L et al. “Database resources of the National Center for Biotechnology Information.” Nucleic acids research vol. 28,1 (2000): 10-4. doi:10.1093/nar/28.1.10
- Borodovsky M. and McIninch J. "GeneMark: parallel gene recognition for both DNA strands." Computers & Chemistry, 1993, Vol. 17, No. 19, pp. 123-133
- Lukashin, A V, and M Borodovsky. “GeneMark.hmm: new solutions for gene finding.” Nucleic acids research vol. 26,4 (1998): 1107-15. doi:10.1093/nar/26.4.1107
- https://blog.theseed.org/servers/2010/07/scan-for-matches.html By The SEED Team on July 16, 2010. The utility was written by Ross Overbeek; David Joerg and Morgan Price wrote sections of an earlier version. It is worth noting that it was strongly influenced by the elegant tools developed and distributed by David Searls.
- Van Rossum, G., & Drake, F. L. (2009). Python 3 Reference Manual. Scotts Valley, CA: CreateSpace.
- Wall, L., & others. (1994). The Perl programming language. Prentice Hall Software Series.

Pour toute question, veuillez contacter [Camille-Astrid Rodrigues](mailto:camilleastrid.cr@gmail.com).

---

Si des ajustements ou des ajouts sont nécessaires, n'hésitez pas à me le signaler !
