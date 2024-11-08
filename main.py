import os

def define_env(env):
    """Define custom macros for MkDocs."""

    @env.macro
    def include_file_as_code(file_path, language="markdown"):
        """
        Include the content of a file within a code block.

        Args:
            file_path (str): The path to the file to include, relative to the project root.
            language (str): The language identifier for syntax highlighting.

        Returns:
            str: A Markdown-formatted code block containing the file's content.
        """
        full_path = os.path.join(env.project_dir, file_path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except FileNotFoundError:
            content = f"**Error:** The file `{file_path}` was not found."

        # Escape triple backticks in content to prevent breaking the code block
        content = content.replace("```", "```\u200b")

        line_nums_string = "{ py linenums='1' }"

        return f"```{language} {line_nums_string}\n{content}\n```"
