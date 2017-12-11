# ML_termProject

Predicting the Cellular Localization Sites of Proteins (By using yeast data set)

1. Introduction 

I chose the project theme as Predicting the Cellular of Yeast Localization Sites of Proteins.
Yeast is composed of cytosolic, nuclear, mitochondrial, membrane protein with no N-terminal signal, 
membrane protein with uncleaved signal, membrane protein, cleaved signal, extracellular, vacuolar, peroxisomal and endoplasmic reticulum lumen. 
It is classified as a different type of protein.
Understanding the localization of proteins in cells is vital to characterizing their functions and possible interactions. 
As a result, identifying the sub cellular compartment within which a protein is located becomes an important problem in protein classification.
                                                                                                                             
                                                                                                                                 
2. Data Set Information

Yeast data set has 1484 dates and 8 predictive attributes. 

1)mcg : McGeoch's method for signal sequence recognition.

2)gvh : von Heijne's method for signal sequence recognition.

3)alm : Score of the ALOM membrane spanning region prediction program.

4)mit : Score of discriminant analysis of the amino acid content of the N-terminal region(20 residues long) of mitochondrial and non-mitochondrial proteins.

5)erl : Presence of "HDEL" substring (thought to act as a signal for retention in the endoplasmic reticulum lumen). Binary attribute.

6)pox : Peroxisomal targeting signal in the C-terminus.

7)vac : Score of discriminant analysis of the amino acid content of vacuolar and extracellular proteins.

8)nuc : Score of discriminant analysis of nuclear localization signals of nuclear and non-nuclear proteins.

field has value of predictive attribute. The last field is the result and this means that it was be categorized as a total 10 kind of proteins. 
So, we can build the model by learning of this data. When new data comes into data set, we can predict what kind of protein it is.

number at last field mean 10 kind of protein.

0 : CYT (cytosolic or cytoskeletal)
1 : NUC (nuclear)  
2 : MIT (mitochondrial)
3 : ME3 (membrane protein, no N-terminal signal)
4 : ME2 (membrane protein, uncleaved signal)  
5 : ME1 (membrane protein, cleaved signal) 
6 : EXC (extracellular)
7 : VAC (vacuolar)  
8 : POX (peroxisomal)
9 : ERL (endoplasmic reticulum lumen)
