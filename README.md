# databricks-debug
tmp repo for debugging Databricks features


# Setup

## Install CLI tools for Databricks
```console
pip install dev-requirements.txt
```

## Configure connection to Databricks
```console
databricks configure --token
```

## Setup project with DBX

```console
dbx init --template="python_basic" \
-p "project_name=cicd-sample-project" \
-p "cloud=AWS" \
-p "cicd_tool='GitHub Actions'" \
-p "profile=DEFAULT" \
--no-input
```
