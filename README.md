# Git Contribution Bot

Git Contribution Bot is a Python-based tool that generates custom GitHub contribution heatmaps by creating commits with specific dates and patterns. It allows you to "draw" text or art on your GitHub profile's contribution graph.

## Features

- Generate GitHub contribution heatmaps with custom text or patterns.
- Control the density of contributions using noise parameters.
- Automatically create and manage a `gh-pages` branch for commits.
- Push commits to a remote repository to update the contribution graph.
- Fully customizable with command-line arguments.

## How It Works

1. **Input Text**: You provide the text or pattern to be drawn on the GitHub contribution graph.
2. **Noise and Art Generation**: The tool generates noise and combines it with the art (text) to create a final contribution pattern.
3. **Commits Creation**: Commits are created for each day in the heatmap, with timestamps and messages.
4. **Push to GitHub**: The commits are pushed to the `gh-pages` branch of your repository, updating your GitHub contribution graph.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LucianoBWille/gitContributionBot.git
   cd gitContributionBot
   ```

<!-- 2. Install the required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Git installed and configured on your system. -->

## Usage

Run the script with the following command-line arguments:

```bash
python GitBot.py --text "YourText" --textStroke 4 --noiseBottom 1 --noiseTop 2
```

### Command-Line Arguments

| Argument          | Alias | Description                                                                 |
|--------------------|-------|-----------------------------------------------------------------------------|
| `--text`          | `-t`  | The text to draw on the GitHub contribution graph.                          |
| `--textStroke`    | `-ts` | The intensity of the text stroke (default: 4).                              |
| `--noiseBottom`   | `-nb` | The minimum noise value for contributions (default: 1).                     |
| `--noiseTop`      | `-nt` | The maximum noise value for contributions (default: 2).                     |

### Example

```bash
python GitBot.py --text "HELLO" --textStroke 3 --noiseBottom 0 --noiseTop 2
```

This will generate a heatmap with the word "HELLO" drawn on it. The number of commits for each day will be:
- level 0: no commits (noise)
- level 1: 3 commits (noise)
- level 2: 6 commits (noise)
- level 3: no commits
- level 4: 12 commits (the text itself)

<!-- ## How to Customize

## Project Structure -->

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

<!-- ## Acknowledgments -->

---

Start customizing your GitHub contributions with **Git Contribution Bot** today!