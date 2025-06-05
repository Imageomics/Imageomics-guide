# Model Card Checklist

Below is a checklist encompassing all sections of a model card. Review notes and guidance provided in the full [model card template](HF_ModelCard_Template_mkdocs.md/) for more details.

!!! tip "Pro tip"

    Use the eye icon at the top of this page to access the source and copy the markdown for the checklist below into an issue on your GitHub [Repo](GitHub-Repo-Guide.md) or [Project](Guide-to-GitHub-Projects.md) so you can check the boxes as you add each element to your [model card](HF_ModelCard_Template_mkdocs.md).

## General Information

- [ ] **Model Name**: Provide the name of the model.
- [ ] **Model Summary**: Provide a quick summary of what the model is/does
- [ ] **License**: Choose an appropriate license (e.g., `cc0-1.0`).
- [ ] **Language(s)**: Specify the language(s) used (e.g., `en`).
- [ ] **Tags**: Include relevant tags (e.g., `biology`, `CV`, `images`, `animals`).
- [ ] **Datasets**: List datasets used for training, linking if hosted on Hugging Face. E.g.: imageomics/TreeOfLife-10M
- [ ] **Metrics**: Specify key evaluation metrics (refer to [Hugging Face metrics list](https://hf.co/metrics)).

---

## Model Details

- [ ] **Detailed Summary**: Provide a longer summary of what this model is.
- [ ] **Developed by**: List the developers.
- [ ] **Model Type**: Describe the model type.
- [ ] **Fine-tuned from**: Specify the base model if fine-tuned.
- [ ] **Version**: Indicate the model version.
- [ ] **Repository**: Provide the link to the project repository (GitHub).
- [ ] **Paper**: Link to any associated research papers (not expected at this point).
- [ ] **Demo**: Link to an interactive demo (if available).

---

## Uses

- [ ] **Direct Use**: Describe how the model can be used without fine-tuning or plugging into a larger ecosystem/app.
- [ ] **Downstream Use**: List potential fine-tuned applications for a task, or plugging into a larger ecosystem/app.
- [ ] **Out-of-Scope Use**: Indicate any misuse, malicious use, and uses that the model will not work well for.

---

## Bias, Risks, and Limitations

- [ ] **Bias, Risks, and Limitations**: Discuss potential biases and in the model, along with possible mitigations.
- [ ] **Recommendations**: Provide responsible usage recommendations with respect to the bias, risk, and technical limitations.

---

## Getting Started

- [ ] **Usage Instructions**: Provide example code for using the model.
- [ ] **Installation Guide**: List dependencies and installation steps.

---

## Training Details

- [ ] **Training Data**: Describe the dataset used for training. This should link to a Dataset Card where possible, otherwise link to the original source with more info.
- [ ] **Preprocessing**: Detail data preprocessing techniques.
- [ ] **Training Procedure**: Describe the training approach.
- [ ] **Training Hyperparameters**: List key hyperparameters used.
- [ ] **Speeds, Sizes, Times**: Provide information about throughput, start/end time, checkpoint size if relevant, etc.

---

## Evaluation

This section describes the evaluation protocols and provides the results.

- [ ] **Testing Data**: Describe the dataset used for testing. This should link to a Dataset Card if possible, otherwise link to the original source with more info.
- [ ] **Factors**: Describe evaluation criteria (e.g., subpopulations, domains).
- [ ] **Metrics**: Specify evaluation metrics and reasoning.
- [ ] **Results**: Summarize model performance on testing data
- [ ] **Benchmark Comparisons**: Compare with existing baselines.

---

## Model Examination

- [ ] **Interpretability**: Provide information on model explainability.
- [ ] **Visualization**: Include any relevant visualizations.

---

## Environmental Impact

- [ ] **Compute Region**: Specify cloud provider and region.
- [ ] **Hardware Type**: List GPUs and CPUs used.
- [ ] **Training Hours**: Estimate the total training time.
- [ ] **Carbon Emissions**: Calculate emissions using the [ML Impact calculator](https://mlco2.github.io/impact#compute).

---

## Technical Specifications

- [ ] **Model Architecture**: Provide a detailed architecture description and the choices behind its selection.
- [ ] **Performance Metrics**: List performance metrics and their significance.
- [ ] **Model Size**: Specify the model size in MB.
- [ ] **Compute Requirements**: List hardware and software requirements.

---

## Licensing and Citation

See discussion and references in the [template](HF_ModelCard_Template_mkdocs.md/#__codelineno-0-19), also remember the [digital product release and licensing policy](Digital-products-release-licensing-policy.md/).

- [ ] **License**: Confirm licensing details.
- [ ] **Citation**: Provide a BibTeX citation for the model and associated paper.

---

## Acknowledgements

- [ ] **Funding and Support**: List sources of funding and institutional support.

---

## Glossary (Optional)

- [ ] **Definitions**: Provide explanations for technical terms.

---

## Additional Information

- [ ] **Notes**: Include any other relevant details.
- [ ] **Model Card Authors**: List contributors to the model card.
- [ ] **Model Card Contact**: [OPTIONAL] We recommend people use HF discussions, but you may indicate a person to contact.

!!! question "[Questions, Comments, or Concerns?](https://github.com/Imageomics/Collaborative-distributed-science-guide/issues)"
