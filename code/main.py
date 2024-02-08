import json
import csv
import pathlib
import subprocess

repo_root = pathlib.Path(__file__).parents[1]

paths = repo_root.rglob("video_url.txt")

list_of_csv_lines = []
for path in paths:
    if path.is_file():
        folder = path.parent
        relative_folder = folder.relative_to(repo_root)
        proc = subprocess.run(["git",
                        "shortlog", "--summary", "--numbered", "--", folder],
                       capture_output=True, check=True, shell=False)
        text = proc.stdout.decode("utf-8")
        print(str(relative_folder))
        csv_line = [str(relative_folder)]
        for line in text.split('\n'):
            fields = line.split('\t')
            if len(fields) >= 2:
                csv_line.append(fields[1])
        list_of_csv_lines.append(csv_line)

with open(repo_root / 'out.txt', 'w', newline='') as f:
    writer = csv.writer(f)
    for line in list_of_csv_lines:
        writer.writerow(line)
