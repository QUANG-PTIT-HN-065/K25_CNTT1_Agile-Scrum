import subprocess
import sys

BRANCH = "Session09"
COMMIT_MESSAGE = BRANCH


def run(command):
    print(f"> {command}")

    result = subprocess.run(
        command,
        shell=True,
        text=True,
        capture_output=True
    )

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        sys.exit(result.returncode)


def main():
    run("git rev-parse --show-toplevel")

    result = subprocess.run(
        f"git branch --list {BRANCH}",
        shell=True,
        text=True,
        capture_output=True
    )

    if result.stdout.strip():
        run(f"git checkout {BRANCH}")
    else:
        run(f"git checkout -b {BRANCH}")

    run("git add .")

    result = subprocess.run(
        f'git commit -m "{COMMIT_MESSAGE}"',
        shell=True,
        text=True,
        capture_output=True
    )

    print(result.stdout)
    print(result.stderr)

    if result.returncode != 0:
        if "nothing to commit" in result.stdout.lower():
            print("Không có thay đổi để commit.")
            return

        sys.exit(result.returncode)

    run(f"git push -u origin {BRANCH}")

    print("Push thành công.")


if __name__ == "__main__":
    main()