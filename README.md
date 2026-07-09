

# README for a VM set up for a new user 

This README explains to a new user how to set up a new VM. After following these steps below, you will have a VM configured with necessary packages installed and your GitHub repository cloned and ready to use. 

## Project Objective 
This project runs a GitHub Actions CI (continuous integration) pipeline through the scripts in the `DS5111` repository. The pipeline ingests data via Standard Input (sys.stdin), processes it using `clean_ids.py`, `enrich_transcripts.py` and `extract_trasncripts`, and pipe results out via Standard Output (sys.stdout). On every push or pull request to `main` branch, GitHub Actions verifies that this code passes linting and the full test suite across Python 3.11, 3.12, and 3.13 before the work is considered mergeable.

## Environment Configuration Variables

| Variable | Description | Example / Format | Required |
|----------|-------------|------------------|----------|
| `GITHUB_USERNAME` | GitHub account username and password | `GitHub_ID and password` | Yes |
| `GEMINI_API_KEY` | API key for authenticating with the Google Gemini API | `...` | Yes |
| `PROXY` | Webshare's residential proxy cluster | `` | Yes |
| `SNOWFLAKE_ID` | Your complete University of Virginia ID in all CAPS | `UVA_ID` | Yes |
| `SNOWFLAKE_PASSWORD` | Use the temporary administrative one-time credential code | `DS5111_UPPER CASE UVA ID_2026!` | Yes |
| `SNOWFLAKE_ROLE` | Snowflake role used for the session | `DS5111` | Yes |
| `SNOWFLAKE_DATABASE` | Target Snowflake database name | `UVA student ID` | Yes |

## Prerequisites

- VM (use the Ubuntu Server 26.04 select as it is the latest version)
- GitHub SSH key that is newly created in your GitHub account (go to Settings > SSH and GPG keys > click 'new SSH key')
- GitHub username and email address

## Steps

### 1. Run the general init file

From your home directory, run:

```bash
bash init.sh
```

When you run this bash line, it will install the packages (make, python3.14, and tree) in the VM. 

**Quick Test**

```bash
tree
```

When you execute tree, you will see the file names, if all went well. This is a quick test to verify before moving to the step 2. 

### 2. Configure your GitHub credentials

Run:

```bash
bash init_git_creds.sh
```

This will set your GitHub email and user name so your commits will be tagged correctly. Same as the step 1, this script was set up to be executed for you, and now Git will know 'who' is checking in commits and pushing. 

**Quick Test**

```bash
git config --global --list
```

You should see your email and username echoed, if all went well. 

### 3. Clone your repository to the VM

```bash
git clone git@github.com:<your-github-username>/DS5111.git
```

Replace `<your-github-username>` with your GitHub user name. With this set up, you will now start working on the machine itself, save your work and push to GitHub. 

**Quick Test**

```bash
cd DS5111
ls
```

You should see two files, `makefile` and `requirements.txt` in the DS5111 repository.

### 4. Create a virtual environment for Python

From the root of the cloned repository, run:

```bash
make update
```

Note that you are not running make env. This is because env was set up as a dependency on update already. `make update` will automatically create the virtual environment first if it doesn't exist, then install packages.

If the env directory does not exist, it will run first. Then, tt will use the `requirements.txt` file and load the packages (pandas and numpy).

**Quick Test**

```bash
. env/bin/activate
pip list
```

The first line will show `(env)` on the left of the prompt, which means the new environment is activated. 

The second line will show `pandas` and `numpy` as they are successfully installed.

