# Dataset Card Checklist

Below is a checklist encompassing all sections of a dataset card. Review notes and guidance provided in the full [dataset card template](HF_DatasetCard_Template_mkdocs.md/) for more details.

!!! tip "Pro tip"

    Use the eye icon at the top of this page to access the source and copy the markdown for the checklist below into an issue on your GitHub [Repo](GitHub-Repo-Guide.md) or [Project](Guide-to-GitHub-Projects.md) so you can check the boxes as you add each element to your [dataset card](HF_DatasetCard_Template_mkdocs.md).

## General Information

- [ ] **License**: Verify and specify the license type (e.g., `cc0-1.0`).
- [ ] **Language**: Indicate the language(s) (e.g., `en`).
- [ ] **Pretty Name**: Provide a descriptive name for the dataset.
- [ ] **Task Categories**: List relevant task categories (e.g., image-classification). Refer to [the coarse-grained taxonomy of task categories as well as subtasks in this file](https://github.com/huggingface/huggingface.js/blob/main/packages/tasks/src/pipelines.ts).
- [ ] **Tags**: Include relevant tags (e.g., `biology`, `image`, `animals`, `CV`).
- [ ] **Size Categories**: Specify dataset size (e.g., `n<1k`, `1k<n<10k`, etc.).

---

## Dataset Details

- [ ] **Curated by**: List curators or authors.
- [ ] **Language(s) (NLP)**: Specify if applicable.
- [ ] **Homepage**: Provide a link to the homepage (if you have a website set up, not required).
- [ ] **Repository**: Link to related GitHub repository.
- [ ] **Paper**: Link to related research paper (not expected at this point).
- [ ] **Description**: Provide a summary of what the dataset is used for.
- [ ] **Supported Tasks and Leaderboards**: List any relevant tasks and leaderboards, e.g., benchmarking results.

---

## Dataset Structure

- [ ] **Data Format**: Describe the structure of the dataset. See guidance on formatting in the [full dataset card template](HF_DatasetCard_Template_mkdocs.md/#__codelineno-0-71).
- [ ] **Data Instances**: Describe data files.
E.g.: All images are named `<img_id>.png`, each within a folder named for the species. They are 1024 x 1024, and the color has been standardized using `<link to color standardization package>`.
- [ ] **Data Fields**: Describe the types of the data files or the columns in a CSV with metadata ([example](HF_DatasetCard_Template_mkdocs.md/#__codelineno-0-114)).
- [ ] **Data Splits**: Describe any splits (e.g., train, test, validation).

---

## Dataset Creation

Refer to examples and explanations provided in the full [dataset card template](HF_DatasetCard_Template_mkdocs.md/#__codelineno-0-129).

- [ ] **Curation Rationale**: Explain why this dataset was created.
- [ ] **Source Data**: Describe the source data.
    - [ ] **Data Collection and Processing**: Describe data creation, selection, filtering, normalization, and tools used.
    - [ ] **Source Data Producers**: List original data producers or sources.
- [ ] **Annotations**: Include details on annotations.
    - [ ] **Annotation Process**: Describe the process and tools used.
    - [ ] **Annotators**: List the annotators if applicable.
- [ ] **Personal and Sensitive Information**: Indicate any sensitive information in the dataset.

---

## Considerations for Using the Data

There are several things to consider while working with the dataset that should be reported to users. For instance, maybe there are hybrids and they are labeled in the `hybrid_stat` column, so to get a subset without hybrids, subset to all instances in the metadata file such that `hybrid_stat` is _not_ "hybrid".

- [ ] **Bias, Risks, and Limitations**: Describe any known issues with the dataset. For instance, if your data exhibits a long-tailed distribution (and why).
- [ ] **Recommendations**: Provide recommendations for using the dataset responsibly.
- [ ] **Reporting issues**: Provide a link to the issue tracker or other mechanism for reporting problems (e.g. mislabeling, corrupted images, etc.). This can simply be the Community tab for the repository or Issues on the associated GitHub repository.

---

## Licensing Information

See discussion and references in the [template](HF_DatasetCard_Template_mkdocs.md/#__codelineno-0-19), also remember the [digital product release and licensing policy](Digital-products-release-licensing-policy.md/).

- [ ] **Licensing Details**: Confirm and list all licensing details.

---

## Citation

- [ ] **Data Citation**: Provide a BibTeX citation for the dataset.
- [ ] **Associated Paper Citation**: Provide a BibTeX citation for any associated papers.

---

## Acknowledgements

- [ ] **Acknowledgements**: Include funding or support acknowledgments.

---

## Glossary (Optional)

- [ ] **Glossary**: Provide definitions for relevant terms or calculations.

---

## More Information (Optional)

- [ ] **Additional Information**: Add any other relevant information.

---

## Dataset Card Authors

- [ ] **Authors**: List the authors of the dataset card.

---

## Dataset Card Contact

- [ ] **Contact Information**: [OPTIONAL] We recommend people use HF discussions, but you may indicate a person to contact.

!!! question "[Questions, Comments, or Concerns?](https://github.com/Imageomics/Collaborative-distributed-science-guide/issues)"
