---
license: # See note below on choosing a license.
language:
- en
library_name: # Allows for Inference API widget on sidebar of model card
tags:
- biology
- CV
- images
- animals
datasets: # Adds link if on HF & shows up on sidebar. Ex: Imageomics/TreeOfLife-10M
metrics: # key list: https://hf.co/metrics
---

<!--

NOTE: Add more tags (your particular animal, type of model and use-case, etc.).

As with your GitHub Project repo, it is important to choose an appropriate license for your model. Alongside the appropriate stakeholders (eg., your PI, co-authors), select a license that is [Open Source Initiative](https://opensource.org/licenses) (OSI) compliant. You may also wish to consider adding a [RAIL license](https://www.licenses.ai/ai-licenses), which addresses responsible use.
For more information on how to choose a license and why it matters, see [Choose A License](https://choosealicense.com) and [A Quick Guide to Software Licensing for the Scientist-Programmer](https://doi.org/10.1371/journal.pcbi.1002598) by A. Morin, et al.
See the [ABC Global Center policy for licensing](https://docs.google.com/document/d/1SlITG-r7kdJB6C8f4FCJ9Z7o7ccwldZoSRJKjhRAWVA/edit#heading=h.c1sxg0wsiqru) for more information.

License tags (for the `yaml` above) can be found [here](https://hf.co/docs/hub/repositories-licenses).

See more options for the above information by clicking "edit model card" on your repo.

Fill in as much information as you can at each location that says "More information needed".
-->


<!--
Image with caption (jpg or png):
|![Figure #](https://huggingface.co/ABC-Center/<model-repo>/resolve/main/<filepath>)|
|:--|
|**Figure #.** [Image of <describe image>](https://huggingface.co/ABC-Center/<model-repo>/raw/main/<filepath>) <caption description>.|
-->

<!--
Notes on styling:

To render LaTex in your README, wrap the code in `\\(` and `\\)`. Example: \\(\frac{1}{2}\\)

Escape underscores ("_") with a "\". Example: image\_RGB
-->

# Model Card for [Model Name]

<!-- Provide a quick summary of what the model is/does. 

This model card aims to be a base template for new models. It has been generated using [this raw template](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md?plain=1), and further altered to suit ABC Global Center needs. -->

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Developed by:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** [More Information Needed -- choose a license (see above notes)]
- **Fine-tuned from model:** [More Information Needed]

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** [Project Repo]
- **Paper:** [More Information Needed--optional]
- **Demo:** [More Information Needed--encouraged]

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

### Downstream Use

<!-- [optional] This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model

Use the code below to get started with the model.

<!-- Put code here or links to files to run. Set up code blocks like this:
```
<code here>
```
-->

[More Information Needed]

## Training Details

### Training Data

<!-- This should link to a Dataset Card where possible, otherwise link to the original source with more info. 
Provide a basic overview of the training data and documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure 

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing

[More Information Needed--encouraged]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times 

<!-- [optional] This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

[More Information Needed]

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible, otherwise link to the original source with more info.
Provide a basic overview of the test data and documentation related to any data pre-processing or additional filtering. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary

[More Information Needed]

## Model Examination

<!-- [optional] Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- 
It would be great to try to include this.

Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://doi.org/10.48550/arXiv.1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications 
[More Information Needed--optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed: hardware requirements]

#### Software

[More Information Needed]

## Citation

<!-- If there is a paper introducing the model, the Bibtex information for that should go in this section. 

See notes at top of file about selecting a license. 
If you choose CC0: This model is dedicated to the public domain for the benefit of scientific pursuits. We ask that you cite the model and journal paper using the below citations if you make use of it in your research.

-->

**BibTeX:**

[More Information Needed]
<!--
Replace "<>"s with your info:

If you use our model in your work, please cite the model and associated paper.

**Model**
```
@software{<ref_code>,
  author = {<author1 and author2>},
  doi = {<doi once generated>},
  title = {<title>},
  version = {<version#>},
  year = {<year>},
  url = {https://huggingface.co/ABC-Center/<model_name>}
}
```

-for an associated paper:
**Paper**
```
@article{<ref_code>,
  title    = {<title>},
  author   = {<author1 and author2>},
  journal  = {<journal_name>},
  year     =  <year>,
  url      = {<DOI_URL>},
  doi      = {<DOI>}
}
```
-->


## Acknowledgements

This work was supported by the [AI and Biodiversity Change (ABC) Global Center](http://abcresearchcenter.org/), which is funded by the US National Science Foundation under [Award No. 2330423](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2330423&HistoricalAwards=false) and Natural Sciences and Engineering Research Council of Canada under [Award No. 585136](https://www.nserc-crsng.gc.ca/ase-oro/Details-Detailles_eng.asp?id=782440). This model draws on research supported by the Social Sciences and Humanities Research Council. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation, Natural Sciences and Engineering Research Council of Canada, or Social Sciences and Humanities Research Council.

Ce travail a été soutenu par le centre de recherche [AI and Biodiversity Change (ABC)](http://abcresearchcenter.org/), financé conjointement par la National Science Foundation des États-Unis ([Financement #2330423](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2330423&HistoricalAwards=false)) et par le Conseil de recherches en sciences naturelles et en génie du Canada ([Financement \#585136](https://www.nserc-crsng.gc.ca/ase-oro/Details-Detailles_eng.asp?id=782440)). Ce jeu de données repose également en partie sur des travaux de recherche financés par le Conseil de recherches en sciences humaines du Canada. Les opinions, conclusions ou recommandations exprimées dans ce document sont celles de(s) auteur(s) et ne reflètent pas nécessairement celles de la National Science Foundation, du Conseil de recherches en sciences naturelles et en génie du Canada, ou du Conseil de recherches en sciences humaines du Canada.

## Glossary 

<!-- [optional] If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

## More Information 

<!-- [optional] Any other relevant information that doesn't fit elsewhere. -->

## Model Card Authors

[More Information Needed]

## Model Card Contact

[More Information Needed--optional]
<!-- Could include who to contact with questions, but this is also what the "Discussions" tab is for. -->