# Imageomics Glossary

This glossary is designed as a resource for members of the Imageomics Institute from various backgrounds to familiarize themselves with key terms and concepts encountered in our work. 

It includes concepts in biology, ecology, genetics, machine learning and artificial intelligence, computer science, and software engineering. 

Definitions are not meant to be comprehensive. Ideally, they will be tailored to our institute's context.

It is meant to be a collaborative effort, so please contribute terms you would like defined, definitions you know, or corrections for errors you notice!

# A
### Application Programming Interface (API)


### Autoencoder


# B

# C

### CARE Principles for Indigenous Data Governance
"People and purpose-oriented" to complement [FAIR Principles](#fair-data-principles).

**C**ollective Benefit

**A**uthority to Control

**R**esponsibility

**E**thics

For more information, see [CARE Principles for Indigenous Data Governance](https://www.gida-global.org/care).

### Contrastive Language-Image Pre-training (CLIP)

# D
### Decoder


### Dimensionality Reduction
Used in machine learning and data analysis to refer to a set of methods used to reduce the number of variables or features under consideration to a smaller subset with the greatest explanatory power without drastically reducing the accuracy of the model or analysis. The purpose is to exclude irrelevant, redundant, and noisy information, thereby improving computational complexity and model interpretability. 

That is, it seeks to preserve the "most important" variables or features of the data based on some quantitative metric, such as variance, while removing "less important" variables or features. This is especially helpful when using high-dimensional data such as images or genomes.

Dimensionality reduction techniques can be subdivided into two main categories:
* [Feature Extraction](#feature-extraction)
* [Feature Selection](#feature-selection)

### Docker


# E
### Ecology


### Epoch (in machine learning)


### Encoder


### Experiment (in machine learning)

# F
### FAIR Data Principles
**F**indable -- metadata and data easily found by both humans and machines

**A**ccessible -- clear indication of how to access data once it is found.

**I**nteroperable -- ability to integrate with other data and be used by various systems (applications and workflows).

**R**eusable -- clearly described so it is easily used by others.

For more information, see [fair principles](https://www.go-fair.org/fair-principles/).

### Feature
In machine learning and data science, a feature is a single measurable property or characteristic of the phenomenon under observation. With tabular data, a feature is a column in the dataset used by a model to make predictions. In genomics, a feature could be, for example, gene expression levels, the presence (or absence) of certain genetic variants (such as [SNPs](#single-nucleotide-polymorphism-snp), insertions and deletions (indels), and others), or epigenetic markers.

### Feature Extraction
A set of [dimensionality reduction](#dimensionality-reduction) techniques used to map raw data to a smaller set of features. Example techniques include [PCA](#principal-component-analysis-pca), [MDS](#multidimensional-scaling-mds), [t-SNE](#t-distributed-stochastic-neighbor-embedding-t-sne), [autoencoders](#autoencoder), and Fourier or wavelet transforms.

The key difference from feature selection is that feature extraction generates a new set of features from the original dataset by projecting or mapping the data into a new feature space rather than selecting from existing features.

### Feature Selection
A method to select a subset of relevant features for use in model construction.

The key difference from feature extraction is that feature selection does not generate new features but rather identifies the most meaningful existing features in a dataset by excluding redundant or irrelevant features. For example, in genomics, feature selection would involve selecting the most important gene(s) relevant to a certain phenotype among thousands of genes. 

### Feature Space


# G
### Genome-Wide Association Study (GWAS)


# H
### Hyperparameter Tuning
The process of selecting the best hyperparameters for a machine learning model by minimizing the [loss function](#loss-function). This can be done through [experiments](#experiments-in-ml) or in some cases, using optimization techniques. Hyperparameters are parameters that are set by the researcher before training and are not learned during the training process. Some examples of common hyperparameters are [learning rate](#learning-rate), number of [epochs](#epoch-in-machine-learning), number of clusters (k) in [k-means clustering](#k-means-clustering), and many others.  

# I
### Imageomics

i-'mi-j**ə**-'**ō**-miks

A new scientific field in which computational (machine learning) tools built around biological knowledge bases are used by biologists to analyze image data in order to characterize patterns and gain insights into traits and relationships at individual, population and species scales—insights that then get incorporated into the algorithms that run the tools.

# J

# K
### K-Means Clustering


# L
### Latent Space


### Learning Rate


### Loss Function


# M
### Multidimensional Scaling (MDS)

# N
### Nucleotide
The fundamental building blocks of DNA and RNA. A nucleotide is composed of a base and a sugar-phosphate backbone. 

Bases for DNA: adenine (A), guanine (G), cytosine (C), and thymine (T). 

Bases for RNA: adenine (A), guanine (G), cytosine (C), and uracil (U).

Backbone sugar for RNA: ribose

Backbone sugar for DNA: deoxyribose (one less oxygen atom than ribose)

The bases A, G, and C are the same molecule for DNA and RNA. T and U are incorporated into their sequences differently due to the presence of substrate molecules accessible to DNA polymerase and RNA polymerase, which are the enzymes responsible for "manufacturing" the relevant sequences. DNA polymerase must use deoxyribonucleotides (dNTPs), and RNA polymerase must use ribonucleotide triphosphates (NTPs). Again, the difference is that there is one less oxygen atom in dNTPs vs NTPs. Cells have dATPs, dGTPs, dCTPs, and dTTPs for DNA polymerase to incorporate into a DNA sequence, but there are normally no dUTPs (and in cases where dUTPs are present and incorporated into DNA, "error correction" enzymes replace them using dTTPs). Likewise for RNA polymerase, ATP, GTP, CTP and UTP are available, but TTP is not. These substrates also serve other important purposes, such as how ATP (adenosine triphosphate) is used as a primary source of energy for many cellular processes.

A DNA or RNA molecule consists of a chain of the four relevant nucleotides in a sequence, where the order of A, G, C, and T in the DNA sequence determines the "blueprint" for the organism, and the order and length of A, G, C, and U in an RNA sequence determines the purpose and function of the RNA molecule, which can be a messenger RNA (mRNA) that encodes a protein, a microRNA (miRNA) which are short RNAs that help regulate gene expression by binding to other mRNAs, and many others.

# O
### Ontology


# P
### Phenotype


### Phylogeny


### Pre-training


### Principal Component Analysis (PCA)


# Q

# R

# S
### Single Nucleotide Polymorphism (SNP)
A SNP (pronounced "snip") is a variation in the [nucleotide](#nucleotide) present at a single position in a DNA sequence among individuals in a species. For example, a SNP may be the replacement of a cytosine (C) by a thymine (T) at the same location in a stretch of DNA, where C is observed in a subset of individuals and T is observed in the others.

### Snakemake


### Subspecies


### Supervised Learning
As opposed to [unsupervised learning](#unsupervised-learning), supervised learning methods learn from labeled data. That is, it is trained using input data that is labeled with corresponding outputs, such as the input of an image and the output of a classification.

# T
### Taxonomy


### t-Distributed Stochastic Neighbor Embedding (t-SNE)


### Trait

### Transfer Learning

# U
### Unsupervised Learning
As opposed to [supervised learning](#supervised-learning), unsupervised learning detects patterns or structures within the input data without any labels. Clustering and dimensionality reduction techniques are some examples.

# V
VLMs (Vision-Language Models)

# W

# X

# Y

# Z
### Zero-Shot Prediction

