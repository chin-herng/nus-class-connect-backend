# nus-class-connect-backend

## Description
This repository is the backend for nus-class-connect.

## Table of Contents
- [nus-class-connect-backend](#nus-class-connect-backend)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Credits](#credits)

## Prerequisites

- You have Python installed in your computer.
- You are not connected to NUS wifi.
- Chin Herng is willing to give you the connection string of the database.

## Usage

Clone the repository:

```
git clone https://github.com/chin-herng/nus-class-connect-backend.git
```

In the project root, create a file named `.env` with the following contents:

```
HOST=<connection_string>
```

where `<connection_string>` is the connection string Chin Herng gave you.

Open a command terminal, `cd` into the project root, and use the `python auth.py` command to run the backend server.

## Credits
- [Chin Herng](https://www.linkedin.com/in/chong-chin-herng/) set up the MongoDB and Flask endpoints, as well as tidied up the codebase.
- [Sahej Agarwal](https://in.linkedin.com/in/sahej-agarwal-b60045175) contributed the actual signup and login logic.
