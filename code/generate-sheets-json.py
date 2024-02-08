import json
import csv
import pathlib
import subprocess

repo_root = pathlib.Path(__file__).parents[1]
print(repo_root)

paths = sorted(repo_root.rglob("video_url.txt"))

list_of_lines = [['Video','Contributors']]
for path in paths:
    if path.is_file():
        folder = path.parent
        relative_folder = folder.relative_to(repo_root)
        proc = subprocess.run(["git", "-P",
                        "shortlog", "--summary", "--numbered", "HEAD", "--", folder],
                       capture_output=True, check=True, shell=False)
        text = proc.stdout.decode("utf-8")
        print(relative_folder.as_posix())
        csv_line = [relative_folder.as_posix()]
        for line in text.split('\n'):
            fields = line.split('\t')
            if len(fields) >= 2:
                csv_line.append(fields[1])
        list_of_lines.append(csv_line)

json_text = json.dumps({
            'contributors_per_video': list_of_lines
        })

(repo_root / "sheets.json").write_text(json_text)
