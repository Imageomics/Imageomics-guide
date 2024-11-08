# Hugging Face Dataset Guide

## Create a New Dataset Repository
When creating a new dataset repository, you can make the dataset **Public** (accessible to anyone on the internet) or **Private** (accessible only to members of the organization).

![New dataset repository interface](images/HF-dataset-upload/346972860-ed0feb0e-529b-4021-b44f-41ac96680bc3.png){ loading=lazy, width=800 }
/// caption
///

## Upload a Dataset with the Web Interface
In the Files and versions tab of the Dataset card, you can choose to add file in the hugging web interface.

![Dataset repository Add file button](images/HF-dataset-upload/346190430-9e6cef9b-18ef-4d4a-84c5-1a3f75ac9336.png){ loading=lazy }

## Upload a Dataset with HfApi
``` py linenums="1"
from huggingface_hub import login

# Login with your personal token (find your tokens at: Settings/Access Tokens)
login()

from huggingface_hub import HfApi
api = HfApi()

api.upload_file (
    path_or_fileobj = <the local file path that you would like to upload>,
    path_in_repo = <the path in the repo>,
    repo_id = <ABC-climate/dataset name>,
    repo_type = 'dataset'
)
```

## Upload a Dataset with Git
### If the Dataset is Less Than 5GB
Navigate to the folder for the repository:
```
# Clone the repository
git clone https://huggingface.co/datasets/username/repo-name

# Add, commit, and push the files
git add
git commit -m 'comments'
git push

```
### If the Dataset is Larger Than 5GB
#### Install Git LFS
Follow instructions at https://git-lfs.com/

#### Install the Hugging Face CLI
```
brew install huggingface-cli
pip install -U "huggingface_hub[cli]"
```

#### Enable the repository to upload large files
```
huggingface-cli lfs-enable-largefiles <your local dataset>
```

#### Initialize Git LFS
```
git lfs install
```

#### Track large files (e.g., .csv files)
```
# Adds a line to .gitattributes, which Git uses to determine files managed by LFS
git lfs track "*.csv"  
git add .gitattributes
git commit -m "Track large files with Git LFS"
```

#### Add, commit, and push the files
```
git add 
git commit -m 'comments'
git push
```
