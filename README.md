# Collaborative Distributed Science Guide

Welcome to the Collaborative Distributed Science Guide!

Just joining or starting a new project?
Check out the [Collaborative Distributed Science Guide](https://imageomics.github.io/Collaborative-distributed-science-guide/) for guidance on conventions and best practices.

## About the Guide

This guide started as an Imageomics Institute-internal wiki, focused on providing guidance and best practices for collaborative and interdisciplinary (computer science + biology) work. Recognizing that the topics and suggestions are broadly applicable to anyone working in similar or adjacent fields, we moved the vast majority to this [guide](https://imageomics.github.io/Collaborative-distributed-science-guide/). To increase accessibility for those less familiar with GitHub, we generated the website from our Markdown documents (which used to be wiki pages) with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Please feel free to open an [issue](https://github.com/Imageomics/Collaborative-distributed-science-guide/issues) with any questions regarding the content of this guide.

### How to Use the Guide

This Guide is set up as a template repository such that there are two primary means of interacting with it:

1. Building a personalized version of the Guide: select "Use this Template" at the top of the repo to generate your own version. This will create a new repository (generated from the template repo) that does _not_ share the commit history of the template. Updates could still be added from the template upstream through [`git cherry-pick`](https://git-scm.com/docs/git-cherry-pick). More details are provided below, in [Personalizing the Guide](#personalizing-the-guide).
2. Contributing to the Guide: fork this repo, make changes, and submit a pull request (PR) for review. Some guidance is provided in the [Pull Request Guide](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/The-GitHub-Pull-Request-Guide/); please provide a detailed description of your changes and review the contributing guidelines (coming soon).

### Personalizing the Guide

Welcome to your new guide repo! The first step in updating your new guide is to give it a name; ideally this should match the name you give to the repo when using the template. You will need to update the name and hardcoded repo links across various files.

Primary pages to personalize are:

- [`mkdocs.yaml`](mkdocs.yaml) has comments indicating locations to personalize (e.g., updating name, logos, socials). All pages use relative links within the repository, so those connections only need to be updated if adding or removing pages.
- [`index.md`](docs/index.md): this is the homepage for the site and should reflect your organization or group's priorities.
- [`CITATION.cff`](CITATION.cff): please set the Collaborative Distributed Science Guide citation as a reference in your citation file after making your own modifications (see [template](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/GitHub-Repo-Guide/#citation) for guidance on formatting).
- [`Digital-products-release-licensing-policy.md`](docs/wiki-guide/Digital-products-release-licensing-policy.md): at a minimum, links should be redirected to your GitHub and Hugging Face organization pages.
    - Other locations in pages such as the [`GitHub-Repo-Guide`](docs/wiki-guide/GitHub-Repo-Guide.md) and [`Hugging-Face-Repo-Guide.md`](docs/wiki-guide/Hugging-Face-Repo-Guide.md) also have links to our organization pages. A search and replace for "Imageomics" can be done to update these.
- [`Technical-Infrastructure.md`](docs/wiki-guide/Technical-Infrastructure.md): this page is Imageomics-specific and includes internal-only links.
- [Glossary for Imageomics](docs/wiki-guide/Glossary-for-Imageomics.md): this page should be updated to a topic relevant to your field or focus.
- Templates should be updated for your organization (mainly the `Acknowledgements` sections, pre-filled URL suggestions, domain-specific suggestions and guidance).

## Contributing

If you'd like to contribute to this guide, please read our [Contributing Guidelines](CONTRIBUTING.md) for information about our standards, development workflow, and submission process.

### Testing

To test this site locally, first clone this repository, then create an environment with `requirements.txt`

```
pip install -r requirements.txt
```

and run `mkdocs serve`:

```
mkdocs serve
```

Then the site will run at <http://127.0.0.1:8000/Collaborative-distributed-science-guide/>.

### History

This guide was developed alongside the [Imageomics Guide](https://imageomics.github.io/Imageomics-guide/), which houses the information needed to get started with and use institute resources readily available to all members. However, most of its content is applicable to anyone working more broadly in the field of [_imageomics_](https://imageomics.github.io/Collaborative-distributed-science-guide/wiki-guide/Glossary-for-Imageomics.md/#imageomics) or adjacent fields of computer and data science, and it is tailored to help domain scientists bridging that gap. _This guide_ is intended to serve as a template for others wishing to develop a similar organization-specific guide, and this solution was born out of the desire to do so for the [AI and Biodiversity Change (ABC) Global Center](http://abcresearchcenter.org) while limiting duplicative updates between guides (Imageomics and ABC share some team members on this project). The general structure of the website should be broadly applicable, but see [Personalizing the Guide](#personalizing-the-guide) for suggestions on tailoring it for the particular organization or group's needs.

## Acknowledgments

This work was supported by both the [Imageomics Institute](https://imageomics.org) and the [AI and Biodiversity Change (ABC) Global Center](http://abcresearchcenter.org). The Imageomics Institute is funded by the US National Science Foundation's Harnessing the Data Revolution (HDR) program under [Award #2118240](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2118240) (Imageomics: A New Frontier of Biological Information Powered by Knowledge-Guided Machine Learning). The ABC Global Climate Center is funded by the US National Science Foundation under [Award No. 2330423](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2330423&HistoricalAwards=false) and Natural Sciences and Engineering Research Council of Canada under [Award No. 585136](https://www.nserc-crsng.gc.ca/ase-oro/Details-Detailles_eng.asp?id=782440). This guide draws on research supported by the Social Sciences and Humanities Research Council. Any opinions, findings and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation, Natural Sciences and Engineering Research Council of Canada, or Social Sciences and Humanities Research Council.
