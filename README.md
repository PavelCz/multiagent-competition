# Competitive Multi-Agent Environments - MuJoCo 2.1

This repository contains the environments for the paper [Emergent Complexity via Multi-agent Competition](https://arxiv.org/abs/1710.03748)

This branch updates the HumanCompatibleAI fork to make gym_compete compatible with MuJoCo 2.1.

List of changes:
- Remove Python 2 and 3 compatibility code with six.
- Updates for mujoco_py changes
  - `env.model` -> `env.sim`
  - Some attributes were renamed.
- Update for compatiblity with newer version of `numpy`.
- Some agents clipped actions before calculating rewards, some didn't. Now there is consistently no clipping.
- The `numarrows` attribute in xml was removed due to it having no function.
- Remove copied code of `openai/gym`'s `mujoco_env` in favor of importing from gym.
- Remove `policy_py` which relies on `tensorflow<2`
- Remove the `demo_tasks.sh` script which wasn't runnable due to prior changes in the HumanCompatibleAI fork.

## Dependencies
Use `pip install -r requirements.txt` to install dependencies. If you haven't used MuJoCo before, please refer to the [installation guide](https://github.com/openai/mujoco-py).
The code has been tested with the following dependencies:
* Python version 3.8
* [OpenAI GYM](https://github.com/openai/gym) version 0.19 with MuJoCo 2.1 support (use mujoco-py version 2.1)
* [Tensorflow](https://www.tensorflow.org/versions/r1.1/install/) version 2.7.0
* [Numpy](https://scipy.org/install.html) version 1.21.5

## Installing Package
After installing all dependencies, make sure gym works with support for MuJoCo environments.
Next install `gym-compete` package as:
```bash
cd gym-compete
pip install -e .
```

Or use pip to install / add to requirements as
```bash
gym_compete @ git+https://github.com/HumanCompatibleAI/multiagent-competition.git@v0.1.0
```
Check install is successful by coming out of the directory and trying `import gym_compete` in python console. Some users might require a `sudo pip install`.

