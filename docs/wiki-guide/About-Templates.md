# Using Dataset and Model Card Templates

We provide Dataset and Model Card templates for both Imageomics and ABC, adapted from Hugging Face's templates. The Imageomics and ABC templates include guidance and examples for the various metadata sections, reference information for Hugging Face's particular flavor of markdown, and the appropriate NSF & NSERC grant acknowledgment.

To use a template for a new dataset or model repository on Hugging Face (HF), simply copy and paste the contents of the appropriate template ([Dataset Card](HF_DatasetCard_Template_mkdocs.md) or [Model Card](HF_ModelCard_Template_mkdocs.md)) into your `README.md` file.[^1] 
Then, follow the descriptions under each section to fill in the appropriate information. This is meant to be an iterative process throughout the life of your project, so do not worry if you cannot answer all parts at the beginning&mdash;that's to be expected!
[^1]: The templates can also be added to your repository thorugh the website user interface (UI): Navigate to the "Model/Dataset Card" tab on your repo, select "Create Model/Dataset Card", copy and paste the template contents into the `README.md` file, and add your content.


!!! tip "Practice makes perfect!"
    If you have never filled out a dataset card before, or are unsure of how to find the answers to fill in the sections, we ran a [workshop](https://github.com/Imageomics/data-workshop-AH-2024) to help familiarize our members with this process. In particular, the portion where we walked through filling out part of a dataset card as we did exploratory data analysis (EDA) was recorded and is available on the [Imageomics YouTube Channel](https://www.youtube.com/@ImageomicsInstitute/videos). Read the [story of the workshop](https://github.com/Imageomics/data-workshop-AH-2024/#story-of-the-workshop) and clone the [repo](https://github.com/Imageomics/data-workshop-AH-2024) to follow along with the 1 hour and 15 minute lesson!

!!! note "Note"
    The Dataset and Model cards have incorporated some of Hugging Face's January 2024 updates (following their [Dataset Card Overhaul](https://github.com/huggingface/huggingface_hub/commit/6dd7ee829bd1b1216663a9993c1943c29b64690a)). It doesn't appear they will be updated more and we do not currently anticipate further large updates on our end as our overall template formats have diverged. Nevertheless, you may wish to check HF for extra information or tagging updates ([HF Dataset Card](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/datasetcard_template.md), [HF Model Card](https://github.com/huggingface/huggingface_hub/blob/main/src/huggingface_hub/templates/modelcard_template.md)).

