# Reddit Comment Upvote Predictor

Reddit is a social news aggregation, web content rating, and discussion website. People registered on the website can submit content in links, text post, images, and as comments to other posts.

Similar to Facebook’s likes and Twitter’s  favorites, Reddit has an upvote system where users are allowed to vote up or down on others’ posts and comments.

Our objective is to design a model that predicts the number of upvotes a comment might receive.

# Running:

## Step 1: Clone from Github:

> git clone git@github.com:uabinf/nlp-fall-2019-project-reddit_upvote-predictor.git

## Step 2: Environment Setup:

> Run setup.sh to setup Virtual environment and required dependencies.

### 2.1 Cheaha Setup:

module load cuda92/toolkit/9.2.88
module load cuda10.0/toolkit
module load CUDA/9.2.88-GCC-7.3.0-2.30
module load Anaconda3/5.3.1

> Run Jupyter on nlp_env kernel.

## Step 3: Setup Praw.ini

Create a developer app on reddit, get the client_id, client_secret and replace them in praw.ini file. Also replace username and password fields with respective credentials.

## Step 4: Running

Run script.py (or Datafetch.ipynb) to fetch comments from reddit. Run Dataprocess multiclass notebook for Simpletransformers model and Dataprocess onehot notebook for FastAI model.

## Files:

**Datafetch.ipynb** contains script for fetching data from reddit.
**praw.ini** contains reddit setup details.
**Dataprocess folder** contains Jupyter notebooks used for data cleaning and organizing.
**SimpleTransformersModel.ipynb** contains simpletransformers model.
**fastmodel.ipynb** contains FastAI based model.



