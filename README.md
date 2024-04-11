# Drug Candidate Development against Non-alcoholic Steato Hepatitis

## Background

Non-alcoholic fatty liver disease (NAFLD) is defined as the ectopic accumulation of fat in the liver (hepatic steatosis) when no other causes of secondary liver fat accumulation are present. Although minor deposition of fat can occur in the livers of healthy adults, deposition of fat in at least 5% of hepatocytes is considered pathological. NAFLD includes both nonalcoholic fatty liver (NAFL) and nonalcoholic steatohepatitis (NASH), which is diagnosed when there is evidence of inflammatory activity and hepatocyte injury in steatotic liver tissue (Pang et al. .,2019, Hester et al ., 2020, Kaplan et al., 2019). Nonalcoholic fatty liver disease (NAFLD), including nonalcoholic steatohepatitis (NASH), reportedly affects the health status of approximately one in four people worldwide according to a recent meta-analysis ( Younossi et al., 2016). Nonalcoholic steatohepatitis (NASH) is the most severe form of nonalcoholic fatty liver disease (NAFLD), a condition in which the liver builds up excessive fat deposits. NASH clearly progresses to cirrhosis with further decompensation, leading to death or liver transplantation in some individuals (Goh et al., 2016, Chalasani et al. ., 2018, Asrani et al., 2019,) 

It is estimated that over 115 million adults are affected by NASH worldwide (Tesfay et al ., 2018). NASH is currently the fastest-rising cause of hepatocellular carcinoma (HCC) worldwide (Tan et al. ., 2022, Huang et al., 2022). Approximately 25% of the adult population worldwide has NAFLD, with the highest prevalence rates in South America (31%) and the Middle East (32%) and the lowest rate in Africa (14%). The prevalence of NASH in adults has been approximated to be 1.5% – 6.45% (Younossi et al. ., 2016). Globally, NAFL/NASH is estimated to account for approximately 25% of the population. The global prevalence of NASH among patients with T2DM is 37.3%. Approximately 17% of the patients with NAFL/NASH and T2DM develop advanced fibrosis. Furthermore, the frequency and severity of NAFL/NASH vary according to the geographic region and ethnicity. Specifically, the Middle East was found to have the highest frequency of NAFL/NASH (31.79%), followed by Asia (27.37%), South America (24.13%), North America (24.13%), and Europe (23.71%), whereas Africa had the lowest prevalence (13.48%) (Mitra et al., 2020, Younossi et al., 2016 ). By 2030, the number of people with NASH in China is expected to reach 48.26 million. Spain had 1.8 million cases in Europe in 2016, with the number expected to increase by 49% by 2030. German cases of NASH stood at 3.33 million in 2016 and are projected to increase by 43% by 2030. In addition, researchers anticipate 27 million cases of NASH in the U.S. by 2030 (Estes et al., 2018). Not only does an increase in NASH cases negatively impact lives, but there can also be a steep economic impact on patients and their families, payers, and governments. In the U.S., the annual direct cost of treating NAFLD reaches $103 billion, while four European countries (Germany, France, Italy, and the United Kingdom) spend approximately €35 billion a year (Younossi et al., 2016).

People with cirrhosis (severe fibrosis or scarring) of the liver related to NASH may experience; Intense itching, Abdominal swelling, Easy bruising and bleeding, Jaundice (yellowing of the skin and eyes), Spider-like blood vessels beneath the skin's surface, Behavior changes, confusion, and slurred speech  ( Sharma et al., 2023). No medications have been approved for the treatment of NAFLD, including NASH, but researchers are currently studying different potential therapies for NASH. 

The Farnesoid X Receptor (FXR), a ligand-activated nuclear receptor transcription factor is considered a crucial and viable target since it is a key metabolic regulator of bile acid homeostasis, inflammation, and metabolism of lipids. 


## Objective

This study seeks to identify novel potential agonists of FXR, presenting promising candidates for drug development aimed at treating Non-Alcoholic Steato Hepatitis (NASH). 


## Workflow 

<p align="center">
    <img width="100%" src="https://github.com/omicscodeathon/hepadrug/blob/main/workflow/Schema.jpeg" alt="Workflow">
</p>

<p align="center">
Figure 1: Detailed flow of the various methods carried out in the study.   
</p>

### Bioinformatics Tools Required 
```
Modeller
PyMOL
LigandScout
DataWarrior
PyRx/AutoDockVina
LigPlot+
GROMACS
PASS Online
SwissADME
SwissParam
GalaxyRefine
CASTp
```


## Methods
- FXR, a bile acid nuclear receptor, is a master regulator of bile acid synthesis, excretion, and absorption. As such, FXR has been a hot drug target for the development of treatments for NASH.
- The 3D crystallographic solved structure of FXR with PDB ID 10SH was retrieved from RCSB Protein Data Bank (https://www.rcsb.org/).
- The structure was visualized with PyMOL by removing water molecules and any additional chains. 
- Modeller was used to replace all missing residues in the structure using modeller scripts (hepadrug/scripts/Modeller_scripts/). 
- Subsequent improvements of the improved tertiary structure of FXR were done with the GalaxyRefined (https://galaxy.seoklab.org/cgi-bin/submit.cgi?ty.pe=REFINE).
- Structure energy minimisation was done using GROMACS utilizing both the CHARMM and OPLS/AA force fields (https://gromacs.bioexcel.eu/t/energy-minimization-and-stereochemistry/506/4). 
- The results obtained from the galaxy were validated using PROCHECK (https://saves.mbi.ucla.edu/).
- CASTp was subsequently used to predict the ligand-binding site of FXR.
- Library preparation; Initially, 3D sdf data of 1871 and 4924 compounds were selected after a rigorous literature review from EANPDB and NANPDB respectively (http://african-compounds.org/nanpdb). 
- Compound screening; Free ADME-Tox Filtering Tool version 4.0 (FAF-Drugs), a program for filtering large compound libraries prior to in silico screening experiments or related modeling studies was used to filter the libraries for Druglike molecules (https://bioserv.rpbs.univ-paris-diderot.fr/services.html). Datawarrior was used for Toxicity screening. 
- LigandScout 4.5 (http://www.inteligand.com/ligandscout), a fully integrated platform for accurate virtual screening based on 3D chemical pharmacophore models was used to generate pharmacophore models from an input set of 15 reported FXR agonists (data/fxr_agonists/). It offers seamless workflows, starting from both ligand-based and structure-based pharmacophore modelling.
- The best-generated model was validated by screening it against the 15 agonists and 500 decoys (output/Ligand-based_pharmacophore/decoys.smi) generated from DUD-E.
- The validated model was used to virtually screen the EANPDB and NANPDB druglike compounds to obtain pharmacophore hits. 
- AutoDock Vina interfaced with PyRx was used to carry out docking studies, screening the pharmacophore hits against the binding site of FXR.
- LigPlot+ and PyMOL were used to analyze the interactions between the pharmacophore hits and the FXR, post docking.
- SwissAME was used to predict the pharmacokinetics and physicochemical properties of hits obtained.
- PASS online predicted the biological activities of obtained hits by receiving SMILES as input.
- Molecular Dynamics Simulations of complexes were done by means of GROMACS.





## Results

<h4 align="center">
Homology Modelling, Refinement and Binding Site Pred 
</h4>

<p><img align="left" width="50%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/modelled_FXR.png" alt="Workflow"> <img width="45%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/energy_minimized_FXR.png" alt="Workflow"> Figure 1: Structure of the Modeller redesigned FXR protein structure, added residues in yellow;   Figure 2: Energy minimized structure through GROMACS. Protein surrounded by water molecules (red) and ions </p>

<p><img align="left" width="45%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/Potential_Energy_Graph.PNG" alt="Workflow"> <img width="50%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/CasTp_Pred..PNG" alt="Workflow"> Figure 3: Potential energy graph of refined FXR through CHARMM and OPLS/AA force fields;   Figure 4: CASTp predicted ligand-binding pocket of FXR (red)  </p>


![CASTp](figures/CastTpred.PNG)
<p align="center">
Figure 5: Corresponding binding amino acid residues in the binding pocket (red) 
</p>


<p align="center">


</p>

<h4 align="center">
Ligand Library Preparation 
</h4>

![EANPDB](figures/EANPDB_DrugLike_summary.JPG)
<p align="left">
Figure 6: Job Summary from EANPDB Drug likeness filtering with FAF-Drugs4.1, 1152 molecules passed the DrugLikeness test. 
</p>

![EANPDB](figures/NANPDB_DrugLike_summary.JPG)
<p align="left">
Figure 7: Job Summary from NANPDB Drug likeness filtering with FAF-Drugs4.1, 2842 molecules passed the DrugLikeness test. 
</p>

<p align="center">


</p>

<h4 align="center">
Pharmacophore Generation and Screening
</h4>

<p><img align="left" width="55%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/Generated_Pharmacophore_model.JPG" alt="Workflow"> <img width="40%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/Model_Validation_ROC.png" alt="Workflow"> Figure 8: LigandScout generated pharmacophore model showing all four features 3 HBA (red) and 1 H (yellow);  Figure 9: ROC curve of validated pharmacophore, overall AUC of 0.80 obtained   </p>


![inhibitors](figures/6_inhibitors_on_pharmacophore.JPG)
![inhibitors](figures/9_inhibitors_on_pharmacophore.JPG)
<p align="center">
Figure 10: All agonists used in model generation and their shared pharmacophore features 
</p>


<p align="center"><img align="center" width="55%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/Top_10_Pharmacophore-Hits_on_Pharmacophore.JPG" alt="Workflow">  </p>

<p align="center">
Figure 11: Top 10 Pharmacophore-Hits mapped onto generated Pharmacophore model 
</p>

<p align="center">



</p>

Table 1: Top 5 EANPDB Pharmacophore Hits after ligand-based screening.
| Ligand | Pharmacophore Fit Score |
| ------ | ----------------------- |
| aloenin acetal | 45.25 |
| busseihydroquinone D | 44.5 |
| 13-acetoxy-17-hydroxy-labda-8,14-diene-17-O-(xylopyranoside triacetate) | 44.51 |
| knipholone mannich base | 44.27 |
| burttinone | 44.2 |

<p align="center">


</p>

<h4 align="center">
Docking Studies 
</h4>

<p align="center"><img align="center" width="55%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/Ligand_in_biniding_site.JPG" alt="Workflow">  </p>

<p align="center">
Figure 12: Surface view of Docked compound (pink) in FXR (blue)
</p>

<p align="center">

<p><img align="left" width="50%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/pose1.JPG" alt="Workflow"> <img width="45%" src="https://github.com/omicscodeathon/hepadrug/blob/main/figures/ validation.JPG" alt="Workflow"> Figure 13: Superimposition of FXR ligands, RSMD of 0.00 was obtained;   Figure 2: Ligand interactions of redesigned FXR and 1OSH structure </p>


## Conclusion





## Team Members
1. Chimenya Ntweya (Department of Biotechnology and Bioinformatics, Deogiri College, Aurangabad, India; Department of Medical Laboratory, Queen Elizabeth Central Hospital, Blantyre, Malawi) chimenyantweya54@gmail.com)
2. Desmond Osarfo Amoah (Department of Parasitology, Noguchi Memorial Institute for Medical Research, University of Ghana) desmondqwejo@gmail.com)
3. Oudou Diabate (diabateoudou@gmail.com), African Centre of Excellence in Bioinformatics (ACE-B), University of Sciences, Techniques and Technologies of Bamako (USTTB), Mali
4. Olaitan I.Awe (laitanawe@gmail.com), African Society for Bioinformatics and Computational Biology, Cape Town, South Africa




