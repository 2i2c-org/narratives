import json
import shutil
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NARRATIVE_DIR = ROOT / "docs" / "narrative"
LIST_FILE = ROOT / "docs" / "_narratives_list.md"
FOOTER_FILE = ROOT / "docs" / "_site" / "footer.md"


def main():
    # Download the issues in the narratives repo, sorted by issue number
    REPO = "2i2c-org/narratives"
    out = subprocess.check_output(
        ["gh", "issue", "list", "--repo", REPO, "--state", "open",
         "--limit", "200", "--json", "number,title,body,url",
         "--jq", "sort_by(.number)"],
        text=True,
    )
    issues = json.loads(out)

    # Clear out the old narrative dir if it exists
    shutil.rmtree(NARRATIVE_DIR, ignore_errors=True)
    NARRATIVE_DIR.mkdir(parents=True)

    # Generate the list of narratives to link in our index.md
    lines = ["**List of Narratives**\n"]
    for issue in issues:
        number = issue["number"]
        title = issue["title"]
        url = issue["url"]
        body = issue["body"]
        (NARRATIVE_DIR / f"{number}.md").write_text(
            f"# {title}\n\n*[View on GitHub »]({url})*\n\n{body}\n"
        )
        lines.append(f"- [{title}](narrative/{number}.md)")
    LIST_FILE.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(issues)} narratives")

    # Download the footer from the roadmap repo so we re-use its config
    FOOTER_URL = "https://github.com/2i2c-org/roadmap/raw/refs/heads/main/docs/_site/footer.md"
    FOOTER_FILE.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(FOOTER_URL, FOOTER_FILE)


if __name__ == "__main__":
    main()
