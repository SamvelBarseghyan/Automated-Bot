# Automated Bot

## Table of contents:
1. [Description](#description)
2. [Config File Structure](#config-file-structure)
3. [How To Setup](#how-to-setup)
4. [How To Run](#how-to-run)
    
    * [With existing `config.ini` file](#1-with-existing-configini-file)
    * [With another config file](#2-with-another-config-file) 

## Description

Automated Bot is a script that parses configuration file and creates users, posts and etc. according to the parsed config file.

## Config File Structure

Configuration file: `config.ini` should contains `[bot_config]` and `[content_config]` sections.

`[content_config]` should contains the following fields:

* number_of_users - Number of users that bot should create in given api.
* max_posts_per_user - Max number of posts that bot should create for user (simulate creation of posts by user).
* max_likes_per_user - Max number of likes that bot can give to the posts of other users.

`[bot_config]` should contains the following fields:

* base_uri - URI of the API which will be used to create users/posts/likes and etc.
* users_path - Path/Endpoint of the API that will be called to create users.
* posts_path - Path/Endpoint of the API that will be called to create/like posts.
* workers_count - Number of workers that will be created to make parallel queries to the API. If value is bigger than 10 it will be automaticaly set to 10.

Example:
```
[content_config]
number_of_users=12
max_posts_per_user=3
max_likes_per_user=2

[bot_config]
base_uri=https://my_api.com
users_path=users/some_other_path
posts_path=posts
```
## How to setup

To setup bot you need to clone project from [repository]():


```shell
$ git clone 
```

After downloading the project you should create configuration file with sedctions:
`[bot_config]`, `[content_config]`.
Information about both sections you can find in [Config File Structure](#config-file-structure) section.

## How to run

There are several ways to run script:

### 1. With existing `config.ini` file

If you have configuration file with default name:  `config.ini` in your script directory then to run the script you need to run command:
```shell
$ ./automated_bot.py
```

### 2. With another config file

If you have config file with not default name you should pass the config file path to script using `-f` or `--config-file` argument. So to run the script you need to run this command:
```shell
$ ./automated_bot.py -f CONFIG_FILE_PATH
```