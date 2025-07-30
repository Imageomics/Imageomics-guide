# Contributing to the Collaborative Distributed Science Guide

Thank you for your interest in contributing to the Collaborative Distributed Science Guide! This document outlines the standards and guidelines for contributing to this template repository.

## Overview

The Collaborative Distributed Science Guide is built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) and deployed via GitHub Pages. All documentation is written in Markdown and follows specific formatting standards to ensure consistent rendering and maintainability.

This is a template repository designed to be forked and customized by different organizations for their collaborative science documentation needs.

## Getting Started

### Local Development Setup

1. Clone the repository
2. Set up a virtual environment (recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

   For more detailed environment setup options (including conda), see our [Virtual Environments guide](docs/wiki-guide/Virtual-Environments.md).

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Serve the site locally:

   ```bash
   mkdocs serve
   ```

5. View the site at <http://127.0.0.1:8000/Collaborative-distributed-science-guide/>

### Testing Changes

Always test your changes locally with `mkdocs serve` before submitting a PR to ensure:

- Content renders correctly
- Links work properly
- Formatting appears as intended
- No build errors occur

## Documentation Standards

### Markdown Formatting

#### Indentation for Nested Lists

- **Use 4 spaces for nested list items** (not 2 spaces)
- This requirement exists due to Python-Markdown compatibility issues with MkDocs
- 2-space indentation causes nested lists to not render properly in the final HTML

**Correct:**

```markdown
- [ ] Main item
    - [ ] Nested item
    - [ ] Another nested item
```

**Incorrect:**

```markdown
- [ ] Main item
  - [ ] Nested item (will not render as nested)
```

#### General Formatting

- Remove trailing whitespace
- Use consistent line breaks
- Follow the project's `.markdownlint.json` configuration
- Ensure proper heading hierarchy (don't skip heading levels)

### License Format Requirements

#### Hugging Face YAML Frontmatter

When specifying licenses in Hugging Face dataset/model card YAML sections, **always use lowercase**:

**Correct:**

```yaml
license: cc0-1.0
```

**Incorrect:**

```yaml
license: CC0-1.0  # Will cause issues with Hugging Face platform
```

This is a platform-specific requirement for Hugging Face compatibility.

#### License References in Text

In prose text, you may use standard capitalization (e.g., "CC0", "MIT"), but YAML frontmatter must be lowercase.

### File Organization

- Documentation content goes in `docs/`
- Wiki-style guides go in `docs/wiki-guide/`
- Images and assets are organized in subdirectories within `docs/`
- Templates use descriptive filenames with consistent naming patterns

### Custom Macros

The project includes custom MkDocs macros defined in `main.py`:

- `include_file_as_code()` - Embeds file content as code blocks
- When using macros, ensure proper syntax and test rendering locally

## Contribution Process

1. **Create an issue** describing the change (for significant additions)
2. **Create a feature branch** from `dev`
3. **Make your changes** following the standards above
4. **Test locally** with `mkdocs serve`
5. **Run linting** to ensure formatting consistency
6. **Submit a pull request** with:
   - Clear description of changes
   - Reference to related issue
   - Screenshots if UI changes are involved

### Pull Request Guidelines

- Keep PRs focused on a single topic when possible
- Follow commit message conventions (see below)
- Update navigation in `mkdocs.yaml` if adding new pages
- Ensure all links work correctly
- Test that the site builds without errors

### Commit Message Guidelines

The most important aspects of good commit messages are that they should be **descriptive** and **atomic** (each commit should represent a single logical change). Additionally:

- **Keep the first line short**: Limit the subject line to 50 characters or less
- **Use the imperative mood**: "Add feature" not "Added feature" or "Adds feature"
- **Separate subject from body**: Use a blank line between the subject line and detailed description

#### Conventional Commits Recommendation

We recommend following the [Conventional Commits](https://www.conventionalcommits.org/) format for commit messages:

**Format:** `type(scope): description`

**Common types:**

- `feat`: New feature or content addition
- `fix`: Bug fix or correction
- `docs`: Documentation updates
- `style`: Formatting changes (no content changes)
- `refactor`: Code/content restructuring without changing functionality
- `chore`: Maintenance tasks, tooling updates

**Examples:**

```bash
feat(fair-guide): add data repository checklist
fix(templates): correct license format in HF dataset card
docs(contributing): add conventional commit guidelines
style(checklists): fix markdown formatting and indentation
chore: update mkdocs dependencies
```

**Scope** is optional but helpful for larger changes. Use the guide section or file type being modified.

**Note:** Since we use squash merges, strict adherence to this format isn't required, but descriptive and atomic commits help maintain a clear project history.

## Quality Assurance

### Linting

The project uses [markdownlint](https://github.com/DavidAnson/markdownlint) with configuration in `.markdownlint.json`. Key settings:

- 4-space indentation for lists (`MD007`)
- No hard tab restrictions disabled
- Line length restrictions disabled (`MD013`)

### Content Review

When reviewing content:

- Verify accuracy of technical information
- Check for consistency with existing guides
- Ensure proper cross-referencing between related pages
- Validate that external links are current and working

## Platform-Specific Considerations

### Hugging Face Integration

- Dataset and model card templates must follow HF specifications
- YAML frontmatter formatting is critical for platform compatibility
- License identifiers must match HF's expected format

### MkDocs/Python-Markdown

- Nested list rendering requires specific indentation
- Some Markdown extensions may behave differently than GitHub Flavored Markdown
- Always test complex formatting locally

## Getting Help

- Open an [issue](https://github.com/Imageomics/Collaborative-distributed-science-guide/issues) for questions or problems
- Reference existing guides and templates for examples
- Check the [MkDocs Material documentation](https://squidfunk.github.io/mkdocs-material/) for advanced features

## Code of Conduct

All contributors must adhere to our [Code of Conduct](docs/CODE_OF_CONDUCT.md) and organizational principles of engagement.

---

Thank you for helping improve the Collaborative Distributed Science Guide! Your contributions help make collaborative scientific computing more accessible and effective.
