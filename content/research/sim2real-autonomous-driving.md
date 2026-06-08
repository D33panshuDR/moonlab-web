---
title: 'Sim2Real Autonomous Driving using Convolutional Neural Network for Urban Environments'
tagline: Autonomous Driving
featured: true
summary: In this paper, we propose a model that utilizes input images from two forward-facing cameras, along with vehicle velocity and traffic light status to predict the future waypoints of the vehicle. Trained on expert demonstrations, the model learns to predict future waypoints in the vehicle frame of reference without access to BEV ground truths.
weight: 100
tags:
  - autonomous-driving
  - sim2real
---

## Abstract

In this paper, we propose a model that utilizes input images from two forward-facing cameras, along with vehicle velocity and traffic light status to predict the future waypoints of the vehicle. Trained on expert demonstrations, the model learns to predict future waypoints in the vehicle frame of reference without access to BEV ground truths. An essential improvement is the inclusion of traffic light status along with velocity as measurement inputs, making the model robust to traffic light signals. Unlike Learning By Cheating, which only considers velocity information, our model directly incorporates traffic light status, preventing the CNN from indirectly inferring traffic light signals. The predicted waypoints are then translated into steering and throttle control parameters using a PID controller. We also introduce improvements to the longitudinal PID controller, enabling effective slowing of the vehicle speed during turnings.

**[Paper Link: Sim2Real Autonomous Driving using Convolutional Neural Network for Urban Environments](https://link.springer.com/chapter/10.1007/978-3-031-63596-0_49)**

## Video Demonstration

{{< youtube-lite inWCiNpWeJc >}}
