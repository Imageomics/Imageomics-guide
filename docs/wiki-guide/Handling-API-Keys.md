# Handling API Keys

If you are using a web service with API keys, there are a few things to keep in mind. The key to key storage is that the process must meet the following requirements:

- Not hard-coded into your code
- Not visible in version-control
- Convenient to use
- Convenient to change if needed
- Unique for different environments

!!! danger "Protect your API Keys and Access Tokens!"
    The most important lesson in key-management is to ***never make them public*** and ***always scope access***. If you think a key has been exposed, ***disable*** and ***regenerate*** it immediately. By keeping access keys and tokens scoped to a single task or repository with the least permissions necessary to complete the needed function, you further reduce the potential impact of a leaked key.

Both GitHub and Hugging Face recommend using *fine-grained* tokens, and provide guidance on creating and managing them within the platforms. Learn more about platform-specific access tokens on [GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) and [Hugging Face](https://huggingface.co/docs/hub/en/security-tokens). Keep reading below for more general API Key management guidance.

## Key Storage

Our recommended way of storing and using API is within `.env` (dotenv) files.

A `.env` file is a simple text file that stores key-value pairs that set local environment variables. Its contents would look something like the following:

```
RESOURCE_API_KEY=your_api_key
```

For instance, if your API key for OpenAI is `sk-AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz`, you would put the following in your `.env` file.

```
OPENAI_API_KEY=sk-AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz
```

- Ensure `.env` is added to your `.gitignore` file. The `.env` should not be published in a remote repository; it should be for your eyes only.
- Store the `.env` file in the root directory for your project.
- Backup the `.env` or key in a secure location. A free personal account with [Bitwarden](https://bitwarden.com/) is an excellent option for this.
- If you notice the key or the `.env` file has been published somewhere public for any length of time, it must be changed immediately.

!!! note "Note"
    The `.env` file is a simple text file, so you can use any text editor to create and edit it.

## Key Usage

If you are using Python, the `dotenv` package will enable to use this approach. First, install with [pip](https://pypi.org/project/python-dotenv/) or [conda](https://anaconda.org/conda-forge/python-dotenv). In your work, the following will get you access to your API key as a Python variable `RESOURCE_API_KEY` (you may name it whatever you like; the Python variable may be different from the environment variable):

```python { py linenums="1" }
import os
from dotenv import load_dotenv

load_dotenv("relative/path/to/your/.env")

RESOURCE_API_KEY = os.getenv("RESOURCE_API_KEY")
```

## Keys for a Shared Resource

If you are part of a group with access to the same API:

- Create a unique API key for each application you use and for each environment you work in.
- Avoid sharing API keys with other users or between different applications/scripts.
