# Metadata Guide

When collecting or compiling new data, there are generally questions one is _trying_ to answer. There are also often questions that will come up later--whether for yourself or others interested in using your data. 

To improve both the _**Findability**_ and _**Reusability**_ of your data (ensuring [FAIR principles](Glossary-for-Imageomics.md#fair-data-principles)) for yourself and others, be sure to note down the following information.

!!! note "This is not an exhaustive list."
    Be sure to include any other information that may be important to your particular project or field.

## Checklist for Metadata to Record
- [ ] **Description:** Summary of your data, for instance:
    - What are the contents of the data (images, text, type of animal)? 
    - Is it machine-ready? 
    - Where did it come from (Source)? 
- [ ] **Data Sources:** Machine-readable sources of the data (links or other files).
- [ ] **License Information:** This is part of retaining records of a data source (eg., museum images, previous dataset). A record of licenses on the images must be retained to ensure they are respected. If dealing with CC licenses, please see this [OSU Library CC best practices guide](https://library.osu.edu/sites/default/files/2022-10/attributing_cc_license_flyer_2022_ac.pdf).
- [ ] **Dataset Structure:**
    - Organization of the full dataset (eg., file structure).
    - Feature information: Information available for each image, such as species and subspecies designations, location information, etc.
    - Instance information: Image type (jpg, tiff, png), number of pixels per image, coloring (RGB, UV), presence of scale or color indicators (ruler or ColorChecker), etc.
- [ ] **Processing Steps:** List modifications performed (as they're done) and include links to the code used (this _should_ be organized somewhere, like a GitHub repository).
    - Similarly, include any annotation process information.
- [ ] **Tasks:** What could this dataset be used for (eg., image classification, feature extraction, image segmentation, etc.).
- [ ] **Curation Rationale:** Why are you collecting and/or modifying this data?
   - This ties into the question of tasks it could be applied to, both to help maintain the group focus, and increase the likelihood others interested in answering similar questions will be able to find and use your data.
- [ ] **Author:** The curator(s)/editor(s) of the data. Assumes sufficient modification of the data by you (and your team) or that you have collected it. 
    - If thinking about publishing the data, add ORCID to all Authors; these can be looked up on [orcid.org](https://orcid.org/). 
- [ ] **Related Publication:** Any papers that are based on this dataset. 
- [ ] **Related Datasets:** Provide links to any related datasets (may include previous/background research).
- [ ] **Other References:** Links to any related/background articles.
- [ ] **Keywords/Tags:** Terms one might search to find this dataset, eg., type(s) of animals, type(s) of images, imbalanced (if not even distribution of species/subspecies/etc).
    - It helps to keep a running list.
- [ ] **Notes:** Any other image/data information.

!!! warning "Remember" 

    Datasets **_cannot_** be redistributed without this information. 

!!! tip "Pro tip" 

    Use the eye icon at the top of this page to access the source and copy the markdown for the checklist above into an issue on your GitHub [Repo](GitHub-Repo-Guide.md) or [Project](Guide-to-GitHub-Projects.md) so you can check the boxes as you add each.

!!! question "[Questions, Comments, or Concerns?](https://github.com/Imageomics/Imageomics-guide/issues)"
