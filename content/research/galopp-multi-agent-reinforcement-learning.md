---
title: 'Multi-Agent Deep Reinforcement Learning For Persistent Monitoring With Sensing, Communication, and Localization Constraints'
tagline: Persistent Monitoring
featured: False
summary: Determining multi-robot motion policies for persistently monitoring a region with limited sensing, communication, and localization constraints in non-GPS environments is a challenging problem. To take the localization constraints into account, in this paper, we consider a heterogeneous robotic system consisting of two types of agents.
weight: 100
tags:
  - persistent-monitoring
  - multi-agent-reinforcement-learning
  - galopp
---

## Abstract

Determining multi-robot motion policies for persistently monitoring a region with limited sensing, communication, and localization constraints in non-GPS environments is a challenging problem. To take the localization constraints into account, in this paper, we consider a heterogeneous robotic system consisting of two types of agents: anchor agents with accurate localization capability and auxiliary agents with low localization accuracy. To localize itself, the auxiliary agents must be within the communication range of an {anchor}, directly or indirectly. The robotic team's objective is to minimize environmental uncertainty through persistent monitoring. We propose a multi-agent deep reinforcement learning (MARL) based architecture with graph convolution called Graph Localized Proximal Policy Optimization (GALOPP), which incorporates the limited sensor field-of-view, communication, and localization constraints of the agents along with persistent monitoring objectives to determine motion policies for each agent. We evaluate the performance of GALOPP on open maps with obstacles having a different number of anchor and auxiliary agents. We further study (i) the effect of communication range, obstacle density, and sensing range on the performance and (ii) compare the performance of GALOPP with non-RL baselines, namely, greedy search, random search, and random search with communication constraint. For its generalization capability, we also evaluated GALOPP in two different environments -- 2-room and 4-room. The results show that GALOPP learns the policies and monitors the area well. As a proof-of-concept, we perform hardware experiments to demonstrate the performance of GALOPP.

**Authors:** Manav Mishra, Prithvi Poddar, Rajat Agrawal, Jingxi Chen, Pratap Tokekar, and P.B. Sujit

## Video Demonstration


