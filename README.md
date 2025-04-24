# Git Contribution Bot

Git Contribution Bot is a Python-based tool that generates custom GitHub contribution heatmaps by creating commits with specific dates and patterns. It allows you to "draw" text or art on your GitHub profile's contribution graph.

## Features

- Generate GitHub contribution heatmaps with custom text or patterns.
- Fetch existing GitHub contributions to avoid overwriting them.
- Automatically adjust contribution levels based on your existing contributions.
- Control the density of contributions using noise parameters.
- Automatically create and manage a `gh-pages` branch for commits.
- Push commits to a remote repository to update the contribution graph.
- Fully customizable with interactive input.

## How It Works

1. **Input Text**: You provide the text or pattern to be drawn on the GitHub contribution graph.
2. **Fetch Contributions**: The tool fetches your existing GitHub contributions to ensure no overwriting and adjusts contribution levels accordingly.
3. **Noise and Art Generation**: The tool generates noise and combines it with the art (text) to create a final contribution pattern.
4. **Commits Creation**: Commits are created for the missing contributions in the heatmap, with timestamps and messages.
5. **Push to GitHub**: The commits are pushed to the `gh-pages` branch of your repository, updating your GitHub contribution graph.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LucianoBWille/gitContributionBot.git
   cd gitContributionBot
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have Git installed and configured on your system.

## Usage

Run the script and follow the prompts:

```bash
python GitBot.py
```

### Input Parameters

| Parameter           | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `Text`             | The text to draw on the GitHub contribution graph.                          |
| `Text Stroke`      | The intensity of the text stroke (default: 1).                              |
| `Noise Bottom`     | The minimum noise value for contributions (default: 1).                     |
| `Noise Top`        | The maximum noise value for contributions (default: 2).                     |
| `GitHub Username`  | Your GitHub username to fetch existing contributions.                       |

### Example

```bash
python GitBot.py
```

When prompted, enter:
- Text: `HELLO`
- Text Stroke: `2`
- Noise Bottom: `1`
- Noise Top: `2`
- GitHub Username: `your-username`

This will generate a heatmap with the word "HELLO" drawn on it, ensuring no existing contributions are overwritten. The contribution levels will be adjusted based on your current GitHub activity.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Start customizing your GitHub contributions with **Git Contribution Bot** today!