# README for a VM set up for a new user 

This README explains to a new user how to set up a new VM. After following these steps below, you will have a VM configured with necessary packages installed and your GitHub repository cloned and ready to use. 

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

