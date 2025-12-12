---
title: "Sim2Real for UGVs"
date: 2025-12-10
description: "Addressing the reality gap in Deep Reinforcement Learning for UAV navigation through domain randomization and sensor noise modeling."


# Header Image
cover_image: "https://moonlab.iiserb.ac.in/assets/images/research/sim2real/cover.png"

# Sidebar Data
resources:
  - name: "Project Page"
    url: "https://moonlab.iiserb.ac.in/research_page/sim2real.html"
    icon: "link"
  - name: "Source Code"
    url: "https://github.com/moonlab-iiserb"
    icon: "github"

# Linking to existing files in content/people/
authors:
  - "karthik" # matches content/people/karthik.md
  - "sujit"   # matches content/people/sujit.md

keywords:
  - "Deep RL"
  - "Sim2Real"
  - "UAV Navigation"
  - "Domain Randomization"
---

## Abstract

Deep Reinforcement Learning (DRL) has shown immense potential in enabling autonomous navigation for Unmanned Aerial Vehicles (UAVs). However, training DRL agents in the real world is fraught with risks, including potential damage to the UAV and the environment. **Sim-to-Real (Sim2Real)** transfer offers a safer alternative by training agents in simulated environments before deploying them in the real world.

The primary challenge in Sim2Real transfer is the **"Reality Gap"**—the discrepancy between the simulation and the physical world. This gap arises due to inaccuracies in physics engines, differences in visual appearance, and sensor noise.

## Methodology

We propose a robust Sim2Real pipeline that leverages **Domain Randomization** and **Sensor Noise Modeling** to bridge the reality gap.

### 1. Domain Randomization
To make the policy robust to visual variations, we randomize textures, lighting, and object positions in the simulation environment (Gazebo). This forces the agent to learn invariant features rather than overfitting to a specific visual setting.

### 2. Sensor Noise Modeling
Real-world sensors (IMU, Camera, Lidar) are noisy. We model this noise in the simulation by injecting Gaussian noise and bias into the sensor readings, mimicking the characteristics of real hardware.

{{< youtube-lite "inWCiNpWeJc" >}}

## Experiments & Results

We validated our approach by training a PPO agent in a randomized Gazebo environment and deploying it on a custom-built quadrotor equipped with an NVIDIA Jetson Nano.

* **Simulation Success Rate:** 95% in unseen environments.
* **Real-World Success Rate:** 85% in clutter-free environments, 70% in moderately cluttered environments.
* **Latency:** The control loop runs at 50Hz on the onboard computer.

![Navigation Path](https://moonlab.iiserb.ac.in/assets/images/research/sim2real/path.png "Figure 1: Comparison of simulated vs real-world trajectories.")