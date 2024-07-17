![img_1.png](docs/Ysocial.png)

YSocial is a client-server application that implements a digital twin of a microblogging platform using Large Language Models (LLMs). This project simulates a social media-like environment where agents are represented by LLMs, allowing for realistic and efficient interactions.

This repository contains the code for the **client-side** of the application. 

The server-side code can be found [here](https://github.com/YSocialTwin/YServer)

#### Features

- Realistic agent simulations using LLMs
- Microblogging platform with posting, commenting, and liking capabilities
- Client-server architecture for scalability and flexibility
- Support for various user interactions (e.g., posting, commenting, liking)
- Ability to simulate a wide range of scenarios and use cases

## Technical Details

![Schema](docs/schema.png)

- Programming Language: Python
- Framework: Flask + PyAutogen + SQlite
- LLMs: Any compatible with OpenAI'API (either commercial or self-hosted)

## Getting Started

- Clone this repository to your local machine using git clone https://github.com/giuliorossetti/YClient.git
- Install dependencies y_client using pip install. 

### Usage

*Step 1:* Make sure to have access (either locally or remotely) to an LLM model compatible with OpenAI's API. 

*Step 2:* Configure the simulation by editing the file `/config_files/config.json`: it allows to specify several parameters, such as the number of agents, the LLM model to be used, the length of the simulation.

*Step 3:* Make sure the y_server is running.

*Step 4:* Run the client to interact with the server.

Under the folder clients, you can find a simple client that interacts with the server.

```bash
cd clients
python plain_y_client.py 
```

Several parameters can be specified while launching `plain_y_client.py`. 
Use the flags and their respective arguments as described below:

#### Configuration File
- **Flag:** `-c`, `--config_file`
- **Default:** `../config_files/config_politics.json`
- **Description:** JSON file describing the simulation configuration.

#### Agents
- **Flag:** `-a`, `--agents`
- **Default:** `None`
- **Description:** JSON file with pre-existing agents (needed to resume an existing simulation).

#### Feeds
- **Flag:** `-f`, `--feeds`
- **Default:** `../config_files/rss_feeds_politics.json`
- **Description:** JSON file containing RSS feed categorized.

#### Owner
- **Flag:** `-o`, `--owner`
- **Default:** `admin`
- **Description:** Simulation owner username (useful in multi-client scenarios).

#### Reset
- **Flag:** `-r`, `--reset`
- **Default:** `False`
- **Description:** Boolean. Whether to reset the experiment status. Default is `False`. If set to `True`, the simulation will start from scratch (the DBs will be cleared).

#### News
- **Flag:** `-n`, `--news`
- **Default:** `False`
  - **Description:** Boolean. Whether to reload the RSS feeds. Default is `False`. If set to `True`, the RSS feeds will be reloaded (the RSS-client DB will be cleared).

#### Content Recommender System
- **Flag:** `-x`, `--crecsys`
- **Default:** `ReverseChronoFollowersPopularity`
- **Description:** Name of the content recommender system to be used. Options: `Random`, `ReverseChrono`, `ReverseChronoPopularity`, `ReverseChronoFollowers`, `ReverseChronoFollowersPopularity`

#### Follower Recommender System
- **Flag:** `-y`, `--frecsys`
- **Default:** `PreferentialAttachment`
- **Description:** Name of the follower recommender system to be used. Options: `Random`, `PreferentialAttachment`, `AdamicAdar`, `Jaccard`, `CommonNeighbors`

#### Output File
- **Flag:** `-w`, `--write_output`
- **Default:** `../config_files/agents.json`
- **Description:** Name of the output file storing the generated agents.

For a description of the available recommender systems, please refer to the Y paper.


## Contribution

Contributions are welcome! If you'd like to improve YSocial, please:

- Fork this repository
- Create a new branch for your feature or bug fix
- Submit a pull request with detailed changes and explanations

## Citation

If you use YSocial in your research, please cite the following paper:

```
@article{rossetti2024ysocial,
  title={Y Social: an LLM-powered microblogging Digital Twin},
  author={Rossetti, Giulio and Stella, Massimo and Cazabet, Rémy and 
  Abramski, Katherine and Cau, Erica and Citraro, Salvatore and 
  Failla, Andrea and Improta, Riccardo and Morini, Virginia and 
  Pansanella, Virginia},
  year={2024}
}
```

## License

YSocial is licensed under the GNU GENERAL PUBLIC LICENSEe. See LICENSE.txt for details.

