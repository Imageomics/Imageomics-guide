# Digital Products Release and Licensing Policy

To further the goals and motivations of the NSF grant supporting the Imageomics Institute, and to fulfill the requirements from the Data Management Plan (DMP) associated with the grant, all data, model, and code products generated or augmented under the auspices and support of the Institute should adhere to [FAIR principles](https://www.go-fair.org/fair-principles/). Datasets that include Indigenous data should also adhere to [CARE principles](https://www.gida-global.org/care).

This means the following policy applies for digital products of the Imageomics Institute:

1. All digital products (code, data, models, documentation, tutorials, etc) are to be released such that they are accessible to the public, at the latest by the time of associated paper publication, under an [Open Content](https://en.wikipedia.org/wiki/Free_content) license or terms of use.

    - Educational materials are outside of the scope of this policy, but are encouraged to follow these guidelines nonetheless.

2. Code is to be released under an [OSI-approved open source license](https://opensource.org/licenses/), or to the public domain (for example, by applying a [CC-Zero](https://creativecommons.org/publicdomain/zero/1.0/) waiver).

    - This should be in a well-documented GitHub repository that follows the format specified in the [Institute GitHub Repo Guide](GitHub-Repo-Guide.md). 

    - If associated with a publication, code should be versioned with a release linked to a DOI that can be referenced in the publication.

3. Data, documents, tutorials, etc are to be released either to the public domain (for example, by applying a [CC-Zero](https://creativecommons.org/publicdomain/zero/1.0/) waiver), or under terms no more restrictive than requiring attribution (such as [CC-BY](https://creativecommons.org/licenses/by/4.0/)).

    - For image and video datasets, this only applies to items that are not already licensed by (and thus used under license from) a third party.

    - For datasets that include Indigenous data, see [Carroll *et al* (2020)](https://doi.org/10.5334/dsj-2020-043) and [Carroll *et al* (2021)](https://doi.org/10.1038/s41597-021-00892-0) for reconciling FAIR and CARE principles for scientific data.

    - Datasets collected in whole or in part from regions that harbor Indigenous researchers are to at least adhere to the Collective Benefit principle (the *C* in CARE), even if they have been expressly released from or are otherwise entirely unencumbered by Indigenous rights. Specifically, at a minimum they are to be made available to respective Indigenous researchers with the least obstacles possible.

    - For ML-ready datasets, for storage, version control, and sharing we recommend using [Hugging Face Dataset Hub](https://huggingface.co/docs/hub/datasets-overview), which provides for rich metadata description in the form of a [Dataset Card](HF_DatasetCard_Template_mkdocs.md). (See [Imageomics datasets](https://huggingface.co/imageomics) published there as examples.)

    - Refer to the Imageomics [Hugging Face](Hugging-Face-Repo-Guide.md) and [Metadata](Metadata-Guide.md) guides for best-practices and further guidance.

4. ML models are to be released under an [OSI-approved open source license](https://opensource.org/licenses/) or to the public domain (for example, by applying a [CC-Zero](https://creativecommons.org/publicdomain/zero/1.0/) waiver). In the case of potentially sensitive models or data (e.g., endangered species information), an Open [Responsible AI License](https://www.licenses.ai/ai-licenses) ([Open RAIL-M](https://www.licenses.ai/blog/2022/8/18/naming-convention-of-responsible-ai-licenses)) may be considered.

    - For further guidance, consider the chapter on [Machine Learning Model Licenses](https://the-turing-way.netlify.app/reproducible-research/licensing/licensing-ml.html) from The Turing Way.

    - For storage, version control, sharing, and publishing (including DOI provision), we recommend using [Hugging Face Model Hub](https://huggingface.co/docs/hub/models), which provides for rich metadata description in the form of a [Model Card](HF_ModelCard_Template_mkdocs.md). (See [Imageomics models](https://huggingface.co/imageomics) published there as examples.)

    - Refer to the [Imageomics Hugging Face Guide](Hugging-Face-Repo-Guide.md) for best-practices and further guidance.

5. All code, data, and models published on the Imageomics Organization ([GitHub](https://github.com/Imageomics) or [Hugging Face](https://huggingface.co/imageomics)) must be reviewed and approved by the Senior Data Scientist or Institute leadership prior to [DOI generation](DOI-Generation.md).

    - Further guidance and resources to best adhere to Institute standards can be found in the [Imageomics Guide](../index.md).
